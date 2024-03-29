import pygame as pg
import sprites
import utils
import player

class Ghost:
    def __init__(self, pos: tuple[int, int], screen: pg.Surface, player: player.Pacman) -> None:
        self.image = sprites.Blinky.sprite
        self.rect = self.image.get_rect(center = pos)
        self.screen = screen
        self.animation_type: sprites.GhostAnimation = sprites.GhostAnimation.CHASE
        self.direction: utils.Direction = utils.Direction.UP
        self.animation_index = 0
        self.target: tuple[int, int] = (0, 0)
        self.player = player
        self.buffer1 = -2
        self.buffer2 = 2

    def calculate_direction(self) -> utils.Direction:
        move_dist = (self.rect.width + self.rect.height) / 2
        points: list[tuple[int, int]] = [
            (self.rect.centerx, self.rect.centery - move_dist),
            (self.rect.centerx, self.rect.centery + move_dist),
            (self.rect.centerx - move_dist, self.rect.centery),
            (self.rect.centerx + move_dist, self.rect.centery)
        ]
        possible_points: list[tuple[int, int]] = []
        for point in points:
            if not utils.check_for_map_collisions(self.rect, utils.get_direction(self.rect.center, point), self.screen, self.buffer1, self.buffer2):
                if self.is_in_home(point[0], point[1]) and not self.is_in_home(self.rect.centerx, self.rect.centery):
                    continue
                possible_points.append(point)
        min_dist = 999999999999999999999.0
        for point in possible_points: 
            direction = utils.get_direction(self.rect.center, point)
            if direction == utils.Direction.flip(self.direction):
                # danger: this will skip the next item in the list, which is fine in this case as only 1 direction can equal the previous direction
                possible_points.remove(point)
        dists: list[float] = [utils.distance(pnt, self.target) for pnt in possible_points]
        if len(dists) == 0:
            return self.direction
        min_dist = min(dists)
        pg.draw.line(self.screen, (255, 0, 0), self.rect.center, possible_points[dists.index(min_dist)], 1)
        direction = utils.get_direction(self.rect.center, possible_points[dists.index(min_dist)])
        return direction
        # for point in possible_points:
        #     dist = utils.distance(point, self.target)
        #     if dist < min_dist:
        #         direction = utils.get_direction(point, self.target)
        #         pg.draw.line(self.screen, (255, 0, 0), self.rect.center, point, 1)
        #         pg.draw.line(self.screen, (0, 255, 0), point, self.target, 1)
        #         if direction != utils.Direction.flip(self.direction):
        #             min_dist = dist
        #         else:
        #             direction = prev_dir
        # return direction

    def move(self) -> None:
        if utils.check_for_map_collisions(self.rect, self.direction, self.screen, self.buffer1, self.buffer2):
            return
        match self.direction:
            case utils.Direction.UP:
                self.rect.y -= 1
            case utils.Direction.DOWN:
                self.rect.y += 1
            case utils.Direction.LEFT:
                self.rect.x -= 1
            case utils.Direction.RIGHT:
                self.rect.x += 1
        if self.rect.x < 0:
            self.rect.x = utils.WIDTH
        if self.rect.x > utils.WIDTH:
            self.rect.x = 0
        if self.rect.y < 0:
            self.rect.y = utils.HEIGHT
        if self.rect.y > utils.HEIGHT:
            self.rect.y = 0

    def is_in_home(self, x: int, y: int):
        if x > 200 and x < 275:
            if y > 200 and y < 263:
                return True
        return False

    def update(self) -> None:
        self.screen.blit(self.image, self.rect)
        self.direction = self.calculate_direction()
        self.move()

class Blinky(Ghost):
    def __init__(self, pos: tuple[int, int], screen: pg.Surface, player: player.Pacman) -> None:
        super().__init__(pos, screen, player)
    
    def update(self) -> None:
        self.screen.blit(self.image, self.rect)
        self.target = self.player.rect.center
        if (self.is_in_home(self.rect.centerx, self.rect.centery)):
            self.target = (221, 85)
        self.direction = self.calculate_direction()
        self.move()

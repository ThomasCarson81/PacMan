import pygame as pg
import sprites
from utils import Direction, WIDTH, HEIGHT, check_for_map_collisions

class Pacman:
	def __init__(self, pos: tuple[int, int], screen: pg.Surface) -> None:
		self.screen = screen
		self.image: pg.Surface = sprites.Pacman.CIRCLE
		self.rect = self.image.get_rect(center = pos)
		self.animation_type: sprites.PacmanAnimation = sprites.PacmanAnimation.RUN
		self.direction: Direction = Direction.UP
		self.animation_index = 0
		self.queue: list[Direction] = []

	def get_input(self) -> None:
		keys = pg.key.get_pressed()
		if keys[pg.K_UP] or keys[pg.K_w]:
			if check_for_map_collisions(self.rect, Direction.UP, self.screen, -2, 2):
				self.queue.append(Direction.UP)
			else:
				self.animation_type = sprites.PacmanAnimation.RUN
				self.direction = Direction.UP
				self.queue.clear()
		elif keys[pg.K_DOWN] or keys[pg.K_s]:
			if check_for_map_collisions(self.rect, Direction.DOWN, self.screen, -2, 2):
				self.queue.append(Direction.DOWN)
			else:
				self.animation_type = sprites.PacmanAnimation.RUN
				self.direction = Direction.DOWN
				self.queue.clear()
		elif keys[pg.K_LEFT] or keys[pg.K_a]:
			if check_for_map_collisions(self.rect, Direction.LEFT, self.screen, -2, 2):
				self.queue.append(Direction.LEFT)
			else:
				self.animation_type = sprites.PacmanAnimation.RUN
				self.direction = Direction.LEFT
				self.queue.clear()
		elif keys[pg.K_RIGHT] or keys[pg.K_d]:
			if check_for_map_collisions(self.rect, Direction.RIGHT, self.screen, -2, 2):
				self.queue.append(Direction.RIGHT)
			else:
				self.animation_type = sprites.PacmanAnimation.RUN
				self.direction = Direction.RIGHT
				self.queue.clear()
		else:
			if len(self.queue) > 0 and not check_for_map_collisions(self.rect, self.queue[0], self.screen, -2, 2):
				self.direction = self.queue.pop(0)

	def animate(self) -> None:
		if self.animation_type == sprites.PacmanAnimation.RUN:
			self.animation_index += 1
			if self.animation_index > 20:
				self.animation_index = 0
			match self.direction:
				case Direction.UP:
					self.image = sprites.Pacman.UP[int(self.animation_index >= 10)]
				case Direction.DOWN:
					self.image = sprites.Pacman.DOWN[int(self.animation_index >= 10)]
				case Direction.LEFT:
					self.image = sprites.Pacman.LEFT[int(self.animation_index >= 10)]
				case Direction.RIGHT:
					self.image = sprites.Pacman.RIGHT[int(self.animation_index >= 10)]

	def move(self) -> None:
		match self.direction:
			case Direction.UP:
				self.rect.y -= 2
			case Direction.DOWN:
				self.rect.y += 2
			case Direction.LEFT:
				self.rect.x -= 2
			case Direction.RIGHT:
				self.rect.x += 2
		if self.rect.x < 0:
			self.rect.x = WIDTH
		if self.rect.x > WIDTH:
			self.rect.x = 0
		if self.rect.y < 0:
			self.rect.y = HEIGHT
		if self.rect.y > HEIGHT:
			self.rect.y = 0

	def update(self) -> None:
		self.screen.blit(self.image, self.rect)
		self.get_input()
		self.animate()
		if not check_for_map_collisions(self.rect, self.direction, self.screen, -2, 2):
			self.move()
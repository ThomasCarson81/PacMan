import pygame as pg
from math import sqrt
from enum import Enum
WIDTH, HEIGHT = 442, 496

class Direction(Enum):
    UP = 0
    DOWN = 1
    LEFT = 2
    RIGHT = 3

    def flip(self):
        match self:
            case Direction.UP:
                return Direction.DOWN
            case Direction.DOWN:
                return Direction.UP
            case Direction.LEFT:
                return Direction.RIGHT
            case Direction.RIGHT:
                return Direction.LEFT

def check_for_map_collisions(rect: pg.Rect, direction: Direction, screen: pg.Surface, buffer1: int, buffer2: int) -> bool:
    map_colour = pg.Color(33, 33, 255)
    match direction:
        case Direction.UP:
            axis = 1
            offset = -1
        case Direction.DOWN:
            axis = 1
            offset = 1
        case Direction.LEFT:
            axis = 0
            offset = -1
        case Direction.RIGHT:
            axis = 0
            offset = 1
    if axis == 0:
        x = int(rect.centerx + (offset * (3+rect.width/2)))
        for i in range(rect.top+buffer1, rect.bottom-buffer1):
            for j in range(x-buffer2, x+buffer2):
                try:
                    if screen.get_at([j, i]) == map_colour:
                        return True
                except:
                    return False
        return False
    elif axis == 1:
        y = int(rect.centery + (offset * (3+rect.height/2)))
        for i in range(rect.left+buffer1, rect.right-buffer1):
            for j in range(y-buffer2, y+buffer2):
                try:
                    if screen.get_at([i, j]) == map_colour:
                        return True
                except:
                    return False
        return False

def distance(a: tuple[int, int], b: tuple[int, int]) -> float:
    x = a[0] - b[0]
    y = a[1] - b[1]
    return sqrt(x*x + y*y)

def get_direction(fromPoint: tuple[int, int], toPoint: tuple[int, int]) -> Direction:
    if fromPoint[0] < toPoint[0]:
        return Direction.RIGHT
    elif fromPoint[0] > toPoint[0]:
        return Direction.LEFT
    elif fromPoint[1] < toPoint[1]:
        return Direction.DOWN
    elif fromPoint[1] > toPoint[1]:
        return Direction.UP

import pygame as pg
from enum import Enum
map_img: pg.Surface = pg.image.load("sprites/map/map_empty_square_double.png").convert_alpha()
class Pacman:
    UP: list[pg.Surface] = [
        pg.transform.scale2x(pg.image.load("sprites/pacman/run/up_0.png").convert_alpha()),
        pg.transform.scale2x(pg.image.load("sprites/pacman/run/up_1.png").convert_alpha())
    ]
    DOWN: list[pg.Surface] = [
        pg.transform.scale2x(pg.image.load("sprites/pacman/run/down_0.png").convert_alpha()),
        pg.transform.scale2x(pg.image.load("sprites/pacman/run/down_1.png").convert_alpha())
    ]
    LEFT: list[pg.Surface] = [
        pg.transform.scale2x(pg.image.load("sprites/pacman/run/left_0.png").convert_alpha()),
        pg.transform.scale2x(pg.image.load("sprites/pacman/run/left_1.png").convert_alpha())
    ]
    RIGHT: list[pg.Surface] = [
        pg.transform.scale2x(pg.image.load("sprites/pacman/run/right_0.png").convert_alpha()),
        pg.transform.scale2x(pg.image.load("sprites/pacman/run/right_1.png").convert_alpha())
    ]
    CIRCLE: pg.Surface = pg.transform.scale2x(pg.image.load("sprites/pacman/circle.png").convert_alpha())
class PacmanDeath:
    ONE: pg.Surface = pg.transform.scale2x(pg.image.load("sprites/pacman/death/1.png").convert_alpha())
    TWO: pg.Surface = pg.transform.scale2x(pg.image.load("sprites/pacman/death/2.png").convert_alpha())
    THREE: pg.Surface = pg.transform.scale2x(pg.image.load("sprites/pacman/death/3.png").convert_alpha())
    FOUR: pg.Surface = pg.transform.scale2x(pg.image.load("sprites/pacman/death/4.png").convert_alpha())
    FIVE: pg.Surface = pg.transform.scale2x(pg.image.load("sprites/pacman/death/5.png").convert_alpha())
    SIX: pg.Surface = pg.transform.scale2x(pg.image.load("sprites/pacman/death/6.png").convert_alpha())
    SEVEN: pg.Surface = pg.transform.scale2x(pg.image.load("sprites/pacman/death/7.png").convert_alpha())
    EIGHT: pg.Surface = pg.transform.scale2x(pg.image.load("sprites/pacman/death/8.png").convert_alpha())
    NINE: pg.Surface = pg.transform.scale2x(pg.image.load("sprites/pacman/death/9.png").convert_alpha())
    TEN: pg.Surface = pg.transform.scale2x(pg.image.load("sprites/pacman/death/10.png").convert_alpha())
    ELEVEN: pg.Surface = pg.transform.scale2x(pg.image.load("sprites/pacman/death/11.png").convert_alpha())
class PacmanAnimation(Enum):
    RUN = 0
    DEATH = 1

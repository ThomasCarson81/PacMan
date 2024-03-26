import pygame as pg
from enum import Enum

class Pacman(Enum):
    UP = [
        pg.image.load("sprites/pacman/up_0.png").convert_alpha(),
        pg.image.load("sprites/pacman/up_1.png").convert_alpha()
    ]
    DOWN = [
        pg.image.load("sprites/pacman/down_0.png").convert_alpha(),
        pg.image.load("sprites/pacman/down_1.png").convert_alpha()
    ]
    LEFT = [
        pg.image.load("sprites/pacman/left_0.png").convert_alpha(),
        pg.image.load("sprites/pacman/left_1.png").convert_alpha()
    ]
    RIGHT = [
        pg.image.load("sprites/pacman/right_0.png").convert_alpha(),
        pg.image.load("sprites/pacman/right_1.png").convert_alpha()
    ]
    CIRCLE = pg.image.load("sprites/pacman/circle.png").convert_alpha()

class PacmanDeath(Enum):
    ONE = pg.image.load("sprites/pacman/death/1.png").convert_alpha()
    TWO = pg.image.load("sprites/pacman/death/2.png").convert_alpha()
    THREE = pg.image.load("sprites/pacman/death/3.png").convert_alpha()
    FOUR = pg.image.load("sprites/pacman/death/4.png").convert_alpha()
    FIVE = pg.image.load("sprites/pacman/death/5.png").convert_alpha()
    SIX = pg.image.load("sprites/pacman/death/6.png").convert_alpha()
    SEVEN = pg.image.load("sprites/pacman/death/7.png").convert_alpha()
    EIGHT = pg.image.load("sprites/pacman/death/8.png").convert_alpha()
    NINE = pg.image.load("sprites/pacman/death/9.png").convert_alpha()
    TEN = pg.image.load("sprites/pacman/death/10.png").convert_alpha()
    ELEVEN = pg.image.load("sprites/pacman/death/11.png").convert_alpha()
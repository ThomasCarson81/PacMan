import pygame as pg
from sys import exit as sysexit
from utils import WIDTH, HEIGHT

pg.init()
screen = pg.display.set_mode((WIDTH, HEIGHT))
pg.display.set_caption("Pac-Man")
clock = pg.time.Clock()
import player, sprites

pacman = player.Pacman((WIDTH/2, HEIGHT/2), screen)

while True:
	for event in pg.event.get():
		if event.type == pg.QUIT:
			pg.quit()
			sysexit()

	screen.fill("black")
	screen.blit(sprites.map_img, (0, 0))
	pacman.update()

	pg.display.update()
	clock.tick(60)

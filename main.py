import pygame as pg
from sys import exit as sysexit
from utils import WIDTH, HEIGHT
# 164, 200 -> 275 263
pg.init()
screen = pg.display.set_mode((WIDTH, HEIGHT))
pg.display.set_caption("Pac-Man")
clock = pg.time.Clock()
import player, sprites, ghosts

pacman = player.Pacman((244,328), screen)
blinky = ghosts.Blinky((WIDTH/2, HEIGHT/2), screen, pacman)

while True:
	for event in pg.event.get():
		if event.type == pg.QUIT:
			pg.quit()
			sysexit()
		elif event.type == pg.MOUSEBUTTONDOWN:
			print(event.pos)

	screen.fill("black")
	screen.blit(sprites.map_img, (0, 0))
	pacman.update()
	blinky.update()

	pg.display.update()
	clock.tick(60)

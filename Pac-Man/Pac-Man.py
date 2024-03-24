import pygame as pg
from sys import exit as sysexit

pg.init()
screen = pg.display.set_mode((800, 800))
pg.display.set_caption("Pac-Man")
clock = pg.time.Clock()


class Pacman:
	def __init__(self) -> None:
		self.image = pg.Surface((50,50))
		self.rect = self.image.get_rect()

	def update(self) -> None:
		screen.blit(self.image, self.rect)

while True:
	for event in pg.event.get():
		if event.type == pg.QUIT:
			pg.quit()
			sysexit()

	pg.display.update()
	clock.tick(60)

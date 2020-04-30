import math
import random
import pygame as pg
import time
from bird import bird
from flock import flock
import shutil
import os

window_width = 1440
window_height = 810

numBirds = 1000

BLACK = (  0,   0,   0)
WHITE = (255, 255, 255)
BLUE =  (  0,   0, 255)
GREEN = (  0, 255,   0)
RED =   (255,   0,   0)

win = pg.display.set_mode((window_width, window_height))

done = False
clock = pg.time.Clock()

the_flock = flock(numBirds, 5, (window_width, window_height))


try:
	shutil.rmtree("images")
except:
	print("Images folder not found to delete")

os.makedirs("images")
n = 0

while not done:
	clock.tick(10)

	for event in pg.event.get(): # User did something
		if event.type == pg.QUIT: # If user clicked close
			done=True

	the_flock.loop()

	win.fill(WHITE)

	the_flock.draw(win)

	# pg.draw.rect(win, BLUE, (0, 0, 100, 100))
	# pg.draw.circle(win, GREEN, [coordX, coordY], 2)
	pg.display.update()

	fname = "images/birds_" + str(n) + ".png"
	pg.image.save(win, fname)

	n += 1


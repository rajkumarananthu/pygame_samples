import pygame ,sys
from pygame.locals import *

pygame.init()

display_surface = pygame.display.set_mode((1000,600))
pygame.display.set_caption("trial2")

FPS = 3
fpsClock = pygame.time.Clock()

C1 = (0,0,0)
C2 = (255,0,0)
C3 = (0,255,0)
C4 = (0,0,255)
x = 1
while True:
	if x == 1:
		display_surface.fill(C1)
	elif x == 2:
		display_surface.fill(C2)
	elif x == 3:
		display_surface.fill(C3)
	elif x == 4:
		display_surface.fill(C4)
	else:
		x = 1
		display_surface.fill(C1)
	
	x+=1
	for event in pygame.event.get():
		if event.type == QUIT :
			pygame.quit()
			sys.exit()
	pygame.display.update()
	fpsClock.tick(FPS)
import sys
import pygame

def draw():
	pygame.init()
	screen = pygame.display.set_mode((1200, 800))
	pygame.display.set_caption("Cutting and Packing")
	
	while True:
		for event in pygame.event.get():
			if event.type == pygame.QUIT:
				sys.exit()
		
		pygame.display.flip()
	
if __name__ == "__main__":
	draw()
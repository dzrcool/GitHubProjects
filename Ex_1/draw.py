import sys
import pygame

class Board():
    def __init__(self, left, top, width, height, color, screen):
        self.left = left
        self.top = top
        self.width = width
        self.height = height
        self.color = color
        self.screen = screen    

    def draw(self):
        pygame.draw.rect(self.screen, self.color, (self.left, self.top, self.width, self.height))
 
class Piece():
    def __init__(self, points, color, screen):
        self.points = points
        self.color = color
        self.screen = screen
        
    def draw(self):
        pygame.draw.lines(self.screen, self.color, True, self.points, 1)
    
def run():
    pygame.init()
    screen = pygame.display.set_mode((1200, 800))
    pygame.display.set_caption("Cutting and Packing")   
    WHITE = (255, 255, 255)
    screen.fill(WHITE)
    
    BLUE = (0, 0, 255)
    b = Board(100, 100, 1000, 600, BLUE, screen)
    b.draw()
    
    RED = (255, 0, 0)
    points = [(100, 100), (120, 200), (130, 240), (150, 300), (120, 130)]
    p1 = Piece(points, RED, screen)
    p1.draw()
    
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()

        pygame.display.flip()
	
if __name__ == "__main__":
    run()
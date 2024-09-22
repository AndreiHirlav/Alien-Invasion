import pygame
import sys
from pygame.sprite import Sprite

pygame.init()

class Star(Sprite):
    def __init__(self):
        super().__init__()
        self.image = pygame.image.load('images/alien.bmp')
        self.rect = self.image.get_rect()
        self.x = 0
        self.y = 0

screen_width = 800
screen_height = 800
screen = pygame.display.set_mode((screen_width, screen_height))
star = Star()
star_width = star.rect.width
star_height = star.rect.height

cols = screen_width // (2 * star_width)
rows = screen_height // (2 * star_height)
while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()
            
    for row in range(rows):
        for col in range(cols):
            star = Star()
            star.x = star_width + 2 * star_width * col
            star.y = star_height + 2 * star_height * row
            screen.blit(star.image, (star.x, star.y))        
    pygame.display.flip()
            
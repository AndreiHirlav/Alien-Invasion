import pygame
from pygame.sprite import Sprite

class Ship(Sprite):
    def __init__(self, ai_game):
        #Initialize the ship and its starting position
        super().__init__()
        self.screen = ai_game.screen
        self.settings = ai_game.settings
        self.screen_rect = ai_game.screen.get_rect()
        
        #Load the ship image and get its rect
        self.image = pygame.image.load('images/ship.bmp')
        self.rect = self.image.get_rect()
        
        #Start each new ship at the bottom center of the screen
        self.rect.midbottom = self.screen_rect.midbottom
        
        self.x = float(self.rect.x)
        
        self.moving_right = False
        self.moving_left = False
        
    def blitme(self):
        #Draw the ship
        self.screen.blit(self.image, self.rect)
        
    def update(self):
        #Update the ship's position based on the movement flags
        if self.moving_right and self.rect.right < self.screen_rect.right:
            self.x += self.settings.ship_speed
        if self.moving_left and self.rect.left > 0:
            self.x -= self.settings.ship_speed
        self.rect.x = self.x
        
    def center_ship(self):
        #Center the ship
        self.rect.midbottom = self.screen_rect.midbottom
        self.x = float(self.rect.x)
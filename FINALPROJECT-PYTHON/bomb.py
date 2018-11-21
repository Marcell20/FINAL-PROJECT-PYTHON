import pygame
import random
from pygame.sprite import Sprite
class Bombs(Sprite):

    def __init__(self, ao_settings , screen):
        self.screen = screen

        #Load the bomb image
        self.image = pygame.image.load('bomb.bmp')
        self.image = pygame.transform.scale(self.image, (50,50))
        self.rect = self.image.get_rect()
        self.screen_rect = screen.get_rect()
        self.rect.centerx = random.randint(50,ao_settings.screen_width - 50)

    def blitme(self,status):
        if status:
            self.rect.bottom += 12.5
            self.screen.blit(self.image, self.rect)

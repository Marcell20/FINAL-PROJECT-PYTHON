import pygame
from pygame.sprite import Sprite
import random
from game_stats import GameStats

class Banana(Sprite):

    def __init__(self, ao_settings , screen):
        self.screen = screen

        #Load the apple image
        self.image = pygame.image.load('banana.bmp')
        self.image = pygame.transform.scale(self.image, (70,70))
        self.rect = self.image.get_rect()
        self.screen_rect = screen.get_rect()
        self.rect.centerx = random.randint(50,ao_settings.screen_width - 50)

    def blitme(self,status):
        if status:
            self.rect.bottom += 5
            self.screen.blit(self.image, self.rect)


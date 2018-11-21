import pygame
import os.path

class Settings():
    """A class to store all settings for APPLE"""

    def __init__(self):
        """Initialize the game's settings."""
        # Screen settings
        self.screen_width = 1000
        self.screen_height  = 800
        self.bg_color = (192,192,192)

        #Input background and settings
        self.background = pygame.image.load('park_1.bmp')
        self.background = pygame.transform.scale(self.background, (self.screen_width, self.screen_height))
        # self.s_top = self.screen_height - self.background.get_height()
        # self.s_left = self.screen_width/2 - self.background.get_width()

        self.initialize_dynamic_settings()

    def initialize_dynamic_settings(self):
        """Initialize settings that change throughout the game."""
        self.basket_speed_factor = 10
        # self.apple_speed_factor = 5
        # self.bomb_speed_factor = 3

        # self.basket_limit = 3

        # Scoring
        self.apples_points = 10
        self.bananas_points = 10
        self.bombs_points = 0
        self.cherrys_points = 20
        self.grapes_points = 30
        self.goldapples_points = 50


    def levelup(self, level):
        file_name = 'park_' + str(level) + '.bmp'
        if os.path.isfile(file_name):
            self.background = pygame.image.load(file_name)
            self.background = pygame.transform.scale(self.background, (self.screen_width, self.screen_height))
            # self.s_top = self.screen_height - self.background.get_height()
            # self.s_left = self.screen_width / 2 - self.background.get_width()
            # stats.

    # def increase_speed(self):
    #     """Increase speed settings"""
    #     self.basket_speed_factor *= self.speedup_scale
    #     self.apple_speed_factor *= self.speedup_scale
    #     self.bomb_speed_factor *= self.speedup_scale


import pygame
class GameStats():
    """Track statistic from apple"""

    def __init__(self,ao_settings):
        """Initialize statistics."""
        self.ao_settings = ao_settings
        self.reset_stats()
        # self.score = 0
        # Start game in an inactivee state.
        self.game_active = False
        self.game_over = False
        self.game_end = False

    def reset_stats(self):
        """Intialize statistics that can change dduring the game."""
        # self.basket_left = self.ao_settings.basket_limit
        self.score = 0
        self.level = 1
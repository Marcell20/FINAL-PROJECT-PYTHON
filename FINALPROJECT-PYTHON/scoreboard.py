import pygame.font

class Scoreboard():
    """A class to report scoring information"""

    def __init__(self,ao_settings,screen,stats):
        """Initialize scorekeeping attributes."""
        self.screen = screen
        self.screen_rect = screen.get_rect()
        self.ao_settings = ao_settings
        self.stats = stats

        # Font settings fot scoring information
        self.text_color = (30,30,30)
        self.font = pygame.font.SysFont(None,60)

        # Prepare the initial score image
        self.prep_score()
        self.prep_level()
        #self.level_rect()

    def prep_level(self):
        """Turn the level into a rendered image."""
        self.level_image = self.font.render('level: '+str(self.stats.level),True, self.text_color, self.ao_settings.bg_color)
        self.level_rect = self.level_image.get_rect()
        self.level_rect.left = 0
        self.level_rect.top = 0

    def prep_score(self):
        """Turn the score into a rendered image."""
        score_str = str(self.stats.score)
        self.score_image = self.font.render(score_str, True, self.text_color, self.ao_settings.bg_color)

        # Display the score at the top right of the screen.
        self.score_rect = self.score_image.get_rect()
        self.score_rect.right = self.screen_rect.right - 460
        self.score_rect.top = 20

        self.ao_settings.levelup(self.stats.level)

    def show_score(self):
        """Draw score to the screen"""
        self.screen.blit(self.score_image, self.score_rect)
        self.screen.blit(self.level_image, self.level_rect)
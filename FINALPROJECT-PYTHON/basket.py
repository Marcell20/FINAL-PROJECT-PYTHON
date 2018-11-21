import pygame

class Basket():

    def __init__(self,ao_settings,screen):
        """Initialize the basket and set its starting position."""
        self.screen = screen
        self.ao_settings = ao_settings

        #Load the ship image and get its rect.
        self.image = pygame.image.load('basket.bmp')
        self.image = pygame.transform.scale(self.image, (180,100))
        self.rect = self.image.get_rect()
        self.screen_rect = screen.get_rect()

        # Start each new basket at the bottom center of the screen.
        self.rect.centerx = self.screen_rect.centerx
        self.rect.bottom = self.screen_rect.bottom

        # Store a decimal value for the ship's center.
        self.center = float(self.rect.centerx)

        # Movement flag.
        self.moving_right = False
        self.moving_left = False

    def update(self):
        """Update the basket's position based on the movement flag."""
        # Update the basket's center value, not the rect.
        if self.moving_right and self.rect.right < self.screen_rect.right:
            self.rect.centerx += self.ao_settings.basket_speed_factor
        if self.moving_left and self.rect.left > 0:
            self.rect.centerx -= self.ao_settings.basket_speed_factor


        #Update rect object from self.center
        # self.rect.centerx = self.center

    def blitme(self):
        """Draw the basket at its current location."""
        self.screen.blit(self.image, self.rect)
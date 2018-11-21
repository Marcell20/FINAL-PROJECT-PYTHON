import pygame.font

class Button():

    def __init__(self,ao_settings,screen,msg):
        """Initialize button atrributtes"""
        self.screen = screen
        self.screen_rect = screen.get_rect()

        # Set the dimensions and properties of button.
        self.screen_width, self.screen_height = 200,50
        self.button_color = (192,192,192)
        self.text_color = (255,255,255)
        self.font = pygame.font.SysFont(None,48)

        # Build the button's object and center it.
        self.rect = pygame.Rect(0, 0, self.screen_width, self.screen_height)
        self.rect.center = self.screen_rect.center

        #The button message need to be prepped only once
        self.prep_msg(msg)

    def prep_msg(self,msg):
        """Turn msg into a rendered image and center text on the button."""
        self.msg_image = self.font.render(msg, True, self.text_color, self.button_color)
        self.msg_image_rect = self.msg_image.get_rect()
        self.msg_image_rect.center = self.rect.center

    def draw_button(self):
        #Draw blank button and then draw message.
        self.screen.fill(self.button_color, self.rect)
        self.screen.blit(self.msg_image, self.msg_image_rect)

# class Image():
#     def __init__(self,screen):
#         self.screen = screen
#         self.screen_rect = screen.get_rect
#         self.width = 230
#         self.height = 160
#         self.load = pygame.image.load("basket.bmp")
#         self.image = pygame.transform.scale(self.load,(self.width,self.height))
#         self.rect = pygame.Rect(0,0,self.width,self.height)
#         self.rect.center =(490,480)
#         # self.font = pygame.font.SysFont(None,48)
#
#     def mouse_hover(self,screen):
#         self.screen = screen
#         self.screen_rect = screen.get_rect
#         self.width = 250
#         self.height = 190
#         self.load = pygame.image.load("basket.bmp")
#         self.image = pygame.transform.scale(self.load,(self.width,self.height))
#         self.rect = pygame.Rect(0,0,self.width,self.height)
#         self.rect.center =(490,480)
#
#     def mouse_back(self,screen):
#         self.screen = screen
#         self.screen_rect = screen.get_rect
#         self.width = 230
#         self.height = 160
#         self.load = pygame.image.load("basket.bmp")
#         self.image = pygame.transform.scale(self.load,(self.width,self.height))
#         self.rect = pygame.Rect(0,0,self.width,self.height)
#         self.rect.center =(490,480)
#
#     def draw_button(self):
#         self.screen.blit(self.image,self.rect)


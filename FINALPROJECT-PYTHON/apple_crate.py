import pygame
import sys
from bomb import Bombs
from settings import Settings
from basket import Basket
from apple import Apple
from banana import Banana
from cherry import Cherry
from grape import Grape
from golden_apple import GoldenApple
from game_stats import GameStats
from button import Button
from scoreboard import Scoreboard

import functions as gf

# initialize pygame, settings, and object.
pygame.init()
pygame.mixer_music.load("soundtrack.wav")
ao_settings = Settings()
screen = pygame.display.set_mode((ao_settings.screen_width, ao_settings.screen_height))
# screen.blit(ao_settings.background, (ao_settings.s_top, ao_settings.s_left))
pygame.display.set_caption("Grab Your Apple")


# def menu():
#     basket=Image(screen)
#     flag=True
#     while flag:
#         # for background in start menu
#         background = pygame.image.load('park_1.bmp')
#         background_menu = pygame.transform.scale(background,(1000,800))
#         screen.blit(background_menu,(0,0))
#
#         # for the title "Grab your apples"
#         title = pygame.image.load('title.bmp')
#         title_menu =pygame.transform.scale(title,(325,325))
#         screen.blit(title_menu,(330,100))
#
#         #for the basket background for start
#         # baskets_background = pygame.image.load('basket.bmp')
#         # baskets_background_menu = pygame.transform.scale(baskets_background, (300, 200))
#         # screen.blit(baskets_background_menu, (350,380))
#         basket.draw_button()
#         pygame.display.flip()
#
#         for event in pygame.event.get():
#             if event.type == pygame.QUIT:
#                 sys.exit()
#
#             if event.type == pygame.MOUSEMOTION:
#                 mouse_x, mouse_y = pygame.mouse.get_pos()
#                 basket_hover = basket.rect.collidepoint(mouse_x, mouse_y)
#                 if basket_hover == True:
#                     basket.mouse_hover(screen)
#                 if basket_hover== False:
#                     basket.mouse_back(screen)
#             if event.type == pygame.MOUSEBUTTONDOWN:
#                 mouse_x, mouse_y = pygame.mouse.get_pos()
#                 basket_clicked = basket.rect.collidepoint(mouse_x,mouse_y)
#                 if basket_clicked == True:
#                     run_game()
#                     flag = False

def run_game():

    pygame.mixer_music.play()

    # Set the background color.
    # bg_color = (230,230,230)


    #Make a basket
    basket = Basket(ao_settings,screen)
    #Make an basket
    bombs = []
    #Make an apple
    apples = []
    # Make a banana
    bananas = []
    #Make GoldApple
    goldapples = []
    #Make cherry
    cherrys = []
    #Make Grape
    grapes = []
    # Make the play button
    play_button = Button(ao_settings,screen, "Play")
    # Retry button
    retry_button = Button(ao_settings,screen, "Retry")

    stats = GameStats(ao_settings)
    sb = Scoreboard(ao_settings, screen, stats)

    game_over = False
   #Start the main loop for the game.
    while True :

        gf.check_events(ao_settings,basket,screen,stats,play_button,retry_button,apples,bananas, bombs)
        basket.update()
        gf.update_screen(ao_settings,screen,stats,sb, basket,play_button,retry_button)



        #For the apples
        if len(apples) < 1:
            apples.append(Apple(ao_settings, screen))
        for apple in apples:
            apple.blitme(stats.game_active)
            if apple.rect.bottom > ao_settings.screen_height:
                apples.remove(apple)
            elif apple.rect.bottom > basket.rect.top and apple.rect.left > basket.rect.left and apple.rect.right < basket.rect.right:
                apples.remove(apple)
                apple.sound.play()

                stats.score += ao_settings.apples_points
                sb.prep_score()


        # For the banana
        if stats.level >= 2:
            if len(bananas) < 1:
                bananas.append(Banana(ao_settings, screen))
            for banana in bananas:
                banana.blitme(stats.game_active)
                if banana.rect.bottom > ao_settings.screen_height:
                    bananas.remove(banana)
                elif banana.rect.bottom > basket.rect.top and banana.rect.left > basket.rect.left and banana.rect.right < basket.rect.right:
                    bananas.remove(banana)

                    stats.score -= ao_settings.bananas_points
                    sb.prep_score()

        # For the bomb
        if stats.level >= 2:
            if len(bombs) < 1:
                bombs.append(Bombs(ao_settings, screen))
            for bomb in bombs:
                bomb.blitme(stats.game_active)
                if bomb.rect.bottom > ao_settings.screen_height:
                    bombs.remove(bomb)
                elif bomb.rect.bottom > basket.rect.top and bomb.rect.left > basket.rect.left and bomb.rect.right < basket.rect.right:
                    bombs.remove(bomb)
                    stats.game_over=True
                    # stats.score -= ao_settings.bombs_points
                    # sb.prep_score()

        #For the gold apple
        if stats.level >= 5:
            if len(goldapples) < 1:
                goldapples.append(GoldenApple(ao_settings, screen))
            for goldapple in goldapples:
                goldapple.blitme(stats.game_active)
                if goldapple.rect.bottom > ao_settings.screen_height:
                    goldapples.remove(goldapple)
                elif goldapple.rect.bottom > basket.rect.top and goldapple.rect.left > basket.rect.left and goldapple.rect.right < basket.rect.right:
                    goldapples.remove(goldapple)

                    stats.score += ao_settings.goldapples_points
                    sb.prep_score()

        # For the Cherry
        if stats.level >= 3:
            if len(cherrys) < 1:
                cherrys.append(Cherry(ao_settings, screen))
            for cherry in cherrys:
                cherry.blitme(stats.game_active)
                if cherry.rect.bottom > ao_settings.screen_height:
                    cherrys.remove(cherry)
                elif cherry.rect.bottom > basket.rect.top and cherry.rect.left > basket.rect.left and cherry.rect.right < basket.rect.right:
                    cherrys.remove(cherry)

                    stats.score -= ao_settings.cherrys_points
                    sb.prep_score()

        # For the Grape
        if stats.level >= 4:
            if len(grapes) < 1:
                grapes.append(Grape(ao_settings, screen))
            for grape in grapes:
                grape.blitme(stats.game_active)
                if grape.rect.bottom > ao_settings.screen_height:
                    grapes.remove(grape)
                elif grape.rect.bottom > basket.rect.top and grape.rect.left > basket.rect.left and grape.rect.right < basket.rect.right:
                    grapes.remove(grape)

                    stats.score -= ao_settings.grapes_points
                    sb.prep_score()

        # Level Up
        if stats.score % 50 == 0:
            stats.level = (stats.score // 50) + 1
            sb.prep_level()
        if stats.level >= 10:
            stats.game_end = True
        # Make the most recently drawn screen visible.
        pygame.display.flip()

# menu()
run_game()
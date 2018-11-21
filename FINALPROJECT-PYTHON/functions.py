import pygame, sys
import pygame.font

def check_events(ao_settings,basket,screen,stats,play_button,retry_button,apples,bananas, bombs):
    """Respond to keypresses and mouse events"""

    # Watch for keyboard and mouse events.
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()
        elif event.type == pygame.KEYDOWN:
            check_keydown_events(event, basket)
        elif event.type == pygame.KEYUP:
            check_keyup_events(event, basket)
        elif event.type == pygame.MOUSEBUTTONDOWN:
            mouse_x, mouse_y = pygame.mouse.get_pos()
            check_retry_button(stats, retry_button, mouse_x, mouse_y)
            check_play_button(stats, play_button, mouse_x, mouse_y)

def check_play_button(stats, play_button, mouse_x, mouse_y):
    """Start a new game when the player clicks play."""
    button_clicked = play_button.rect.collidepoint(mouse_x, mouse_y)
    if button_clicked and not stats.game_active:
        # Reset the game statistics
        stats.reset_stats()
        stats.game_active = True


def check_retry_button(stats, retry_button, mouse_x, mouse_y):
    """Start a new game when game over"""
    retry_clicked = retry_button.rect.collidepoint(mouse_x, mouse_y)
    if retry_clicked :
        stats.game_active = True
        stats.game_over = False
        stats.game_end= False
        stats.reset_stats()

def check_keydown_events(event, basket):
    """ Respond to keypresses."""
    if event.key == pygame.K_RIGHT:
        basket.moving_right = True
    elif event.key == pygame.K_LEFT:
        basket.moving_left = True

def check_keyup_events(event, basket):
    """ Respond to key releases."""
    if event.key == pygame.K_RIGHT:
        basket.moving_right = False
    elif event.key == pygame.K_LEFT:
        basket.moving_left = False


def update_screen(ao_settings, screen, stats,sb,basket, play_button,retry_button):
    """Update image on the screen and flip to the new screen"""
    # Redraw the screen during each pass through the loop
    screen.blit(ao_settings.background, [0, 0])
    basket.blitme()
    if stats.game_over :

        font = pygame.font.SysFont('Arial', 15)
        font_1 = pygame.font.SysFont('Arial',80)
        over = font.render('Your score was: '+str(stats.score), True, (0,0,0))
        game = font_1.render('GAME OVER',True,(0,255,255))
        screen.blit(game,(350,200))
        screen.blit(over,(500,300))
        stats.game_active = False

    elif stats.game_end :
        font = pygame.font.SysFont('Arial', 15)
        font_1 = pygame.font.SysFont('Arial',80)
        end = font.render('Your score was: '+str(stats.score), True, (0,0,0))
        game = font_1.render('You Win!',True,(0,255,255))
        screen.blit(game,(350,200))
        screen.blit(end,(500,300))
        stats.game_active = False

    # Draw the score information

    sb.show_score()

    #Draw the play button if the game is inactive.

    if not stats.game_active and (stats.game_over or stats.game_end):
        retry_button.draw_button()
    if not stats.game_active and not stats.game_over and not stats.game_end :
        play_button.draw_button()








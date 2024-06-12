# main_menu.py

import pygame
import sys
from button import Button
import settings
from screens.egg_hatching_screen import egg_hatching_screen
from screens.show_leaderboard import show_leaderboard

WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
GRAY = (169, 169, 169)

def main_menu(screen):
    menu_background_image = pygame.image.load(settings.menu_background_image_path)
    menu_background_image = pygame.transform.scale(menu_background_image, settings.screen_size)
    menu_font = pygame.font.Font(settings.font_path, settings.menu_font_size)

    start_button = Button(u'開始遊戲', (300, 200), menu_font, screen, GRAY, u'開始遊戲')
    exit_button = Button(u'結束遊戲', (300, 300), menu_font, screen, GRAY, u'結束遊戲')
    leaderboard_button = Button(u'查看排行榜', (300, 400), menu_font, screen, GRAY, u'查看排行榜')
    music_path = "Assets/Bgm/bl cut.mp3"
    pygame.mixer.music.load(music_path)
    pygame.mixer.music.play(-1)  # Play the music in a loop
    # if screen is None:
    #     print("Error: Screen is None!!")
    # else:
    #     print(screen)

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.mixer.music.stop()
                pygame.quit()
                sys.exit()
                

            if event.type == pygame.MOUSEBUTTONDOWN:
                if start_button.click(event):
                    egg_hatching_screen(screen)
                    start_button.release(event)
                if exit_button.click(event):
                    pygame.quit()
                    sys.exit()
                if leaderboard_button.click(event):
                    leaderboard_button.release(event)
                    show_leaderboard(screen)
                    
            # elif event.type == pygame.MOUSEBUTTONUP:
            #     start_button.release(event)
            #     exit_button.release(event)
            #     leaderboard_button.release(event)

        screen.blit(menu_background_image, (0, 0))
        start_button.show()
        exit_button.show()
        leaderboard_button.show()
        pygame.display.update()

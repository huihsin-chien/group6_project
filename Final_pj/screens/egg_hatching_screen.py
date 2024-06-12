import pygame
import sys
import random
import settings
from button import Button
from screens.game_screen import game_screen

WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
GRAY = (169, 169, 169)
heads_image = pygame.image.load('Assets\img\Resized\Male.jpg')
tails_image = pygame.image.load('Assets\img\Resized\Female.jpg')
menu_font = pygame.font.Font(settings.font_path, settings.menu_font_size)

def egg_hatching_screen(screen):
    # screen = pygame.display.get_surface()
    screen.fill(BLACK)
    title_text = menu_font.render('Gender Choosing', True, WHITE)
    screen.blit(title_text, (300, 50))
    toss_button = Button('TOSS', (450, 450), menu_font, screen, GRAY, '')
    toss_button.show()

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                if toss_button.click(event):
                    result = toss_coin()
                    display_result(screen,result)
                    pygame.time.wait(5000)
                    game_screen(screen)
        
        pygame.display.update()



def toss_coin():
    return random.choice(["Female", "Male"])

def display_result(screen, result):
    screen.fill((BLACK))  # 清屏，填充白色
    if result == "Female":
        screen.blit(heads_image, (300, 300))
    else:
        screen.blit(tails_image, (300, 300))
    pygame.display.flip()

if __name__ == "__main__":
    pygame.init()
    screen = pygame.display.set_mode((800, 600))  # 设置窗口大小
    egg_hatching_screen(screen)     


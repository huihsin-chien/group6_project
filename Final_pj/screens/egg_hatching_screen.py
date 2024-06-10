import pygame
import sys
from screens.game_screen import game_screen

WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
GRAY = (169, 169, 169)

def egg_hatching_screen(screen):
    # screen = pygame.display.get_surface()
    start_time = pygame.time.get_ticks()
    while True:
        current_time = pygame.time.get_ticks()
        if current_time - start_time >= 1000:  # 5 秒后跳转到游戏界面
            game_screen(screen)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()

        screen.fill(BLACK)  # 暂时用黑色背景表示孵蛋页面
        pygame.display.update()

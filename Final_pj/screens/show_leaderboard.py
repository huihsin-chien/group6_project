import pygame
import sys
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
GRAY = (169, 169, 169)

def show_leaderboard():
    screen = pygame.display.get_surface()
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()

        screen.fill(GRAY)  # 暂时用灰色背景表示排行榜页面
        pygame.display.update()

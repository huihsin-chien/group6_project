import pygame
import sys
import random
from screens.game_screen import game_screen

WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
GRAY = (169, 169, 169)

def egg_hatching_screen(screen):
    # screen = pygame.display.get_surface()
    start_time = pygame.time.get_ticks()
    while True:
        current_time = pygame.time.get_ticks()
        if current_time - start_time >= 1000:  # 1 秒后跳转到游戏界面
            game_screen(screen)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()

        screen.fill(BLACK)  # 暂时用黑色背景表示孵蛋页面
        pygame.display.update()


heads_image = pygame.image.load('Assets\img\Male.jpg')
tails_image = pygame.image.load('Assets\img\Female.jpg')

def toss_coin():
    return random.choice(["Female", "Male"])

def display_result(screen, result):
    screen.fill((255, 255, 255))  # 清屏，填充白色
    if result == "Female":
        screen.blit(heads_image, (0, 0))
    else:
        screen.blit(tails_image, (0, 0))
    pygame.display.flip()

def main():
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                result = toss_coin()
                display_result(result)


# main.py

import pygame
import sys
import settings
from screens.main_menu import main_menu

pygame.init()
screen = pygame.display.set_mode((800, 600))
pygame.display.set_caption('寵物蛋遊戲')

main_menu(screen)

import pygame

pygame.init()

canvas = pygame.display.set_mode((800, 600))

pygame.display.set_caption("Hello, Pygame!")
exit = False

while not exit:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            exit = True
    pygame.display.update()
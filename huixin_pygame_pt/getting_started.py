import pygame

pygame.init()
color = (255,0,0)
position = (0, 0)
rect_color = (0, 255, 0)


canvas = pygame.display.set_mode((800, 600))

pygame.display.set_caption("Show image!")

image = pygame.image.load(".\OneDrive\git_repo\group6_project\huixin_pygame_pt\image.JPG")
exit = False

while not exit:
    canvas.fill(color)
    canvas.blit(image, dest = position)


    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            exit = True
    pygame.draw.rect(canvas, rect_color, pygame.Rect(30,30,60,60))
    pygame.display.update()
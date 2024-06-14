import pygame
import sys
import random
import settings_general as settings
from button import Button
from screens.game_screen import game_screen
from screens.petname_input import petname
from pet import Pet

pet = Pet()
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
GRAY = (169, 169, 169)
heads_image = pygame.image.load('Assets/img/Resized/Male.jpg').convert_alpha()
heads_image_width, heads_image_height = heads_image.get_size()
for x in range(heads_image_width):
    for y in range(heads_image_height):
        # 获取像素的颜色
        r, g, b, a = heads_image.get_at((x, y))
        
        # 设置一个阈值，将接近白色的像素设置为透明
        if r > 200 and g > 200 and b > 200:
            heads_image.set_at((x, y), (r, g, b, 0))

tails_image = pygame.image.load('Assets/img/Resized/Female.jpg').convert_alpha()
tails_image_width, tails_image_height = tails_image.get_size()
for x in range(tails_image_width):
    for y in range(tails_image_height):
        # 获取像素的颜色
        r, g, b, a = tails_image.get_at((x, y))
        
        # 设置一个阈值，将接近白色的像素设置为透明
        if r > 200 and g > 200 and b > 200:
            tails_image.set_at((x, y), (r, g, b, 0))

menu_font = pygame.font.Font(settings.font_path, settings.menu_font_size)

def egg_hatching_screen(screen):
    # 随机决定宠物性别
    result = toss_coin()
    pet.gender = result
    pet_image = heads_image if result == "Male" else tails_image
    
    # 初始化滑杆位置
    slider_value = 0
    slider_dragging = False

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            elif event.type == pygame.MOUSEBUTTONDOWN:
                if slider_rect.collidepoint(event.pos):
                    slider_dragging = True
            elif event.type == pygame.MOUSEBUTTONUP:
                slider_dragging = False
            elif event.type == pygame.MOUSEMOTION:
                if slider_dragging:
                    slider_value = (event.pos[0] - 400) / 3
                    slider_value = max(0, min(slider_value, 100))

        if slider_value >= 100:
            if petname(screen, pet):
                game_screen(screen, pet)

        # 绘制背景和宠物图片
        # screen.fill(BLACK)
        #  game_background_image = pygame.image.load(settings.game_background_image_path)
        conan_bg_image = pygame.image.load("Assets\img\conan_wall.jpg")
        conan_bg_image = pygame.transform.scale(conan_bg_image, settings.screen_size)
        screen.blit(conan_bg_image, (0, 0))    
        screen.blit(pet_image, (350, 300))

        # 绘制门
        left_door_image = pygame.image.load("Assets/img/conan_left_door.jpg")
        right_door_image = pygame.image.load("Assets/img/conan_right_door.jpg")

        left_door_pos = 0 - slider_value * 3
        right_door_pos = 400 + slider_value * 3
        left_door_image = pygame.transform.scale(left_door_image, (400, 600))
        screen.blit(left_door_image, (left_door_pos, 0))
        right_door_image = pygame.transform.scale(right_door_image, (400,600))
        screen.blit(right_door_image, (right_door_pos, 0))

        # 绘制滑杆
        pygame.draw.rect(screen, GRAY, (400, 500, 300, 10))
        slider_x = 400 + slider_value * 3
        slider_rect = pygame.draw.rect(screen, WHITE, (slider_x, 490, 20, 30))

        pygame.display.update()

def toss_coin():
    return random.choice(["Female", "Male"])

if __name__ == "__main__":
    pygame.init()
    screen = pygame.display.set_mode((800, 600))  # 设置窗口大小
    egg_hatching_screen(screen)

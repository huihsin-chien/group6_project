import pygame
import sys
from time import time
from pet import Pet

pygame.init()
# eat1_image = pygame.image.load("path/to/your/eat1_image.png")
# eat2_image = pygame.image.load("path/to/your/eat2_image.png")

# # 缩放图片
# eat1_image = pygame.transform.scale(eat1_image, (150, 150))
# eat2_image = pygame.transform.scale(eat2_image, (150, 150))
pet = Pet()
def animate_images(screen, img1, img2, duration=3, switch_interval=0.5, x = pet.x, y = pet.y):
    start_time = time()
    last_switch_time = start_time
    current_image = img1
    
    while True:
        current_time = time()
        
        # 检查是否需要停止动画
        if current_time - start_time > duration:
            break
        
        # 检查是否需要切换图片
        if current_time - last_switch_time >= switch_interval:
            last_switch_time = current_time
            current_image = img2 if current_image == img1 else img1
        
        screen.blit(current_image, (x, y))
        
        # 更新显示
        pygame.display.flip()

        # 检查退出事件
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()



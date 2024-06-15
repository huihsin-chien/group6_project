import pygame
import sys
from time import time
from pet import Pet

pygame.init()

pet = Pet()
def animate_images(screen, img1, img2, duration=2, switch_interval=0.2, x = pet.x, y = pet.y):
    start_time = time()
    last_switch_time = start_time
    current_image = img1
    
    while True:
        current_time = time()
        
        # 检查是否需要停止动画
        if current_time - start_time > duration:
            # pygame.mixer.music.unpause()
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



from button import Button
import pygame
import settings_general as settings
import sys
from pet import Pet

WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
GRAY = (169, 169, 169)

menu_font = pygame.font.Font(settings.font_path, settings.menu_font_size)

def setting_screen(screen, pet):
    from screens.main_menu import main_menu
    
    # 初始化滑杆位置和大小
    slider_x = 300
    slider_y = 250
    slider_width = 200
    slider_height = 10
    slider_pos = pygame.mixer.music.get_volume() * slider_width

    resume_button = Button(u'繼續遊戲', (300, 300), menu_font, screen, GRAY, u'繼續遊戲')
    return_to_main_menu_button = Button(u'返回主畫面', (300, 375), menu_font, screen, GRAY, u'返回主畫面')
    
    dragging = False

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                slider_rect = pygame.Rect(slider_x, slider_y, slider_width, slider_height)
                if slider_rect.collidepoint(event.pos):
                    dragging = True
                if resume_button.click(event):
                    return
                if return_to_main_menu_button.click(event):
                    pet.reset()
                    screen.fill(BLACK)
                    main_menu(screen)
            elif event.type == pygame.MOUSEBUTTONUP:
                dragging = False
                resume_button.release(event)
                return_to_main_menu_button.release(event)
            elif event.type == pygame.MOUSEMOTION:
                if dragging:
                    slider_pos = max(0, min(event.pos[0] - slider_x, slider_width))
                    volume = slider_pos / slider_width
                    pygame.mixer.music.set_volume(volume)
                    # print(f"Current volume: {volume:.2f}")
        
        screen.fill(BLACK)
        
        # 绘制滑杆背景
        pygame.draw.rect(screen, GRAY, (slider_x, slider_y, slider_width, slider_height))
        
        # 绘制滑杆位置指示
        pygame.draw.rect(screen, WHITE, (slider_x + slider_pos - 5, slider_y - 5, 10, slider_height + 10))

        # 绘制“音量”文字
        volume_text = menu_font.render("音量", True, WHITE)
        screen.blit(volume_text, (slider_x, slider_y-40 ))
        
        resume_button.show()
        return_to_main_menu_button.show()
        pygame.display.update()

# if __name__ == "__main__":
#     pygame.init()
#     screen = pygame.display.set_mode((800, 600))  # 设置窗口大小
#     pet = Pet()
#     setting_screen(screen, pet)

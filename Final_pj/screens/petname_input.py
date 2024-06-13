import pygame
import sys
from button import Button
import settings


pygame.init()

pygame.display.set_caption("幫你的小寶貝取名字吧")

WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
GRAY = (169, 169, 169)
LIGHTGRAY = (211, 211, 211)

font = pygame.font.Font(settings.font_path, settings.menu_font_size)

# 初始化输入框内容
user_text = ''
input_active = False

# 创建输入框和确认按钮
input_box = pygame.Rect(250, 200, 300, 50)
confirm_button = pygame.Rect(350, 300, 100, 50)

# 主循环
def petname(screen):
    global user_text, input_active
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            elif event.type == pygame.MOUSEBUTTONDOWN:
                # 检查鼠标点击位置是否在输入框内
                if input_box.collidepoint(event.pos):
                    input_active = True
                else:
                    input_active = False
                # 检查鼠标点击位置是否在确认按钮内
                if confirm_button.collidepoint(event.pos):
                    print(f"愛寵名: {user_text}")
                    return True
            elif event.type == pygame.KEYDOWN:
                if input_active:
                    if event.key == pygame.K_RETURN:
                        print(f"愛寵名: {user_text}")
                        user_text = ''
                    elif event.key == pygame.K_BACKSPACE:
                        user_text = user_text[:-1]
                    else:
                        user_text += event.unicode

        # 绘制输入框和确认按钮
        pygame.draw.rect(screen, WHITE, (230, 180, 350, 200))
        pygame.draw.rect(screen, LIGHTGRAY if input_active else GRAY, input_box)
        pygame.draw.rect(screen, GRAY, confirm_button)
        # 绘制按钮文字
        confirm_text = font.render('確認', True, BLACK)
        screen.blit(confirm_text, (confirm_button.x + 20, confirm_button.y + 10))
        # 绘制输入框内容blit
        text_surface = font.render(user_text, True, BLACK)
        screen.blit(text_surface, (input_box.x + 10, input_box.y + 10))
        # 更新显示
        pygame.display.flip()

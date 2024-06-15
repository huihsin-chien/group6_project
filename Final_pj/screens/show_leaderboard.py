import pygame
import sys
from button import Button
import json
import settings_general as settings

WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
GRAY = (169, 169, 169)
menu_font = pygame.font.Font(settings.font_path, 24)
big_font = pygame.font.Font(settings.font_path, settings.menu_font_size)
def show_leaderboard(screen):
    scroll_offset = 0  # 用于记录滚动偏移量
    scroll_speed = 20  # 滚动速度
    dragging = False
    scrollbar_pos = 100  # 初始化滑块位置

    screen.fill(BLACK)
    title_text = big_font.render('Leaderboard', True, WHITE)
    screen.blit(title_text, (300, 50))
    return_button = Button('Return', (300, 500), menu_font, screen, GRAY, 'Return')
    return_button.show()
    pygame.display.update()

    while True:
        try:
            with open(settings.leaderboard_json_path, 'r') as f:
                data = json.load(f)
                # 按 hour 大小排序
                data.sort(key=lambda x: x['hour'], reverse=True)
        except FileNotFoundError:
            data = []

        screen.fill(BLACK)  # 清空屏幕
        screen.blit(title_text, (300, 50))  # 重新绘制标题

        # 计算内容高度
        content_height = 100 + len(data) * 50

        y_offset = 100 - scroll_offset  # 基于滚动偏移量调整起始y位置

        for idx, record in enumerate(data, start=1):
            # 仅显示在可见区域内的记录
            if 100 <= y_offset <= 450:  # 确保文字在标题下方并在Return按钮上方显示
                record_text = menu_font.render(f"{idx}. Hour: {record['hour']}, Hungry: {record['hungry_level']}, Happy: {record['happy_level']}, Healthy: {record['healthy_level']}", True, WHITE)
                screen.blit(record_text, (50, y_offset))
            y_offset += 50
        return_button.show()

        # 绘制滚动条背景
        scrollbar_rect = pygame.Rect(750, 100, 20, 400)
        pygame.draw.rect(screen, GRAY, scrollbar_rect)

        # 计算滚动条滑块高度和位置
        if content_height > 400:
            scrollbar_height = max(20, 400 * 400 // content_height)  # 最小高度为20像素
            scrollbar_pos = 100 + (400 - scrollbar_height) * scroll_offset // (content_height - 400)
            scrollbar_slider_rect = pygame.Rect(750, scrollbar_pos, 20, scrollbar_height)
            pygame.draw.rect(screen, WHITE, scrollbar_slider_rect)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                if return_button.click(event):
                    return
                # Check if scrollbar is clicked
                if scrollbar_slider_rect.collidepoint(event.pos):
                    dragging = True
                    mouse_y_start = event.pos[1]
                    scroll_start = scroll_offset
            elif event.type == pygame.MOUSEBUTTONUP:
                return_button.release(event)
                dragging = False
            elif event.type == pygame.MOUSEMOTION:
                if dragging:
                    delta_y = event.pos[1] - mouse_y_start
                    max_scroll_offset = max(0, content_height - 400)  # 限制最大滚动偏移量
                    scroll_offset = max(0, min(scroll_start + delta_y * (content_height / 400), max_scroll_offset))
            elif event.type == pygame.MOUSEWHEEL:  # 捕获鼠标滚轮事件
                scroll_offset -= event.y * scroll_speed  # 调整滚动偏移量，乘以20以增加滚动速度
                max_scroll_offset = max(0, content_height - 400)  # 限制最大滚动偏移量
                scroll_offset = max(0, min(scroll_offset, max_scroll_offset))  # 限制滚动范围

        pygame.display.update()

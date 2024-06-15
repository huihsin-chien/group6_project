import json
import pygame
import settings_general as settings

menu_font = pygame.font.Font(settings.font_path, 15)

WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
GRAY = (169, 169, 169)

def draw_progress_bar(screen, x, y, width, height, color, percentage):
    pygame.draw.rect(screen, BLACK, (x, y, width+1, height+1))
    pygame.draw.rect(screen, color, (x, y, width * percentage / 100, height))


def draw_chart(screen, data):
    if not data:
        return

    chart_rect = pygame.Rect(50, 100, 700, 400)
    pygame.draw.rect(screen, WHITE, chart_rect, 2)

    max_hour = max(record['hour'] for record in data)
    num_ticks = 10
    tick_interval = max_hour / num_ticks

    # Draw y-axis and ticks
    for i in range(num_ticks + 1):
        y = chart_rect.y + chart_rect.height - (i * chart_rect.height // num_ticks)
        hour_value = i * tick_interval
        tick_text = menu_font.render(f'{hour_value:.1f}', True, WHITE)
        screen.blit(tick_text, (chart_rect.x - 50, y - 10))
        pygame.draw.line(screen, WHITE, (chart_rect.x - 5, y), (chart_rect.x, y), 2)

    # Calculate bar width and padding
    num_bars = len(data)
    bar_width = chart_rect.width // (num_bars + (num_bars - 1) // 4)
    bar_padding = bar_width // 4

    for i, record in enumerate(data):
        x = chart_rect.x + i * (bar_width + bar_padding)
        hour_height = chart_rect.height * record['hour'] // max_hour
        y = chart_rect.y + chart_rect.height - hour_height

        bar_rect = pygame.Rect(x, y, bar_width, hour_height)
        pygame.draw.rect(screen, (0,0,255), bar_rect)

    y_label = menu_font.render('Hours', True, WHITE)
    screen.blit(y_label, (chart_rect.x - 50, chart_rect.y - 50))

    
    
def save_record(record, file_path='leaderboard.json'):
    try:
        with open(file_path, 'r') as f:
            data = json.load(f)
    except FileNotFoundError:
        data = []

    data.append(record)
    with open(file_path, 'w') as f:
        json.dump(data, f, indent=4)

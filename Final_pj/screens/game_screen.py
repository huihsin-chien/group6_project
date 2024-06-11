import pygame
import sys
from button import Button
from pet import Pet
import settings
from time import time
import random


WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
GRAY = (169, 169, 169)

pet = Pet()

menu_font = pygame.font.Font(settings.font_path, settings.menu_font_size)

def draw_progress_bar(screen, x, y, width, height, color, percentage):
    pygame.draw.rect(screen, BLACK, (x, y, width+1, height+1))
    pygame.draw.rect(screen, color, (x, y, width * percentage / 100, height))

def draw_pet_location(screen, pet_image_path):
    pet_image = pygame.image.load(pet_image_path)
    pet.rect = pet_image.get_rect()
    pet.rect.topleft = (pet.x, pet.y)
    img_width, img_height = pet_image.get_size()
    screen.blit(pet_image, pet.rect.topleft)
    return (img_width, img_height)

def draw_pet_attributes(screen, food_button, water_button):
    hungry_text = menu_font.render(f'Hungry Level', True, WHITE)
    screen.blit(hungry_text, (50, 50))
    draw_progress_bar(screen, 50, 100, 200, 20, (255, 0, 0), pet.hungry_level)

    happy_text = menu_font.render(f'Happy Level', True, WHITE)
    screen.blit(happy_text, (50, 100))
    draw_progress_bar(screen, 50, 150, 200, 20, (255, 255, 0), pet.happy_level)

    healthy_text = menu_font.render(f'Healthy Level', True, WHITE)
    screen.blit(healthy_text, (50, 150))
    draw_progress_bar(screen, 50, 200, 200, 20, (0, 255, 0), pet.healthy_level)

    food_button.show()
    water_button.show()

def draw_player_info(screen, shop_button, settings_button):
    state_text = menu_font.render(f'State: {pet.state}', True, WHITE)
    screen.blit(state_text, (500, 50))

    money_text = menu_font.render(f'Money: {pet.money}', True, WHITE)
    screen.blit(money_text, (500, 100))

    hour_text = menu_font.render(f'Hour: {pet.hour}', True, WHITE)
    screen.blit(hour_text, (500, 200))

    status_text = menu_font.render(f'Status: {pet.status}', True, WHITE)
    screen.blit(status_text, (500, 250))
    settings_button.show()
    shop_button.show()

def change_direction():
    pet.speed_x = random.choice([-1, 0, 1])
    pet.speed_y = random.choice([-1, 0, 1])

def game_screen(screen):
    last_update_time = time()
    direction_change_time = time()
    shop_button = Button(u'Shop', (500, 150), menu_font, screen, GRAY, u'Shop')
    food_button = Button(f'Food:{pet.food_amount}', (50, 200), menu_font, screen, GRAY, f'Food{pet.food_amount}')
    water_button = Button(f'Water:{pet.water_amount}', (50, 250), menu_font, screen, GRAY, f'Water:{pet.water_amount}')
    settings_button = Button(u'Settings', (500, 200), menu_font, screen, GRAY, u'Settings')

    pet_image_path = settings.baby_pet_image_path if pet.state == 'baby' else (settings.teen_pet_image_path if pet.state == 'teen' else settings.adult_pet_image_path)
    happy_pet_image_path = settings.happy_pet_image_path  # 假设这是宠物开心状态的图片路径
    pet_happy_start_time = 0
    pet_is_happy = False

    change_direction()

    while True:
        current_time = time()
        if pet.status == 'dead':
            game_over_screen(screen)
            break
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            

            if event.type == pygame.MOUSEBUTTONDOWN:
                if shop_button.click(event):
                    open_shop(screen)
                if food_button.click(event):
                    pet.feed()
                    food_button = Button(f'Food:{pet.food_amount}', (50, 200), menu_font, screen, GRAY, f'Food{pet.food_amount}')
                if water_button.click(event):
                    pet.drink()
                    water_button = Button(f'Water:{pet.water_amount}', (50, 250), menu_font, screen, GRAY, f'Water:{pet.water_amount}')
                if settings_button.click(event):
                    setting_screen(screen)
                # 检查是否点击宠物
                if pet.rect.collidepoint(event.pos):
                    pet.touch_pet()
                    pet_image_path = happy_pet_image_path
                    pet_happy_start_time = current_time
                    pet_is_happy = True

            elif event.type == pygame.MOUSEBUTTONUP:
                shop_button.release(event)
                food_button.release(event)
                water_button.release(event)

        # 恢复宠物原始图片
        if pet_is_happy and current_time - pet_happy_start_time > 2:  # 2秒钟后恢复原始图片
            pet_image_path = settings.baby_pet_image_path if pet.state == 'baby' else (settings.teen_pet_image_path if pet.state == 'teen' else settings.adult_pet_image_path)
            pet_is_happy = False

        screen.fill(BLACK)
        draw_pet_attributes(screen, food_button, water_button)
        draw_player_info(screen, shop_button, settings_button)
        img_width, img_height = draw_pet_location(screen, pet_image_path)

        if current_time - last_update_time >= 1:
            last_update_time = current_time
            pet.update_hour()

        if current_time - direction_change_time >= 1:  # change direction every 1 second
            direction_change_time = current_time
            change_direction()

        if current_time - last_update_time >= 0.5 and current_time - last_update_time <= 0.55 or \
           current_time - last_update_time >= 0.95 and current_time - last_update_time <= 1:
            pet.x += pet.speed_x
            pet.y += pet.speed_y

        #check if pet is out of screen
        if pet.x < 0:
            pet.x = 0
            change_direction()
        elif pet.x > screen.get_width() - img_width:
            pet.x = screen.get_width() - img_width
            change_direction()

        if pet.y < 0:
            pet.y = 0
            change_direction()
        elif pet.y > screen.get_height() - img_height:
            pet.y = screen.get_height() - img_height
            change_direction()

        pygame.display.update()

def open_shop(screen):
    buy_food_button = Button(u'Food: 3 dollar', (300, 200), menu_font, screen, GRAY, u'Food: 3 dollar')
    buy_water_button = Button(u'Water: 1 dollar', (300, 300), menu_font, screen, GRAY, u'Water: 1 dollar')
    return_to_game_button = Button(u'Return to Game', (300, 400), menu_font, screen, GRAY, u'Return to Game')
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                if buy_food_button.click(event):
                    pet.buy_food()
                if buy_water_button.click(event):
                    pet.buy_water()
                if return_to_game_button.click(event):
                    game_screen(screen)
            elif event.type == pygame.MOUSEBUTTONUP:
                buy_food_button.release(event)
                buy_water_button.release(event)
        screen.fill(BLACK)
        buy_food_button.show()
        buy_water_button.show()
        return_to_game_button.show()

        money_text = menu_font.render(f'Money: {pet.money}', True, WHITE)
        screen.blit(money_text, (500, 100))
        food_text = menu_font.render(f'Food: {pet.food_amount}', True, WHITE)
        screen.blit(food_text, (500, 150))
        water_text = menu_font.render(f'Water: {pet.water_amount}', True, WHITE)
        screen.blit(water_text, (500, 200))
        pygame.display.update()

def setting_screen(screen): #volumn, resume, return to main menu
    from screens.main_menu import main_menu
    vol_up_button = Button(u'Volume Up', (300, 200), menu_font, screen, GRAY, u'Volume Up')
    vol_down_button = Button(u'Volume Down', (300, 300), menu_font, screen, GRAY, u'Volume Down')
    resume_button = Button(u'Resume', (300, 400), menu_font, screen, GRAY, u'Resume')
    return_to_main_menu_button = Button(u'Return to Main Menu', (300, 500), menu_font, screen, GRAY, u'Return to Main Menu')
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                if vol_up_button.click(event):
                    pass
                if vol_down_button.click(event):
                    pass
                if resume_button.click(event):
                    game_screen(screen)
                if return_to_main_menu_button.click(event):
                    pet.reset()
                    screen.fill(BLACK)
                    main_menu(screen)
            elif event.type == pygame.MOUSEBUTTONUP:
                vol_up_button.release(event)
                vol_down_button.release(event)
                resume_button.release(event)
                return_to_main_menu_button.release(event)
        screen.fill(BLACK)
        vol_up_button.show()
        vol_down_button.show()
        resume_button.show()
        return_to_main_menu_button.show()
        pygame.display.update()
    
def draw_chart(screen, data):
    # 设置图表区域
    chart_rect = pygame.Rect(50, 100, 700, 400)
    pygame.draw.rect(screen, WHITE, chart_rect, 2)

    max_hour = max(record['hour'] for record in data)
    max_value = max(max(record['hungry_level'], record['happy_level'], record['healthy_level']) for record in data)

    # 绘制图表内容
    for i, record in enumerate(data):
        x = chart_rect.x + (i * chart_rect.width // len(data))
        hungry_height = chart_rect.height * record['hungry_level'] // max_value
        happy_height = chart_rect.height * record['happy_level'] // max_value
        healthy_height = chart_rect.height * record['healthy_level'] // max_value

        pygame.draw.rect(screen, (255, 0, 0), (x, chart_rect.y + chart_rect.height - hungry_height, 10, hungry_height))
        pygame.draw.rect(screen, (0, 255, 0), (x + 15, chart_rect.y + chart_rect.height - happy_height, 10, happy_height))
        pygame.draw.rect(screen, (0, 0, 255), (x + 30, chart_rect.y + chart_rect.height - healthy_height, 10, healthy_height))

def show_leaderboard_with_chart(screen):
    try:
        with open('leaderboard.json', 'r') as f:
            data = json.load(f)
    except FileNotFoundError:
        data = []

    screen.fill(BLACK)
    title_text = menu_font.render('Leaderboard', True, WHITE)
    screen.blit(title_text, (300, 50))

    draw_chart(screen, data)

    return_button = Button('Return', (300, 500), menu_font, screen, GRAY, 'Return')
    return_button.show()
    pygame.display.update()

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                if return_button.click(event):
                    return
            elif event.type == pygame.MOUSEBUTTONUP:
                return_button.release(event)


def game_over_screen(screen):
    from screens.main_menu import main_menu
    game_over_text = menu_font.render(u'Game Over', True, WHITE)
    screen.fill(BLACK)
    screen.blit(game_over_text, (300, 200))
    record_text = menu_font.render(f'Your final hour: {pet.hour}', True, WHITE)
    screen.blit(record_text, (300, 250))
    play_again_button = Button(u'Play Again', (300, 300), menu_font, screen, GRAY, u'Play Again')
    leaderboard_button = Button(u'Leaderboard', (300, 400), menu_font, screen, GRAY, u'Leaderboard')
    play_again_button.show()
    leaderboard_button.show()
    pygame.display.update()

    save_record(pet.get_summary())

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                if play_again_button.click(event):
                    pet.reset()
                    screen.fill(BLACK)
                    main_menu(screen)  # 返回游戏主菜单
                if leaderboard_button.click(event):
                    show_leaderboard_with_chart(screen)  # 显示排行榜
            elif event.type == pygame.MOUSEBUTTONUP:
                play_again_button.release(event)
                leaderboard_button.release(event)



import json

def save_record(record, file_path= settings.leaderboard_json_path):
    try:
        with open(file_path, 'r') as f:
            data = json.load(f)
    except FileNotFoundError:
        data = []

    data.append(record)
    with open(file_path, 'w') as f:
        json.dump(data, f, indent=4)
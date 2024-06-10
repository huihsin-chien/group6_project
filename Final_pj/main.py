import pygame
import sys
import settings
from button import Button

pygame.init()

screen = pygame.display.set_mode((800, 600))
pygame.display.set_caption('寵物蛋遊戲')

menu_background_image = pygame.image.load(settings.menu_background_image_path)

WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
GRAY = (169, 169, 169)

menu_font = pygame.font.Font(settings.font_path, settings.menu_font_size)

# 创建按钮
start_button = Button(u'開始遊戲', (300, 200), menu_font, GRAY, u'開始遊戲')
exit_button = Button(u'結束遊戲', (300, 300), menu_font, GRAY, u'結束遊戲')
leaderboard_button = Button(u'查看排行榜', (300, 400), menu_font, GRAY, u'查看排行榜')

# 主菜单界面
def main_menu():
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()

            if event.type == pygame.MOUSEBUTTONDOWN:
                if start_button.click(event):
                    egg_hatching_screen()
                if exit_button.click(event):
                    pygame.quit()
                    sys.exit()
                if leaderboard_button.click(event):
                    show_leaderboard()
            elif event.type == pygame.MOUSEBUTTONUP:
                start_button.release(event)
                exit_button.release(event)
                leaderboard_button.release(event)

        screen.blit(menu_background_image, (0, 0))
        start_button.show()
        exit_button.show()
        leaderboard_button.show()
        pygame.display.update()

# 孵蛋页面
def egg_hatching_screen():
    start_time = pygame.time.get_ticks()
    while True:
        current_time = pygame.time.get_ticks()
        if current_time - start_time >= 1000:  # 5 秒后跳转到游戏界面
            game_screen()
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()

        screen.fill(BLACK)  # 暂时用黑色背景表示孵蛋页面
        pygame.display.update()

# 查看排行榜页面
def show_leaderboard():
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()

        screen.fill(GRAY)  # 暂时用灰色背景表示排行榜页面
        pygame.display.update()

class Pet:
    def __init__(self):
        self.hour = 0  # 寵物活了幾小時
        self.status = 'hungry'  # 寵物狀態（hungry, full）
        self.hungry_level = 50  # 飢餓程度（0-100%）
        self.happy_level = 50  # 快樂程度（0-100%）
        self.healthy_level = 100  # 健康程度（0-100%）
        self.state = 'baby'  # 寵物狀態（baby, teens, adult）
        self.food_amount = 10  # 玩家擁有的食物數量
        self.water_amount = 10  # 玩家擁有的水數量
        self.money = 100  # 玩家擁有的金錢數量
        self.time_since_last_hour = 0  # 距离上次小时的时间

    def update_hour(self):
        self.time_since_last_hour += 1
        if self.time_since_last_hour >= 300:  # 每300帧（大约5秒）增加一小时
            self.hour += 1
            self.hungry_level -= 5
            self.time_since_last_hour = 0

            # 根据hour更改state
            if self.hour < 50:
                self.state = 'baby'
            elif self.hour < 150:
                self.state = 'teen'
            else:
                self.state = 'adult'

            # 更新status
            if self.hungry_level <= 0:
                self.status = 'dead'
            elif self.hungry_level <= 10:
                self.status = 'starving'
            elif self.hungry_level <= 20:
                self.status = 'hungry'
            else:
                self.status = 'full'

    def feed(self):
        if self.food_amount > 0:
            self.food_amount -= 1
            self.hungry_level += 10
            self.happy_level += 5
            self.healthy_level += 5

    def drink(self):
        if self.water_amount > 0:
            self.water_amount -= 1
            self.hungry_level += 5
            self.happy_level += 5
            self.healthy_level += 10

    def buy_food(self):
        if self.money >= 10:
            self.money -= 10
            self.food_amount += 5

    def buy_water(self):
        if self.money >= 10:
            self.money -= 10
            self.water_amount += 5

pet = Pet()

def draw_pet_attributes():
    # 绘制左侧寵物属性
    hungry_text = menu_font.render(f'Hungry Level: {pet.hungry_level}%', True, WHITE)
    screen.blit(hungry_text, (50, 50))

    happy_text = menu_font.render(f'Happy Level: {pet.happy_level}%', True, WHITE)
    screen.blit(happy_text, (50, 100))

    healthy_text = menu_font.render(f'Healthy Level: {pet.healthy_level}%', True, WHITE)
    screen.blit(healthy_text, (50, 150))

    # food_text = menu_font.render(f'Food Amount: {pet.food_amount}', True, WHITE)
    # screen.blit(food_text, (50, 200))

    # water_text = menu_font.render(f'Water Amount: {pet.water_amount}', True, WHITE)
    # screen.blit(water_text, (50, 250))
    food_button.show()
    water_button.show()

def draw_player_info():
    # 绘制右侧玩家信息
    state_text = menu_font.render(f'State: {pet.state}', True, WHITE)
    screen.blit(state_text, (500, 50))

    money_text = menu_font.render(f'Money: {pet.money}', True, WHITE)
    screen.blit(money_text, (500, 100))

    hour_text = menu_font.render(f'Hour: {pet.hour}', True, WHITE)
    screen.blit(hour_text, (500, 200))

    shop_button.show()

# 创建商店按钮
shop_button = Button(u'Shop', (500, 150), menu_font, GRAY,u'Shop')
food_button = Button(u'Food', (50, 200), menu_font, GRAY, u'Food')
water_button = Button(u'Water', (50, 250), menu_font, GRAY, u'Water')

def game_screen():
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()

            if event.type == pygame.MOUSEBUTTONDOWN:
                if shop_button.click(event):
                    open_shop()
                if food_button.click(event):
                    pet.feed()
                if water_button.click(event):
                    pet.drink()
            elif event.type == pygame.MOUSEBUTTONUP:
                shop_button.release(event)
                food_button.release(event)
                water_button.release(event)

        # 清空屏幕并填充黑色背景
        screen.fill(BLACK)

        # 绘制寵物属性和玩家信息
        draw_pet_attributes()
        draw_player_info()
        pet.update_hour()

        # 更新屏幕
        pygame.display.update()

def open_shop():
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()

        # 清空屏幕并填充黑色背景
        screen.fill(BLACK)
        pygame.display.update()

# 启动主菜单
main_menu()

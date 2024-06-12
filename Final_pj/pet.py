# from time import time
import pygame
import sys
import settings


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
        self.x = 200
        self.y = 400
        self.speed_x = 0.0000001
        self.speed_y = 0.0000001


    def update_hour(self):
        self.time_since_last_hour += 1
        if self.time_since_last_hour <= 9:  # 每3秒钟更新一次hour
            self.hour += 1
            if self.time_since_last_hour == 3 or self.time_since_last_hour == 6 or self.time_since_last_hour == 9:
                self.hungry_level -= 10
            if self.time_since_last_hour == 5 or self.time_since_last_hour == 0:
                self.happy_level -= 5
                self.money += 1
            if self.time_since_last_hour == 7:
                self.healthy_level -= 5
                
        else:
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
            # self.eating = True
            # eat1_image = pygame.image.load(settings.baby_eat1_image_path)
            # eat2_image = pygame.image.load(settings.baby_eat2_image_path)
            # eat1_image = pygame.transform.scale(eat1_image, (150,150))
            # eat2_image = pygame.transform.scale(eat2_image, (150,150))
            # last_switch_time = time()
            # self.eat_start_time = time()
            # current_image = eat1_image
            # switch_interval = 0.5
            # while self.eating:
            #     current_time = time()
            #     if current_time - self.eat_start_time > 3:  # 1秒后停止吃东西动画
            #         self.eating = False
            #         self.current_image = settings.baby_pet_image_path 
            #     # 檢查是否需要切換圖片
            #     elif current_time - last_switch_time >= switch_interval:
            #         last_switch_time = current_time
            #         # 切換圖片
            #         current_image = eat2_image if current_image == eat1_image else eat2_image
            #     # 繪製當前圖片
            #     draw_pet_location(screen, settings.listen_to_speech_pet_path)
            #     draw_pet_attributes(screen, food_button, water_button,speech_recognition_button)
            #     draw_player_info(screen, shop_button, settings_button)
            #     pygame.display.update()
            #     screen.blit(current_image, (0, 0))
            #     # 更新顯示
            #     pygame.display.flip()
            if self.hungry_level < 100:
                if (self.hungry_level + 10) > 100:
                    self.hungry_level = 100
                else:
                    self.hungry_level += 10
            else:
                self.hungry_level = 100

            if self.happy_level < 100:
                if (self.happy_level + 5) > 100:
                    self.happy_level = 100
                else:
                    self.happy_level += 5
            else:
                self.happy_level = 100

            if self.healthy_level < 100:
                if (self.healthy_level + 5) > 100:
                    self.healthy_level = 100
                else:
                    self.healthy_level += 5
            else:
                self.healthy_level = 100

    def drink(self):
        if self.water_amount > 0:
            self.water_amount -= 1
                
            if self.happy_level < 100:
                if (self.happy_level + 5) > 100:
                    self.happy_level = 100
                else:
                    self.happy_level += 5
            else:
                self.happy_level = 100

            if self.healthy_level < 100:
                if (self.healthy_level + 10) > 100:
                    self.healthy_level = 100
                else:
                    self.healthy_level += 10
            else:
                self.healthy_level = 100

    def buy_food(self):
        if self.money >= 3:
            self.money -= 3
            self.food_amount += 1

    def buy_water(self):
        if self.money >= 1:
            self.money -= 1
            self.water_amount += 1
    
    def touch_pet(self):
        if self.happy_level < 100:
            if (self.happy_level + 5) > 100:
                self.happy_level = 100
            else:
                self.happy_level += 5
        else:
            self.happy_level = 100
    
    def reset(self):
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
        self.x = 100
        self.y = 100
        self.speed_x = 0.0000001
        self.speed_y = 0.0000001
    def get_summary(self):
        return {
            'hour': self.hour,
            'hungry_level': self.hungry_level,
            'happy_level': self.happy_level,
            'healthy_level': self.healthy_level,
        }
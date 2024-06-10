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
        if self.hour % 10 == 0:
            self.happy_level -= 5
            self.money += 1
        if self.hour % 20 == 0:
            self.healthy_level -= 5
        

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
        if self.money >= 3:
            self.money -= 3
            self.food_amount += 1

    def buy_water(self):
        if self.money >= 1:
            self.money -= 1
            self.water_amount += 1

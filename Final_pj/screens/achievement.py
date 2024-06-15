import pygame
import sys
import settings_general as settings
from button import Button

pygame.init()

# 設定顯示視窗
screen_width, screen_height = 800, 600
screen = pygame.display.set_mode((screen_width, screen_height))
pygame.display.set_caption("Achievement Page")

# 顏色設定
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
GREEN = (0, 255, 0)
GRAY = (169, 169, 169)

# 字體設定
font = pygame.font.Font(settings.font_path, settings.menu_font_size)

# 成就類別
class Achievement:
    def __init__(self, name, position):
        self.name = name
        self.position = position
        self.completed = False
        self.animation_playing = False
        self.animation_frame = 0

    def complete(self):
        self.completed = True
        self.animation_playing = True

    def update(self):
        if self.animation_playing:
            self.animation_frame += 1
            if self.animation_frame > 30:  # 動畫播放幀數
                self.animation_playing = False
                self.animation_frame = 0

    def draw(self, screen):
        color = GREEN if self.completed else WHITE
        pygame.draw.rect(screen, color, (*self.position, 550, 40))
        text = font.render(self.name, True, BLACK)
        screen.blit(text, (self.position[0] + 10, self.position[1] + 10))

# 成就頁面類別
class AchievementPage:
    def __init__(self):
        names = ["寵物摸摸大師", "麥當勞叔叔", "有種餓叫媽媽覺得你餓", "甚麼球都接得到喔", "酒鬼"]
        self.achievements = [Achievement(name, (100 if i < 5 else 400, 50 + (i % 5) * 100)) for i, name in enumerate(names)]
        self.completed_achievements = [False] * len(self.achievements)

    def complete_achievement(self, index):
        if 0 <= index < len(self.achievements):
            self.achievements[index].complete()
            self.completed_achievements[index] = True

    def update(self):
        for achievement in self.achievements:
            achievement.update()

    def draw(self, screen):
        for achievement in self.achievements:
            achievement.draw(screen)

    def save_state(self):
        return self.completed_achievements

    def load_state(self, state):
        for i, completed in enumerate(state):
            if completed:
                self.achievements[i].complete()

# 主函數
def achievement(achieve=False, index=0, saved_state=None):
    clock = pygame.time.Clock()
    achievement_page = AchievementPage()
    if saved_state:
        achievement_page.load_state(saved_state)

    show_achievement_page = True

    while show_achievement_page:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            elif achieve:
                achievement_page.complete_achievement(index - 1)
                achieve = False
            elif event.type == pygame.MOUSEBUTTONDOWN:
                if return_button.click(event):
                    show_achievement_page = False
        screen.fill(BLACK)
        achievement_page.update()
        achievement_page.draw(screen)
        
        return_button = Button(u'Return', (300, 550), font, screen, GRAY, u'Return')
        return_button.show()
        
        pygame.display.flip()
        clock.tick(30)


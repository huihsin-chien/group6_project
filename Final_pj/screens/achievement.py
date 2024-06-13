import pygame
import sys
import pickle
import settings

pygame.init()

# 設定顯示視窗
screen_width, screen_height = 800, 600
screen = pygame.display.set_mode((screen_width, screen_height))
pygame.display.set_caption("Achievement Page")

# 顏色設定
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
GREEN = (0, 255, 0)

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
        pygame.draw.rect(screen, color, (*self.position, 150, 50))
        text = font.render(self.name, True, BLACK)
        screen.blit(text, (self.position[0] + 10, self.position[1] + 10))

# 成就頁面類別
class AchievementPage:
    def __init__(self):
        self.achievements = []
        self.load_achievements()

    def load_achievements(self):
        try:
            with open('achievements.pkl', 'rb') as f:
                self.achievements = pickle.load(f)
        except FileNotFoundError:
            for i in range(10):
                x = 100 if i < 5 else 400
                y = 50 + (i % 5) * 100
                self.achievements.append(Achievement(f"Achievement {i+1}", (x, y)))

    def save_achievements(self):
        with open('achievements.pkl', 'wb') as f:
            pickle.dump(self.achievements, f)

    def complete_achievement(self, index):
        if 0 <= index < len(self.achievements):
            self.achievements[index].complete()
            self.save_achievements()

    def update(self):
        for achievement in self.achievements:
            achievement.update()

    def draw(self, screen):
        for achievement in self.achievements:
            achievement.draw(screen)

# 主函數
def achievement():
    clock = pygame.time.Clock()
    achievement_page = AchievementPage()
    show_achievement_page = False

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_a:
                    show_achievement_page = not show_achievement_page
                elif event.key == pygame.K_c:
                    achievement_page.complete_achievement(0)

        screen.fill(BLACK)

        if show_achievement_page:
            achievement_page.update()
            achievement_page.draw(screen)

        pygame.display.flip()
        clock.tick(30)


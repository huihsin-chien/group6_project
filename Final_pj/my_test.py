import pytest
import pygame
from screens.achievement import AchievementPage, Button, Achievement

# Initialize Pygame since we're testing Pygame functionality
pygame.init()
screen = pygame.display.set_mode((800, 600))


# Test the Achievement class
def test_achievement_initialization():
    achievement = Achievement("Test Achievement", (100, 50))
    assert achievement.name == "Test Achievement"
    assert achievement.position == (100, 50)
    assert not achievement.completed
    assert not achievement.animation_playing
    assert achievement.animation_frame == 0

def test_achievement_complete():
    achievement = Achievement("Test Achievement", (100, 50))
    achievement.complete()
    assert achievement.completed
    assert achievement.animation_playing

# Test the AchievementPage class
def test_achievement_page_initialization():
    achievement_page = AchievementPage()
    assert len(achievement_page.achievements) == 5

def test_achievement_page_complete_achievement():
    achievement_page = AchievementPage()
    achievement_page.complete_achievement(0)
    assert achievement_page.achievements[0].completed
    assert achievement_page.achievement_message_counter == achievement_page.achievement_message_duration

def test_achievement_page_update():
    achievement_page = AchievementPage()
    achievement_page.complete_achievement(0)
    initial_counter = achievement_page.achievement_message_counter
    achievement_page.update()
    assert achievement_page.achievement_message_counter == initial_counter - 1

def test_achievement_page_draw():
    achievement_page = AchievementPage()
    achievement_page.complete_achievement(0)
    achievement_page.draw(screen)
    # This test will just check if the draw function executes without errors
    # Manual verification might be required to visually check the drawing

def test_draw_achievement_message():
    achievement_page = AchievementPage()
    achievement_page.show_achievement_complete_message()
    assert achievement_page.achievement_message_counter == achievement_page.achievement_message_duration
    achievement_page.draw_achievement_message(screen, index=0)
    # Similar to the above draw test, this will just check if the function executes without errors


if __name__ == "__main__":
    pytest.main()

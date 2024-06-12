import pygame
import sys
from button import Button
import settings

menu_font = pygame.font.Font(settings.font_path, settings.menu_font_size)

WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
GRAY = (169, 169, 169)

def open_shop(screen, pet):
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
                    return  # Simply return to go back to the game screen
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

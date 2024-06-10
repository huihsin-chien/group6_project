import pygame
import sys
from button import Button
from pet import Pet
import settings


WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
GRAY = (169, 169, 169)

pet = Pet()

menu_font = pygame.font.Font(settings.font_path, settings.menu_font_size)

def draw_pet_attributes(screen, food_button, water_button):
    
    hungry_text = menu_font.render(f'Hungry Level: {pet.hungry_level}%', True, WHITE)
    screen.blit(hungry_text, (50, 50))

    happy_text = menu_font.render(f'Happy Level: {pet.happy_level}%', True, WHITE)
    screen.blit(happy_text, (50, 100))

    healthy_text = menu_font.render(f'Healthy Level: {pet.healthy_level}%', True, WHITE)
    screen.blit(healthy_text, (50, 150))

    food_button.show()
    water_button.show()

def draw_player_info(screen, shop_button):
   
    state_text = menu_font.render(f'State: {pet.state}', True, WHITE)
    screen.blit(state_text, (500, 50))

    money_text = menu_font.render(f'Money: {pet.money}', True, WHITE)
    screen.blit(money_text, (500, 100))

    hour_text = menu_font.render(f'Hour: {pet.hour}', True, WHITE)
    screen.blit(hour_text, (500, 200))

    shop_button.show()

def game_screen(screen):

    shop_button = Button(u'Shop', (500, 150), menu_font,screen, GRAY, u'Shop')
    food_button = Button(u'Food', (50, 200), menu_font,screen, GRAY, u'Food')
    water_button = Button(u'Water', (50, 250), menu_font,screen, GRAY, u'Water')

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

        screen.fill(BLACK)
        draw_pet_attributes(screen, food_button, water_button)
        draw_player_info(screen, shop_button)
        pet.update_hour()
        pygame.display.update()

def open_shop():
    screen = pygame.display.get_surface()
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()

        screen.fill(BLACK)
        pygame.display.update()

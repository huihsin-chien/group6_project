import pytest
from unittest.mock import patch, Mock
from pet import Pet

@pytest.fixture
def pet():
    return Pet()

def test_initialization(pet):
    assert pet.hour == 0
    assert pet.status == 'hungry'
    assert pet.hungry_level == 50
    assert pet.happy_level == 100
    assert pet.healthy_level == 50
    assert pet.state == 'baby'
    assert pet.food_amount == 2
    assert pet.water_amount == 2
    assert pet.money == 100
    assert pet.time_since_last_hour == 0
    assert pet.x == 200
    assert pet.y == 400
    assert pet.speed_x == 1
    assert pet.speed_y == 0
    assert pet.name == ''
    assert pet.gender is None

def test_update_position(pet):
    pet.x = 100
    pet.y = 200
    pet.update_position()
    assert pet.rect.topleft == (100, 200)

def test_move(pet):
    pet.move()
    assert pet.x == 201
    assert pet.y == 400

@patch('screens.achievement.achievement')
def test_feed(mock_achievement, pet):
    pet.hungry_level = 10
    pet.feed()
    assert pet.food_amount == 1
    assert pet.hungry_level == 20
    assert pet.happy_level == 100
    assert pet.healthy_level == 55

    pet.food_amount = 0
    result = pet.feed()
    assert result == "no food"

@patch('screens.achievement.achievement')
def test_drink(mock_achievement, pet):
    pet.water_amount = 1
    pet.happy_level = 90
    pet.healthy_level = 90
    pet.drink()
    assert pet.water_amount == 0
    assert pet.happy_level == 95
    assert pet.healthy_level == 100

    pet.water_amount = 0
    result = pet.drink()
    assert result == "no water"

def test_buy_food(pet):
    pet.money = 5
    pet.buy_food()
    assert pet.money == 2
    assert pet.food_amount == 3

    pet.money = 2
    pet.buy_food()
    assert pet.money == 2
    assert pet.food_amount == 3

def test_buy_water(pet):
    pet.money = 2
    pet.buy_water()
    assert pet.money == 1
    assert pet.water_amount == 3

    pet.money = 0
    pet.buy_water()
    assert pet.money == 0
    assert pet.water_amount == 3

def test_touch_pet(pet):
    pet.happy_level = 90
    pet.touch_pet()
    assert pet.happy_level == 95

    pet.happy_level = 100
    pet.touch_pet()
    assert pet.happy_level == 100

def test_reset(pet):
    pet.reset()
    assert pet.hour == 0
    assert pet.status == 'hungry'
    assert pet.hungry_level == 50
    assert pet.happy_level == 100
    assert pet.healthy_level == 50
    assert pet.state == 'baby'
    assert pet.food_amount == 2
    assert pet.water_amount == 2
    assert pet.money == 100
    assert pet.time_since_last_hour == 0
    assert pet.x == 200
    assert pet.y == 400
    assert pet.speed_x == 1
    assert pet.speed_y == 0
    assert pet.name == ''
    assert pet.gender == ''

def test_get_summary(pet):
    summary = pet.get_summary()
    assert summary['hour'] == 0
    assert summary['hungry_level'] == 50
    assert summary['happy_level'] == 100
    assert summary['healthy_level'] == 50

@patch('pygame.image.load')
def test_pet_image_initialization(mock_load):
    mock_load.return_value = Mock()
    pet = Pet()
    assert pet.image == mock_load.return_value

def test_update_hour(pet):
    pet.time_since_last_hour = 8
    pet.hour = 4
    pet.update_hour()
    assert pet.hour == 5
    assert pet.state == 'teen'

    pet.time_since_last_hour = 3
    pet.hour = 49
    pet.update_hour()
    assert pet.hour == 50
    assert pet.state == 'adult'

from app import *


def test_score():
    butterscotch = Ingredient.load("Butterscotch: capacity -1, durability -2, flavor 6, texture 3, calories 8")
    cinnamon = Ingredient.load("Cinnamon: capacity 2, durability 3, flavor -2, texture -1, calories 3")

    recipe = Recipe()
    recipe.add_ingredient(butterscotch, 44)
    recipe.add_ingredient(cinnamon, 56)

    assert recipe.score() == 62842880

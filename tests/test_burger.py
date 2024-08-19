import pytest

from src.pytemplate.domain.models import Burger


def test_burger_with_all_ingredients():
    burger = Burger(bread="Wheat", patty="Beef", sauce=["Mayo", "Ketchup"], toppings=["Lettuce", "Tomato"])
    assert str(burger) == "Wheat Beef ['Mayo', 'Ketchup'] ['Lettuce', 'Tomato'] "


def test_burger_without_toppings():
    burger = Burger(bread="Wheat", patty="Beef", sauce=["Mayo", "Ketchup"])
    assert str(burger) == "Wheat Beef ['Mayo', 'Ketchup'] no toppings "


def test_burger_without_sauce():
    burger = Burger(bread="Wheat", patty="Beef", toppings=["Lettuce", "Tomato"])
    assert str(burger) == "Wheat Beef no sauce ['Lettuce', 'Tomato'] "


def test_burger_without_sauce_and_toppings():
    burger = Burger(bread="Wheat", patty="Beef")
    assert str(burger) == "Wheat Beef no sauce no toppings "

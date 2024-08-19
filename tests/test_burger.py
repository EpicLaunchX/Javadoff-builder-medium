import pytest

from src.pytemplate.domain.models import Burger


def test_burger_with_all_ingredients():
    burger = Burger("Wheat", "Beef", ["Mayo", "Ketchup"], ["Lettuce", "Tomato"])
    assert str(burger) == "Wheat Beef ['Mayo', 'Ketchup'] ['Lettuce', 'Tomato'] "


def test_burger_without_toppings():
    burger = Burger("Wheat", "Beef", ["Mayo", "Ketchup"])
    assert str(burger) == "Wheat Beef ['Mayo', 'Ketchup'] no toppings "


def test_burger_without_sauce():
    burger = Burger("Wheat", "Beef", toppings=["Lettuce", "Tomato"])
    assert str(burger) == "Wheat Beef no sauce ['Lettuce', 'Tomato'] "


def test_burger_without_sauce_and_toppings():
    burger = Burger("Wheat", "Beef")
    assert str(burger) == "Wheat Beef no sauce no toppings "

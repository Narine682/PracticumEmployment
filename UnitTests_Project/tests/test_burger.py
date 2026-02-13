import sys
import os

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
import pytest
from unittest.mock import Mock
from praktikum.burger import Burger
from praktikum.bun import Bun
from praktikum.ingredient import Ingredient
from praktikum.ingredient_types import INGREDIENT_TYPE_SAUCE, INGREDIENT_TYPE_FILLING

class TestBurger:
    def test_set_buns(self):
        """Проверяет, что булка корректно устанавливается в бургер"""
        burger = Burger()
        bun = Bun("white bun", 100)
        burger.set_buns(bun)
        assert burger.bun == bun


    def test_add_ingredient_adds_item_to_list(self):
        """Проверяет добавление ингредиента в бургер"""
        burger = Burger()
        ingredient = Ingredient(INGREDIENT_TYPE_FILLING, "cutlet", 100)
        burger.add_ingredient(ingredient)
        assert len(burger.ingredients) == 1
        assert burger.ingredients[0].name == "cutlet"


    def test_remove_ingredient_removes_item_from_list(self):
        """Проверка удаление ингредиента из списка ингредиентов"""
        burger = Burger()
        ingredient = Ingredient(INGREDIENT_TYPE_FILLING, "cutlet", 100)
        burger.ingredients = [ingredient]
        burger.remove_ingredient(0)
        assert len(burger.ingredients) == 0


    def test_move_ingredient_move_item_to_new_position(self):
        """Проверяет перемещение ингредиента внутри списка"""
        burger = Burger()
        i1 = Ingredient(INGREDIENT_TYPE_FILLING, "cutlet", 100)
        i2 = Ingredient(INGREDIENT_TYPE_SAUCE, "sauce", 50)
        burger.add_ingredient(i1)
        burger.add_ingredient(i2)
        burger.move_ingredient(0, 1)
        assert burger.ingredients[1] == i1


    def test_get_price_with_mock(self):
        """Проверяет корректность расчета цены бургера с моками"""
        burger = Burger()
        bun = Mock()
        bun.get_price.return_value = 100
        burger.set_buns(bun)

        ingredient1 = Mock()
        ingredient1.get_price.return_value = 50
        ingredient2 = Mock()
        ingredient2.get_price.return_value = 25

        burger.add_ingredient(ingredient1)
        burger.add_ingredient(ingredient2)
        assert burger.get_price() == 100 * 2 + 50 + 25


    def test_get_receipt(self, monkeypatch):
        """Проверяет корректность формирования чека бургера с моками"""
        burger = Burger()
        bun = Mock()
        bun.get_name.return_value = "black bun"
        bun.get_price.return_value = 100
        burger.set_buns(bun)

        ingredient = Mock()
        ingredient.get_name.return_value = "cutlet"
        ingredient.get_type.return_value = INGREDIENT_TYPE_FILLING
        ingredient.get_price.return_value = 50
        burger.add_ingredient(ingredient)

        text = burger.get_receipt()

        assert "(==== black bun ====)" in text
        assert "= filling cutlet =" in text
        assert "Price: 250" in text



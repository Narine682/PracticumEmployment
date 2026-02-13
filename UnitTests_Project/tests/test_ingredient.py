
import sys
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
import pytest
from praktikum.ingredient import Ingredient
from praktikum.ingredient_types import INGREDIENT_TYPE_SAUCE,INGREDIENT_TYPE_FILLING


class TestIngredient:
    @pytest.mark.parametrize("type_, name, price", [
        (INGREDIENT_TYPE_SAUCE, "hot sauce", 50),
        (INGREDIENT_TYPE_FILLING, "cutlet", 200)
    ])
    def test_ingredient_fields(self,type_,name, price):
        """Проверяет корректность полей и методов объекта Ingredient"""
        ingredient = Ingredient(type_,name,price)
        assert ingredient.get_type() == type_
        assert ingredient.get_name() == name
        assert ingredient.get_price() == price

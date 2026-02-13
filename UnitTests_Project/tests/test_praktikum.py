
import pytest
from unittest.mock import Mock
from praktikum.praktikum import main
from praktikum.burger import Burger
from praktikum.bun import Bun
from praktikum.database import Database
from praktikum.ingredient import Ingredient
from praktikum import praktikum
import importlib


class TestPraktikum:
    def test_main(self, monkeypatch, capsys):
        """Проверяет выполнение функции main с моками Database, Bun и Ingredient"""
        mock_db = Mock(spec=Database)

        mock_bun = Mock(spec=Bun)
        mock_bun.get_name.return_value = "black bun"
        mock_bun.get_price.return_value = 100
        mock_db.available_buns.return_value = [mock_bun]

        ingredient1 = Mock(spec=Ingredient)
        ingredient1.get_name.return_value = "ingredient1"
        ingredient1.get_type.return_value = "filling"
        ingredient1.get_price.return_value = 10

        ingredient2 = Mock(spec=Ingredient)
        ingredient2.get_name.return_value = "ingredient2"
        ingredient2.get_type.return_value = "filling"
        ingredient2.get_price.return_value = 20

        ingredient3 = Mock(spec=Ingredient)
        ingredient3.get_name.return_value = "ingredient3"
        ingredient3.get_type.return_value = "filling"
        ingredient3.get_price.return_value = 30

        ingredient4 = Mock(spec=Ingredient)
        ingredient4.get_name.return_value = "ingredient4"
        ingredient4.get_type.return_value = "sauce"
        ingredient4.get_price.return_value = 40



        mock_db.available_ingredients.return_value = [ingredient1, ingredient2, ingredient3, ingredient4
        ]

        monkeypatch.setattr("praktikum.praktikum.Database", lambda: mock_db)

        main()

        captured =capsys.readouterr()
        output = captured.out

        print(output)

        assert "black bun" in output
        assert any(x in output for x in ["ingredient1", "ingredient2", "ingredient3", "ingredient4"])
        assert "Price: " in output

    def test_run_as_main(self, monkeypatch):
        """Проверяет  выполнение модуля при __name__== '__main__' без запуска main"""
        monkeypatch.setattr(praktikum, "main", lambda: None)

        praktikum.__name__ = "__main__"
        importlib.reload(praktikum)

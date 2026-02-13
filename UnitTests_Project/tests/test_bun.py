
import sys
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
from praktikum.bun import Bun


class TestBun:
    def test_bun_fields_and_methods(self):
        """Проверяет, что Bun корректно сохраняет имя и цену, и методы возвращают правильные значения"""
        bun = Bun("white bun", 150)
        assert bun.get_name() == "white bun"
        assert bun.get_price() == 150

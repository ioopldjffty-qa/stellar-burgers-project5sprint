import sys
sys.path.insert(0, 'C:/Users/Ильяс/Desktop/stellar-burgers-project')
from praktikum.database import Database
from praktikum.bun import Bun
from praktikum.ingredient import Ingredient
from praktikum.ingredient_types import IngredientType

class TestDatabase:
    def test_available_buns(self):
        db = Database()
        buns = db.available_buns()
        assert len(buns) == 3

    def test_available_ingredients(self):
        db = Database()
        ingredients = db.available_ingredients()
        assert len(ingredients) == 6

    def test_buns_are_bun_objects(self):
        db = Database()
        buns = db.available_buns()
        for bun in buns:
            assert isinstance(bun, Bun)

    def test_ingredients_are_ingredient_objects(self):
        db = Database()
        ingredients = db.available_ingredients()
        for ing in ingredients:
            assert isinstance(ing, Ingredient)

    def test_ingredients_types_count(self):
        db = Database()
        ingredients = db.available_ingredients()
        sauces = [ing for ing in ingredients if ing.get_type() == IngredientType.SAUCE]
        fillings = [ing for ing in ingredients if ing.get_type() == IngredientType.FILLING]
        assert len(sauces) == 3
        assert len(fillings) == 3

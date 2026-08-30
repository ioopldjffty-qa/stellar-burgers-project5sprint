import sys
sys.path.insert(0, 'C:/Users/Ильяс/Desktop/stellar-burgers-project')
from praktikum.ingredient import Ingredient
from praktikum.ingredient_types import IngredientType

class TestIngredient:
    def test_get_type(self):
        ingredient = Ingredient(IngredientType.SAUCE, 'hot sauce', 100)
        assert ingredient.get_type() == IngredientType.SAUCE

    def test_get_name(self):
        ingredient = Ingredient(IngredientType.FILLING, 'cutlet', 100)
        assert ingredient.get_name() == 'cutlet'

    def test_get_price(self):
        ingredient = Ingredient(IngredientType.SAUCE, 'hot sauce', 100)
        assert ingredient.get_price() == 100

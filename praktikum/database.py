from praktikum.bun import Bun
from praktikum.ingredient import Ingredient
from praktikum.ingredient_types import IngredientType

class Database:
    def __init__(self):
        self.buns = [
            Bun("black bun", 100),
            Bun("white bun", 200),
            Bun("red bun", 300)
        ]
        self.ingredients = [
            Ingredient(IngredientType.SAUCE, "hot sauce", 100),
            Ingredient(IngredientType.SAUCE, "sour cream", 200),
            Ingredient(IngredientType.SAUCE, "chili sauce", 300),
            Ingredient(IngredientType.FILLING, "cutlet", 100),
            Ingredient(IngredientType.FILLING, "dinosaur", 200),
            Ingredient(IngredientType.FILLING, "sausage", 300)
        ]

    def available_buns(self) -> list:
        return self.buns

    def available_ingredients(self) -> list:
        return self.ingredients

from praktikum.ingredient_types import IngredientType

class Ingredient:
    def __init__(self, ingredient_type: IngredientType, name: str, price: float):
        self.ingredient_type = ingredient_type
        self.name = name
        self.price = price

    def get_type(self) -> IngredientType:
        return self.ingredient_type

    def get_name(self) -> str:
        return self.name

    def get_price(self) -> float:
        return self.price

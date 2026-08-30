from praktikum.bun import Bun
from praktikum.ingredient import Ingredient
from praktikum.ingredient_types import IngredientType

class Burger:
    def __init__(self):
        self.bun = None
        self.ingredients = []

    def set_buns(self, bun: Bun):
        self.bun = bun

    def add_ingredient(self, ingredient: Ingredient):
        self.ingredients.append(ingredient)

    def remove_ingredient(self, index: int):
        if 0 <= index < len(self.ingredients):
            del self.ingredients[index]

    def move_ingredient(self, index: int, new_index: int):
        if 0 <= index < len(self.ingredients) and 0 <= new_index < len(self.ingredients):
            ingredient = self.ingredients.pop(index)
            self.ingredients.insert(new_index, ingredient)

    def get_price(self) -> float:
        price = 0.0
        if self.bun:
            price += self.bun.get_price() * 2
        for ingredient in self.ingredients:
            price += ingredient.get_price()
        return price

    def get_receipt(self) -> list:
        receipt = []
        if self.bun:
            receipt.append(f"(==== {self.bun.get_name()} ====)")
        for ingredient in self.ingredients:
            if ingredient.get_type() == IngredientType.SAUCE:
                receipt.append(f"= sauce {ingredient.get_name()} =")
            else:
                receipt.append(f"= filling {ingredient.get_name()} =")
        if self.bun:
            receipt.append(f"(==== {self.bun.get_name()} ====)")
        receipt.append(f"Price: {self.get_price()}")
        return receipt

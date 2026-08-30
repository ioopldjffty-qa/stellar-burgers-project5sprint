import sys
sys.path.insert(0, 'C:/Users/Ильяс/Desktop/stellar-burgers-project')
from praktikum.burger import Burger
from praktikum.bun import Bun
from praktikum.ingredient import Ingredient
from praktikum.ingredient_types import IngredientType

class TestBurger:
    def test_set_buns(self):
        burger = Burger()
        bun = Bun('black bun', 100)
        burger.set_buns(bun)
        assert burger.bun == bun

    def test_add_ingredient(self):
        burger = Burger()
        ingredient = Ingredient(IngredientType.SAUCE, 'hot sauce', 100)
        burger.add_ingredient(ingredient)
        assert len(burger.ingredients) == 1

    def test_remove_ingredient(self):
        burger = Burger()
        ingredient = Ingredient(IngredientType.SAUCE, 'hot sauce', 100)
        burger.add_ingredient(ingredient)
        burger.remove_ingredient(0)
        assert len(burger.ingredients) == 0

    def test_move_ingredient(self):
        burger = Burger()
        sauce = Ingredient(IngredientType.SAUCE, 'hot sauce', 100)
        cutlet = Ingredient(IngredientType.FILLING, 'cutlet', 100)
        burger.add_ingredient(sauce)
        burger.add_ingredient(cutlet)
        burger.move_ingredient(0, 1)
        assert burger.ingredients[0] == cutlet
        assert burger.ingredients[1] == sauce

    def test_get_price(self):
        burger = Burger()
        bun = Bun('black bun', 100)
        burger.set_buns(bun)
        sauce = Ingredient(IngredientType.SAUCE, 'hot sauce', 100)
        cutlet = Ingredient(IngredientType.FILLING, 'cutlet', 200)
        burger.add_ingredient(sauce)
        burger.add_ingredient(cutlet)
        assert burger.get_price() == 500

    def test_get_receipt(self):
        burger = Burger()
        bun = Bun('black bun', 100)
        burger.set_buns(bun)
        sauce = Ingredient(IngredientType.SAUCE, 'hot sauce', 100)
        burger.add_ingredient(sauce)
        receipt = burger.get_receipt()
        assert receipt[0] == '(==== black bun ====)'
        assert receipt[1] == '= sauce hot sauce ='
        assert receipt[2] == '(==== black bun ====)'
        assert receipt[3] == 'Price: 300.0'

    def test_get_receipt_without_ingredients(self):
        burger = Burger()
        bun = Bun('white bun', 100)
        burger.set_buns(bun)
        receipt = burger.get_receipt()
        assert len(receipt) == 3  # две строки с булочкой и цена
        assert any("white bun" in line.lower() for line in receipt)

    def test_get_receipt_english(self):
        burger = Burger()
        bun = Bun('white bun', 100)
        burger.set_buns(bun)
        burger.add_ingredient(Ingredient(IngredientType.SAUCE, 'hot sauce', 50))
        receipt = burger.get_receipt()
        assert any("bun" in line.lower() for line in receipt)

    def test_add_duplicate_ingredient(self):
        burger = Burger()
        bun = Bun('white bun', 100)
        burger.set_buns(bun)
        ingredient = Ingredient(IngredientType.SAUCE, 'hot sauce', 50)
        burger.add_ingredient(ingredient)
        burger.add_ingredient(ingredient)
        assert len(burger.ingredients) == 2

    def test_get_receipt_upper_case(self):
        burger = Burger()
        bun = Bun('WHITE BUN', 100)
        burger.set_buns(bun)
        receipt = burger.get_receipt()
        assert any("WHITE BUN" in line for line in receipt)

    def test_get_price_with_ingredients(self):
        burger = Burger()
        bun = Bun('white bun', 100)
        burger.set_buns(bun)
        burger.add_ingredient(Ingredient(IngredientType.SAUCE, 'hot sauce', 50))
        burger.add_ingredient(Ingredient(IngredientType.FILLING, 'cutlet', 150))
        assert burger.get_price() == 400

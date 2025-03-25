from praktikum.ingredient import Ingredient
from data import IngredientData
import pytest


class TestIngredient:

    @pytest.mark.parametrize(
        'ingredient_type, ingredient_name, ingredient_price',
        [
            (IngredientData.TYPE[0], IngredientData.NAME[0], IngredientData.PRICE[0]),
            (IngredientData.TYPE[1], IngredientData.NAME[1], IngredientData.PRICE[1])
        ])
    def test_get_ingredient_type(self, ingredient_type, ingredient_name, ingredient_price):
        ingredient = Ingredient(ingredient_type=ingredient_type, name=ingredient_name, price=ingredient_price)
        assert ingredient.get_type() == ingredient_type

    @pytest.mark.parametrize(
        'ingredient_type, ingredient_name, ingredient_price',
        [
            (IngredientData.TYPE[0], IngredientData.NAME[0], IngredientData.PRICE[0]),
            (IngredientData.TYPE[1], IngredientData.NAME[1], IngredientData.PRICE[1])
        ])
    def test_get_name(self, ingredient_type, ingredient_name, ingredient_price):
        ingredient = Ingredient(ingredient_type=ingredient_type, name=ingredient_name, price=ingredient_price)
        assert ingredient.get_name() == ingredient_name

    @pytest.mark.parametrize(
        'ingredient_type, ingredient_name, ingredient_price',
        [
            (IngredientData.TYPE[0], IngredientData.NAME[0], IngredientData.PRICE[0]),
            (IngredientData.TYPE[1], IngredientData.NAME[1], IngredientData.PRICE[1])
        ])
    def test_get_price(self, ingredient_type, ingredient_name, ingredient_price):
        ingredient = Ingredient(ingredient_type=ingredient_type, name=ingredient_name, price=ingredient_price)
        assert ingredient.get_price() == ingredient_price

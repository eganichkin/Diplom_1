import pytest
from unittest.mock import Mock
from data import BunData, IngredientData
from praktikum.burger import Burger


@pytest.fixture()
def burger():
    return Burger()


@pytest.fixture()
def mock_bun():
    bun_mock = Mock()
    bun_mock.name = BunData.NAME[0]
    bun_mock.price = BunData.PRICE[0]
    bun_mock.get_name.return_value = BunData.NAME[0]
    bun_mock.get_price.return_value = BunData.PRICE[0]
    return bun_mock


@pytest.fixture()
def mock_ingredient():
    ingredient_mock = Mock()
    ingredient_mock.type = IngredientData.TYPE[IngredientData.INDEX]
    ingredient_mock.name = IngredientData.NAME[IngredientData.INDEX]
    ingredient_mock.price = IngredientData.PRICE[IngredientData.INDEX]
    ingredient_mock.get_type.return_value = IngredientData.TYPE[IngredientData.INDEX]
    ingredient_mock.get_name.return_value = IngredientData.NAME[IngredientData.INDEX]
    ingredient_mock.get_price.return_value = IngredientData.PRICE[IngredientData.INDEX]
    return ingredient_mock

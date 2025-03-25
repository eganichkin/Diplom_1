from data import BunData, IngredientData
from unittest.mock import Mock


class TestBurger:

    @staticmethod
    def mock_ingredient(index):
        ingredient_mock = Mock()
        ingredient_mock.type = IngredientData.TYPE[index]
        ingredient_mock.name = IngredientData.NAME[index]
        ingredient_mock.price = IngredientData.PRICE[index]
        ingredient_mock.get_type.return_value = IngredientData.TYPE[index]
        ingredient_mock.get_name.return_value = IngredientData.NAME[index]
        ingredient_mock.get_price.return_value = IngredientData.PRICE[index]
        return ingredient_mock

    @staticmethod
    def assert_ingredient_condition(ingredients, actual_index, expected_index, expected_length):
        return (ingredients[actual_index].name == IngredientData.NAME[expected_index]
                and ingredients[actual_index].type == IngredientData.TYPE[expected_index]
                and ingredients[actual_index].price == IngredientData.PRICE[expected_index]
                and len(ingredients) == expected_length)

    def add_ingredient_with_mock(self, burger, ingredient_index):
        burger.add_ingredient(self.mock_ingredient(ingredient_index))
        return burger.ingredients

    def add_two_ingredients(self, burger):
        self.add_ingredient_with_mock(burger, 0)
        self.add_ingredient_with_mock(burger, 1)

    def test_set_buns(self, burger, mock_bun):
        burger.set_buns(mock_bun)
        assert burger.bun.name == mock_bun.name and burger.bun.price == mock_bun.price

    def test_add_two_ingredients(self, burger):
        self.add_two_ingredients(burger)
        assert self.assert_ingredient_condition(burger.ingredients, 0, 0, 2)

    def test_remove_ingredient(self, burger):
        self.add_two_ingredients(burger)
        burger.remove_ingredient(1)
        assert self.assert_ingredient_condition(burger.ingredients, 0, 0, 1)

    def test_move_ingredient(self, burger):
        self.add_two_ingredients(burger)
        burger.move_ingredient(0, 1)
        assert self.assert_ingredient_condition(burger.ingredients, 0, 1, 2)

    def test_get_price(self, burger, mock_bun, mock_ingredient):
        burger.set_buns(mock_bun)
        self.add_two_ingredients(burger)
        expected_price = burger.get_price()
        actual_price = sum(IngredientData.PRICE) + 2 * BunData.PRICE[0]
        assert actual_price == expected_price

    def test_get_receipt(self, burger, mock_bun):
        burger.set_buns(mock_bun)
        self.add_two_ingredients(burger)

        actual_receipt = burger.get_receipt()
        expected_price = sum(IngredientData.PRICE) + 2 * BunData.PRICE[0]
        expected_receipt_list = [f'(==== {BunData.NAME[0]} ====)']

        for i in range(0, 2):
            expected_receipt_list.append(f'= {str(IngredientData.TYPE[i]).lower()} {IngredientData.NAME[i]} =')

        expected_receipt_list.append(f'(==== {BunData.NAME[0]} ====)\n')
        expected_receipt_list.append(f'Price: {expected_price}')
        expected_receipt = '\n'.join(expected_receipt_list)

        assert expected_receipt == actual_receipt

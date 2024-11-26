from praktikum.database import Database


class TestDatabase:
    def test_available_buns(self):
        database = Database()
        buns = database.available_buns()
        len_buns = len(buns)
        assert len_buns == 3 and buns[len_buns - 1].name == 'red bun'

    def test_available_ingredients(self):
        database = Database()
        ingredients = database.available_ingredients()
        len_ingredients = len(ingredients)
        assert len_ingredients == 6 and ingredients[len_ingredients - 1].name == 'sausage'

from praktikum.bun import Bun
from data import BunData
import pytest


class TestBun:
    @pytest.mark.parametrize(
        'bun_name, bun_price',
        [
            (BunData.NAME[0], BunData.PRICE[0]),
            (BunData.NAME[1], BunData.PRICE[1])
        ])
    def test_get_name(self, bun_name, bun_price):
        bun = Bun(name=bun_name, price=bun_price)
        assert bun.get_name() == bun_name

    @pytest.mark.parametrize(
        'bun_name, bun_price',
        [
            (BunData.NAME[0], BunData.PRICE[0]),
            (BunData.NAME[1], BunData.PRICE[1])
        ])
    def test_get_price(self, bun_name, bun_price):
        bun = Bun(name=bun_name, price=bun_price)
        assert bun.get_price() == bun_price

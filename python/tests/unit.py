"""Module for testing main.py
"""
import pytest
from freezegun import freeze_time
from main import even_odd, sum_all, time_of_day, Product, Shop


@pytest.mark.parametrize("new_val, expected", [(2, "even"), (3, "odd"), (0, "even"), (5, "odd")])
def test_even(new_val, expected):
    """Method for testing even()
    """
    assert even_odd(new_val) == expected

@pytest.mark.parametrize("new_val, expected", [([1, 2, 3, 4], 10), ([-10, 5, 7, 10], 12),
                                                ([10, 20, 30, 40], 100), ([-10], -10)])
def test_sum(new_val, expected):
    """Method for testing sum_all()
    """
    assert sum_all(*new_val) == expected

@freeze_time("2012-01-01 00:00:00")
def test_time_of_night():
    """Method for testing time_of_day()
    """
    assert time_of_day() == "night"

@freeze_time("2012-01-01 06:00:00")
def test_time_of_morning():
    """Method for testing time_of_day()
    """
    assert time_of_day() == "morning"

@freeze_time("2012-01-01 12:00:00")
def test_time_of_afternoon():
    """Method for testing time_of_day()
    """
    assert time_of_day() == "afternoon"

@pytest.fixture
def product_add():
    """Fixture method for testing add_quantity()
    """
    product = Product("apple", 15, 25)
    product.add_quantity()
    return product

@pytest.fixture
def product_sub():
    """Fixture method for testing subtract_quantity()
    """
    product = Product("apple", 15, 25)
    product.subtract_quantity()
    return product

@pytest.fixture
def product_set_price():
    """Fixture method for testing change_price()
    """
    product = Product("apple", 15, 25)
    product.change_price(20)
    return product.price

def test_product(product_sub, product_add, product_set_price):
    """Method for testing Product class
    """
    assert product_add.quantity == 26
    assert product_sub.quantity == 24
    assert product_set_price == 20

@pytest.fixture
def shop_add():
    """Fixture method for testing add_product()
    """
    shop = Shop([Product("apple", 15, 10), Product("banana", 30, 15), Product("orange", 30, 20)])
    shop.add_product(Product("pineapple", 50, 5))
    return shop.products[-1].title

@pytest.fixture
def shop_sell():
    """Fixture method for testing sell_product()
    """
    shop = Shop([Product("apple", 15, 10), Product("banana", 30, 15), Product("orange", 30, 20)])
    return shop.sell_product("apple", 10)

def test_shop(shop_add, shop_sell):
    """Method for testing Product class
    """
    assert shop_add == "pineapple"
    assert shop_sell == 150

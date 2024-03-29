"""
Протестируйте классы из модуля homework/models.py
"""
import pytest

from homework.models import Product, Cart


@pytest.fixture
def product():
    return Product("book", 100, "This is a book", 1000)

@pytest.fixture
def phone():
    return Product("phone", 10, "This is a phone", 100)

@pytest.fixture
def cart():
    return Cart()

class TestProducts:
    """
    Тестовый класс - это способ группировки ваших тестов по какой-то тематике
    Например, текущий класс группирует тесты на класс Product
    """

    def test_product_check_quantity(self, product, phone):
        # TODO напишите проверки на метод check_quantity
        assert product.check_quantity(101)
        assert not phone.check_quantity(1001)

    def test_product_buy(self, product):
        # TODO напишите проверки на метод buy
        product.buy(100)
        assert product.quantity == 900

    def test_product_buy_more_than_available(self, product, phone):
        # TODO напишите проверки на метод buy,
        #  которые ожидают ошибку ValueError при попытке купить больше, чем есть в наличии
        with pytest.raises(ValueError):
            product.buy(1001)
            phone.buy(101)


class TestCart:
    """
    TODO Напишите тесты на методы класса Cart
        На каждый метод у вас должен получиться отдельный тест
        На некоторые методы у вас может быть несколько тестов.
        Например, негативные тесты, ожидающие ошибку (используйте pytest.raises, чтобы проверить это)
    """

    def test_add_product_to_cart(self, cart, product):
        cart.add_product(product, 100)
        assert cart.products[product] == 100
        cart.add_product(product, 1)
        assert cart.products[product] == 101

    def test_remove_product_from_cart_more_than_available(self, cart, product):
        cart.add_product(product, 3)
        cart.remove_product(product, 10)
        assert cart.products == {}

    def test_remove_more_product_than_cart_have(self, cart, product, phone):
        cart.add_product(product, 3)
        cart.remove_product(product)
        assert cart.products == {}

    def test_remove_product_that_in_cart(self, cart, phone):
        cart.add_product(phone, 3)
        cart.remove_product(phone, 3)
        assert cart.products == {}

    def test_remove_product_from_cart(self, cart, product):
        cart.add_product(product, 3)
        cart.remove_product(product, 2)
        assert cart.products[product] == 1

    def test_clear_cart(self, cart, product, phone):
        cart.add_product(product, 1)
        cart.add_product(phone, 1)
        cart.clear()
        assert cart.products == {}

    def test_get_total_price(self, cart, product, phone):
        cart.add_product(product, 10)
        cart.add_product(phone, 2)
        assert cart.get_total_price() == 1020

    def test_buy_more_products_that_available(self, cart, product):
        cart.add_product(product, 1001)
        with pytest.raises(ValueError):
            cart.buy()

    def test_buy_products(self, cart, product):
        cart.add_product(product, 100)
        cart.buy()
        assert product.quantity == 900
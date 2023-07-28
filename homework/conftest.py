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
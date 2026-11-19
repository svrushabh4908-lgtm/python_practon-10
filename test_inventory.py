"""
Unit Testing for Product Inventory Management System.
"""

import pytest

from inventory import apply_discount, calculate_total_price, check_stock

# Tests for calculate_total_price()


def test_calculate_total_price():
    assert calculate_total_price(100, 5) == 500


def test_calculate_total_price_with_decimal():
    assert calculate_total_price(99.50, 2) == 199.0


def test_negative_price():
    with pytest.raises(ValueError):
        calculate_total_price(-100, 5)


def test_zero_quantity():
    with pytest.raises(ValueError):
        calculate_total_price(100, 0)


# Tests for apply_discount()


def test_apply_discount():
    assert apply_discount(1000, 10) == 900


def test_zero_discount():
    assert apply_discount(500, 0) == 500


def test_full_discount():
    assert apply_discount(1000, 100) == 0


def test_invalid_discount():
    with pytest.raises(ValueError):
        apply_discount(1000, 120)


# Tests for check_stock()


def test_stock_available():
    assert check_stock(20, 5) is True


def test_stock_unavailable():
    assert check_stock(3, 5) is False


def test_negative_stock():
    with pytest.raises(ValueError):
        check_stock(-10, 5)


def test_zero_requested_quantity():
    with pytest.raises(ValueError):
        check_stock(20, 0)


# Tests for invalid data types


def test_invalid_price_type():
    with pytest.raises(TypeError):
        calculate_total_price("100", 5)


def test_invalid_quantity_type():
    with pytest.raises(TypeError):
        calculate_total_price(100, 2.5)

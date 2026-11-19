"""
Product Inventory Management System
Main application logic.
"""

import logging
import math

logger = logging.getLogger(__name__)


def calculate_total_price(price, quantity):
    """
    Calculate total product price.

    Formula:
    Total Price = Price * Quantity
    """

    # Validate price
    if isinstance(price, bool) or not isinstance(price, (int, float)):
        logger.error("Invalid price type: %s", price)
        raise TypeError("Price must be a number")

    if not math.isfinite(price):
        logger.error("Price must be a finite number: %s", price)
        raise ValueError("Price must be finite")

    if price < 0:
        logger.error("Price cannot be negative: %s", price)
        raise ValueError("Price cannot be negative")

    # Validate quantity
    if isinstance(quantity, bool) or not isinstance(quantity, int):
        logger.error("Invalid quantity: %s", quantity)
        raise TypeError("Quantity must be an integer")

    if quantity <= 0:
        logger.error("Quantity must be greater than zero")
        raise ValueError("Quantity must be greater than zero")

    total = price * quantity

    logger.info("Total price calculated successfully: %.2f", total)

    return total


def apply_discount(total, discount_percent):
    """
    Apply percentage discount to the total amount.

    Formula:
    Discounted Amount = Total - (Total * Discount / 100)
    """

    if isinstance(total, bool) or not isinstance(total, (int, float)):
        logger.error("Invalid total amount: %s", total)
        raise TypeError("Total must be a number")

    if not math.isfinite(total):
        logger.error("Total must be finite: %s", total)
        raise ValueError("Total must be finite")

    if total < 0:
        logger.error("Total cannot be negative: %s", total)
        raise ValueError("Total cannot be negative")

    if isinstance(discount_percent, bool) or not isinstance(
        discount_percent, (int, float)
    ):
        logger.error("Invalid discount type: %s", discount_percent)
        raise TypeError("Discount must be a number")

    if not math.isfinite(discount_percent):
        logger.error("Discount must be finite: %s", discount_percent)
        raise ValueError("Discount must be finite")

    if not 0 <= discount_percent <= 100:
        logger.error("Invalid discount percentage: %s", discount_percent)
        raise ValueError("Discount must be between 0 and 100")

    discount_amount = total * discount_percent / 100

    final_amount = total - discount_amount

    logger.info(
        "Discount of %.2f%% applied successfully. Final amount: %.2f",
        discount_percent,
        final_amount,
    )

    return final_amount


def check_stock(available_stock, requested_quantity):
    """
    Check whether the requested product quantity is available.

    Returns:
        True  - If sufficient stock is available.
        False - If stock is insufficient.
    """

    if isinstance(available_stock, bool) or not isinstance(available_stock, int):
        logger.error("Available stock must be an integer")
        raise TypeError("Available stock must be an integer")

    if available_stock < 0:
        logger.error("Available stock cannot be negative")
        raise ValueError("Available stock cannot be negative")

    if isinstance(requested_quantity, bool) or not isinstance(requested_quantity, int):
        logger.error("Requested quantity must be an integer")
        raise TypeError("Requested quantity must be an integer")

    if requested_quantity <= 0:
        logger.error("Requested quantity must be greater than zero")
        raise ValueError("Requested quantity must be greater than zero")

    if requested_quantity <= available_stock:
        logger.info(
            "Stock available. Requested: %d, Available: %d",
            requested_quantity,
            available_stock,
        )

        return True

    logger.warning(
        "Insufficient stock. Requested: %d, Available: %d",
        requested_quantity,
        available_stock,
    )

    return False

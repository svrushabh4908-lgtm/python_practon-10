"""
Logging demonstration for Product Inventory Management.
"""

import logging

from inventory import apply_discount, calculate_total_price, check_stock

# Configure logging

logging.basicConfig(
    filename="application.log",
    level=logging.DEBUG,
    format="%(asctime)s - %(levelname)s - %(message)s",
)

logger = logging.getLogger(__name__)


def main():

    logger.debug("Inventory application started")

    try:
        # Calculate product price
        total = calculate_total_price(250, 4)

        logger.info("Product total price: ₹%.2f", total)

        # Apply discount
        final_amount = apply_discount(total, 10)

        logger.info("Final amount after discount: ₹%.2f", final_amount)

        # Check available stock
        stock = check_stock(20, 4)

        if stock:
            logger.info("Product stock is available")
        else:
            logger.warning("Product stock is not available")

        # Check insufficient stock
        check_stock(2, 5)

        # Demonstrate error handling
        try:
            calculate_total_price(-100, 2)

        except ValueError as error:
            logger.error("Invalid product price: %s", error)

        logger.info("Inventory application completed successfully")

    except Exception:
        logger.exception("Unexpected application error")
        raise


if __name__ == "__main__":
    main()

"""
Main program for Product Inventory Management System.
"""

from inventory import apply_discount, calculate_total_price, check_stock


def main():

    print("===================================")
    print(" PRODUCT INVENTORY MANAGEMENT")
    print("===================================")

    product_name = "Laptop"

    price = 50000
    quantity = 2
    discount_percent = 10
    available_stock = 10

    print("\nProduct Name:", product_name)
    print("Price:", price)
    print("Quantity:", quantity)

    # Calculate total price
    total = calculate_total_price(price, quantity)

    print("\nTotal Price: ₹", total)

    # Apply discount
    final_amount = apply_discount(total, discount_percent)

    print("Discount:", discount_percent, "%")
    print("Final Amount: ₹", final_amount)

    # Check stock
    stock = check_stock(available_stock, quantity)

    if stock:
        print("\nStock Status: Available")
        print("Order can be processed.")
    else:
        print("\nStock Status: Not Available")
        print("Insufficient stock.")

    print("\n===================================")
    print("       APPLICATION COMPLETED")
    print("===================================")


if __name__ == "__main__":
    main()

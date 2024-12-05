# E-Commerce Shopping Cart

This project is an E-Commerce Shopping Cart application that allows users to manage products in their shopping cart. Users can add, remove, and modify product quantities, as well as calculate totals with applicable taxes and discounts. The application includes a testing function to simulate common operations and edge cases.

## Features

1. **Add Product**: Add a specified quantity of a product to the shopping cart, checking for stock availability.
2. **Remove Product**: Remove a product from the shopping cart.
3. **Modify Product Quantity**: Change the quantity of a product in the cart, with options to reduce or completely remove it.
4. **Calculate Total**: Calculate the total price of items in the cart, including optional tax rates and discounts.
5. **Run Tests**: Execute a set of predefined tests to verify the functionality of the shopping cart operations.

## Usage

The application is designed to be run directly in Python. The main function includes a series of tests that demonstrate how to interact with the shopping cart. 

### Running the Application

1. Ensure you have Python installed on your machine.
2. Copy the provided code into a Python file (e.g., `E-commerceShoppingCart.py`).
3. Run the file using the command:
   ```bash
   python E-commerceShoppingCart.py
   ```

### Testing Operations

The tests included in the `run_tests` function simulate various operations:

- Adding products to the cart.
- Modifying quantities of products.
- Removing products from the cart.
- Calculating totals with tax and discounts.

You can modify or expand upon these tests as needed to cover additional scenarios or edge cases.

## Example Output

When running the tests, you will see output indicating the success or failure of each operation, along with the final calculated total. For example:
```
Added 3 of Apple to the cart.
Updated Apple quantity to 5.
Removed Banana from the cart.
Total with tax and discount applied: $1.65
```
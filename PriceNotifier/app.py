from price_notifier import PriceNotifier

# Show the products
def products_show(notifier):
    products = notifier.get_products()

    if not products:
        print('No products found')
        return

    print(f" Monitorized Products: {len(products)}".center(50, '='))

    for i, product in enumerate(products, 1):
        print(f" Product {i} ".center(50, '='))
        print(f"Name: {product['name']}")
        print(f"URL: {product['url']}")
        print(f"Current Price: {product.get('current_price', 'N/A')}")
        print(f"Wanted Price: {product.get('wanted_price')}")

        # Show the history if there is any
        if product.get('history'):
            print("Price History:")
            # Show the last 3 items
            for item in product['history'][-3:]:
                print(f"Date: {item['date']} - Price: {item['price']}")
        print()

def main():
    notifier = PriceNotifier()

    while True:
        print(" Price Notifier by David Caleb ".center(50, '='))
        print("1. Add Product")
        print("2. Show Products")
        print("3. Update Products")
        print("4. Remove Product")
        print("5. Exit")
        option = input("Select an option: (1-5): ")

        # Add a product
        if option == '1':
            name = input("Enter the name of the product: ")
            url = input("Enter the URL of the product: ")
            wanted_price = input("Enter the wanted price: ")

            use_selector = input("Do you want to use a CSS selector? (y/n): ").lower()
            selector_css = None
            if use_selector == 'y':
                selector_css = input("Enter the CSS selector: ")

            decimal_separator = input("What is the decimal separator? (. or ,) [for default ',']: ").strip()
            if decimal_separator not in ('.', ','):
                decimal_separator = ','
                print("Invalid separator, using ',' as default")
            result = notifier.add_product(name, url, wanted_price, selector_css, decimal_separator)

            if result:
                print(f"\nProduct {name} added successfully\n")
            else:
                print(f"\nError adding product '{name}' (Maybe the URL is invalid)")
        # Show the products
        elif option == '2':
            products_show(notifier)

        # Update the products
        elif option == '3':
            print("Updating Products".center(50, '='))
            updated_products = notifier.update_products()
            if updated_products:
                print(f"\n ¡They found {len(updated_products)} products that meet the conditions!")
                for product in updated_products:
                    print(f" - {product['name']} - Current Price: {product['current_price']}")
            else:
                print("\nNo products found that meet the conditions")

        # Remove a product
        elif option == '4':
            products_show(notifier)

            products = notifier.load_products()
            if products:
                try:
                    index = int(input("Enter the index of the product to remove: "))
                    if notifier.remove_product(index):
                        print(f"\nProduct #{index} removed successfully\n")
                    else:
                        print(f"\nNo product found with that #{index}")
                except ValueError:
                    print("Please enter a valid number")
            else:
                print("No products found")
        elif option == '5':
            print(f"\nExiting Price Notifier")
            break
        else:
            print("Invalid option. Please select a valid option (1-5)")

if __name__ == "__main__":
    main()
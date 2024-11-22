from Controller.controller import BakeryController
from View.view import BakeryView

def main():
    controller = BakeryController()

    while True:
        BakeryView.display_menu()
        
        choice = input("Choose an option (1-7): ")
        
        if choice == '1':
            items = controller.get_all_items()
            BakeryView.display_items(items)
        
        elif choice == '2':
            name, price, quantity = BakeryView.get_item_details()
            message = controller.add_item(name, price, quantity)
            BakeryView.display_success_message(message)
        
        elif choice == '3':
            index = BakeryView.get_item_index()
            message = controller.remove_item(index)
            BakeryView.display_success_message(message)

        elif choice == '4':
            index = BakeryView.get_item_index()
            new_name, new_price, new_quantity = BakeryView.get_update_details()
            message = controller.update_item(index,
                                            new_name if new_name else None,
                                            new_price,
                                            new_quantity)
            BakeryView.display_success_message(message)

        elif choice == '5':
            name = BakeryView.get_item_name()
            found_items = controller.search_item_by_name(name)
            
            if found_items:
                BakeryView.display_items(found_items)
            else:
                BakeryView.display_error_message("No items found with that name.")

        elif choice == '6':
            total_value = controller.total_inventory_value()
            BakeryView.display_total_value(total_value)

        elif choice == '7':
            print("Exiting the application. Goodbye!")
            break
        
        else:
            BakeryView.display_error_message("Invalid option. Please choose again.")

if __name__ == "__main__":
    main()
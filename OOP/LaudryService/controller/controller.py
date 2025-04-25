from typing import Optional
from model.model import LaundryModel, Order, OrderItem, Garment, SpecialWash
from view.view import LaundryView

# Main controller class handling application logic
class LaundryController:
    
    def __init__(self):
        self.model = LaundryModel()
        self.view = LaundryView()
        self.running = True

    # Main application loop
    def run(self):
        while self.running:
            self.view.clear_screen()
            choice = self.view.display_main_menu()
            
            if choice == "1":
                self.handle_order_management()
            elif choice == "2":
                self.handle_garment_management()
            elif choice == "3":
                self.handle_wash_management()
            elif choice == "4":
                self.handle_reports()
            elif choice == "5":
                self.running = False
                self.view.show_message("Thank you for using Laundry Service Management System!")
            else:
                self.view.show_error("Invalid choice! Please try again.")

    # Handle order management menu
    def handle_order_management(self):
        while True:
            self.view.clear_screen()
            choice = self.view.display_order_management_menu()
            
            if choice == "1":
                self.create_order()
            elif choice == "2":
                self.view_all_orders()
            elif choice == "3":
                self.view_order_details()
            elif choice == "4":
                self.update_order_status()
            elif choice == "5":
                self.delete_order()
            elif choice == "6":
                break
            else:
                self.view.show_error("Invalid choice! Please try again.")
            
            input("\nPress Enter to continue...")

    # Handle garment type management menu
    def handle_garment_management(self):
        while True:
            self.view.clear_screen()
            choice = self.view.display_garment_menu()
            
            if choice == "1":
                garments = self.model.get_all_garments()
                self.view.display_garments(garments)
            elif choice == "2":
                garment_id = self.view.get_order_id_input("Enter Garment ID: ")
                garment = self.model.get_garment_by_id(garment_id)
                if garment:
                    self.view.display_garment_details(garment)
                else:
                    self.view.show_error("Garment not found!")
            elif choice == "3":
                break
            else:
                self.view.show_error("Invalid choice! Please try again.")
            
            input("\nPress Enter to continue...")

    # Handle special wash management menu
    def handle_wash_management(self):
        while True:
            self.view.clear_screen()
            choice = self.view.display_wash_menu()
            
            if choice == "1":
                washes = self.model.get_all_special_washes()
                self.view.display_special_washes(washes)
            elif choice == "2":
                wash_id = self.view.get_order_id_input("Enter Wash Option ID: ")
                wash = self.model.get_special_wash_by_id(wash_id)
                if wash:
                    self.view.display_wash_details(wash)
                else:
                    self.view.show_error("Wash option not found!")
            elif choice == "3":
                break
            else:
                self.view.show_error("Invalid choice! Please try again.")
            
            input("\nPress Enter to continue...")

    # Handle reports menu
    def handle_reports(self):
        while True:
            self.view.clear_screen()
            choice = self.view.display_reports_menu()
            
            if choice == "1":
                status = input("Enter status to filter by (Pending/In Progress/Ready for Delivery/Delivered/Cancelled): ")
                orders = self.model.get_orders_by_status(status)
                self.view.display_orders_by_status(orders, status)
            elif choice == "2":
                customer_name = self.view.get_customer_name_input()
                orders = self.model.get_orders_by_customer(customer_name)
                self.view.display_orders_by_customer(orders, customer_name)
            elif choice == "3":
                orders = self.model.get_all_orders()
                self.view.display_revenue_report(orders)
            elif choice == "4":
                break
            else:
                self.view.show_error("Invalid choice! Please try again.")
            
            input("\nPress Enter to continue...")

    # Handle order creation
    def create_order(self):
        order_data = self.view.get_order_input()
        garments = self.model.get_all_garments()
        washes = self.model.get_all_special_washes()
        
        items_data = self.view.get_order_items_input(garments, washes)
        if not items_data:
            self.view.show_error("Order must have at least one item!")
            return
            
        # Convert items data to OrderItem objects
        items = [
            OrderItem(
                item["garment"],
                item["quantity"],
                item["special_washes"]
            ) for item in items_data
        ]
        
        order = self.model.create_order(
            order_data["customer_name"],
            order_data["contact_phone"],
            order_data["pickup_address"],
            order_data["delivery_address"],
            items
        )
        
        self.view.show_message(f"Order created successfully! Order ID: {order.order_id}")
        self.view.display_order_details(order)

    # Display all orders
    def view_all_orders(self):
        orders = self.model.get_all_orders()
        if orders:
            self.view.display_orders(orders)
        else:
            self.view.show_message("No orders found!")

    # Display details of a specific order
    def view_order_details(self):
        order_id = self.view.get_order_id_input()
        order = self.model.get_order(order_id)
        if order:
            self.view.display_order_details(order)
        else:
            self.view.show_error("Order not found!")

    # Update an order's status
    def update_order_status(self):
        order_id = self.view.get_order_id_input()
        order = self.model.get_order(order_id)
        if not order:
            self.view.show_error("Order not found!")
            return
            
        self.view.display_order_details(order)
        new_status = self.view.get_status_input()
        
        if self.model.update_order_status(order_id, new_status):
            self.view.show_message(f"Order status updated to {new_status} successfully!")
        else:
            self.view.show_error("Failed to update order status!")

    # Delete an order
    def delete_order(self):
        order_id = self.view.get_order_id_input()
        order = self.model.get_order(order_id)
        if not order:
            self.view.show_error("Order not found!")
            return
            
        self.view.display_order_details(order)
        confirm = input("Are you sure you want to delete this order? (y/n): ")
        if confirm.lower() == 'y':
            if self.model.delete_order(order_id):
                self.view.show_message("Order deleted successfully!")
            else:
                self.view.show_error("Failed to delete order!")
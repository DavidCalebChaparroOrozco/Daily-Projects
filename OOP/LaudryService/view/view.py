# Import necessary libraries
from typing import List, Optional
from datetime import datetime
from model.model import Garment, SpecialWash, Order, OrderItem

# Class handling all user interface interactions
class LaundryView:
    
    # Display the main menu
    def display_main_menu(self):
        print("\nLaundry Service Management System ")
        print("1. Order Management")
        print("2. Garment Types")
        print("3. Special Wash Options")
        print("4. Reports and Analytics")
        print("5. Exit")
        return input("Please select an option (1-5): ")

    # Display the order management menu
    def display_order_management_menu(self):
        print("\nOrder Management ")
        print("1. Create New Order")
        print("2. View All Orders")
        print("3. View Order Details")
        print("4. Update Order Status")
        print("5. Delete Order")
        print("6. Back to Main Menu")
        return input("Please select an option (1-6): ")

    # Display the garment types menu
    def display_garment_menu(self):
        print("\nGarment Types ")
        print("1. View All Garment Types")
        print("2. View Garment Details")
        print("3. Back to Main Menu")
        return input("Please select an option (1-3): ")

    # Display the special wash menu
    def display_wash_menu(self):
        print("\nSpecial Wash Options ")
        print("1. View All Wash Options")
        print("2. View Wash Option Details")
        print("3. Back to Main Menu")
        return input("Please select an option (1-3): ")

    # Display the reports menu
    def display_reports_menu(self):
        print("\nReports and Analytics ")
        print("1. Orders by Status")
        print("2. Orders by Customer")
        print("3. Revenue Report")
        print("4. Back to Main Menu")
        return input("Please select an option (1-4): ")

    # Display a list of garment types
    def display_garments(self, garments: List[Garment]):
        print("\nGarment Types ")
        for garment in garments:
            print(f"{garment.garment_id}. {garment.name} - Base Price: ${garment.base_price:.2f} - Wash Time: {garment.wash_time} hours")

    # Display details of a specific garment
    def display_garment_details(self, garment: Garment):
        print("\nGarment Details ")
        print(f"ID: {garment.garment_id}")
        print(f"Name: {garment.name}")
        print(f"Base Price: ${garment.base_price:.2f}")
        print(f"Standard Wash Time: {garment.wash_time} hours")

    # Display a list of special wash options
    def display_special_washes(self, washes: List[SpecialWash]):
        print("\nSpecial Wash Options ")
        for wash in washes:
            print(f"{wash.wash_id}. {wash.name} - Price Multiplier: {wash.price_multiplier:.1f}x")

    # Display details of a special wash option
    def display_wash_details(self, wash: SpecialWash):
        print("\nSpecial Wash Details ")
        print(f"ID: {wash.wash_id}")
        print(f"Name: {wash.name}")
        print(f"Description: {wash.description}")
        print(f"Price Multiplier: {wash.price_multiplier:.1f}x base price")

    # Display a list of orders
    def display_orders(self, orders: List[Order]):
        print("\nOrders ")
        for order in orders:
            print(f"{order.order_id}. {order.customer_name} - Status: {order.status} - Total: ${order.calculate_total_price():.2f}")

    # Display details of a specific order
    def display_order_details(self, order: Order):
        print("\nOrder Details ")
        print(f"Order ID: {order.order_id}")
        print(f"Customer: {order.customer_name}")
        print(f"Contact Phone: {order.contact_phone}")
        print(f"Pickup Address: {order.pickup_address}")
        print(f"Delivery Address: {order.delivery_address}")
        print(f"Order Date: {order.order_date.strftime('%Y-%m-%d %H:%M')}")
        print(f"Estimated Completion: {order.estimated_completion.strftime('%Y-%m-%d %H:%M')}")
        print(f"Status: {order.status}")
        print("\nItems:")
        for item in order.items:
            print(f"- {item.quantity}x {item.garment.name}", end="")
            if item.special_washes:
                print(" (Special washes: ", end="")
                print(", ".join(wash.name for wash in item.special_washes), end=")")
            print(f" - Item Total: ${item.calculate_price():.2f}")
        print(f"\nOrder Total: ${order.calculate_total_price():.2f}")

    # Display orders filtered by status
    def display_orders_by_status(self, orders: List[Order], status: str):
        print(f"\nOrders with Status: {status} ")
        self.display_orders(orders)

    # Display orders filtered by customer
    def display_orders_by_customer(self, orders: List[Order], customer_name: str):
        print(f"\nOrders for Customer: {customer_name} ")
        self.display_orders(orders)

    # Display a revenue report
    def display_revenue_report(self, orders: List[Order]):
        print("\nRevenue Report ")
        total_revenue = sum(order.calculate_total_price() for order in orders)
        pending_orders = [o for o in orders if o.status == "Pending"]
        in_progress_orders = [o for o in orders if o.status == "In Progress"]
        delivered_orders = [o for o in orders if o.status == "Delivered"]
        
        print(f"Total Orders: {len(orders)}")
        print(f"Total Revenue: ${total_revenue:.2f}")
        print(f"Pending Orders: {len(pending_orders)}")
        print(f"In Progress Orders: {len(in_progress_orders)}")
        print(f"Delivered Orders: {len(delivered_orders)}")

    # Get input for creating a new order
    def get_order_input(self) -> dict:
        print("\nCreate New Order ")
        customer_name = input("Customer Name: ")
        contact_phone = input("Contact Phone: ")
        pickup_address = input("Pickup Address: ")
        delivery_address = input("Delivery Address (leave empty if same as pickup): ")
        
        if not delivery_address:
            delivery_address = pickup_address
            
        return {
            "customer_name": customer_name,
            "contact_phone": contact_phone,
            "pickup_address": pickup_address,
            "delivery_address": delivery_address
        }

    # Get input for order items
    def get_order_items_input(self, garments: List[Garment], washes: List[SpecialWash]) -> List[dict]:
        items = []
        while True:
            print("\nAdd Item to Order ")
            self.display_garments(garments)
            garment_id = int(input("Select garment ID (0 to finish): "))
            
            if garment_id == 0:
                break
                
            garment = next((g for g in garments if g.garment_id == garment_id), None)
            if not garment:
                print("Invalid garment ID!")
                continue
                
            quantity = int(input("Quantity: "))
            if quantity <= 0:
                print("Quantity must be positive!")
                continue
                
            special_washes = []
            if input("Add special washes? (y/n): ").lower() == 'y':
                self.display_special_washes(washes)
                wash_ids = input("Enter wash IDs separated by commas (or leave blank): ")
                if wash_ids:
                    for wash_id in wash_ids.split(','):
                        try:
                            wash_id = int(wash_id.strip())
                            wash = next((w for w in washes if w.wash_id == wash_id), None)
                            if wash:
                                special_washes.append(wash)
                            else:
                                print(f"Invalid wash ID: {wash_id}")
                        except ValueError:
                            print(f"Invalid input: {wash_id}")
            
            items.append({
                "garment": garment,
                "quantity": quantity,
                "special_washes": special_washes
            })
            
        return items

    # Get an order ID from user input
    def get_order_id_input(self, prompt: str = "Enter Order ID: ") -> int:
        try:
            return int(input(prompt))
        except ValueError:
            print("Invalid input! Please enter a number.")
            return -1

    # Get a new status from user input
    def get_status_input(self) -> str:
        print("\nAvailable statuses:")
        print("1. Pending")
        print("2. In Progress")
        print("3. Ready for Delivery")
        print("4. Delivered")
        print("5. Cancelled")
        
        choice = input("Select new status (1-5): ")
        status_map = {
            "1": "Pending",
            "2": "In Progress",
            "3": "Ready for Delivery",
            "4": "Delivered",
            "5": "Cancelled"
        }
        return status_map.get(choice, "Pending")

    # Get a customer name for filtering
    def get_customer_name_input(self) -> str:
        return input("Enter customer name to search: ")

    # Display a message to the user
    def show_message(self, message: str):
        print(f"\n{message}")

    # Display an error message to the user
    def show_error(self, error: str):
        print(f"\nERROR: {error}")

    # Clear the console screen
    def clear_screen(self):
        # Simple way to "clear" the screen
        print("\n" * 2)
        # print("=".center(50, "="))
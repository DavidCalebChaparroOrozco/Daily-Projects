# Import necessary libraries
import json
import os
from datetime import datetime, timedelta
from typing import List, Dict, Optional, Union

# Class representing a garment type
class Garment:
    def __init__(self, garment_id: int, name: str, base_price: float, wash_time: int):
        """
        garment_id: Unique ID for the garment type
        name: Name of the garment type
        base_price: Base price for washing this garment
        wash_time: Time required to wash (in hours)
        """
        self.garment_id = garment_id
        self.name = name
        self.base_price = base_price
        self.wash_time = wash_time

# Class representing a special wash option
class SpecialWash:
    def __init__(self, wash_id: int, name: str, description: str, price_multiplier: float):
        """
        wash_id: Unique ID for the wash option
        name: Name of the wash option
        description: Description of the wash
        price_multiplier: Multiplier for the base price
        """
        self.wash_id = wash_id
        self.name = name
        self.description = description
        self.price_multiplier = price_multiplier

# Class representing an item in an order
class OrderItem:
    def __init__(self, garment: Garment, quantity: int, special_washes: List[SpecialWash]):
        """
        garment: Garment type
        quantity: Quantity of this garment
        special_washes: List of special washes applied
        """
        self.garment = garment
        self.quantity = quantity
        self.special_washes = special_washes

    # Calculate the total price for this order item
    def calculate_price(self) -> float:
        base_total = self.garment.base_price * self.quantity
        special_total = sum(wash.price_multiplier for wash in self.special_washes) * base_total
        return base_total + special_total

    # Calculate the total wash time for this order item
    def calculate_wash_time(self) -> int:
        return self.garment.wash_time * (1 + len(self.special_washes) * 0.2)  # Each special wash adds 20% time

# Class representing a customer order
class Order:
    def __init__(self, order_id: int, customer_name: str, contact_phone: str, 
                    pickup_address: str, delivery_address: str, items: List[OrderItem]):
        """
        order_id: Unique order ID
        customer_name: Customer's name
        contact_phone: Customer's phone number
        pickup_address: Pickup address
        delivery_address: Delivery address
        items: List of order items
        """
        self.order_id = order_id
        self.customer_name = customer_name
        self.contact_phone = contact_phone
        self.pickup_address = pickup_address
        self.delivery_address = delivery_address
        self.items = items
        self.order_date = datetime.now()
        # Pending, In Progress, Ready for Delivery, Delivered, Cancelled
        self.status = "Pending"  
        self.estimated_completion = self._calculate_completion_time()

    # Calculate estimated completion time based on items
    def _calculate_completion_time(self) -> datetime:
        total_hours = sum(item.calculate_wash_time() for item in self.items)
        return self.order_date + timedelta(hours=total_hours)

    # Calculate the total price for the order
    def calculate_total_price(self) -> float:
        return sum(item.calculate_price() for item in self.items)

    # Update the order status
    def update_status(self, new_status: str):
        valid_statuses = ["Pending", "In Progress", "Ready for Delivery", "Delivered", "Cancelled"]
        if new_status in valid_statuses:
            self.status = new_status
        else:
            raise ValueError(f"Invalid status. Must be one of: {', '.join(valid_statuses)}")

# Main model class handling data storage and operations
class LaundryModel:
    def __init__(self):
        self.orders: Dict[int, Order] = {}
        self.garments: Dict[int, Garment] = {}
        self.special_washes: Dict[int, SpecialWash] = {}
        self.next_order_id = 1
        self._initialize_sample_data()
        self._load_data()

    # Initialize with sample data if no data exists
    def _initialize_sample_data(self):
        if not self.garments:
            self.garments = {
                1: Garment(1, "T-Shirt", 5.0, 1),
                2: Garment(2, "Jeans", 8.0, 2),
                3: Garment(3, "Dress", 12.0, 3),
                4: Garment(4, "Suit", 20.0, 4),
                5: Garment(5, "Bed Sheet", 15.0, 3)
            }

        if not self.special_washes:
            self.special_washes = {
                1: SpecialWash(1, "Eco Wash", "Environmentally friendly wash", 0.2),
                2: SpecialWash(2, "Quick Wash", "Faster delivery", 0.3),
                3: SpecialWash(3, "Delicate Wash", "For fragile fabrics", 0.4),
                4: SpecialWash(4, "Stain Removal", "Special stain treatment", 0.5),
                5: SpecialWash(5, "Ironing", "Professional ironing", 0.3)
            }

    # Load data from JSON files if they exist
    def _load_data(self):
        try:
            if os.path.exists("orders.json"):
                with open("orders.json", "r") as f:
                    orders_data = json.load(f)
                    for order_id, order_data in orders_data.items():
                        items = []
                        for item_data in order_data["items"]:
                            garment = self.garments[item_data["garment_id"]]
                            special_washes = [self.special_washes[wash_id] for wash_id in item_data["special_washes"]]
                            items.append(OrderItem(garment, item_data["quantity"], special_washes))
                        
                        order = Order(
                            int(order_id),
                            order_data["customer_name"],
                            order_data["contact_phone"],
                            order_data["pickup_address"],
                            order_data["delivery_address"],
                            items
                        )
                        order.status = order_data["status"]
                        order.order_date = datetime.strptime(order_data["order_date"], "%Y-%m-%d %H:%M:%S")
                        order.estimated_completion = datetime.strptime(order_data["estimated_completion"], "%Y-%m-%d %H:%M:%S")
                        self.orders[int(order_id)] = order
                    
                    if self.orders:
                        self.next_order_id = max(self.orders.keys()) + 1

        except Exception as e:
            print(f"Error loading data: {e}")

    # Save data to JSON files
    def _save_data(self):
        try:
            orders_data = {}
            for order_id, order in self.orders.items():
                items_data = []
                for item in order.items:
                    items_data.append({
                        "garment_id": item.garment.garment_id,
                        "quantity": item.quantity,
                        "special_washes": [wash.wash_id for wash in item.special_washes]
                    })
                
                orders_data[order_id] = {
                    "customer_name": order.customer_name,
                    "contact_phone": order.contact_phone,
                    "pickup_address": order.pickup_address,
                    "delivery_address": order.delivery_address,
                    "items": items_data,
                    "status": order.status,
                    "order_date": order.order_date.strftime("%Y-%m-%d %H:%M:%S"),
                    "estimated_completion": order.estimated_completion.strftime("%Y-%m-%d %H:%M:%S")
                }

            with open("orders.json", "w") as f:
                json.dump(orders_data, f, indent=4)

        except Exception as e:
            print(f"Error saving data: {e}")

    # Create a new order
    def create_order(self, customer_name: str, contact_phone: str, pickup_address: str, 
                    delivery_address: str, items: List[OrderItem]) -> Order:
        order = Order(
            self.next_order_id,
            customer_name,
            contact_phone,
            pickup_address,
            delivery_address,
            items
        )
        self.orders[self.next_order_id] = order
        self.next_order_id += 1
        self._save_data()
        return order

    # Get an order by ID
    def get_order(self, order_id: int) -> Optional[Order]:
        return self.orders.get(order_id)

    # Get all orders
    def get_all_orders(self) -> List[Order]:
        return list(self.orders.values())

    # Update an order's status
    def update_order_status(self, order_id: int, new_status: str) -> bool:
        order = self.orders.get(order_id)
        if order:
            order.update_status(new_status)
            self._save_data()
            return True
        return False

    # Delete an order
    def delete_order(self, order_id: int) -> bool:
        if order_id in self.orders:
            del self.orders[order_id]
            self._save_data()
            return True
        return False

    # Get all garment types
    def get_all_garments(self) -> List[Garment]:
        return list(self.garments.values())

    # Get a garment type by ID
    def get_garment_by_id(self, garment_id: int) -> Optional[Garment]:
        return self.garments.get(garment_id)

    # Get all special wash options
    def get_all_special_washes(self) -> List[SpecialWash]:
        return list(self.special_washes.values())

    # Get a special wash option by ID
    def get_special_wash_by_id(self, wash_id: int) -> Optional[SpecialWash]:
        return self.special_washes.get(wash_id)

    # Get orders by status
    def get_orders_by_status(self, status: str) -> List[Order]:
        """
        status: Status to filter by
        """
        return [order for order in self.orders.values() if order.status == status]

    # Get orders by customer name
    def get_orders_by_customer(self, customer_name: str) -> List[Order]:
        """
        customer_name: Customer name to filter by
        """
        return [order for order in self.orders.values() if order.customer_name.lower() == customer_name.lower()]
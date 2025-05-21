# Import necessary libraries
from datetime import datetime
from typing import List, Dict, Optional

# Represents a bus with its properties and available seats.
class Bus:
    # Initialize a Bus instance.
    def __init__(self, bus_id: str, origin: str, destination: str, departure_time: str, total_seats: int):
        """        
        Args:
            bus_id: Unique identifier for the bus
            origin: Starting location of the bus
            destination: Ending location of the bus
            departure_time: Time when the bus departs
            total_seats: Total number of seats available
        """
        self.bus_id = bus_id
        self.origin = origin
        self.destination = destination
        self.departure_time = departure_time
        self.total_seats = total_seats
        self.available_seats = total_seats
        # Seat number to Passenger mapping
        self.seats = {i: None for i in range(1, total_seats + 1)}  

    # Reserve a seat on the bus for a passenger.
    def reserve_seat(self, seat_number: int, passenger: 'Passenger') -> bool:
        """    
        Args:
            seat_number: Seat number to reserve
            passenger (Passenger): Passenger object to assign to the seat
            
        Returns:
            bool: True if reservation was successful, False otherwise
        """
        if 1 <= seat_number <= self.total_seats and self.seats[seat_number] is None:
            self.seats[seat_number] = passenger
            self.available_seats -= 1
            return True
        return False

    # Cancel a seat reservation.
    def cancel_seat(self, seat_number: int) -> bool:
        """    
        Args:
            seat_number: Seat number to cancel
            
        Returns:
            bool: True if cancellation was successful, False otherwise
        """
        if 1 <= seat_number <= self.total_seats and self.seats[seat_number] is not None:
            self.seats[seat_number] = None
            self.available_seats += 1
            return True
        return False

    # Get a list of available seat numbers.
    def get_available_seats(self) -> List[int]:
        """    
        Returns:
            List[int]: List of available seat numbers
        """
        return [seat for seat, passenger in self.seats.items() if passenger is None]

    # Get bus information as a dictionary.
    def get_bus_info(self) -> Dict:
        """    
        Returns:
            Dict: Bus information including ID, route, and departure time
        """
        return {
            'bus_id': self.bus_id,
            'origin': self.origin,
            'destination': self.destination,
            'departure_time': self.departure_time,
            'total_seats': self.total_seats,
            'available_seats': self.available_seats
        }


# Represents a passenger with personal details.
class Passenger:
    # Initialize a Passenger instance.
    def __init__(self, passenger_id: str, name: str, email: str, phone: str):
        """    
        Args:
            passenger_id: Unique identifier for the passenger
            name: Full name of the passenger
            email: Email address of the passenger
            phone: Phone number of the passenger
        """
        self.passenger_id = passenger_id
        self.name = name
        self.email = email
        self.phone = phone

    # Get passenger information as a dictionary.
    def get_passenger_info(self) -> Dict:
        """    
        Returns:
            Dict: Passenger information including ID, name, and contact details
        """
        return {
            'passenger_id': self.passenger_id,
            'name': self.name,
            'email': self.email,
            'phone': self.phone
        }


# Represents a bus ticket with all relevant details.
class Ticket:
    # Initialize a Ticket instance.
    def __init__(self, ticket_id: str, bus: Bus, passenger: Passenger, seat_number: int, purchase_date: str):
        """    
        Args:
            ticket_id: Unique identifier for the ticket
            bus (Bus): Bus object associated with the ticket
            passenger (Passenger): Passenger object associated with the ticket
            seat_number: Seat number assigned to the ticket
            purchase_date: Date when the ticket was purchased
        """
        self.ticket_id = ticket_id
        self.bus = bus
        self.passenger = passenger
        self.seat_number = seat_number
        self.purchase_date = purchase_date
        self.is_cancelled = False
        self.cancellation_date = None

    # Cancel the ticket if it hasn't been cancelled already.
    def cancel_ticket(self) -> bool:
        """    
        Returns:
            bool: True if cancellation was successful, False otherwise
        """
        if not self.is_cancelled:
            self.is_cancelled = True
            self.cancellation_date = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
            return self.bus.cancel_seat(self.seat_number)
        return False

    # Get ticket information as a dictionary.
    def get_ticket_info(self) -> Dict:
        """    
        Returns:
            Dict: Complete ticket information including bus, passenger, and status
        """
        return {
            'ticket_id': self.ticket_id,
            'bus_info': self.bus.get_bus_info(),
            'passenger_info': self.passenger.get_passenger_info(),
            'seat_number': self.seat_number,
            'purchase_date': self.purchase_date,
            'is_cancelled': self.is_cancelled,
            'cancellation_date': self.cancellation_date
        }
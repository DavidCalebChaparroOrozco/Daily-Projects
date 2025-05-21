from datetime import datetime
from typing import Dict, Optional
from model.model import Bus, Passenger, Ticket
from view.view import BusTicketView

# Main controller class that manages the bus ticket system operations.
class BusTicketController:
    
    # Initialize the controller with sample data and view instance.
    def __init__(self):
        self.view = BusTicketView()
        # List of Bus objects
        self.buses = []          
        # List of Ticket objects
        self.tickets = []         
        # Counter for ticket IDs
        self.next_ticket_id = 1   
        
        # Initialize with sample data
        self._initialize_sample_data()

    # Initialize the system with some sample buses.
    def _initialize_sample_data(self) -> None:
        # Create sample buses
        self.buses.append(Bus("B001", "New York", "Boston", "2023-12-15 08:00", 30))
        self.buses.append(Bus("B002", "New York", "Washington", "2023-12-15 10:30", 40))
        self.buses.append(Bus("B003", "Boston", "Philadelphia", "2023-12-16 09:15", 25))
        self.buses.append(Bus("B004", "Washington", "New York", "2023-12-16 16:45", 35))

    def run(self) -> None:
        while True:
            choice = self.view.display_menu()
            
            if choice == 1:
                self._handle_view_buses()
            elif choice == 2:
                self._handle_purchase_ticket()
            elif choice == 3:
                self._handle_view_ticket()
            elif choice == 4:
                self._handle_cancel_ticket()
            elif choice == 5:
                self.view.display_message("Thank you for using the Bus Ticket Simulation System. Goodbye!")
                break

    # Handle the view buses operation.
    def _handle_view_buses(self) -> None:
        self.view.display_buses(self.buses)
        self.view.display_separator()
        input("Press Enter to return to the main menu...")

    # Handle the ticket purchase process.
    def _handle_purchase_ticket(self) -> None:
        # Step 1: Show available buses
        self.view.display_buses(self.buses)
        
        # Step 2: Get bus selection
        bus_id = self.view.get_bus_selection(self.buses)
        if not bus_id:
            return  # User chose to go back
            
        # Find the selected bus
        selected_bus = next((bus for bus in self.buses if bus.get_bus_info()['bus_id'] == bus_id), None)
        if not selected_bus:
            self.view.display_message("Bus not found.", is_error=True)
            return
            
        # Check if bus has available seats
        if selected_bus.available_seats <= 0:
            self.view.display_message("Sorry, this bus is fully booked.", is_error=True)
            return
            
        # Step 3: Get passenger details
        passenger_details = self.view.get_passenger_details()
        
        # Step 4: Show available seats and get selection
        available_seats = selected_bus.get_available_seats()
        seat_number = self.view.get_seat_selection(available_seats)
        
        # Step 5: Create passenger and ticket
        passenger_id = f"P{datetime.now().strftime('%Y%m%d%H%M%S')}"
        passenger = Passenger(
            passenger_id=passenger_id,
            name=passenger_details['name'],
            email=passenger_details['email'],
            phone=passenger_details['phone']
        )
        
        ticket_id = f"T{self.next_ticket_id:04d}"
        self.next_ticket_id += 1
        
        purchase_date = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        ticket = Ticket(
            ticket_id=ticket_id,
            bus=selected_bus,
            passenger=passenger,
            seat_number=seat_number,
            purchase_date=purchase_date
        )
        
        # Reserve the seat
        if selected_bus.reserve_seat(seat_number, passenger):
            self.tickets.append(ticket)
            self.view.display_message(f"Ticket purchased successfully! Your Ticket ID is: {ticket_id}")
            self.view.display_separator()
            self.view.display_ticket(ticket.get_ticket_info())
        else:
            self.view.display_message("Failed to reserve seat. Please try again.", is_error=True)

    # Handle the view ticket details operation.
    def _handle_view_ticket(self) -> None:
        ticket_id = self.view.get_ticket_id()
        ticket = self._find_ticket(ticket_id)
        
        if ticket:
            self.view.display_ticket(ticket.get_ticket_info())
        else:
            self.view.display_message("Ticket not found. Please check the Ticket ID.", is_error=True)
            
        self.view.display_separator()
        input("Press Enter to return to the main menu...")

    # Handle the ticket cancellation process.
    def _handle_cancel_ticket(self) -> None:
        ticket_id = self.view.get_ticket_id()
        ticket = self._find_ticket(ticket_id)
        
        if not ticket:
            self.view.display_message("Ticket not found. Please check the Ticket ID.", is_error=True)
            return
            
        if ticket.is_cancelled:
            self.view.display_message("This ticket has already been cancelled.", is_error=True)
            return
            
        # Confirm cancellation
        self.view.display_ticket(ticket.get_ticket_info())
        confirm = input("\nAre you sure you want to cancel this ticket? (yes/no): ").strip().lower()
        
        if confirm == 'yes':
            if ticket.cancel_ticket():
                self.view.display_message("Ticket cancelled successfully.")
            else:
                self.view.display_message("Failed to cancel ticket. Please try again.", is_error=True)
        else:
            self.view.display_message("Ticket cancellation aborted.")
            
        self.view.display_separator()
        input("Press Enter to return to the main menu...")

    # Find a ticket by its ID.
    def _find_ticket(self, ticket_id: str) -> Optional[Ticket]:
        """    
        Args:
            ticket_id: Ticket ID to search for
            
        Returns:
            Optional[Ticket]: Ticket object if found, None otherwise
        """
        for ticket in self.tickets:
            if ticket.ticket_id == ticket_id:
                return ticket
        return None
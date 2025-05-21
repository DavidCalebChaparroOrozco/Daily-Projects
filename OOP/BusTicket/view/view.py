# Handles all user interface interactions for the bus ticket system.
class BusTicketView:
    # Display the main menu and get user choice.
    @staticmethod
    def display_menu() -> int:
        """     
        Returns:
            int: User's menu choice
        """
        print("=".center(50, "="))
        print("BUS TICKET SIMULATION SYSTEM BY DAVID CALEB".center(50))
        print("=".center(50, "="))
        print("1. View Available Buses")
        print("2. Purchase Ticket")
        print("3. View Ticket Details")
        print("4. Cancel Ticket")
        print("5. Exit")
        print("=".center(50, "="))
        
        while True:
            try:
                choice = int(input("Please enter your choice (1-5): "))
                if 1 <= choice <= 5:
                    return choice
                print("Invalid choice. Please enter a number between 1 and 5.")
            except ValueError:
                print("Invalid input. Please enter a number.")

    # Display available buses in a formatted table.
    @staticmethod
    def display_buses(buses: list) -> None:
        """    
        Args:
            buses: List of Bus objects or dictionaries with bus info
        """
        if not buses:
            print("\nNo buses available at the moment.")
            return
            
        print("\n" + "="*100)
        print("AVAILABLE BUSES".center(100))
        print("=".center(100, "="))
        print(f"{'Bus ID':<10}{'Origin':<20}{'Destination':<20}{'Departure Time':<20}{'Total Seats':<15}{'Available Seats':<15}")
        print("-".center(100, "-"))
        
        for bus in buses:
            if hasattr(bus, 'get_bus_info'):
                bus_info = bus.get_bus_info()
            else:
                bus_info = bus
                
            print(f"{bus_info['bus_id']:<10}{bus_info['origin']:<20}{bus_info['destination']:<20}"
                    f"{bus_info['departure_time']:<20}{bus_info['total_seats']:<15}{bus_info['available_seats']:<15}")
        print("=".center(100, "="))

    # Get user selection for a specific bus.
    @staticmethod
    def get_bus_selection(buses: list) -> str:
        """    
        Args:
            buses: List of available buses
            
        Returns:
            str: Selected bus ID
        """
        while True:
            bus_id = input("\nEnter the Bus ID you want to book (or 'back' to return): ").strip()
            if bus_id.lower() == 'back':
                return None
                
            for bus in buses:
                if hasattr(bus, 'get_bus_info'):
                    current_id = bus.get_bus_info()['bus_id']
                else:
                    current_id = bus['bus_id']
                    
                if current_id == bus_id:
                    return bus_id
                    
            print("Invalid Bus ID. Please try again or type 'back' to return.")

    # Collect passenger details from user input.
    @staticmethod
    def get_passenger_details() -> dict:
        """    
        Returns:
            dict: Dictionary containing passenger information
        """
        print("=".center(50, "="))
        print("PASSENGER DETAILS".center(50))
        print("=".center(50, "="))
        
        while True:
            name = input("Full Name: ").strip()
            if name:
                break
            print("Name cannot be empty. Please try again.")
            
        while True:
            email = input("Email: ").strip()
            if '@' in email and '.' in email:
                break
            print("Please enter a valid email address.")
            
        while True:
            phone = input("Phone Number: ").strip()
            if phone.isdigit() and len(phone) >= 8:
                break
            print("Please enter a valid phone number (at least 8 digits).")
            
        return {
            'name': name,
            'email': email,
            'phone': phone
        }

    # Get user selection for a seat number.
    @staticmethod
    def get_seat_selection(available_seats: list) -> int:
        """    
        Args:
            available_seats: List of available seat numbers
            
        Returns:
            int: Selected seat number
        """
        print("\nAvailable Seats:", ", ".join(map(str, available_seats)))
        
        while True:
            try:
                seat = int(input("Select your seat number: "))
                if seat in available_seats:
                    return seat
                print("Invalid seat number. Please choose from available seats.")
            except ValueError:
                print("Please enter a valid seat number.")

    # Display ticket information in a formatted way.
    @staticmethod
    def display_ticket(ticket_info: dict) -> None:
        """    
        Args:
            ticket_info (dict): Dictionary containing ticket details
        """
        if not ticket_info:
            print("\nNo ticket information to display.")
            return
            
        print("\n" + "="*70)
        print("TICKET DETAILS".center(70))
        print("=".center(70, "="))
        print(f"Ticket ID: {ticket_info['ticket_id']}")
        print(f"Purchase Date: {ticket_info['purchase_date']}")
        print(f"Status: {'CANCELLED' if ticket_info['is_cancelled'] else 'ACTIVE'}")
        if ticket_info['is_cancelled']:
            print(f"Cancellation Date: {ticket_info['cancellation_date']}")
        print("\nPassenger Information:")
        print(f"Name: {ticket_info['passenger_info']['name']}")
        print(f"Email: {ticket_info['passenger_info']['email']}")
        print(f"Phone: {ticket_info['passenger_info']['phone']}")
        print("\nBus Information:")
        print(f"Bus ID: {ticket_info['bus_info']['bus_id']}")
        print(f"Route: {ticket_info['bus_info']['origin']} to {ticket_info['bus_info']['destination']}")
        print(f"Departure: {ticket_info['bus_info']['departure_time']}")
        print(f"Seat Number: {ticket_info['seat_number']}")
        print("=".center(70, "="))

    # Get ticket ID from user input.
    @staticmethod
    def get_ticket_id() -> str:
        """    
        Returns:
            str: Ticket ID entered by user
        """
        return input("\nEnter Ticket ID: ").strip()

    # Display a message to the user.
    @staticmethod
    def display_message(message: str, is_error: bool = False) -> None:
        """    
        Args:
            message: Message to display
            is_error: Whether the message is an error message
        """
        if is_error:
            print("\n[ERROR] " + message)
        else:
            print("\n" + message)

    # Display a visual separator.
    @staticmethod
    def display_separator() -> None:
        print("\n" + "-"*50)
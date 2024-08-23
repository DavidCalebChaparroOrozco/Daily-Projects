# Importing necessary libraries
from abc import ABC, abstractmethod

# Base Class for Room and Guest
class Person(ABC):
    def __init__(self, name, id_number):
        # Encapsulation: Making attributes private
        self._name = name
        self._id_number = id_number

    @abstractmethod
    def get_description(self):
        """
        Abstract method to get the description of the person.
        Subclasses must implement this method.
        """
        pass

    # Getter method to retrieve the name of the person
    def get_name(self):
        return self._name

    # Getter method to retrieve the ID number of the person
    def get_id_number(self):
        return self._id_number


# Inheritance for Guest
class Guest(Person):
    def __init__(self, name, id_number, age):
        super().__init__(name, id_number)
        self._age = age
        self._reservations = []

    # Implement the abstract method to get the description of the guest
    def get_description(self):
        return f"Guest: {self.get_name()} (ID: {self.get_id_number()}, Age: {self._age})"

    # Method to add a reservation for the guest
    def add_reservation(self, reservation):
        self._reservations.append(reservation)

    # Method to get the list of reservations for the guest
    def get_reservations(self):
        return self._reservations


# Class for Room
class Room:
    def __init__(self, room_number, beds, baths, food_service, entertainment):
        self._room_number = room_number
        self._beds = beds
        self._baths = baths
        self._food_service = food_service
        self._entertainment = entertainment
        self._guests = []

    # Method to get the description of the room
    def get_description(self):
        food_service_status = "Yes" if self._food_service else "No"
        entertainment_status = "Yes" if self._entertainment else "No"
        return (f"Room {self._room_number}: Beds: {self._beds}, Baths: {self._baths}, "
                f"Food Service: {food_service_status}, Entertainment: {entertainment_status}")

    # Method to add a guest to the room
    def add_guest(self, guest):
        self._guests.append(guest)

    # Method to get the list of guests in the room
    def get_guests(self):
        return self._guests


# Class for Reservation
class Reservation:
    def __init__(self, guest, room, check_in_date, check_out_date):
        self._guest = guest
        self._room = room
        self._check_in_date = check_in_date
        self._check_out_date = check_out_date

    # Method to get the reservation details
    def get_details(self):
        return (f"Reservation for {self._guest.get_name()} in Room {self._room._room_number} "
                f"from {self._check_in_date} to {self._check_out_date}")


# Function to display the menu
def display_menu():
    print("\nHotel Reservation System")
    print("1. Register new guest")
    print("2. Register new room")
    print("3. Make a reservation")
    print("4. Display guest details")
    print("5. Display room details")
    print("6. Exit")
    print("=".center(50, "="))
    return input("Select an option: ")


# Main code
if __name__ == "__main__":
    # Dictionary to hold guests
    guests = {}

    # Dictionary to hold rooms
    rooms = {}

    while True:
        option = display_menu()

        if option == "1":
            # Register new guest
            guest_name = input("Enter guest name: ")
            guest_id = input("Enter guest ID: ")
            guest_age = int(input("Enter guest age: "))
            if guest_id not in guests:
                guests[guest_id] = Guest(guest_name, guest_id, guest_age)
                print("Guest registered successfully.")
            else:
                print("Guest ID already exists.")

        elif option == "2":
            # Register new room
            room_number = input("Enter room number: ")
            beds = int(input("Enter number of beds: "))
            baths = int(input("Enter number of baths: "))
            food_service = input("Food service available (yes/no): ").lower() == 'yes'
            entertainment = input("Entertainment available (yes/no): ").lower() == 'yes'
            if room_number not in rooms:
                rooms[room_number] = Room(room_number, beds, baths, food_service, entertainment)
                print("Room registered successfully.")
            else:
                print("Room number already exists.")

        elif option == "3":
            # Make a reservation
            guest_id = input("Enter guest ID: ")
            room_number = input("Enter room number: ")
            if guest_id in guests and room_number in rooms:
                check_in_date = input("Enter check-in date (YYYY-MM-DD): ")
                check_out_date = input("Enter check-out date (YYYY-MM-DD): ")
                guest = guests[guest_id]
                room = rooms[room_number]
                reservation = Reservation(guest, room, check_in_date, check_out_date)
                guest.add_reservation(reservation)
                room.add_guest(guest)
                print("Reservation made successfully.")
            else:
                print("Guest or Room not found.")

        elif option == "4":
            # Display guest details
            guest_id = input("Enter guest ID: ")
            if guest_id in guests:
                guest = guests[guest_id]
                print(guest.get_description())
                for reservation in guest.get_reservations():
                    print(f" - {reservation.get_details()}")
            else:
                print("Guest not found.")

        elif option == "5":
            # Display room details
            room_number = input("Enter room number: ")
            if room_number in rooms:
                room = rooms[room_number]
                print(room.get_description())
                for guest in room.get_guests():
                    print(f" - {guest.get_description()}")
            else:
                print("Room not found.")

        elif option == "6":
            # Exit
            break

        else:
            print("Invalid option. Please try again.")

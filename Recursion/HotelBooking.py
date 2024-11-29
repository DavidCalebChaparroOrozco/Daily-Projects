# Function to book a room
def book_room(available_rooms):
    # Check if there are available rooms
    if available_rooms <= 0:
        print("Sorry, no rooms available.")
        return

    # Prompt user for booking details
    guest_name = input("Enter guest name: ")
    nights = int(input("Enter number of nights: "))

    # Confirm the booking
    print(f"Booking confirmed for {guest_name} for {nights} nights.")
    
    # Decrease the number of available rooms
    available_rooms -= 1

    # Ask if the user wants to book another room
    another_booking = input("Do you want to book another room? (yes/no): ").strip().lower()
    
    if another_booking == 'yes':
        # Recursive call to book another room
        book_room(available_rooms)
    else:
        print("Thank you for using our hotel booking system!")

# Main function to start the booking process
def main():
    total_rooms = 5  # Total number of rooms in the hotel
    print(f"Welcome to our hotel! We have {total_rooms} rooms available.")
    
    # Start booking process
    book_room(total_rooms)

if __name__ == "__main__":
    main()
# Class definition for a movie
class Movie:
    def __init__(self, title, duration, price):
        self.title = title
        self.duration = duration
        self.price = price

    # Method to display movie information
    def show_information(self):
        print("Movie Information:")
        print("Title:", self.title)
        print("Duration:", self.duration, "minutes")
        print("Price:", self.price)

# Class definition for a room
class Room:
    def __init__(self, num_rows, seats_per_row):
        self.num_rows = num_rows
        self.seats_per_row = seats_per_row
        self.available_seats = [['O' for _ in range(seats_per_row)] for _ in range(num_rows)]

    # Method to display available seats in the room
    def show_seats(self):
        for row in self.available_seats:
            print(' '.join(row))

    # Method to check the availability of a seat
    def check_availability(self, row, seat):
        if row < 1 or row > self.num_rows or seat < 1 or seat > self.seats_per_row:
            print("Invalid row or seat.")
            return False
        if self.available_seats[row - 1][seat - 1] == 'X':
            print("This seat is already reserved.")
            return False
        print("This seat is available.")
        return True

    # Method to reserve a seat
    def reserve_seat(self, row, seat):
        if not self.check_availability(row, seat):
            return False
        self.available_seats[row - 1][seat - 1] = 'X'
        print("Seat reserved successfully.")
        return True

    # Method to cancel a reservation
    def cancel_reservation(self, row, seat):
        if row < 1 or row > self.num_rows or seat < 1 or seat > self.seats_per_row:
            print("Invalid row or seat.")
            return False
        if self.available_seats[row - 1][seat - 1] == 'O':
            print("No reservation found for this seat.")
            return False
        self.available_seats[row - 1][seat - 1] = 'O'
        print("Reservation canceled successfully.")
        return True

    # Method to release a seat
    def release_seat(self, row, seat):
        if row < 1 or row > self.num_rows or seat < 1 or seat > self.seats_per_row:
            print("Invalid row or seat.")
            return False
        if self.available_seats[row - 1][seat - 1] == 'O':
            print("This seat is not reserved.")
            return False
        self.available_seats[row - 1][seat - 1] = 'O'
        print("Seat released successfully.")
        return True

# Class definition for a reservation
class Reservation:
    def __init__(self, movie, room, row, seat):
        self.movie = movie
        self.room = room
        self.row = row
        self.seat = seat

# Class definition for a cinema
class Cinema:
    def __init__(self):
        self.movies = []
        self.rooms = []
        self.reservations = []

    # Method to find a movie by its title
    def find_movie_by_title(self, title):
        for movie in self.movies:
            if movie.title == title:
                return movie
        return None

    # Method to find rooms with capacity greater than or equal to a given capacity
    def find_room_by_capacity(self, min_capacity):
        found_rooms = []
        for room in self.rooms:
            room_capacity = room.num_rows * room.seats_per_row
            if room_capacity >= min_capacity:
                found_rooms.append(room)
        return found_rooms

    # Method to find reservations made by a specific customer
    def find_reservations_by_customer(self, customer):
        customer_reservations = []
        for reservation in self.reservations:
            if reservation.customer == customer:
                customer_reservations.append(reservation)
        return customer_reservations

# Function to display the main menu
def show_menu():
    print("\nMenu")
    print("1. Create a new movie")
    print("2. Create a new room")
    print("3. Show movie information")
    print("4. Show available seats in room")
    print("5. Reserve a seat")
    print("6. Cancel a reservation")
    print("7. Release a seat")
    print("8. Exit")


cinema = Cinema()
movie = None
room = None

option = 0
while option != 8:
    show_menu()
    option = int(input("Select an option: "))

    if option == 1:
        title = input("Enter the movie title: ")
        duration = int(input("Enter the movie duration in minutes: "))
        price = int(input("Enter the price of the ticket: "))
        movie = Movie(title, duration, price)
        cinema.movies.append(movie)
        print("Movie created successfully.")
    elif option == 2:
        rows = int(input("Enter the number of rows for the room: "))
        seats_per_row = int(input("Enter the number of seats per row for the room: "))
        room = Room(rows, seats_per_row)
        cinema.rooms.append(room)
        print("Room created successfully.")
    elif option == 3:
        if movie:
            movie.show_information()
        else:
            print("No movie created yet.")
    elif option == 4:
        if room:
            print("\nAvailable seats:")
            room.show_seats()
        else:
            print("No room created yet.")
    elif option == 5:
        if room:
            row = int(input("Enter the row number: "))
            seat = int(input("Enter the seat number: "))
            room.reserve_seat(row, seat)
        else:
            print("No room created yet.")
    elif option == 6:
        if room:
            row = int(input("Enter the row number of the reservation to cancel: "))
            seat = int(input("Enter the seat number of the reservation to cancel: "))
            room.cancel_reservation(row, seat)
        else:
            print("No room created yet.")
    elif option == 7:
        if room:
            row = int(input("Enter the row number of the seat to release: "))
            seat = int(input("Enter the seat number to release: "))
            room.release_seat(row, seat)
        else:
            print("No room created yet.")
    elif option == 8:
        print("Exiting the program...")
    else:
        print("Invalid option. Please select a valid option.")

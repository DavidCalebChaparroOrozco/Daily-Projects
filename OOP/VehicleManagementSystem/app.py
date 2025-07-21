# Importing necessary libraries
from datetime import datetime
from collections import defaultdict

class VehicleManagementSystem:
    def __init__(self):
        # List to store vehicles currently on campus
        self.active_vehicles = []  
        # List to store history of vehicles that have exited
        self.history = []  
        # Dictionary to store entry logs by license plate
        self.entry_log = defaultdict(list)  

    # Adds a vehicle to the active vehicles list and logs the entry.
    def enter_vehicle(self, license_plate: str):
        """
        Args:
        license_plate (str): The license plate of the vehicle entering the campus.
        """
        entry_time = datetime.now()
        self.active_vehicles.append({'license_plate': license_plate, 'entry_time': entry_time})
        self.entry_log[license_plate].append(entry_time)
        print(f"Vehicle {license_plate} entered at {entry_time}")

    # Removes a vehicle from the active vehicles list and adds it to the history log.
    def exit_vehicle(self, license_plate: str):
        """
        Args:
        license_plate (str): The license plate of the vehicle exiting the campus.
        """
        for vehicle in self.active_vehicles:
            if vehicle['license_plate'] == license_plate:
                self.active_vehicles.remove(vehicle)
                self.history.append(vehicle)
                print(f"Vehicle {license_plate} exited at {datetime.now()}")
                return
        print(f"Vehicle {license_plate} not found in the active vehicles list.")

    # Returns the count of vehicles that entered the campus on a specific date.
    def vehicles_entered_on_date(self, date: datetime) -> int:
        """    
        Args:
        date (datetime): The date to check for vehicle entries.
        
        Returns:
        int: The count of vehicles that entered on the specified date.
        """
        count = 0
        for vehicle in self.active_vehicles + self.history:
            if vehicle['entry_time'].date() == date.date():
                count += 1
        return count

    # Returns the number of times a specific vehicle has entered the campus.
    def entry_count_for_vehicle(self, license_plate: str) -> int:
        """
        Args:
        license_plate (str): The license plate of the vehicle to check.
        
        Returns:
        int: The number of times the vehicle has entered the campus.
        """
        return len(self.entry_log[license_plate])

# Repeatedly prompts the user for input until a non-empty string is entered.
def get_valid_input(prompt):
    """    
    Args:
    prompt (str): The prompt message to display to the user.
    
    Returns:
    str: The valid input entered by the user.
    """
    user_input = ""
    while not user_input.strip():
        user_input = input(prompt).strip()
        if not user_input:
            print("Input cannot be empty. Please try again.")
    return user_input

def main():
    vms = VehicleManagementSystem()
    while True:
        print("\nVehicle Management System Menu")
        print("1. Enter a vehicle")
        print("2. Exit a vehicle")
        print("3. Determine the number of vehicles entered on a specific date")
        print("4. List the number of times a vehicle has entered")
        print("5. Exit")

        choice = get_valid_input("Enter your choice: ")
        
        if choice == "1":
            license_plate = get_valid_input("Enter the vehicle's license plate: ")
            vms.enter_vehicle(license_plate)
        
        elif choice == "2":
            license_plate = get_valid_input("Enter the vehicle's license plate: ")
            vms.exit_vehicle(license_plate)
        
        elif choice == "3":
            date_str = get_valid_input("Enter the date (YYYY-MM-DD): ")
            try:
                date = datetime.strptime(date_str, "%Y-%m-%d")
                count = vms.vehicles_entered_on_date(date)
                print(f"Number of vehicles entered on {date.date()}: {count}")
            except ValueError:
                print("Invalid date format. Please use YYYY-MM-DD.")
        
        elif choice == "4":
            license_plate = get_valid_input("Enter the vehicle's license plate: ")
            count = vms.entry_count_for_vehicle(license_plate)
            print(f"Vehicle {license_plate} has entered {count} times")
        
        elif choice == "5":
            print("Exiting the Vehicle Management System. Goodbye!")
            break
        
        else:
            print("Invalid choice. Please enter a number between 1 and 5.")

if __name__ == "__main__":
    main()

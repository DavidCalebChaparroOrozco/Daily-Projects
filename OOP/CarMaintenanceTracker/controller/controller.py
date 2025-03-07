from model.model import CarMaintenanceModel
from view.view import CarMaintenanceView

class CarMaintenanceController:
    def __init__(self):
        self.model = CarMaintenanceModel()
        self.view = CarMaintenanceView()

    # Run the application.
    def run(self):
        while True:
            self.view.display_menu()
            choice = self.view.get_user_input("Select an option: ")

            if choice == '1':
                self.add_vehicle()
            elif choice == '2':
                self.add_maintenance_record()
            elif choice == '3':
                self.view_maintenance_records()
            elif choice == '4':
                self.view_all_vehicles()
            elif choice == '5':
                self.visualize_maintenance_data()
            elif choice == '6':
                self.view.display_message("Exiting the application. Goodbye!")
                break
            else:
                self.view.display_message("Invalid option. Please try again.")

    # Add a new vehicle.
    def add_vehicle(self):
        vehicle_id = self.view.get_user_input("Enter vehicle ID: ")
        make = self.view.get_user_input("Enter vehicle make: ")
        model = self.view.get_user_input("Enter vehicle model: ")
        year = self.view.get_user_input("Enter vehicle year: ")

        if self.model.add_vehicle(vehicle_id, make, model, year):
            self.view.display_message("Vehicle added successfully!")
        else:
            self.view.display_message("Vehicle already exists.")

    # Add a maintenance record.
    def add_maintenance_record(self):
        vehicle_id = self.view.get_user_input("Enter vehicle ID: ")
        service_type = self.view.get_user_input("Enter service type: ")
        date = self.view.get_user_input("Enter service date (YYYY-MM-DD): ")
        description = self.view.get_user_input("Enter service description: ")

        if self.model.add_maintenance_record(vehicle_id, service_type, date, description):
            self.view.display_message("Maintenance record added successfully!")
        else:
            self.view.display_message("Vehicle not found.")

    # View maintenance records for a vehicle.
    def view_maintenance_records(self):
        vehicle_id = self.view.get_user_input("Enter vehicle ID: ")
        records = self.model.get_vehicle_maintenance(vehicle_id)
        if records is None:
            self.view.display_message("Vehicle not found.")
        else:
            self.view.display_vehicle_maintenance(records)

    # View all registered vehicles.
    def view_all_vehicles(self):
        vehicles = self.model.get_all_vehicles()
        self.view.display_all_vehicles(vehicles)

    # Visualize maintenance data using Matplotlib.
    def visualize_maintenance_data(self):
        vehicles = self.model.get_all_vehicles()
        self.view.visualize_maintenance_data(vehicles)
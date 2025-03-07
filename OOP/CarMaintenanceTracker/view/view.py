# Import necessary libraries
import matplotlib.pyplot as plt

class CarMaintenanceView:
    # Display the main menu to the user.
    @staticmethod
    def display_menu():
        print("\n Car Maintenance Tracker by David Caleb")
        print("1. Add Vehicle")
        print("2. Add Maintenance Record")
        print("3. View Maintenance Records")
        print("4. View All Vehicles")
        print("5. Visualize Maintenance Data")
        print("6. Exit")

    # Get user input.
    @staticmethod
    def get_user_input(prompt):
        return input(prompt)

    # Display a message to the user.
    @staticmethod
    def display_message(message):
        print(message)

    # Display maintenance records for a vehicle.
    @staticmethod
    def display_vehicle_maintenance(records):
        if not records:
            print("No maintenance records found.")
        else:
            print("\nMaintenance Records:")
            for record in records:
                print(f"Service: {record['service_type']}, Date: {record['date']}, Description: {record['description']}")

    # Display all registered vehicles.
    @staticmethod
    def display_all_vehicles(vehicles):
        if not vehicles:
            print("No vehicles found.")
        else:
            print("\nRegistered Vehicles:")
            for vehicle_id, details in vehicles.items():
                print(f"ID: {vehicle_id}, Make: {details['make']}, Model: {details['model']}, Year: {details['year']}")

    # Visualize maintenance data using Matplotlib.
    @staticmethod
    def visualize_maintenance_data(vehicles):
        if not vehicles:
            print("No vehicles found.")
            return

        # Prepare data for visualization
        service_counts = {}
        for vehicle_id, details in vehicles.items():
            for record in details['maintenance_records']:
                service_type = record['service_type']
                if service_type in service_counts:
                    service_counts[service_type] += 1
                else:
                    service_counts[service_type] = 1

        if not service_counts:
            print("No maintenance records found to visualize.")
            return

        # Plot the data
        plt.bar(service_counts.keys(), service_counts.values())
        plt.xlabel('Service Type')
        plt.ylabel('Number of Services')
        plt.title('Maintenance Service Distribution')
        plt.xticks(rotation=45)
        plt.tight_layout()
        plt.show()
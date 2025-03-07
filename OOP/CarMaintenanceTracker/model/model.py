class CarMaintenanceModel:
    def __init__(self):
        # Simulate a database to store vehicles and their maintenance records
        self.vehicles = {}

    # Add a new vehicle to the system.
    def add_vehicle(self, vehicle_id, make, model, year):
        if vehicle_id in self.vehicles:
            # Vehicle already exists
            return False  
        self.vehicles[vehicle_id] = {
            'make': make,
            'model': model,
            'year': year,
            'maintenance_records': []
        }
        return True

    # Add a maintenance record to a vehicle.
    def add_maintenance_record(self, vehicle_id, service_type, date, description):
        if vehicle_id not in self.vehicles:
            # Vehicle does not exist
            return False  
        self.vehicles[vehicle_id]['maintenance_records'].append({
            'service_type': service_type,
            'date': date,
            'description': description
        })
        return True

    # Get all maintenance records for a vehicle.
    def get_vehicle_maintenance(self, vehicle_id):
        if vehicle_id not in self.vehicles:
            return None  # Vehicle does not exist
        return self.vehicles[vehicle_id]['maintenance_records']

    # Get all registered vehicles.
    def get_all_vehicles(self):
        return self.vehicles
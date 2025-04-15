class MuseumController:
    def __init__(self, model, view):
        self.model = model
        self.view = view
        self.current_user = None
        self.admin_username = "admin"
        self.admin_password = "museum123"  

    def run(self):
        while True:
            choice = self.view.display_menu()
            
            if choice == "1":
                self.explore_artifacts()
            elif choice == "2":
                self.view_exhibitions()
            elif choice == "3":
                self.take_virtual_tour()
            elif choice == "4":
                self.manage_artifacts()
            elif choice == "5":
                self.manage_exhibitions()
            elif choice == "6":
                self.manage_tours()
            elif choice == "0":
                self.view.display_message("Thank you for using MuseumGuide. Goodbye!")
                break
            else:
                self.view.display_message("Invalid choice. Please try again.", is_error=True)

    # Handle artifact exploration.
    def explore_artifacts(self):
        artifacts = self.model.list_artifacts()
        self.view.display_artifacts(artifacts)
        
        if artifacts:
            artifact_id = input("\nEnter artifact ID to view details (or 0 to go back): ")
            if artifact_id != "0":
                artifact = self.model.get_artifact(int(artifact_id))
                if artifact:
                    self.view.display_artifact_details(artifact)
                else:
                    self.view.display_message("Artifact not found.", is_error=True)

    # Handle exhibition viewing.
    def view_exhibitions(self):
        exhibitions = self.model.list_exhibitions()
        self.view.display_exhibitions(exhibitions)
        
        if exhibitions:
            exhibition_id = input("\nEnter exhibition ID to view details (or 0 to go back): ")
            if exhibition_id != "0":
                exhibition = self.model.get_exhibition(int(exhibition_id))
                if exhibition:
                    self.view.display_exhibition_details(exhibition)
                else:
                    self.view.display_message("Exhibition not found.", is_error=True)

    # Handle virtual tours.
    def take_virtual_tour(self):
        tours = self.model.list_tours()
        self.view.display_tours(tours)
        
        if tours:
            tour_id = input("\nEnter tour ID to view details (or 0 to go back): ")
            if tour_id != "0":
                tour = self.model.get_tour(int(tour_id))
                if tour:
                    self.view.display_tour_details(tour)
                else:
                    self.view.display_message("Tour not found.", is_error=True)

    # Admin interface for artifact management.
    def manage_artifacts(self):
        if not self.authenticate_admin():
            return
            
        while True:
            choice = self.view.display_admin_menu("artifacts")
            
            if choice == "1":
                self.add_artifact()
            elif choice == "2":
                self.view_artifact_details()
            elif choice == "3":
                self.update_artifact()
            elif choice == "4":
                self.delete_artifact()
            elif choice == "5":
                artifacts = self.model.list_artifacts()
                self.view.display_artifacts(artifacts)
            elif choice == "0":
                break
            else:
                self.view.display_message("Invalid choice. Please try again.", is_error=True)

    # Admin interface for exhibition management.
    def manage_exhibitions(self):
        if not self.authenticate_admin():
            return
            
        while True:
            choice = self.view.display_admin_menu("exhibitions")
            
            if choice == "1":
                self.add_exhibition()
            elif choice == "2":
                self.view_exhibition_details()
            elif choice == "3":
                self.update_exhibition()
            elif choice == "4":
                self.delete_exhibition()
            elif choice == "5":
                exhibitions = self.model.list_exhibitions()
                self.view.display_exhibitions(exhibitions)
            elif choice == "0":
                break
            else:
                self.view.display_message("Invalid choice. Please try again.", is_error=True)

    # Admin interface for tour management.
    def manage_tours(self):
        if not self.authenticate_admin():
            return
            
        while True:
            choice = self.view.display_admin_menu("tours")
            
            if choice == "1":
                self.add_tour()
            elif choice == "2":
                self.view_tour_details()
            elif choice == "3":
                self.update_tour()
            elif choice == "4":
                self.delete_tour()
            elif choice == "5":
                tours = self.model.list_tours()
                self.view.display_tours(tours)
            elif choice == "0":
                break
            else:
                self.view.display_message("Invalid choice. Please try again.", is_error=True)

    # Authenticate admin user.
    def authenticate_admin(self):
        username, password = self.view.admin_login()
        if username == self.admin_username and password == self.admin_password:
            self.current_user = {'username': username, 'role': 'admin'}
            return True
        else:
            self.view.display_message("Invalid credentials. Access denied.", is_error=True)
            return False

    # Add a new artifact.
    def add_artifact(self):
        artifact_data = self.view.get_artifact_input()
        artifact = self.model.add_artifact(artifact_data)
        self.view.display_message(f"Artifact '{artifact['name']}' added successfully!")

    # View details of a specific artifact.
    def view_artifact_details(self):
        artifact_id = self.view.get_id_input("artifact")
        artifact = self.model.get_artifact(artifact_id)
        if artifact:
            self.view.display_artifact_details(artifact)
        else:
            self.view.display_message("Artifact not found.", is_error=True)

    # Update an existing artifact.
    def update_artifact(self):
        artifact_id = self.view.get_id_input("artifact")
        artifact = self.model.get_artifact(artifact_id)
        if artifact:
            self.view.display_artifact_details(artifact)
            updated_data = self.view.get_artifact_input()
            updated_artifact = self.model.update_artifact(artifact_id, updated_data)
            if updated_artifact:
                self.view.display_message(f"Artifact '{updated_artifact['name']}' updated successfully!")
        else:
            self.view.display_message("Artifact not found.", is_error=True)

    # Delete an artifact.
    def delete_artifact(self):
        artifact_id = self.view.get_id_input("artifact")
        if self.model.delete_artifact(artifact_id):
            self.view.display_message("Artifact deleted successfully!")
        else:
            self.view.display_message("Artifact not found.", is_error=True)

    # Add a new exhibition.
    def add_exhibition(self):
        exhibition_data = self.view.get_exhibition_input()
        exhibition = self.model.add_exhibition(exhibition_data)
        self.view.display_message(f"Exhibition '{exhibition['title']}' added successfully!")

    # View details of a specific exhibition.
    def view_exhibition_details(self):
        exhibition_id = self.view.get_id_input("exhibition")
        exhibition = self.model.get_exhibition(exhibition_id)
        if exhibition:
            self.view.display_exhibition_details(exhibition)
        else:
            self.view.display_message("Exhibition not found.", is_error=True)

    # Update an existing exhibition.
    def update_exhibition(self):
        exhibition_id = self.view.get_id_input("exhibition")
        exhibition = self.model.get_exhibition(exhibition_id)
        if exhibition:
            self.view.display_exhibition_details(exhibition)
            updated_data = self.view.get_exhibition_input()
            updated_exhibition = self.model.update_exhibition(exhibition_id, updated_data)
            if updated_exhibition:
                self.view.display_message(f"Exhibition '{updated_exhibition['title']}' updated successfully!")
        else:
            self.view.display_message("Exhibition not found.", is_error=True)

    # Delete an exhibition.
    def delete_exhibition(self):
        exhibition_id = self.view.get_id_input("exhibition")
        if self.model.delete_exhibition(exhibition_id):
            self.view.display_message("Exhibition deleted successfully!")
        else:
            self.view.display_message("Exhibition not found.", is_error=True)

    # Add a new virtual tour.
    def add_tour(self):
        tour_data = self.view.get_tour_input()
        tour = self.model.add_tour(tour_data)
        self.view.display_message(f"Virtual tour '{tour['name']}' added successfully!")

    # View details of a specific tour.
    def view_tour_details(self):
        tour_id = self.view.get_id_input("tour")
        tour = self.model.get_tour(tour_id)
        if tour:
            self.view.display_tour_details(tour)
        else:
            self.view.display_message("Tour not found.", is_error=True)

    # Update an existing tour.
    def update_tour(self):
        tour_id = self.view.get_id_input("tour")
        tour = self.model.get_tour(tour_id)
        if tour:
            self.view.display_tour_details(tour)
            updated_data = self.view.get_tour_input()
            updated_tour = self.model.update_tour(tour_id, updated_data)
            if updated_tour:
                self.view.display_message(f"Virtual tour '{updated_tour['name']}' updated successfully!")
        else:
            self.view.display_message("Tour not found.", is_error=True)

    # Delete a tour.
    def delete_tour(self):
        tour_id = self.view.get_id_input("tour")
        if self.model.delete_tour(tour_id):
            self.view.display_message("Virtual tour deleted successfully!")
        else:
            self.view.display_message("Tour not found.", is_error=True)
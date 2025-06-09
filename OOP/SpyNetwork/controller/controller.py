class SpyController:
    # Initialize the controller with model and view reference
    def __init__(self, model, view):
        self.model = model
        self.view = view

    # Main application loop
    def run(self):
        while True:
            self.view.display_menu()
            choice = self.view.get_user_input("Enter your choice (1-5)")
            
            if choice == '1':
                self.manage_spies()
            elif choice == '2':
                self.manage_missions()
            elif choice == '3':
                self.manage_leaks()
            elif choice == '4':
                self.generate_reports()
            elif choice == '5':
                self.view.display_message("Exiting Spy Network Management System. Stay covert!")
                break
            else:
                self.view.display_message("Invalid choice. Please try again.", is_error=True)

    # Handle the spy management submen
    def manage_spies(self):
        while True:
            self.view.display_spy_menu()
            choice = self.view.get_user_input("Enter your choice (1-5)")
            
            if choice == '1':
                self.add_spy()
            elif choice == '2':
                self.view_all_spies()
            elif choice == '3':
                self.view_spy_details()
            elif choice == '4':
                self.deactivate_spy()
            elif choice == '5':
                break
            else:
                self.view.display_message("Invalid choice. Please try again.", is_error=True)

    # Handle the mission management submen
    def manage_missions(self):
        while True:
            self.view.display_mission_menu()
            choice = self.view.get_user_input("Enter your choice (1-6)")
            
            if choice == '1':
                self.create_mission()
            elif choice == '2':
                self.view_all_missions()
            elif choice == '3':
                self.view_mission_details()
            elif choice == '4':
                self.assign_spy_to_mission()
            elif choice == '5':
                self.complete_mission()
            elif choice == '6':
                break
            else:
                self.view.display_message("Invalid choice. Please try again.", is_error=True)

    # Handle the information leak submen
    def manage_leaks(self):
        while True:
            self.view.display_leak_menu()
            choice = self.view.get_user_input("Enter your choice (1-5)")
            
            if choice == '1':
                self.create_leak()
            elif choice == '2':
                self.view_all_leaks()
            elif choice == '3':
                self.view_leak_details()
            elif choice == '4':
                self.verify_leak()
            elif choice == '5':
                break
            else:
                self.view.display_message("Invalid choice. Please try again.", is_error=True)

    # Handle the report generation submen
    def generate_reports(self):
        while True:
            self.view.display_report_menu()
            choice = self.view.get_user_input("Enter your choice (1-5)")
            
            if choice == '1':
                report_data = self.model.generate_report()
                self.view.display_report(report_data, "network status")
            elif choice == '2':
                missions = self.model.get_all_missions(status_filter="In Progress")
                self.view.display_report(missions, "active missions")
            elif choice == '3':
                spies = self.model.get_all_spies()
                self.view.display_report(spies, "skills inventory")
            elif choice == '4':
                leaks = self.model.get_all_leaks()
                self.view.display_report(leaks, "leak analysis")
            elif choice == '5':
                break
            else:
                self.view.display_message("Invalid choice. Please try again.", is_error=True)

    # Handle adding a new sp
    def add_spy(self):
        self.view.display_message("Adding a new spy to the network...")
        
        real_name = self.view.get_user_input("Enter spy's real name")
        cover_name = self.view.get_user_input("Enter spy's cover name")
        nationality = self.view.get_user_input("Enter spy's nationality")
        
        skills = []
        while True:
            skill = self.view.get_user_input("Enter a skill (or 'done' to finish)")
            if skill.lower() == 'done':
                break
            skills.append(skill)
            
        clearance_level = self.view.get_user_input("Enter clearance level (1-5)")
        while not clearance_level.isdigit() or int(clearance_level) < 1 or int(clearance_level) > 5:
            self.view.display_message("Invalid clearance level. Must be between 1 and 5.", is_error=True)
            clearance_level = self.view.get_user_input("Enter clearance level (1-5)")
            
        spy = self.model.add_spy(real_name, cover_name, nationality, skills, int(clearance_level))
        self.view.display_message(f"Spy {spy['cover_name']} added successfully with ID: {spy['id']}")

    # Display all spie
    def view_all_spies(self):
        active_only = self.view.get_user_input("Show only active spies? (y/n)").lower() == 'y'
        spies = self.model.get_all_spies(active_only=active_only)
        self.view.display_spies_list(spies)

    # Display details for a specific sp
    def view_spy_details(self):
        spy_id = self.view.get_user_input("Enter spy ID (or 'list' to view all spies)")
        if spy_id.lower() == 'list':
            self.view_all_spies()
            spy_id = self.view.get_user_input("Enter spy ID")
            
        spy = self.model.get_spy_by_id(spy_id)
        self.view.display_spy_details(spy)

    # Handle deactivating a sp
    def deactivate_spy(self):
        spy_id = self.view.get_user_input("Enter spy ID to deactivate (or 'list' to view all spies)")
        if spy_id.lower() == 'list':
            self.view_all_spies()
            spy_id = self.view.get_user_input("Enter spy ID to deactivate")
            
        success = self.model.deactivate_spy(spy_id)
        if success:
            self.view.display_message("Spy deactivated successfully")
        else:
            self.view.display_message("Failed to deactivate spy. ID not found.", is_error=True)

    # Handle creating a new missio
    def create_mission(self):
        self.view.display_message("Creating a new mission...")
        
        name = self.view.get_user_input("Enter mission name")
        objective = self.view.get_user_input("Enter mission objective")
        location = self.view.get_user_input("Enter mission location")
        
        priority = self.view.get_user_input("Enter priority (1-3)")
        while not priority.isdigit() or int(priority) < 1 or int(priority) > 3:
            self.view.display_message("Invalid priority. Must be between 1 and 3.", is_error=True)
            priority = self.view.get_user_input("Enter priority (1-3)")
            
        required_skills = []
        while True:
            skill = self.view.get_user_input("Enter a required skill (or 'done' to finish)")
            if skill.lower() == 'done':
                break
            required_skills.append(skill)
            
        mission = self.model.create_mission(name, objective, location, int(priority), required_skills)
        self.view.display_message(f"Mission {mission['name']} created successfully with ID: {mission['id']}")

    # Display all mission
    def view_all_missions(self):
        status_filter = None
        filter_choice = self.view.get_user_input("Filter by status? (all/pending/in progress/completed/failed)")
        if filter_choice.lower() in ['pending', 'in progress', 'completed', 'failed']:
            status_filter = filter_choice.title()
            
        missions = self.model.get_all_missions(status_filter=status_filter)
        self.view.display_missions_list(missions)

    # Display details for a specific missio
    def view_mission_details(self):
        mission_id = self.view.get_user_input("Enter mission ID (or 'list' to view all missions)")
        if mission_id.lower() == 'list':
            self.view_all_missions()
            mission_id = self.view.get_user_input("Enter mission ID")
            
        mission = self.model.get_mission_by_id(mission_id)
        self.view.display_mission_details(mission)

    # Handle assigning a spy to a missio
    def assign_spy_to_mission(self):
        spy_id = self.view.get_user_input("Enter spy ID to assign (or 'list' to view all spies)")
        if spy_id.lower() == 'list':
            self.view_all_spies()
            spy_id = self.view.get_user_input("Enter spy ID to assign")
            
        mission_id = self.view.get_user_input("Enter mission ID (or 'list' to view all missions)")
        if mission_id.lower() == 'list':
            self.view_all_missions()
            mission_id = self.view.get_user_input("Enter mission ID")
            
        success = self.model.assign_spy_to_mission(spy_id, mission_id)
        if success:
            spy = self.model.get_spy_by_id(spy_id)
            mission = self.model.get_mission_by_id(mission_id)
            self.view.display_message(f"Spy {spy['cover_name']} assigned to mission {mission['name']}")
        else:
            self.view.display_message("Failed to assign spy to mission. Check IDs.", is_error=True)

    # Handle completing a missio
    def complete_mission(self):
        mission_id = self.view.get_user_input("Enter mission ID to complete (or 'list' to view all missions)")
        if mission_id.lower() == 'list':
            self.view_all_missions()
            mission_id = self.view.get_user_input("Enter mission ID to complete")
            
        success_choice = self.view.get_user_input("Was the mission successful? (y/n)").lower()
        success = success_choice == 'y'
        
        result = self.model.complete_mission(mission_id, success)
        if result:
            status = "completed successfully" if success else "marked as failed"
            self.view.display_message(f"Mission {status}")
        else:
            self.view.display_message("Failed to update mission status. ID not found.", is_error=True)

    # Handle creating a new information lea
    def create_leak(self):
        self.view.display_message("Creating a new information leak...")
        
        source = self.view.get_user_input("Enter leak source (spy ID or external source)")
        content = self.view.get_user_input("Enter leak content")
        classification = self.view.get_user_input("Enter classification level")
        recipient = self.view.get_user_input("Enter recipient (leave blank if unknown)")
        
        leak = self.model.create_leak(source, content, classification, recipient if recipient else None)
        self.view.display_message(f"Leak recorded successfully with ID: {leak['id']}")

    # Display all information leak
    def view_all_leaks(self):
        verified_only = self.view.get_user_input("Show only verified leaks? (y/n)").lower() == 'y'
        leaks = self.model.get_all_leaks(verified_only=verified_only)
        self.view.display_leaks_list(leaks)

    # Display details for a specific lea
    def view_leak_details(self):
        leak_id = self.view.get_user_input("Enter leak ID (or 'list' to view all leaks)")
        if leak_id.lower() == 'list':
            self.view_all_leaks()
            leak_id = self.view.get_user_input("Enter leak ID")
            
        leak = self.model.get_leak_by_id(leak_id)
        self.view.display_leak_details(leak)

    # Handle verifying an information lea
    def verify_leak(self):
        leak_id = self.view.get_user_input("Enter leak ID to verify (or 'list' to view all leaks)")
        if leak_id.lower() == 'list':
            self.view_all_leaks()
            leak_id = self.view.get_user_input("Enter leak ID to verify")
            
        authentic_choice = self.view.get_user_input("Is this leak authentic? (y/n)").lower()
        is_authentic = authentic_choice == 'y'
        
        success = self.model.verify_leak(leak_id, is_authentic)
        if success:
            status = "verified as authentic" if is_authentic else "marked as false"
            self.view.display_message(f"Leak {status}")
        else:
            self.view.display_message("Failed to verify leak. ID not found.", is_error=True)
# Class handling all display and user interaction for the community simulation.
class CommunityView:
    
    # Display the main menu to the user.
    @staticmethod
    def display_menu():
        print("\nVirtual Post-Apocalypse Community ")
        print("1. Manage Survivors")
        print("2. Manage Resources")
        print("3. Community Actions")
        print("4. View Community Status")
        print("5. Advance Day")
        print("6. View Events Log")
        print("7. Exit")
    
    # Display the survivors management menu.
    @staticmethod
    def display_survivors_menu():
        print("\nSurvivors Management ")
        print("1. Add New Survivor")
        print("2. View All Survivors")
        print("3. View Survivor Details")
        print("4. Return to Main Menu")
    
    # Display the resources management menu.
    @staticmethod
    def display_resources_menu():
        print("\nResources Management ")
        print("1. View Resource Levels")
        print("2. Distribute Food")
        print("3. Improve Shelter")
        print("4. Return to Main Menu")
    
    # Display the community actions menu.
    @staticmethod
    def display_community_actions_menu():
        print("\nCommunity Actions ")
        print("1. Assign Work")
        print("2. Organize Rest")
        print("3. Scavenge for Supplies")
        print("4. Return to Main Menu")
    
    # Display the current community status.
    @staticmethod
    def display_community_status(status):
        print("\nCommunity Status ")
        print(f"Day: {status['day']}")
        print(f"Community Name: {status['name']}")
        print(f"Survivors: {status['alive_survivors']} alive, {status['deceased_survivors']} deceased")
        print(f"Shelter Quality: {status['shelter_quality']}/100")
        print(f"Security Level: {status['security_level']}/100")
        print("\nResources:")
        for name, quantity in status['resources'].items():
            print(f"- {name.capitalize()}: {quantity:.1f} units")
    
    # Display a list of all survivors.
    @staticmethod
    def display_survivors(survivors):
        print("\nSurvivors List ")
        if not survivors:
            print("No survivors in the community yet.")
            return
        
        for i, survivor in enumerate(survivors, 1):
            status = "Alive" if survivor.is_alive else "Deceased"
            print(f"{i}. {survivor.name} ({survivor.age} yrs, {status})")
    
    # Display detailed information about a survivor.
    @staticmethod
    def display_survivor_details(survivor):
        print("\nSurvivor Details ")
        print(survivor)
    
    # Display the events log.
    @staticmethod
    def display_events_log(events):
        print("\nRecent Events ")
        for event in events:
            print(f"- {event}")
    
    # Get validated user input of a specific type.
    @staticmethod
    def get_user_input(prompt, input_type=str):
        while True:
            try:
                user_input = input(prompt)
                return input_type(user_input)
            except ValueError:
                print(f"Invalid input. Please enter a {input_type.__name__}.")
    
    # Get information for a new survivor from the user.
    @staticmethod
    def get_new_survivor_info():
        print("\nAdd New Survivor ")
        name = CommunityView.get_user_input("Enter survivor name: ", str)
        age = CommunityView.get_user_input("Enter survivor age: ", int)
        
        print("Enter survivor skills (comma separated):")
        print("Available skills: hunting, farming, building, healing, scavenging, leadership")
        skills_input = CommunityView.get_user_input("Skills: ", str)
        skills = [skill.strip().lower() for skill in skills_input.split(",")]
        
        return {"name": name, "age": age, "skills": skills}
    
    # # Display a message to the user.
    @staticmethod
    def display_message(message):
        print(f"\n{message}")
    
    # # Display an error message to the user.
    @staticmethod
    def display_error(message):
        print(f"\nERROR: {message}")
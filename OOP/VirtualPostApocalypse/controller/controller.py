from model.model import Survivor, Community
from view.view import CommunityView
import random

# Controller class for the post-apocalyptic community simulation
class CommunityController:
    
    # Initialize the controller with a community and view
    def __init__(self):
        self.view = CommunityView()
        self.community = None
    
    # Start the simulation by setting up the community
    def start_simulation(self):
        print("Welcome to Virtual Post-Apocalypse Community Simulator!")
        community_name = self.view.get_user_input("Enter your community name: ", str)
        self.community = Community(community_name)
        
        # Add some initial survivors
        initial_survivors = [
            Survivor("Alex", 32, ["hunting", "building"]),
            Survivor("Morgan", 28, ["healing", "farming"]),
            Survivor("Casey", 45, ["leadership", "scavenging"])
        ]
        
        for survivor in initial_survivors:
            self.community.add_survivor(survivor)
        
        self.run_main_menu()
    
    # Run the main menu loop
    def run_main_menu(self):
        while True:
            self.view.display_menu()
            choice = self.view.get_user_input("Enter your choice (1-7): ", int)
            
            if choice == 1:
                self.manage_survivors()
            elif choice == 2:
                self.manage_resources()
            elif choice == 3:
                self.community_actions()
            elif choice == 4:
                self.view_community_status()
            elif choice == 5:
                self.advance_day()
            elif choice == 6:
                self.view_events_log()
            elif choice == 7:
                print("\nThank you for playing Virtual Post-Apocalypse!")
                break
            else:
                self.view.display_error("Invalid choice. Please select 1-7.")
    
    # Handle the survivors management menu
    def manage_survivors(self):
        while True:
            self.view.display_survivors_menu()
            choice = self.view.get_user_input("Enter your choice (1-4): ", int)
            
            if choice == 1:
                self.add_survivor()
            elif choice == 2:
                self.view_all_survivors()
            elif choice == 3:
                self.view_survivor_details()
            elif choice == 4:
                break
            else:
                self.view.display_error("Invalid choice. Please select 1-4.")
    
    # Handle the resources management menu
    def manage_resources(self):
        while True:
            self.view.display_resources_menu()
            choice = self.view.get_user_input("Enter your choice (1-4): ", int)
            
            if choice == 1:
                self.view_community_status()
            elif choice == 2:
                self.distribute_food()
            elif choice == 3:
                self.improve_shelter()
            elif choice == 4:
                break
            else:
                self.view.display_error("Invalid choice. Please select 1-4.")
    
    # Handle the community actions menu
    def community_actions(self):
        while True:
            self.view.display_community_actions_menu()
            choice = self.view.get_user_input("Enter your choice (1-4): ", int)
            
            if choice == 1:
                self.assign_work()
            elif choice == 2:
                self.organize_rest()
            elif choice == 3:
                self.scavenge_supplies()
            elif choice == 4:
                break
            else:
                self.view.display_error("Invalid choice. Please select 1-4.")
    
    # Add a new survivor to the community
    def add_survivor(self):
        survivor_info = self.view.get_new_survivor_info()
        new_survivor = Survivor(**survivor_info)
        self.community.add_survivor(new_survivor)
        self.view.display_message(f"{new_survivor.name} has joined the community!")
    
    # Display all survivors in the community
    def view_all_survivors(self):
        alive_survivors = [s for s in self.community.survivors if s.is_alive]
        self.view.display_survivors(alive_survivors)
    
    # Display details of a specific survivor
    def view_survivor_details(self):
        self.view_all_survivors()
        if not self.community.survivors:
            return
        
        try:
            choice = self.view.get_user_input("Select survivor number to view details: ", int)
            selected = self.community.survivors[choice-1]
            self.view.display_survivor_details(selected)
        except (IndexError, ValueError):
            self.view.display_error("Invalid survivor selection.")
    
    # Display the current community status
    def view_community_status(self):
        status = self.community.get_status()
        self.view.display_community_status(status)
    
    # Display the recent events log
    def view_events_log(self):
        events = self.community.get_events_log()
        self.view.display_events_log(events)
    
    # Distribute food to all survivors
    def distribute_food(self):
        if self.community.distribute_food():
            self.view.display_message("Food distributed successfully!")
        else:
            self.view.display_error("Not enough food to feed everyone!")
    
    # Attempt to improve the community shelter
    def improve_shelter(self):
        if self.community.improve_shelter():
            self.view.display_message("Shelter improved!")
        else:
            self.view.display_error("Not enough building materials!")
    
    # Assign work to survivors
    def assign_work(self):
        alive_survivors = [s for s in self.community.survivors if s.is_alive]
        if not alive_survivors:
            self.view.display_error("No alive survivors to assign work!")
            return
        
        # Randomly assign work
        for survivor in alive_survivors:
            survivor.work(difficulty=random.randint(30, 70))
        
        # Potential resource gains
        if random.random() < 0.7:  # 70% chance of finding something
            resource_gained = random.choice(["food", "water", "building_materials"])
            amount = random.randint(5, 20)
            self.community.resources[resource_gained].quantity += amount
            self.community.log_event(f"Survivors found {amount} units of {resource_gained} while working.")
        
        self.view.display_message("Survivors have completed their work assignments.")
    
    # Organize rest for survivors
    def organize_rest(self):
        alive_survivors = [s for s in self.community.survivors if s.is_alive]
        if not alive_survivors:
            self.view.display_error("No alive survivors to organize rest for!")
            return
        
        for survivor in alive_survivors:
            survivor.rest()
        
        self.community.log_event("Survivors took a day to rest and recover.")
        self.view.display_message("Survivors have rested and recovered some health and morale.")
    
    # Organize a scavenging mission
    def scavenge_supplies(self):
        alive_survivors = [s for s in self.community.survivors if s.is_alive]
        if not alive_survivors:
            self.view.display_error("No alive survivors to send scavenging!")
            return
        
        # Determine success based on number of scavengers and skill
        scavengers = [s for s in alive_survivors if "scavenging" in s.skills]
        success_chance = min(0.9, 0.3 + 0.1 * len(scavengers))
        
        if random.random() < success_chance:
            # Successful scavenge
            resource_gained = random.choice(list(self.community.resources.keys()))
            amount = random.randint(10, 40)
            self.community.resources[resource_gained].quantity += amount
            self.community.log_event(f"Scavenging team found {amount} units of {resource_gained}!")
            
            # Possible injuries
            if random.random() < 0.2:
                injured = random.choice(alive_survivors)
                injury = random.randint(10, 30)
                injured.health = max(0, injured.health - injury)
                self.community.log_event(f"{injured.name} was injured while scavenging (-{injury} health).")
            
            self.view.display_message(f"Scavenging successful! Gained {amount} {resource_gained}.")
        else:
            # Failed scavenge
            self.community.log_event("Scavenging team returned empty-handed.")
            
            # Possible injuries
            if random.random() < 0.4:
                injured = random.choice(alive_survivors)
                injury = random.randint(15, 40)
                injured.health = max(0, injured.health - injury)
                self.community.log_event(f"{injured.name} was badly injured while scavenging (-{injury} health).")
                self.view.display_message("Scavenging failed and someone was injured!")
            else:
                self.view.display_message("Scavenging failed but everyone returned safely.")
    
    # Advance the simulation by one day
    def advance_day(self):
        self.community.advance_day()
        self.view.display_message(f"Day {self.community.day} begins...")
        
        # Check for deaths
        deaths = [s for s in self.community.survivors if not s.is_alive]
        if deaths:
            for survivor in deaths:
                self.view.display_message(f"{survivor.name} has died.")
        
        # Display new events
        events = self.community.get_events_log(3)  # Get last 3 events
        self.view.display_events_log(events)
        
        # Check for game over
        alive_survivors = [s for s in self.community.survivors if s.is_alive]
        if not alive_survivors:
            self.view.display_message("\nGAME OVER - All survivors have perished.")
            return False
        
        return True
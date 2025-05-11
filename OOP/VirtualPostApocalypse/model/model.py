import random
from datetime import datetime, timedelta

# Class representing a survivor in the post-apocalyptic community.
class Survivor:
    
    # Initialize a survivor.
    def __init__(self, name, age, skills, health=100, hunger=0, morale=50):
        """    
        Args:
            name: Survivor's name
            age: Survivor's age
            skills: List of skills the survivor has
            health: Health status (0-100)
            hunger: Hunger level (0-100)
            morale: Morale level (0-100)
        """
        self.name = name
        self.age = age
        self.skills = skills
        self.health = health
        self.hunger = hunger
        self.morale = morale
        self.is_alive = True
        self.join_date = datetime.now()
        self.last_meal_date = datetime.now()
    
    # Update the survivor's status based on time passing.
    def update_status(self):
        time_since_last_meal = datetime.now() - self.last_meal_date
        if time_since_last_meal > timedelta(hours=12):
            self.hunger = min(100, self.hunger + 10)
        
        if self.hunger > 70:
            self.health = max(0, self.health - 5)
            self.morale = max(0, self.morale - 10)
        elif self.hunger > 40:
            self.health = max(0, self.health - 2)
            self.morale = max(0, self.morale - 5)
        
        if self.health <= 0:
            self.is_alive = False
    
    # Simulate the survivor eating food.
    def eat(self, food_quality=50):
        self.hunger = max(0, self.hunger - food_quality)
        self.last_meal_date = datetime.now()
        self.morale = min(100, self.morale + 10)
    
    # Simulate the survivor working.
    def work(self, difficulty=50):
        if not self.is_alive:
            return False
        
        self.hunger = min(100, self.hunger + 20)
        self.morale = max(0, self.morale - difficulty//10)
        
        if random.random() < 0.1:  # 10% chance of injury
            self.health = max(0, self.health - random.randint(5, 20))
        
        return True
    
    # Simulate the survivor resting.
    def rest(self):
        self.health = min(100, self.health + 10)
        self.morale = min(100, self.morale + 15)
        self.hunger = min(100, self.hunger + 5)
    
    def __str__(self):
        status = "Alive" if self.is_alive else "Deceased"
        return (f"{self.name} ({self.age} yrs, {status}) - "
                f"Health: {self.health}, Hunger: {self.hunger}, Morale: {self.morale}\n"
                f"Skills: {', '.join(self.skills)}")


# Class representing a resource in the post-apocalyptic world.
class Resource:
    
    # Initialize a resource.
    def __init__(self, name, quantity, quality=50, replenish_rate=0):
        """    
        Args:
            name: Resource name
            quantity: Amount available
            quality: Quality of resource (0-100)
            replenish_rate: Daily replenishment rate
        """
        self.name = name
        self.quantity = quantity
        self.quality = quality
        self.replenish_rate = replenish_rate
        self.last_updated = datetime.now()
    
    # Update resource quantity based on replenishment rate.
    def update(self):
        time_elapsed = datetime.now() - self.last_updated
        days_elapsed = time_elapsed.total_seconds() / 86400
        self.quantity += days_elapsed * self.replenish_rate
        self.last_updated = datetime.now()
    
    # Consume a certain amount of the resource.
    def consume(self, amount):
        if amount <= self.quantity:
            self.quantity -= amount
            return True
        return False
    
    def __str__(self):
        return f"{self.name}: {self.quantity:.1f} units (Quality: {self.quality})"


# Class representing the post-apocalyptic community.
class Community:
    
    # Initialize the community.
    def __init__(self, name):
        """    
        Args:
            name: Community name
        """
        self.name = name
        self.survivors = []
        self.resources = {
            "food": Resource("Food", 100, 60, 5),
            "water": Resource("Water", 200, 70, 10),
            "medicine": Resource("Medicine", 20, 40, 0.1),
            "building_materials": Resource("Building Materials", 50, 50, 0.5)
        }
        self.day = 1
        self.events_log = []
        self.shelter_quality = 50
        self.security_level = 50
    
    # Add a new survivor to the community.
    def add_survivor(self, survivor):
        self.survivors.append(survivor)
        self.log_event(f"{survivor.name} joined the community.")
    
    # Remove a survivor from the community.
    def remove_survivor(self, survivor):
        if survivor in self.survivors:
            self.survivors.remove(survivor)
            self.log_event(f"{survivor.name} left or died.")
    
    # Log an event in the community's history.
    def log_event(self, event):
        timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        self.events_log.append(f"Day {self.day} - {timestamp}: {event}")
    
    # Advance the simulation by one day.
    def advance_day(self):
        self.day += 1
        
        # Update all resources
        for resource in self.resources.values():
            resource.update()
        
        # Update all survivors
        for survivor in self.survivors:
            survivor.update_status()
            if not survivor.is_alive:
                self.remove_survivor(survivor)
        
        # Random events
        self._random_events()
    
    # Handle random events that can occur.
    def _random_events(self):
        event_chance = random.random()
        
        if event_chance < 0.1:  # 10% chance for an event
            events = [
                "A passing trader offered to exchange goods.",
                "A storm damaged some of your shelter.",
                "A wild animal attacked your food supplies.",
                "You found an abandoned cache of supplies.",
                "A group of raiders was spotted nearby.",
                "A survivor discovered a new skill.",
                "A sickness is spreading among the survivors."
            ]
            event = random.choice(events)
            self.log_event(f"Random Event: {event}")
            
            # Apply event effects
            if "trader" in event:
                self.resources["food"].quantity += 10
                self.resources["medicine"].quantity -= 2
            elif "storm" in event:
                self.shelter_quality = max(0, self.shelter_quality - 10)
            elif "animal" in event:
                self.resources["food"].quantity = max(0, self.resources["food"].quantity - 15)
            elif "cache" in event:
                for resource in self.resources.values():
                    resource.quantity += random.randint(5, 20)
            elif "raiders" in event:
                self.security_level = max(0, self.security_level - 15)
            elif "sickness" in event:
                for survivor in self.survivors:
                    if random.random() < 0.3:
                        survivor.health = max(0, survivor.health - 20)
    
    # Distribute food to all survivors.
    def distribute_food(self):
        food_needed = len([s for s in self.survivors if s.is_alive]) * 1.5
        if self.resources["food"].consume(food_needed):
            food_quality = self.resources["food"].quality
            for survivor in self.survivors:
                if survivor.is_alive:
                    survivor.eat(food_quality)
            self.log_event(f"Distributed {food_needed:.1f} units of food to survivors.")
            return True
        else:
            self.log_event("Not enough food to feed everyone!")
            return False
    
    # Attempt to improve the community shelter.
    def improve_shelter(self):
        materials_needed = 10
        if self.resources["building_materials"].consume(materials_needed):
            self.shelter_quality = min(100, self.shelter_quality + 5)
            self.log_event(f"Used {materials_needed} building materials to improve shelter.")
            return True
        return False
    
    # Get the current status of the community.
    def get_status(self):
        alive_count = len([s for s in self.survivors if s.is_alive])
        deceased_count = len([s for s in self.survivors if not s.is_alive])
        
        status = {
            "day": self.day,
            "name": self.name,
            "alive_survivors": alive_count,
            "deceased_survivors": deceased_count,
            "shelter_quality": self.shelter_quality,
            "security_level": self.security_level,
            "resources": {name: resource.quantity for name, resource in self.resources.items()}
        }
        
        return status
    
    # Get a detailed report on all survivors.
    def get_survivors_report(self):
        return [str(survivor) for survivor in self.survivors]
    
    # Get the most recent events from the log.
    def get_events_log(self, num_events=5):
        return self.events_log[-num_events:] if self.events_log else ["No events recorded yet."]
class BirdStudy:
    def __init__(self):
        # Initialize an empty list to store bird names
        self.birds = []

    # Add a new bird to the study.
    def add_bird(self, bird_name):
        if bird_name not in self.birds:
            self.birds.append(bird_name)

    # Remove a bird from the study.
    def remove_bird(self, bird_name):
        if bird_name in self.birds:
            self.birds.remove(bird_name)
            return True
        return False

    # Return a list of all birds.
    def get_all_birds(self):
        return self.birds

    # Search for a bird by name.
    def search_bird(self, bird_name):
        if bird_name in self.birds:
            return bird_name
        return None

    # Update the name of an existing bird.
    def update_bird(self, old_name, new_name):
        if old_name in self.birds and new_name not in self.birds:
            index = self.birds.index(old_name)
            self.birds[index] = new_name
            return True
        return False

    # Return the total number of birds.
    def count_birds(self):
        return len(self.birds)

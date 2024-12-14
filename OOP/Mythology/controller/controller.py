from model.model import CharacterModel, MythicalCharacter

class CharacterPresenter:
    # Initialize the model
    def __init__(self):
        self.model = CharacterModel()  

    def add_character(self, name, mythology, description):
        # Create a new character
        character = MythicalCharacter(name, mythology, description)  
        self.model.add_character(character)

    def remove_character(self, name):
        # Remove a character by name
        self.model.remove_character(name)  

    def get_characters(self):
        # Get all characters
        return self.model.get_all_characters()  

    def get_character_by_name(self, name):
        # Get a specific character by name
        return self.model.get_character_by_name(name)  

    def update_character(self, name, new_name, new_mythology, new_description):
        # Update character details
        self.model.update_character(name, new_name, new_mythology, new_description)  

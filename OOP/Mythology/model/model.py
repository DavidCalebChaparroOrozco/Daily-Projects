class MythicalCharacter:
    def __init__(self, name, mythology, description):
        # Name of the character
        self.name = name  
        # Mythological origin (e.g., Greek, Arthurian)
        self.mythology = mythology  
        # Brief description of the character
        self.description = description  

class CharacterModel:
    def __init__(self):
        # List to store characters
        self.characters = []  

    def add_character(self, character):
        # Add a new character to the list
        self.characters.append(character)  

    def remove_character(self, name):
        # Remove a character by name
        self.characters = [char for char in self.characters if char.name != name]

    def get_all_characters(self):
        # Return all characters
        return self.characters  

    def get_character_by_name(self, name):
        # Find a character by name
        for char in self.characters:
            if char.name.lower() == name.lower():
                return char
        # Return None if not found
        return None  

    def update_character(self, name, new_name, new_mythology, new_description):
        character = self.get_character_by_name(name)
        if character:
            character.name = new_name
            character.mythology = new_mythology
            # Update character details
            character.description = new_description  

class CharacterView:
    @staticmethod
    def display_menu():
        print("\nWelcome to the Mythical Characters Management System by David Caleb")
        print("1. View all mythical characters")
        print("2. Add new mythical character")
        print("3. Remove mythical character")
        print("4. View specific mythical character")
        print("5. Update existing mythical character")
        print("6. Exit")

    @staticmethod
    def show_characters(characters):
        if not characters:
            print("No characters available.")
            return
        print("\nCurrent Mythical Characters:")
        for char in characters:
            print(f"- Name: {char.name}, Mythology: {char.mythology}, Description: {char.description}")

    @staticmethod
    def get_character_input():
        name = input("Enter character name: ")
        mythology = input("Enter mythology (e.g., Greek, Arthurian): ")
        description = input("Enter a brief description: ")
        return name, mythology, description

    @staticmethod
    def get_character_name():
        return input("Enter the name of the character to remove: ")

    @staticmethod
    def get_specific_character_name():
        return input("Enter the name of the character to view: ")

    @staticmethod
    def get_update_input():
        old_name = input("Enter the current name of the character to update: ")
        new_name = input("Enter the new name: ")
        new_mythology = input("Enter the new mythology: ")
        new_description = input("Enter the new description: ")
        return old_name, new_name, new_mythology, new_description

    @staticmethod
    def show_specific_character(character):
        if not character:
            print("Character not found.")
            return
        print(f"\nCharacter Details:\n- Name: {character.name}\n- Mythology: {character.mythology}\n- Description: {character.description}")

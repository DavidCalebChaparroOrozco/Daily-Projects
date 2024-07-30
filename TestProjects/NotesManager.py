# Import necessary libraries
import unittest

# NoteManager class to manage notes
class NoteManager:
    def __init__(self):
        # Initialize an empty list to store notes
        self.notes = []

    def add_note(self, note):
        # Add a note to the list
        self.notes.append(note)

    def delete_note(self, note):
        # Delete a note from the list if it exists
        if note in self.notes:
            self.notes.remove(note)

    def search_note(self, query):
        # Search for notes that contain the query string
        return [note for note in self.notes if query in note]

# Unit test class for the NoteManager
class TestNoteManager(unittest.TestCase):

    def setUp(self):
        # Create a new instance of NoteManager for each test
        self.note_manager = NoteManager()

    def test_add_note(self):
        # Test adding a note
        self.note_manager.add_note("This is a test note.")
        self.assertIn("This is a test note.", self.note_manager.notes)

    def test_delete_note_existing(self):
        # Test deleting an existing note
        self.note_manager.add_note("Note to be deleted.")
        self.note_manager.delete_note("Note to be deleted.")
        self.assertNotIn("Note to be deleted.", self.note_manager.notes)

    def test_delete_note_non_existing(self):
        # Test deleting a non-existing note (should not raise an error)
        self.note_manager.add_note("Existing note.")
        self.note_manager.delete_note("Non-existing note.")
        self.assertIn("Existing note.", self.note_manager.notes)
        self.assertNotIn("Non-existing note.", self.note_manager.notes)

    def test_search_note_found(self):
        # Test searching for a note that exists
        self.note_manager.add_note("This is a searchable note.")
        result = self.note_manager.search_note("searchable")
        self.assertEqual(result, ["This is a searchable note."])

    def test_search_note_not_found(self):
        # Test searching for a note that does not exist
        self.note_manager.add_note("This is another note.")
        result = self.note_manager.search_note("non-existent")
        self.assertEqual(result, [])

# Function to display the menu and handle user input
def menu():
    note_manager = NoteManager()
    while True:
        print("\nNote Manager Menu:")
        print("1. Add Note")
        print("2. Delete Note")
        print("3. Search Notes")
        print("4. Run Tests")
        print("5. Exit")
        choice = input("Enter your choice: ")

        if choice == '1':
            note = input("Enter the note to add: ")
            note_manager.add_note(note)
            print("Note added.")

        elif choice == '2':
            note = input("Enter the note to delete: ")
            note_manager.delete_note(note)
            print("Note deleted.")

        elif choice == '3':
            query = input("Enter the search query: ")
            results = note_manager.search_note(query)
            print("Search results:")
            for note in results:
                print(note)

        elif choice == '4':
            print("Running tests...")
            unittest.main(argv=[''], verbosity=2, exit=False)

        elif choice == '5':
            print("Exiting...")
            break

        else:
            print("Invalid choice. Please try again.")

# Run the menu
if __name__ == '__main__':
    menu()

from model.model import UserStoryModel
from view.view import UserStoryView

class UserStoryController:
    def __init__(self):
        self.model = UserStoryModel()
        self.view = UserStoryView()
        
        # Load existing user stories from a file at startup
        self.model.load_from_file('user_stories.json')

    def run(self):
        while True:
            self.view.display_menu()
            choice = input("Choose an option: ")

            if choice == '1':
                stories = self.model.get_all_user_stories()
                self.view.display_user_stories(stories)

            elif choice == '2':
                title, description, priority = self.view.prompt_for_user_story()
                self.model.add_user_story(title, description, priority)
                self.view.display_message(f"User story '{title}' added.")

            elif choice == '3':
                title = self.view.prompt_for_title()
                if self.model.find_user_story(title):
                    self.model.remove_user_story(title)
                    self.view.display_message(f"User story '{title}' removed.")
                else:
                    self.view.display_message(f"No user story found with title '{title}'.")

            elif choice == '4':
                title = input("Enter the title of the user story to edit: ")
                if self.model.find_user_story(title):
                    description, priority, status = self.view.prompt_for_edit(title)
                    existing_story = self.model.find_user_story(title)
                    existing_story.description = description
                    existing_story.priority = priority
                    existing_story.status = status
                    self.view.display_message(f"User story '{title}' updated.")
                else:
                    self.view.display_message(f"No user story found with title '{title}'.")

            elif choice == '5':
                # Save all user stories to a file before exiting
                self.model.save_to_file('user_stories.json')
                self.view.display_message("Exiting the application.")
                break

            else:
                self.view.display_message("Invalid option. Please try again.")

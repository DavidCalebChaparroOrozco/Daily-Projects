class UserStoryView:
    @staticmethod
    def display_menu():
        print("\nWelcome to the User Story Manager by David Caleb")
        print("1. View all user stories")
        print("2. Add new user story")
        print("3. Remove user story")
        print("4. Edit user story")
        print("5. Exit")

    @staticmethod
    def display_user_stories(user_stories):
        if not user_stories:
            print("No user stories available.")
            return
        
        print("\nUser Stories:")
        for story in user_stories:
            print(f"- {story}")

    @staticmethod
    def prompt_for_user_story():
        title = input("Enter the title of the user story: ")
        description = input("Enter the description of the user story: ")
        priority = input("Enter priority (High/Medium/Low): ")
        return title, description, priority

    @staticmethod
    def prompt_for_title():
        return input("Enter the title of the user story to remove: ")

    @staticmethod
    def prompt_for_edit(title):
        description = input(f"Enter new description for '{title}': ")
        priority = input("Enter new priority (High/Medium/Low): ")
        status = input("Enter new status (Pending/In Progress/Completed): ")
        return description, priority, status

    @staticmethod
    def display_message(message):
        print(message)

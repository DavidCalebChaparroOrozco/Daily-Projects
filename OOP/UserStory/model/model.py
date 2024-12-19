import json

class UserStory:
    def __init__(self, title, description, priority='Medium', status='Pending'):
        self.title = title
        self.description = description
        # Priority can be High, Medium, Low
        self.priority = priority  
        # Status can be Pending, In Progress, Completed
        self.status = status      

    def __str__(self):
        return f"[{self.priority}] {self.title}: {self.description} (Status: {self.status})"


class UserStoryModel:
    def __init__(self):
        self.user_stories = []

    def add_user_story(self, title, description, priority='Medium', status='Pending'):
        new_story = UserStory(title, description, priority, status)
        self.user_stories.append(new_story)

    # Remove a user story given a title
    def remove_user_story(self, title):
        self.user_stories = [story for story in self.user_stories if story.title != title]

    def get_all_user_stories(self):
        return self.user_stories

    # Find a user story given a title
    def find_user_story(self, title):
        for story in self.user_stories:
            if story.title == title:
                return story
        return None

    # Save user stories to a JSON file.
    def save_to_file(self, filename):
        with open(filename, 'w') as file:
            json.dump([story.__dict__ for story in self.user_stories], file)

    # Load user stories from a JSON file.
    def load_from_file(self, filename):
        try:
            with open(filename, 'r') as file:
                stories_data = json.load(file)
                self.user_stories = [UserStory(**data) for data in stories_data]
        except FileNotFoundError:
            print("No previous data found.")

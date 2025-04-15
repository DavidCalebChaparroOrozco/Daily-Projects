# Import necessary libraries
import json
import os
from datetime import datetime

class MuseumModel:
    def __init__(self):
        self.artifacts = []
        self.exhibitions = []
        self.tours = []
        self.users = []
        self.data_file = "museum_data.json"
        self.load_data()

    # Load museum data from JSON file if it exists.
    def load_data(self):
        if os.path.exists(self.data_file):
            with open(self.data_file, 'r') as file:
                data = json.load(file)
                self.artifacts = data.get('artifacts', [])
                self.exhibitions = data.get('exhibitions', [])
                self.tours = data.get('tours', [])
                self.users = data.get('users', [])

    # Save museum data to JSON file.
    def save_data(self):
        data = {
            'artifacts': self.artifacts,
            'exhibitions': self.exhibitions,
            'tours': self.tours,
            'users': self.users
        }
        with open(self.data_file, 'w') as file:
            json.dump(data, file, indent=4)

    # Artifact CRUD operations
    # Add a new artifact to the collection.
    def add_artifact(self, artifact):
        artifact['id'] = len(self.artifacts) + 1
        artifact['created_at'] = datetime.now().isoformat()
        self.artifacts.append(artifact)
        self.save_data()
        return artifact

    # Get an artifact by ID.
    def get_artifact(self, artifact_id):
        for artifact in self.artifacts:
            if artifact['id'] == artifact_id:
                return artifact
        return None

    # Update an existing artifact.
    def update_artifact(self, artifact_id, updated_data):
        for artifact in self.artifacts:
            if artifact['id'] == artifact_id:
                artifact.update(updated_data)
                artifact['updated_at'] = datetime.now().isoformat()
                self.save_data()
                return artifact
        return None

    # Delete an artifact by ID.
    def delete_artifact(self, artifact_id):
        self.artifacts = [a for a in self.artifacts if a['id'] != artifact_id]
        self.save_data()
        return True

    # List all artifacts.
    def list_artifacts(self):
        return self.artifacts

    # Exhibition CRUD operations
    # Add a new exhibition.
    def add_exhibition(self, exhibition):
        exhibition['id'] = len(self.exhibitions) + 1
        exhibition['created_at'] = datetime.now().isoformat()
        self.exhibitions.append(exhibition)
        self.save_data()
        return exhibition

    # Get an exhibition by ID.
    def get_exhibition(self, exhibition_id):
        for exhibition in self.exhibitions:
            if exhibition['id'] == exhibition_id:
                return exhibition
        return None

    # List all exhibitions.
    def list_exhibitions(self):
        return self.exhibitions

    # Tour CRUD operations
    # Add a new virtual tour.
    def add_tour(self, tour):
        tour['id'] = len(self.tours) + 1
        tour['created_at'] = datetime.now().isoformat()
        self.tours.append(tour)
        self.save_data()
        return tour

    # Get a tour by ID.
    def get_tour(self, tour_id):
        for tour in self.tours:
            if tour['id'] == tour_id:
                return tour
        return None

    # List all virtual tours.
    def list_tours(self):
        return self.tours

    # User management
    # Add a new user (for future authentication).
    def add_user(self, user):
        user['id'] = len(self.users) + 1
        user['created_at'] = datetime.now().isoformat()
        self.users.append(user)
        self.save_data()
        return user

    # Authenticate a user (basic implementation).
    def authenticate_user(self, username, password):
        for user in self.users:
            if user['username'] == username and user['password'] == password:
                return user
        return None
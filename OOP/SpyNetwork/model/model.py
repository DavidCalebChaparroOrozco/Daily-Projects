# Import necessary libraries
import json
import random
from datetime import datetime
from uuid import uuid4
import hashlib

class SpyModel:
    # Initialize the model with empty data structures
    def __init__(self):
        # List to store spy objects
        self.spies = []          
        # List to store mission objects
        self.missions = []       
        # List to store information leaks
        self.leaks = []          
        # Load existing data from files
        self.load_data()         

    # Load data from JSON files if they exist
    def load_data(self):
        try:
            with open('spies.json', 'r') as f:
                self.spies = json.load(f)
        except (FileNotFoundError, json.JSONDecodeError):
            self.spies = []
            
        try:
            with open('missions.json', 'r') as f:
                self.missions = json.load(f)
        except (FileNotFoundError, json.JSONDecodeError):
            self.missions = []
            
        try:
            with open('leaks.json', 'r') as f:
                self.leaks = json.load(f)
        except (FileNotFoundError, json.JSONDecodeError):
            self.leaks = []

    # Save all data to JSON files
    def save_data(self):
        with open('spies.json', 'w') as f:
            json.dump(self.spies, f, indent=4)
        with open('missions.json', 'w') as f:
            json.dump(self.missions, f, indent=4)
        with open('leaks.json', 'w') as f:
            json.dump(self.leaks, f, indent=4)

    # Add a new spy to the network
    def add_spy(self, real_name, cover_name, nationality, skills, clearance_level):
        """
        Args:
            real_name: Spy's real name
            cover_name: Spy's cover identity
            nationality: Spy's nationality
            skills: List of skills
            clearance_level: Security clearance level (1-5)
        Returns:
            dict: The created spy object
        """
        spy_id = str(uuid4())
        new_spy = {
            'id': spy_id,
            'real_name': real_name,
            'cover_name': cover_name,
            'nationality': nationality,
            'skills': skills,
            'clearance_level': clearance_level,
            'active': True,
            'created_at': datetime.now().isoformat(),
            'last_mission': None
        }
        self.spies.append(new_spy)
        self.save_data()
        return new_spy

    # Deactivate a spy (mark as inactive)
    def deactivate_spy(self, spy_id):
        """
        Args:
            spy_id: ID of the spy to deactivate
        Returns:
            bool: True if successful, False if spy not found
        """
        for spy in self.spies:
            if spy['id'] == spy_id:
                spy['active'] = False
                self.save_data()
                return True
        return False

    # Create a new mission
    def create_mission(self, name, objective, location, priority, required_skills):
        """
        Args:
            name: Mission name
            objective: Mission objective
            location: Mission location
            priority: Priority level (1-3)
            required_skills: List of required skills
        Returns:
            dict: The created mission object
        """
        mission_id = str(uuid4())
        new_mission = {
            'id': mission_id,
            'name': name,
            'objective': objective,
            'location': location,
            'priority': priority,
            'required_skills': required_skills,
            # Pending, In Progress, Completed, Failed
            'status': 'Pending',  
            'assigned_spies': [],
            'start_date': None,
            'end_date': None,
            'created_at': datetime.now().isoformat()
        }
        self.missions.append(new_mission)
        self.save_data()
        return new_mission

    # Assign a spy to a mission
    def assign_spy_to_mission(self, spy_id, mission_id):
        """
        Args:
            spy_id: ID of the spy to assign
            mission_id: ID of the mission
        Returns:
            bool: True if successful, False if spy or mission not found
        """
        spy = next((s for s in self.spies if s['id'] == spy_id), None)
        mission = next((m for m in self.missions if m['id'] == mission_id), None)
        
        if not spy or not mission:
            return False
            
        if spy_id not in mission['assigned_spies']:
            mission['assigned_spies'].append(spy_id)
            
        if mission['status'] == 'Pending':
            mission['status'] = 'In Progress'
            mission['start_date'] = datetime.now().isoformat()
            
        spy['last_mission'] = mission_id
        self.save_data()
        return True

    # Mark a mission as completed or failed
    def complete_mission(self, mission_id, success=True):
        """
        Args:
            mission_id: ID of the mission
            success (bool): True if mission succeeded, False if failed
        Returns:
            bool: True if successful, False if mission not found
        """
        mission = next((m for m in self.missions if m['id'] == mission_id), None)
        if not mission:
            return False
            
        mission['status'] = 'Completed' if success else 'Failed'
        mission['end_date'] = datetime.now().isoformat()
        self.save_data()
        return True

    # Create an information leak
    def create_leak(self, source, content, classification, recipient=None):
        """
        Args:
            source: Source of the information (spy ID or external)
            content: Content of the leak
            classification: Classification level
            recipient (str, optional): Recipient of the leak
        Returns:
            dict: The created leak object
        """
        leak_id = str(uuid4())
        encrypted_content = hashlib.sha256(content.encode()).hexdigest()  # Simple "encryption"
        
        new_leak = {
            'id': leak_id,
            'source': source,
            'content': content,
            'encrypted_content': encrypted_content,
            'classification': classification,
            'recipient': recipient,
            'leak_date': datetime.now().isoformat(),
            'verified': False
        }
        self.leaks.append(new_leak)
        self.save_data()
        return new_leak

    # Verify or discredit a leak
    def verify_leak(self, leak_id, is_authentic):
        """
        Args:
            leak_id: ID of the leak
            is_authentic (bool): True if leak is authentic
        Returns:
            bool: True if successful, False if leak not found
        """
        leak = next((l for l in self.leaks if l['id'] == leak_id), None)
        if not leak:
            return False
            
        leak['verified'] = is_authentic
        self.save_data()
        return True

    # Generate a comprehensive report of the spy network
    def generate_report(self):
        """
        Returns:
            dict: Report containing statistics
        """
        active_spies = len([s for s in self.spies if s['active']])
        inactive_spies = len([s for s in self.spies if not s['active']])
        
        missions_completed = len([m for m in self.missions if m['status'] == 'Completed'])
        missions_failed = len([m for m in self.missions if m['status'] == 'Failed'])
        missions_in_progress = len([m for m in self.missions if m['status'] == 'In Progress'])
        
        verified_leaks = len([l for l in self.leaks if l['verified']])
        unverified_leaks = len([l for l in self.leaks if not l['verified']])
        
        return {
            'active_spies': active_spies,
            'inactive_spies': inactive_spies,
            'total_spies': active_spies + inactive_spies,
            'missions_completed': missions_completed,
            'missions_failed': missions_failed,
            'missions_in_progress': missions_in_progress,
            'total_missions': missions_completed + missions_failed + missions_in_progress,
            'verified_leaks': verified_leaks,
            'unverified_leaks': unverified_leaks,
            'total_leaks': verified_leaks + unverified_leaks
        }

    # Retrieve a spy by their I
    def get_spy_by_id(self, spy_id):
        return next((s for s in self.spies if s['id'] == spy_id), None)

    # Retrieve a mission by its I
    def get_mission_by_id(self, mission_id):
        return next((m for m in self.missions if m['id'] == mission_id), None)

    # Retrieve a leak by its I
    def get_leak_by_id(self, leak_id):
        return next((l for l in self.leaks if l['id'] == leak_id), None)

    # Retrieve all spies (optionally only active ones
    def get_all_spies(self, active_only=True):
        if active_only:
            return [s for s in self.spies if s['active']]
        return self.spies

    # Retrieve all missions (optionally filtered by status
    def get_all_missions(self, status_filter=None):
        if status_filter:
            return [m for m in self.missions if m['status'] == status_filter]
        return self.missions

    # Retrieve all leaks (optionally only verified ones
    def get_all_leaks(self, verified_only=False):
        if verified_only:
            return [l for l in self.leaks if l['verified']]
        return self.leaks
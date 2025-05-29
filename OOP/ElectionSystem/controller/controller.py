
from model.model import Candidate, Voter, Election, Ballot, Result
from view.view import ElectionView
import uuid
from typing import List, Dict

# Main controller for the election system.
# Handles all business logic and coordinates between models and views.
class ElectionController:
    def __init__(self):
        self.current_election = None
        self.view = ElectionView()

    # Create a new election.
    def create_election(self):
        self.view.display_header("CREATE NEW ELECTION")
        
        # Get election details
        name = self.view.get_input("Enter election name: ")
        positions_input = self.view.get_input("Enter positions (comma separated): ")
        positions = [pos.strip() for pos in positions_input.split(",") if pos.strip()]
        
        if not positions:
            self.view.display_message("At least one position is required.", is_error=True)
            self.view.press_enter_to_continue()
            return
        
        # Create election
        election_id = str(uuid.uuid4())
        self.current_election = Election(election_id, name, positions)
        
        self.view.display_message(f"Election '{name}' created successfully with positions: {', '.join(positions)}")
        self.view.press_enter_to_continue()

    # Add a candidate to the current election.
    def add_candidate(self):
        if not self.current_election:
            self.view.display_message("No active election. Please create an election first.", is_error=True)
            self.view.press_enter_to_continue()
            return
        
        self.view.display_header("ADD CANDIDATE")
        
        # Display available positions
        print("Available positions:")
        for i, position in enumerate(self.current_election.positions, 1):
            print(f"{i}. {position}")
        
        # Get position choice
        pos_choice = self.view.get_user_choice(
            "\nSelect position (number): ",
            len(self.current_election.positions)
        )
        position = self.current_election.positions[pos_choice - 1]
        
        # Get candidate details
        name = self.view.get_input("Enter candidate name: ")
        party = self.view.get_input("Enter party affiliation: ")
        age = int(self.view.get_input("Enter candidate age: "))
        
        # Create and add candidate
        candidate_id = str(uuid.uuid4())
        candidate = Candidate(candidate_id, name, party, age, position)
        self.current_election.add_candidate(candidate)
        
        self.view.display_message(f"Candidate '{name}' added successfully for {position} position.")
        self.view.press_enter_to_continue()

    # Register a new voter.
    def register_voter(self):
        if not self.current_election:
            self.view.display_message("No active election. Please create an election first.", is_error=True)
            self.view.press_enter_to_continue()
            return
        
        self.view.display_header("REGISTER VOTER")
        
        # Get voter details
        name = self.view.get_input("Enter voter name: ")
        age = int(self.view.get_input("Enter voter age: "))
        
        # Create and register voter
        voter_id = str(uuid.uuid4())
        voter = Voter(voter_id, name, age)
        self.current_election.register_voter(voter)
        
        self.view.display_message(f"Voter '{name}' registered successfully with ID: {voter_id}")
        self.view.press_enter_to_continue()

    # Conduct the voting process.
    def conduct_voting(self):
        if not self.current_election:
            self.view.display_message("No active election. Please create an election first.", is_error=True)
            self.view.press_enter_to_continue()
            return
        
        if not self.current_election.is_active:
            self.view.display_message("This election has been closed. No more voting allowed.", is_error=True)
            self.view.press_enter_to_continue()
            return
        
        self.view.display_header("VOTING PROCESS")
        
        # Get voter ID
        voter_id = self.view.get_input("Enter your voter ID: ")
        
        # Verify voter
        if voter_id not in self.current_election.voters:
            self.view.display_message("Voter not found. Please register first.", is_error=True)
            self.view.press_enter_to_continue()
            return
        
        voter = self.current_election.voters[voter_id]
        
        # Check eligibility
        if not voter.verify_eligibility():
            if voter.has_voted:
                self.view.display_message("You have already voted in this election.", is_error=True)
            elif voter.age < 18:
                self.view.display_message("You must be at least 18 years old to vote.", is_error=True)
            else:
                self.view.display_message("You are not eligible to vote.", is_error=True)
            self.view.press_enter_to_continue()
            return
        
        # Create ballot
        ballot = self.current_election.create_ballot(voter_id)
        
        # Voting for each position
        for position in self.current_election.positions:
            candidates = self.current_election.candidates[position]
            
            if not candidates:
                self.view.display_message(f"No candidates available for {position}. Skipping...", is_error=True)
                continue
            
            self.view.display_header(f"VOTE FOR {position.upper()}")
            self.view.display_candidates(candidates, position)
            
            # Get candidate choice
            choice = self.view.get_user_choice(
                f"Select candidate (1-{len(candidates)}): ",
                len(candidates)
            )
            selected_candidate = candidates[choice - 1]
            
            # Add vote to ballot
            ballot.add_vote(selected_candidate)
        
        # Cast ballot
        ballot.cast_ballot()
        self.current_election.ballots.append(ballot)
        voter.has_voted = True
        
        self.view.display_message("Thank you for voting! Your ballot has been cast.")
        self.view.press_enter_to_continue()

    # Close the current election and calculate results.
    def close_election(self):
        if not self.current_election:
            self.view.display_message("No active election to close.", is_error=True)
            self.view.press_enter_to_continue()
            return
        
        if not self.current_election.is_active:
            self.view.display_message("Election is already closed.", is_error=True)
            self.view.press_enter_to_continue()
            return
        
        # Confirm with user
        confirm = self.view.get_input("Are you sure you want to close the election? (yes/no): ").lower()
        if confirm != 'yes':
            self.view.display_message("Election remains open.")
            self.view.press_enter_to_continue()
            return
        
        # Close election and calculate results
        self.current_election.close_election()
        self.view.display_message("Election closed successfully. Results are now available.")
        self.view.press_enter_to_continue()

    # View election results.
    def view_results(self):
        if not self.current_election:
            self.view.display_message("No election data available.", is_error=True)
            self.view.press_enter_to_continue()
            return
        
        if not self.current_election.results:
            self.view.display_message("Results are not available yet. Please close the election first.", is_error=True)
            self.view.press_enter_to_continue()
            return
        
        self.view.display_header("ELECTION RESULTS")
        self.view.display_results(self.current_election.results)
        self.view.press_enter_to_continue()

    # View current election data.
    def view_election_data(self):
        if not self.current_election:
            self.view.display_message("No election data available.", is_error=True)
            self.view.press_enter_to_continue()
            return
        
        self.view.display_header("ELECTION DATA")
        
        # Display election status
        self.view.display_election_status(self.current_election)
        
        # Display candidates by position
        for position in self.current_election.positions:
            candidates = self.current_election.candidates[position]
            if candidates:
                self.view.display_candidates(candidates, position)
        
        # Display voters
        self.view.display_voters(list(self.current_election.voters.values()))
        
        self.view.press_enter_to_continue()

    def run(self):
        main_menu = [
            "Create New Election",
            "Add Candidate",
            "Register Voter",
            "Conduct Voting",
            "View Election Data",
            "Close Election & View Results"
        ]
        
        while True:
            self.view.display_menu(main_menu, "ELECTION SYSTEM")
            choice = self.view.get_user_choice("Enter your choice: ", len(main_menu))
            
            if choice == 1:
                self.create_election()
            elif choice == 2:
                self.add_candidate()
            elif choice == 3:
                self.register_voter()
            elif choice == 4:
                self.conduct_voting()
            elif choice == 5:
                self.view_election_data()
            elif choice == 6:
                self.close_election()
                self.view_results()
            elif choice == 0:
                self.view.display_message("Thank you for using the Election System. Goodbye!")
                break
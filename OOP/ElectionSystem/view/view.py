from typing import List, Dict
from model.model import Candidate, Voter, Election, Result
import textwrap
import os


# Handles all user interface interactions for the election system.
class ElectionView:
    # Clear the terminal screen
    @staticmethod
    def clear_screen():
        os.system('cls' if os.name == 'nt' else 'clear')

    # Display a formatted header
    @staticmethod
    def display_header(title: str):
        ElectionView.clear_screen()
        print("=".center(50, "="))
        print(f"{title:^50}")
        print("=".center(50, "="))
        print()

    # Display a menu with numbered options.
    @staticmethod
    def display_menu(options: List[str], title: str = "MAIN MENU"):
        """ 
        Args:
            options: List of menu option strings
            title: Title for the menu
        """
        ElectionView.display_header(title)
        for i, option in enumerate(options, 1):
            print(f"{i}. {option}")
        print("\n0. Exit")
        print("=".center(50, "="))

    # Get and validate user menu choice.
    @staticmethod
    def get_user_choice(prompt: str, max_option: int) -> int:
        """                
        Args:
            prompt: Input prompt to display
            max_option: Highest valid option number
            
        Returns:
            Validated user choice as integer
        """
        while True:
            try:
                choice = int(input(prompt))
                if 0 <= choice <= max_option:
                    return choice
                print(f"Please enter a number between 0 and {max_option}")
            except ValueError:
                print("Invalid input. Please enter a number.")

    # Get user input with optional validation for required fields.
    @staticmethod
    def get_input(prompt: str, required: bool = True) -> str:
        """   
        Args:
            prompt: Input prompt to display
            required: Whether the input is required
            
        Returns:
            User input string
        """
        while True:
            value = input(prompt).strip()
            if not required or value:
                return value
            print("This field is required. Please try again.")

    # Display a list of candidates.
    @staticmethod
    def display_candidates(candidates: List[Candidate], position: str = None):
        if position:
            print(f"\nCandidates for {position}:")
        else:
            print("\nAll Candidates:")
            
        print("-".center(50,"-"))
        print(f"{'ID':<5}{'Name':<20}{'Party':<15}{'Age':<5}{'Position':<15}")
        print("-".center(50,"-"))
        for candidate in candidates:
            print(f"{candidate.id:<5}{candidate.name:<20}{candidate.party:<15}"
                    f"{candidate.age:<5}{candidate.position:<15}")
        print("-".center(50,"-"))

    # Display a list of voters.
    @staticmethod
    def display_voters(voters: List[Voter]):
        print("\nRegistered Voters:")
        print("-".center(50,"-"))
        print(f"{'ID':<10}{'Name':<20}{'Age':<5}{'Voted?':<10}")
        print("-".center(50,"-"))
        for voter in voters:
            print(f"{voter.id:<10}{voter.name:<20}{voter.age:<5}{'Yes' if voter.has_voted else 'No':<10}")
        print("-".center(50,"-"))

    # Display current election status.
    @staticmethod
    def display_election_status(election: Election):
        status = "ACTIVE" if election.is_active else "CLOSED"
        print("\nElection Status:")
        print("-".center(50,"-"))
        print(f"Name: {election.name}")
        print(f"Status: {status}")
        print(f"Start Date: {election.start_date.strftime('%Y-%m-%d %H:%M:%S')}")
        if election.end_date:
            print(f"End Date: {election.end_date.strftime('%Y-%m-%d %H:%M:%S')}")
        print(f"Registered Voters: {len(election.voters)}")
        print(f"Votes Cast: {len(election.ballots)}")
        print(f"Voter Turnout: {election.get_voter_turnout():.2f}%")
        print("-".center(50,"-"))

    # Display election results.
    @staticmethod
    def display_results(results: Result):
        print("\nElection Results:")
        print("=".center(50,"="))
        print(f"Total Voters: {results.total_voters}")
        print(f"Total Votes Cast: {results.total_votes}")
        print(f"Voter Turnout: {(results.total_votes/results.total_voters)*100:.2f}%")
        print("=".center(50,"="))
        
        for position, candidates in results.results.items():
            print(f"\nResults for {position}:")
            print("-".center(50,"-"))
            print(f"{'Rank':<5}{'Name':<20}{'Party':<15}{'Votes':<10}{'% of Votes':<10}")
            print("-".center(50,"-"))
            
            for i, candidate in enumerate(candidates, 1):
                vote_percentage = results.get_percentage(candidate, position)
                print(f"{i:<5}{candidate.name:<20}{candidate.party:<15}"
                        f"{candidate.votes:<10}{vote_percentage:.1f}%")
            
            # Announce the winner
            winner = results.get_winner(position)
            print("\n" + "=" * 60)
            print(f"WINNER: {winner.name} ({winner.party}) with {winner.votes} votes "
                    f"({results.get_percentage(winner, position):.1f}%)")
            print("=".center(50,"="))

    # Display a message to the user.
    @staticmethod
    def display_message(message: str, is_error: bool = False):
        if is_error:
            print(f"\n[ERROR] {message}")
        else:
            print(f"\n[INFO] {message}")

    # Prompt user to press Enter to continue.
    @staticmethod
    def press_enter_to_continue():
        input("\nPress Enter to continue...")
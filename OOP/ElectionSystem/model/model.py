# Import necessary libraries
from dataclasses import dataclass
from typing import List, Dict
import random
import uuid
from datetime import datetime


# Represents a candidate in the election.
@dataclass
class Candidate:
    id: str
    name: str
    party: str
    age: int
    position: str
    votes: int = 0

    # Increment the vote count for this candidate.
    def receive_vote(self):
        self.votes += 1


# Represents a voter in the election system.
@dataclass
class Voter:
    id: str
    name: str
    age: int
    has_voted: bool = False
    is_registered: bool = True

    # Check if voter is eligible to vote.
    def verify_eligibility(self, min_voting_age: int = 18) -> bool:
        return self.age >= min_voting_age and self.is_registered and not self.has_voted


# Represents a ballot in the election system.
class Ballot:
    def __init__(self, ballot_id: str, election_id: str):
        self.ballot_id = ballot_id
        self.election_id = election_id
        self.candidates_voted: List[Candidate] = []
        self.is_cast = False

    # Add a candidate to the ballot.
    def add_vote(self, candidate: Candidate):
        if not self.is_cast:
            self.candidates_voted.append(candidate)
            candidate.receive_vote()

    # Mark the ballot as cast.
    def cast_ballot(self):
        self.is_cast = True


# Represents an election with candidates and voters.
class Election:
    def __init__(self, election_id: str, name: str, positions: List[str]):
        self.election_id = election_id
        self.name = name
        self.start_date = datetime.now()
        self.end_date = None
        self.is_active = True
        self.positions = positions
        self.candidates: Dict[str, List[Candidate]] = {position: [] for position in positions}
        self.voters: Dict[str, Voter] = {}
        self.ballots: List[Ballot] = []
        self.results = None

    # Add a candidate to the election for their position.
    def add_candidate(self, candidate: Candidate):
        if candidate.position in self.positions:
            self.candidates[candidate.position].append(candidate)
        else:
            raise ValueError(f"Invalid position: {candidate.position}")

    # Register a voter for the election.
    def register_voter(self, voter: Voter):
        if voter.id not in self.voters:
            self.voters[voter.id] = voter
        else:
            raise ValueError("Voter already registered")

    # Create a new ballot for a voter.
    def create_ballot(self, voter_id: str) -> Ballot:
        if voter_id not in self.voters:
            raise ValueError("Voter not registered")
        
        if self.voters[voter_id].has_voted:
            raise ValueError("Voter has already voted")
        
        ballot_id = str(uuid.uuid4())
        ballot = Ballot(ballot_id, self.election_id)
        return ballot

    # Close the election and calculate results.
    def close_election(self):
        self.is_active = False
        self.end_date = datetime.now()
        self.calculate_results()

    # Calculate and store election results.
    def calculate_results(self):
        results = {}
        for position in self.positions:
            candidates = self.candidates[position]
            candidates_sorted = sorted(candidates, key=lambda x: x.votes, reverse=True)
            results[position] = candidates_sorted
        
        self.results = Result(self.election_id, results, len(self.ballots), self.get_total_voters())

    # Get the total number of registered voters.
    def get_total_voters(self) -> int:
        return len(self.voters)

    # Calculate voter turnout percentage.
    def get_voter_turnout(self) -> float:
        if not self.voters:
            return 0.0
        return (len(self.ballots) / len(self.voters)) * 100


# Represents the results of an election.
class Result:
    def __init__(self, election_id: str, results: Dict[str, List[Candidate]], total_votes: int, total_voters: int):
        self.election_id = election_id
        self.results = results
        self.total_votes = total_votes
        self.total_voters = total_voters
        self.timestamp = datetime.now()

    # Get the winning candidate for a specific position.
    def get_winner(self, position: str) -> Candidate:
        return self.results[position][0]

    # Calculate the percentage of votes a candidate received.
    def get_percentage(self, candidate: Candidate, position: str) -> float:
        total_votes_for_position = sum(c.votes for c in self.results[position])
        if total_votes_for_position == 0:
            return 0.0
        return (candidate.votes / total_votes_for_position) * 100
# Import necessary libraries
import spacy
from collections import defaultdict
import re

# Load English language model for NLP
nlp = spacy.load("en_core_web_sm")

# A class to summarize basketball games by extracting key entities and statistics from game chronicles.
class BasketballGameSummarizer:

    # Define basketball-specific entity labels
    def __init__(self):
        self.player_label = "PLAYER"
        self.team_label = "TEAM"
        self.stat_label = "STAT"
        
        # Initialize patterns for entity recognition
        self._initialize_patterns()
        
    # Initialize patterns for rule-based entity recognition.
    def _initialize_patterns(self):
        # Add patterns to the pipeline
        ruler = nlp.add_pipe("entity_ruler", before="ner")
        
        patterns = [
            # Player names (typically capitalized words)
            {"label": self.player_label, "pattern": [{"TEXT": {"REGEX": "^[A-Z][a-z]+$"}}, 
                                                    {"TEXT": {"REGEX": "^[A-Z][a-z]+$"}}]},
            # Team names (often include city names or mascots)
            {"label": self.team_label, "pattern": [{"TEXT": {"REGEX": "^[A-Z][a-z]+$"}}, 
                                                    {"TEXT": {"REGEX": "^[A-Z][a-z]+$"}}]},
            # Statistics (numbers followed by terms like points, rebounds, etc.)
            {"label": self.stat_label, "pattern": [{"LIKE_NUM": True}, 
                                                    {"LOWER": {"IN": ["points", "rebounds", "assists", "blocks", "steals"]}}]}
        ]
        
        ruler.add_patterns(patterns)
    
    # Analyze the game text and extract key entities and statistics.
    def analyze_game_text(self, game_text):
        """    
        Args:
            game_text: The chronicle/text of the basketball game
            
        Returns:
            dict: A dictionary containing extracted entities and summary
        """
        doc = nlp(game_text)
        
        # Initialize data structures to store extracted information
        players = set()
        teams = set()
        stats = defaultdict(list)
        mvp_candidates = []
        top_scorers = []
        
        # Extract entities and their context
        for ent in doc.ents:
            if ent.label_ == self.player_label:
                players.add(ent.text)
            elif ent.label_ == self.team_label:
                teams.add(ent.text)
            elif ent.label_ == self.stat_label:
                # Extract player stats if mentioned near a player name
                for token in ent.sent:
                    if token.ent_type_ == self.player_label:
                        stats[token.text].append(ent.text)
        
        # Find MVP candidates (players with high stats)
        for player, player_stats in stats.items():
            points = 0
            for stat in player_stats:
                if "points" in stat:
                    points = max(points, int(stat.split()[0]))
            if points > 20:  # Consider players with >20 points as MVP candidates
                mvp_candidates.append((player, points))
        
        # Sort MVP candidates by points
        mvp_candidates.sort(key=lambda x: x[1], reverse=True)
        
        # Find top scorers
        top_scorers = mvp_candidates[:3] if len(mvp_candidates) > 3 else mvp_candidates
        
        # Try to determine winning team (heuristic: team mentioned with "win" or "defeat")
        winning_team = None
        for sent in doc.sents:
            if "win" in sent.text.lower() or "defeat" in sent.text.lower():
                for ent in sent.ents:
                    if ent.label_ == self.team_label:
                        winning_team = ent.text
                        break
        
        # Prepare summary
        summary = {
            "players": list(players),
            "teams": list(teams),
            "mvp_candidates": mvp_candidates,
            "top_scorers": top_scorers,
            "winning_team": winning_team,
            "player_stats": dict(stats)
        }
        
        return summary
    
    # Generate a human-readable summary from the analysis.
    def generate_summary_report(self, analysis):
        """    
        Args:
            analysis: The analysis dictionary from analyze_game_text
            
        Returns:
            str: A formatted summary string
        """
        report = []
        
        # Game overview
        report.append("BASKETBALL GAME SUMMARY BY DAVID CALEB")
        report.append(f"\nTeams: {' vs. '.join(analysis['teams'])}")
        
        # Winning team
        if analysis['winning_team']:
            report.append(f"\nWinning Team: {analysis['winning_team']}")
        else:
            report.append("\nWinning Team: Could not be determined from text")
        
        # MVP
        if analysis['mvp_candidates']:
            mvp, points = analysis['mvp_candidates'][0]
            report.append(f"\nMVP: {mvp} with {points} points")
        else:
            report.append("\nMVP: No clear MVP candidate identified")
        
        # Top scorers
        if analysis['top_scorers']:
            report.append("\nTop Scorers:")
            for i, (player, points) in enumerate(analysis['top_scorers'], 1):
                report.append(f"{i}. {player}: {points} points")
        
        # Player stats
        report.append("\nKey Statistics:")
        for player, stats in analysis['player_stats'].items():
            report.append(f"\n{player}:")
            for stat in stats:
                report.append(f"- {stat}")
        
        return "\n".join(report)


# Example usage
if __name__ == "__main__":
    # Sample game chronicle
    game_text = """
    In an exciting matchup between the Los Angeles Lakers and the Boston Celtics, 
    LeBron James led the Lakers to a 112-108 victory. James scored 32 points, 
    grabbed 10 rebounds, and dished out 8 assists, cementing his MVP performance. 
    Anthony Davis contributed with 28 points and 7 rebounds, while Jayson Tatum 
    led the Celtics with 30 points. The Lakers' defense stepped up in the fourth 
    quarter to secure the win against their historic rivals.
    """
    
    # Initialize summarizer
    summarizer = BasketballGameSummarizer()
    
    # Analyze the game text
    analysis = summarizer.analyze_game_text(game_text)
    
    # Generate and print the summary
    summary = summarizer.generate_summary_report(analysis)
    print(summary)
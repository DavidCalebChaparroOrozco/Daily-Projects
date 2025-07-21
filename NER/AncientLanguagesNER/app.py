# Import necessary libraries
import spacy
from collections import defaultdict
import re

# Load English language model for NLP
nlp = spacy.load("en_core_web_sm")

# A class to extract entities related to ancient texts such as gods, historical cities, and battles
class AncientTextEntityRecognizer:

    # Define custom entity labels
    def __init__(self):
        self.god_label = "GOD"
        self.city_label = "CITY"
        self.battle_label = "BATTLE"
        
        # Initialize the custom patterns for entity recognition
        self._initialize_patterns()
        
    # Initialize rule-based patterns for entity recognition
    def _initialize_patterns(self):
        # Add EntityRuler to the pipeline before the default NER
        ruler = nlp.add_pipe("entity_ruler", before="ner")
        
        # Define patterns for gods, historical cities, and famous battles
        patterns = [
            {"label": self.god_label, "pattern": [{"LOWER": "zeus"}]},
            {"label": self.god_label, "pattern": [{"LOWER": "apollo"}]},
            {"label": self.god_label, "pattern": [{"LOWER": "athena"}]},
            {"label": self.city_label, "pattern": [{"LOWER": "athens"}]},
            {"label": self.city_label, "pattern": [{"LOWER": "sparta"}]},
            {"label": self.city_label, "pattern": [{"LOWER": "rome"}]},
            {"label": self.battle_label, "pattern": [{"LOWER": "thermopylae"}]},
            {"label": self.battle_label, "pattern": [{"LOWER": "marathon"}]},
            {"label": self.battle_label, "pattern": [{"LOWER": "salamis"}]}
        ]
        
        # Add all patterns to the ruler
        ruler.add_patterns(patterns)
    
    # Analyze ancient text and extract entities
    def analyze_ancient_text(self, text):
        """
        Args:
            text: The ancient text or historical narrative as input
            
        Returns:
            dict: A dictionary containing lists of recognized gods, cities, and battles
        """
        doc = nlp(text)
        
        # Initialize data structures to store the entities
        gods = set()
        cities = set()
        battles = set()
        
        # Extract entities based on their labels
        for ent in doc.ents:
            if ent.label_ == self.god_label:
                gods.add(ent.text.capitalize())
            elif ent.label_ == self.city_label:
                cities.add(ent.text.capitalize())
            elif ent.label_ == self.battle_label:
                battles.add(ent.text.capitalize())
        
        # Return the extracted entities
        return {
            "gods": list(gods),
            "cities": list(cities),
            "battles": list(battles)
        }
    
    # Generate a human-readable summary of the findings
    def generate_summary_report(self, analysis):
        """
        Args:
            analysis: Dictionary returned by analyze_ancient_text
            
        Returns:
            str: A formatted string summarizing the extracted entities
        """
        report = []
        
        report.append("ANCIENT TEXT ENTITY RECOGNITION REPORT BY DAVID CALEB\n")
        
        # List gods mentioned
        if analysis['gods']:
            report.append("Gods Mentioned:")
            for god in analysis['gods']:
                report.append(f"- {god}")
        else:
            report.append("Gods Mentioned: None found")
        
        # List historical cities mentioned
        if analysis['cities']:
            report.append("\nHistorical Cities Mentioned:")
            for city in analysis['cities']:
                report.append(f"- {city}")
        else:
            report.append("\nHistorical Cities Mentioned: None found")
        
        # List battles mentioned
        if analysis['battles']:
            report.append("\nBattles Mentioned:")
            for battle in analysis['battles']:
                report.append(f"- {battle}")
        else:
            report.append("\nBattles Mentioned: None found")
        
        return "\n".join(report)


# Example usage
if __name__ == "__main__":
    # Sample ancient text
    ancient_text = """
    During the great Battle of Thermopylae, the Spartans led by King Leonidas faced the massive Persian army. 
    The gods watched closely, with Zeus favoring the Greeks while Apollo admired the bravery of the Spartans.
    The city of Athens prepared for the inevitable confrontation at the Battle of Salamis, where the tides of war changed.
    In Rome, tales of the Marathon run inspired warriors for generations.
    """
    
    # Initialize the entity recognizer
    recognizer = AncientTextEntityRecognizer()
    
    # Analyze the sample ancient text
    analysis = recognizer.analyze_ancient_text(ancient_text)
    
    # Generate and print the summary
    summary = recognizer.generate_summary_report(analysis)
    print(summary)

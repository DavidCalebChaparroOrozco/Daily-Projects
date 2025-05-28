# Import necessary libraries
import json
import spacy
import webbrowser
from spacy.pipeline import EntityRuler
from spacy.lang.en import English
from spacy.tokens import Span
from spacy import displacy
# Initialize the FairyTale NER system with custom patterns and rules.
class FairyTaleNER:
    def __init__(self):
        # Load English language model from spaCy
        self.nlp = spacy.load("en_core_web_sm")
        
        # Create custom entity ruler for fairy tale specific entities
        ruler = self.nlp.add_pipe("entity_ruler", before="ner")
        
        # Define patterns for fairy tale entities
        patterns = self._get_patterns()
        ruler.add_patterns(patterns)
        
        # Register custom entity labels
        self._register_entity_labels()
    
    # Define custom patterns for fairy tale entities.
    def _get_patterns(self):
        """
        Returns:
            list: List of pattern dictionaries for EntityRuler
        """
        patterns = [
            {"label": "CHARACTER", "pattern": [{"LOWER": "gilgamesh"}]},
            {"label": "CHARACTER", "pattern": [{"LOWER": "enkidu"}]},
            {"label": "CHARACTER", "pattern": [{"LOWER": "utnapishtim"}]},
            {"label": "MAGICAL_CREATURE", "pattern": [{"LOWER": "humbaba"}]},
            {"label": "MAGICAL_CREATURE", "pattern": [{"LOWER": "bull"}, {"LOWER": "of"}, {"LOWER": "heaven"}]},
            {"label": "CHARACTER", "pattern": [{"LOWER": "king"}, {"LOWER": "arthur"}]},
            {"label": "CHARACTER", "pattern": [{"LOWER": "uther"}, {"LOWER": "pendragon"}]},
            {"label": "CHARACTER", "pattern": [{"LOWER": "guinevere"}]},
            {"label": "MAGICAL_OBJECT", "pattern": [{"LOWER": "excalibur"}]},
            {"label": "KINGDOM", "pattern": [{"LOWER": "camelot"}]},
            {"label": "CHARACTER", "pattern": [{"LOWER": "Baba"}, {"LOWER": "Yaga"}]},
            {"label": "MAGICAL_OBJECT", "pattern": [{"LOWER": "hut"}, {"LOWER": "on"}, {"LOWER": "chicken"}, {"LOWER": "legs"}]},
            {"label": "CHARACTER", "pattern": [{"LOWER": "snow"}, {"LOWER": "white"}]},
            {"label": "CHARACTER", "pattern": [{"LOWER": "cinderella"}]},
            {"label": "CHARACTER", "pattern": [{"LOWER": "prince"}, {"LOWER": "charming"}]},
            {"label": "MAGICAL_OBJECT", "pattern": [{"LOWER": "magic"}, {"LOWER": "mirror"}]},
            {"label": "SPELL", "pattern": [{"LOWER": "bippity"}, {"LOWER": "boppity"}, {"LOWER": "boo"}]},
            {"label": "MAGICAL_CREATURE", "pattern": [{"LOWER": "dragon"}]},
            {"label": "MAGICAL_OBJECT", "pattern": [{"LOWER": "golden"}, {"LOWER": "shoe"}]},
        ]
        return patterns
    
    # Register custom entity labels and set colors for visualization.
    def _register_entity_labels(self):
        # Define custom colors for entities
        colors = {
            # Light Salmon
            "CHARACTER": "#FFA07A",  
            # Pale Green
            "MAGICAL_CREATURE": "#98FB98",  
            # Light Blue
            "KINGDOM": "#ADD8E6",  
            # Gold
            "SPELL": "#FFD700",  
            # Violet
            "MAGICAL_OBJECT": "#EE82EE",  
        }
        
        # Add entity labels to the pipeline
        for label in colors.keys():
            if label not in self.nlp.vocab.strings:
                self.nlp.vocab.strings.add(label)
        
        # Set colors for displaCy visualization
        Span.set_extension("color", default=None, force=True)
        for label, color in colors.items():
            Span.set_extension(f"{label}_color", default=color, force=True)
    
    # Analyze text and extract fairy tale entities.
    def analyze_text(self, text):
        """    
        Args:
            text: Input text to analyze
        Returns:
            doc: spaCy Doc object with entities
        """
        return self.nlp(text)
        
    # Generate HTML visualization of entities and metadata.
    def visualize_entities_in_browser(self, doc, analysis_results=None):
        # Render NER entities in HTML format using spaCy's displaCy
        html = displacy.render(doc, style="ent", page=True, options={
            "colors": {
                "CHARACTER": "#FFA07A",
                "MAGICAL_CREATURE": "#98FB98",
                "KINGDOM": "#ADD8E6",
                "SPELL": "#FFD700",
                "MAGICAL_OBJECT": "#EE82EE",
            }
        })

        # Current doc entities in JSON format
        entities_data = [
            {
                "text": ent.text,
                "label": ent.label_,
                "start": ent.start_char,
                "end": ent.end_char,
            }
            for ent in doc.ents
        ]
        json_output = json.dumps(entities_data, indent=4, ensure_ascii=False)
        # Global analysis JSON
        full_analysis_json = json.dumps(analysis_results, indent=4, ensure_ascii=False) if analysis_results else ""
        
        # Load example.json as redable text
        try:
            with open("example.json", "r", encoding="utf-8") as file:
                example_data = json.load(file)
            # Color mapping
            label_colors = {
                "CHARACTER": "#FFA07A",
                "MAGICAL_CREATURE": "#98FB98",
                "KINGDOM": "#ADD8E6",
                "SPELL": "#FFD700",
                "MAGICAL_OBJECT": "#EE82EE"
            }
                # example_json_str = json.dumps(example_data, indent=4, ensure_ascii=False)
            annoted_selection = ""
            for key, value in example_data.items():
                if key.startswith('metadata'):
                    continue
                doc_example = self.nlp(value)
                # Annotate text by replacing entities with "text (label)"
                annotated_text = value
                offset = 0
                # Reverse to not mess up offsets
                for ent in doc_example.ents:
                    color = label_colors.get(ent.label_, "#ccc")
                    replacement = (
                        f'<span class="ent" style="background:{color}; padding:2px; border-radius:4px;">'
                        f'{ent.text} <span class="label">{ent.label_}</span></span>'
                    )
                    start = ent.start_char + offset
                    end = ent.end_char + offset
                    annotated_text = (
                        annotated_text[:start] + replacement + annotated_text[end:]
                    )
                    offset += len(replacement) - (end - start)
                annoted_selection+= f"<h3>{key}</h3><p>{annotated_text}</p>"
        except FileNotFoundError:
            example_json_str = "example.json file not found."

        full_html = f"""
        <html>
        <head>
            <title>Fairy Tale Entities by David Caleb</title>
            <style>
                body {{
                    font-family: Arial, sans-serif;
                    margin: 20px;
                }}
                pre {{
                    background-color: #f4f4f4;
                    padding: 10px;
                    border: 1px solid #ccc;
                    white-space: pre-wrap;
                    word-wrap: break-word;
                }}
                h2 {{
                    color: #333;
                }}
                .ent {{
                    display: inline-block;
                    line-height: 1.5;
                    padding: 0 0.25em;
                    margin: 0 0.25em;
                    border-radius: 0.25em;
                    color: black;
                }}
                .label {{
                    font-size: 0.75em;
                    font-weight: bold;
                    color: white;
                    background: rgba(0, 0, 0, 0.6);
                    padding: 0.1em 0.4em;
                    margin-left: 0.5em;
                    border-radius: 0.25em;
                }}
            </style>
        </head>
        <body>
        {html}
            <h2>Current Document Entities (JSON)</h2>
            <pre>{json_output}</pre>

            <h2>Global Analysis Results (JSON)</h2>
            <pre>{full_analysis_json}</pre>

            <h2>Original Text and Metadata (example.json)</h2>
            <pre>{annotated_text}</pre>
            <p>Generated by David Caleb</p>
        </body>
        </html>
        """

        with open("entities.html", "w", encoding="utf-8") as file:
            file.write(full_html)

        
        webbrowser.open("entities.html")


    # Generate a report of found entities.
    def get_entity_report(self, doc):
        """    
        Args:
            doc: spaCy Doc object with entities 
        Returns:
            dict: Dictionary with entity types and their counts
        """
        entity_counts = {
            "CHARACTER": 0,
            "MAGICAL_CREATURE": 0,
            "KINGDOM": 0,
            "SPELL": 0,
            "MAGICAL_OBJECT": 0,
        }
        
        for ent in doc.ents:
            if ent.label_ in entity_counts:
                entity_counts[ent.label_] += 1
        
        return entity_counts

    # Analyze a JSON file containing fairy tale texts.
    def analyze_json_file(self, file_path):
        """    
        Args:
            file_path: Path to the JSON file
            
        Returns:
            dict: Dictionary with analysis results for each text
        """
        with open(file_path, 'r', encoding='utf-8') as f:
            data = json.load(f)
        
        results = {}
        
        for key, text in data.items():
            if key.startswith('metadata'):
                continue  # Skip metadata entries
            doc = self.analyze_text(text)
            results[key] = {
                'entities': [(ent.text, ent.label_) for ent in doc.ents],
                'report': self.get_entity_report(doc)
            }
        
        return results

# Example usage
if __name__ == "__main__":
    # Initialize the NER system
    fairy_tale_ner = FairyTaleNER()
    
    # Sample fairy tale text
    sample_text = """
    Once upon a time, Snow White lived in the Enchanted Forest with seven dwarfs. 
    The evil queen had a Magic Mirror that told her Snow White was the fairest of them all. 
    A Fairy Godmother helped Cinderella go to the ball by saying 'Bippity Boppity Boo'. 
    Prince Charming later found her golden shoe. Meanwhile, a dragon guarded a golden egg in Camelot.
    """
    
    # Analyze the text
    doc = fairy_tale_ner.analyze_text(sample_text)
    
    # Print the entities found
    print("\nEntities Found:")
    for ent in doc.ents:
        print(f"{ent.text} ({ent.label_})")
    
    # Get entity report
    report = fairy_tale_ner.get_entity_report(doc)
    print("\nEntity Report:")
    for entity_type, count in report.items():
        print(f"{entity_type}: {count}")
    
    # Visualize entities in browser
    fairy_tale_ner.visualize_entities_in_browser(doc, analysis_results=report)
    
    # Analyze the JSON file
    json_results = fairy_tale_ner.analyze_json_file("example.json")
    print("\nJSON Analysis Results:")
    for tale, result in json_results.items():
        print(f"\n{tale}:")
        print("Entities:", result['entities'])
        print("Report:", result['report'])

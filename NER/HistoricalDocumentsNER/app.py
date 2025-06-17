# Import necessary libraries
import spacy
import re
import matplotlib.pyplot as plt
from collections import defaultdict

# Load English NER model from spaCy
nlp = spacy.load("en_core_web_sm")

class HistoricalDocumentsNER:
    """
    # A Named Entity Recognition system for processing historical documents to extract:
    - Historical figures
    - Events
    - Dates
    - Locations
    
    Includes visualization capabilities for chronological events.
    """
    
    def __init__(self):
        # Example dataset: Famous speeches and historical documents
        self.documents = [
            {
                "title": "Gettysburg Address",
                "text": """Four score and seven years ago our fathers brought forth on this continent, a new nation, 
                conceived in Liberty, and dedicated to the proposition that all men are created equal. 
                Now we are engaged in a great civil war, testing whether that nation, or any nation so conceived 
                and so dedicated, can long endure. We are met on a great battlefield of that war.""",
                "source": "Abraham Lincoln",
                "year": 1863
            },
            {
                "title": "Declaration of Independence",
                "text": """In Congress, July 4, 1776. The unanimous Declaration of the thirteen united States of America, 
                When in the Course of human events, it becomes necessary for one people to dissolve the political bands 
                which have connected them with another...""",
                "source": "Continental Congress",
                "year": 1776
            },
            {
                "title": "I Have a Dream",
                "text": """I have a dream that one day this nation will rise up and live out the true meaning of its creed: 
                We hold these truths to be self-evident, that all men are created equal. 
                Martin Luther King Jr. delivered this speech on August 28, 1963, during the March on Washington.""",
                "source": "Martin Luther King Jr.",
                "year": 1963
            },
            {
                "title": "The Council of Elrond Speech",
                "text": """I will take the Ring, though I do not know the way. I know not the strength of my body, nor the wisdom of my mind, but I will bear this burden if such is my fate. 
                The Road must be trod, but it will be neither short nor easy. We cannot escape our doom by hiding or delaying, and the shadows of Mordor will fall upon all lands if we fail.""",
                "source": "Frodo Baggins",
                "year": 3018
            }
        ]
        
        # Store NER results
        self.ner_results = []
        
    # Extract named entities from historical documents using spaCy NER.
    # Identifies persons, places, dates, and events.
    def extract_entities(self):
        results = []
        
        for doc_data in self.documents:
            title = doc_data["title"]
            text = doc_data["text"]
            doc = nlp(text)
            
            # Initialize sets to store unique entities
            entities = {
                "PERSON": set(),
                # Geo-political entities (countries, cities, states)
                "GPE": set(),  
                # Non-GPE locations
                "LOC": set(),   
                "DATE": set(),
                "EVENT": set()
            }
            
            # Extract entities using spaCy
            for ent in doc.ents:
                if ent.label_ in entities:
                    entities[ent.label_].add(ent.text)
            
            # Additional date extraction using regex to catch numeric years
            year_matches = re.findall(r'\b\d{4}\b', text)
            for year in year_matches:
                entities["DATE"].add(year)
            
            # Store results for this document
            results.append({
                "title": title,
                "source": doc_data.get("source", ""),
                "year": doc_data.get("year", None),
                "persons": list(entities["PERSON"]),
                "places": list(entities["GPE"].union(entities["LOC"])),
                "dates": list(entities["DATE"]),
                "events": list(entities["EVENT"])
            })
        
        self.ner_results = results
        return results
    
    def print_entity_report(self):
        if not self.ner_results:
            self.extract_entities()
            
        print("\nHistorical Documents NER Report")
        print("=".center(50, "="))
        
        for result in self.ner_results:
            print(f"\nDocument: {result['title']}")
            print(f"Source: {result.get('source', 'Unknown')}")
            print(f"Persons: {', '.join(result['persons']) if result['persons'] else 'None found'}")
            print(f"Places: {', '.join(result['places']) if result['places'] else 'None found'}")
            print(f"Dates: {', '.join(result['dates']) if result['dates'] else 'None found'}")
            print(f"Events: {', '.join(result['events']) if result['events'] else 'None found'}")
    
    # Visualize documents and their entities on a chronological timeline.
    # Shows documents by year with extracted entities.
    def plot_timeline(self):
        if not self.ner_results:
            self.extract_entities()
            
        # Prepare timeline data
        timeline_data = []
        entity_data = defaultdict(list)
        
        for doc in self.ner_results:
            # Use document year if available, otherwise try to extract from dates
            if doc.get('year'):
                year = doc['year']
            elif doc['dates']:
                # Find first 4-digit year in dates
                for date in doc['dates']:
                    year_match = re.search(r'\d{4}', date)
                    if year_match:
                        year = int(year_match.group())
                        break
                else:
                    # Skip if no valid year found
                    continue  
            else:
                # Skip if no year information
                continue  
            
            timeline_data.append((year, doc['title']))
            
            # Collect entities for this document
            entity_data[year].extend([
                *doc['persons'],
                *doc['places'],
                *doc['events']
            ])
        
        # Sort by year
        timeline_data.sort()
        
        # Extract data for plotting
        years = [data[0] for data in timeline_data]
        titles = [data[1] for data in timeline_data]
        
        # Create figure
        plt.figure(figsize=(12, 8))
        
        # Plot timeline points
        plt.scatter(years, [1] * len(years), c='red', s=100, alpha=0.7)
        
        # Add document titles and entities
        for i, (year, title) in enumerate(timeline_data):
            # Position document title above the point
            plt.text(
                year, 1.05, 
                f"{title} ({year})", 
                rotation=45, 
                ha='right', 
                fontsize=10,
                bbox=dict(facecolor='white', alpha=0.8, edgecolor='none')
            )
            
            # List entities below the point
            entities = "\n".join(entity_data[year])
            if entities:
                plt.text(
                    year, 0.93, 
                    entities, 
                    fontsize=8,
                    ha='center',
                    va='top',
                    bbox=dict(facecolor='lightgray', alpha=0.5, boxstyle='round')
                )
        
        # Format the plot
        plt.yticks([])
        plt.xlabel("Year", fontsize=12)
        plt.title("Chronological Timeline of Historical Documents with Extracted Entities", pad=20)
        plt.grid(axis='x', linestyle='--', alpha=0.7)
        
        # Adjust layout to prevent overlap
        plt.tight_layout()
        plt.show()
    
    # Add a new historical document to the collection
    def add_document(self, title, text, source=None, year=None):
        self.documents.append({
            "title": title,
            "text": text,
            "source": source,
            "year": year
        })
        
        # Clear previous NER results since we've added new data
        self.ner_results = []
    
    # Export the NER results to a text file.
    def export_results(self, filename="historical_ner_results.txt"):
        if not self.ner_results:
            self.extract_entities()
            
        with open(filename, 'w', encoding='utf-8') as file:
            file.write("Historical Documents NER Analysis\n")
            file.write("=" * 50 + "\n\n")
            
            for result in self.ner_results:
                file.write(f"Document: {result['title']}\n")
                file.write(f"Source: {result.get('source', 'Unknown')}\n")
                file.write(f"Persons: {', '.join(result['persons']) if result['persons'] else 'None found'}\n")
                file.write(f"Places: {', '.join(result['places']) if result['places'] else 'None found'}\n")
                file.write(f"Dates: {', '.join(result['dates']) if result['dates'] else 'None found'}\n")
                file.write(f"Events: {', '.join(result['events']) if result['events'] else 'None found'}\n\n")
        
        print(f"Results exported to {filename}")

# Main execution
if __name__ == "__main__":
    # Initialize the NER processor
    processor = HistoricalDocumentsNER()
    
    # Extract entities from documents
    processor.extract_entities()
    
    # Print the entity report
    processor.print_entity_report()
    
    # Generate the timeline visualization
    processor.plot_timeline()
    
    # Export results to file
    processor.export_results()
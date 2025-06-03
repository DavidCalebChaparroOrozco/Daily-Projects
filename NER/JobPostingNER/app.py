# Import necessary libraries
import re
import spacy
from spacy import displacy
import pandas as pd
import matplotlib.pyplot as plt
from datetime import datetime
import json
import os
from collections import defaultdict

# Load English language model for spaCy
try:
    nlp = spacy.load("en_core_web_lg")
except OSError:
    print("Downloading language model for spaCy... (this may take a few minutes)")
    from spacy.cli import download
    download("en_core_web_lg")
    nlp = spacy.load("en_core_web_lg")

# Custom patterns for entity recognition
patterns = [
    # Salary patterns
    {"label": "SALARY", "pattern": [{"LIKE_NUM": True}, {"LOWER": {"IN": ["k", "k/year", "k/yr"]}}]},
    {"label": "SALARY", "pattern": [{"TEXT": {"REGEX": "\\$\\d{1,3}(?:,\\d{3})*(?:\\.\\d{2})?"}}]},
    {"label": "SALARY", "pattern": [{"TEXT": {"REGEX": "\\d{1,3}(?:,\\d{3})*\\s*(?:USD|usd|\\$)"}}]},
    
    # Technology patterns
    {"label": "TECHNOLOGY", "pattern": [{"LOWER": {"IN": ["python", "java", "javascript"]}}]},
    {"label": "TECHNOLOGY", "pattern": [{"LOWER": {"REGEX": "^react|^angular|^vue"}}]},
    
    # Job role patterns
    {"label": "ROLE", "pattern": [{"LOWER": "developer"}]},
    {"label": "ROLE", "pattern": [{"LOWER": "engineer"}]},
    {"label": "ROLE", "pattern": [{"LOWER": "analyst"}]},
    
    # Benefit patterns
    {"label": "BENEFIT", "pattern": [{"LOWER": "health"}, {"LOWER": "insurance"}]},
    {"label": "BENEFIT", "pattern": [{"LOWER": "remote"}, {"LOWER": "work"}]},
]

# Add patterns to the pipeline
ruler = nlp.add_pipe("entity_ruler", before="ner")
ruler.add_patterns(patterns)

# Main class for analyzing job postings and extracting key entities.
class JobPostingAnalyzer:    
    def __init__(self):
        self.job_postings = []
        self.analysis_results = []
        self.custom_patterns = patterns.copy()
        
    # Analyze a job posting text and extract entities.
    # Now optimized for structured job postings with fields like Job Title, Company, etc.
    def analyze_text(self, text):
        doc = nlp(text)
        
        entities = {
            "roles": [],
            "technologies": [],
            "salaries": [],
            "locations": [],
            "requirements": [],
            "benefits": []
        }
        
        # Extract Job Title as primary role
        title_match = re.search(r"Job Title:\s*(.+)", text)
        if title_match:
            entities["roles"].append(title_match.group(1))
        
        # Extract Location
        loc_match = re.search(r"Location:\s*(.+)", text)
        if loc_match:
            entities["locations"].append(loc_match.group(1))
        
        # Extract Job Types as technologies/roles
        types_match = re.search(r"Job Types:\s*(.+)", text)
        if types_match:
            types = types_match.group(1).split(", ")
            entities["technologies"].extend(types)
        
        # Additional spaCy entity extraction
        for ent in doc.ents:
            if ent.label_ == "ROLE" and ent.text not in entities["roles"]:
                entities["roles"].append(ent.text)
            elif ent.label_ == "TECHNOLOGY" and ent.text not in entities["technologies"]:
                entities["technologies"].append(ent.text)
            elif ent.label_ == "SALARY":
                entities["salaries"].append(ent.text)
            elif ent.label_ == "GPE" or ent.label_ == "LOC":
                if ent.text not in entities["locations"]:
                    entities["locations"].append(ent.text)
            elif ent.label_ == "BENEFIT":
                entities["benefits"].append(ent.text)
        
        # Additional processing for requirements
        requirement_keywords = ["require", "must have", "should have", "qualification"]
        sentences = [sent.text for sent in doc.sents if any(keyword in sent.text.lower() for keyword in requirement_keywords)]
        entities["requirements"] = sentences
        
        return entities
    
    # Analyze multiple job postings at once.
    def batch_analyze(self, texts):
        """    
        Args:
            texts: List of job posting texts
        Returns:
            list: List of analysis results
        """
        results = []
        for text in texts:
            results.append(self.analyze_text(text))
        return results
    
    # Generate a visualization of entities in the text.
    def visualize_entities(self, text):
        """
        Args:
            text: Job posting text to visualize
        """
        doc = nlp(text)
        displacy.render(doc, style="ent", jupyter=False)
    
    # Export analysis results to a file.
    def export_results(self, results, format="json"):
        """
        Args:
            results: Analysis results to export
            format: Export format (json, csv, excel)
        """
        timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
        
        if format == "json":
            filename = f"job_analysis_{timestamp}.json"
            with open(filename, "w") as f:
                json.dump(results, f, indent=2)
            print(f"Results exported to {filename}")
        
        elif format == "csv":
            # Flatten results for CSV export
            flat_results = []
            for result in results:
                flat_result = {
                    "roles": "; ".join(result["roles"]),
                    "technologies": "; ".join(result["technologies"]),
                    "salaries": "; ".join(result["salaries"]),
                    "locations": "; ".join(result["locations"]),
                    "requirements": "; ".join(" | ".join(result["requirements"])),
                    "benefits": "; ".join(result["benefits"])
                }
                flat_results.append(flat_result)
            
            df = pd.DataFrame(flat_results)
            filename = f"job_analysis_{timestamp}.csv"
            df.to_csv(filename, index=False)
            print(f"Results exported to {filename}")
        
        elif format == "excel":
            # Similar flattening for Excel
            flat_results = []
            for result in results:
                flat_result = {
                    "roles": "; ".join(result["roles"]),
                    "technologies": "; ".join(result["technologies"]),
                    "salaries": "; ".join(result["salaries"]),
                    "locations": "; ".join(result["locations"]),
                    "requirements": "; ".join(" | ".join(result["requirements"])),
                    "benefits": "; ".join(result["benefits"])
                }
                flat_results.append(flat_result)
            
            df = pd.DataFrame(flat_results)
            filename = f"job_analysis_{timestamp}.xlsx"
            df.to_excel(filename, index=False)
            print(f"Results exported to {filename}")
    
    # Generate a summary report of the analysis.
    def generate_report(self, results):
        """
        Args:
            results: List of analysis results
        """
        if not results:
            print("No results to generate report from.")
            return
        
        # Aggregate data across all job postings
        aggregated = {
            "roles": defaultdict(int),
            "technologies": defaultdict(int),
            "salaries": [],
            "locations": defaultdict(int),
            "benefits": defaultdict(int)
        }
        
        for result in results:
            for role in result["roles"]:
                aggregated["roles"][role] += 1
            
            for tech in result["technologies"]:
                aggregated["technologies"][tech] += 1
            
            for salary in result["salaries"]:
                aggregated["salaries"].append(salary)
            
            for loc in result["locations"]:
                aggregated["locations"][loc] += 1
            
            for benefit in result["benefits"]:
                aggregated["benefits"][benefit] += 1
        
        # Generate report
        print("\n JOB MARKET ANALYSIS REPORT ")
        print(f"Analyzed {len(results)} job postings\n")
        
        # Roles section
        print("\nTop Job Roles:")
        sorted_roles = sorted(aggregated["roles"].items(), key=lambda x: x[1], reverse=True)[:5]
        for role, count in sorted_roles:
            print(f"- {role}: {count} postings")
        
        # Technologies section
        print("\nTop Technologies:")
        sorted_tech = sorted(aggregated["technologies"].items(), key=lambda x: x[1], reverse=True)[:5]
        for tech, count in sorted_tech:
            print(f"- {tech}: {count} postings")
        
        # Salaries section (if any)
        if aggregated["salaries"]:
            print("\nSalary Information:")
            print(f"- Found {len(aggregated['salaries'])} salary mentions")
            print(f"- Sample salaries: {', '.join(aggregated['salaries'][:3])}...")
        
        # Locations section
        print("\nTop Locations:")
        sorted_locs = sorted(aggregated["locations"].items(), key=lambda x: x[1], reverse=True)[:5]
        for loc, count in sorted_locs:
            print(f"- {loc}: {count} postings")
        
        # Benefits section
        print("\nMost Common Benefits:")
        sorted_benefits = sorted(aggregated["benefits"].items(), key=lambda x: x[1], reverse=True)[:5]
        for benefit, count in sorted_benefits:
            print(f"- {benefit}: {count} postings")
        
        # Generate visualizations
        self._generate_visualizations(aggregated)
    
    # Helper method to generate visualizations from aggregated data.
    def _generate_visualizations(self, data):
        """
        Args:
            data: Aggregated analysis data
        """
        # Create visualizations directory if it doesn't exist
        os.makedirs("visualizations", exist_ok=True)
        timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
        
        # Plot top roles
        if data["roles"]:
            top_roles = sorted(data["roles"].items(), key=lambda x: x[1], reverse=True)[:10]
            roles, counts = zip(*top_roles)
            plt.figure(figsize=(10, 6))
            plt.barh(roles, counts)
            plt.title("Top Job Roles")
            plt.xlabel("Number of Postings")
            plt.tight_layout()
            plt.savefig(f"visualizations/roles_{timestamp}.png")
            plt.close()
        
        # Plot top technologies
        if data["technologies"]:
            top_tech = sorted(data["technologies"].items(), key=lambda x: x[1], reverse=True)[:10]
            tech, counts = zip(*top_tech)
            plt.figure(figsize=(10, 6))
            plt.barh(tech, counts)
            plt.title("Top Technologies")
            plt.xlabel("Number of Postings")
            plt.tight_layout()
            plt.savefig(f"visualizations/technologies_{timestamp}.png")
            plt.close()
        
        print("\nVisualizations saved in the 'visualizations' directory.")

def display_menu():
    print("\n JobPostingNER - Job Market Analysis Tool ")
    print("1. Analyze a single job posting")
    print("2. Analyze multiple job postings from a file")
    print("3. View/Add custom entity patterns")
    print("4. Generate market report from previous analyses")
    print("5. Export previous analysis results")
    print("6. Visualize entities in a job posting")
    print("7. Settings")
    print("8. Exit")
    
    choice = input("\nEnter your choice (1-8): ")
    return choice

# Handle single job posting analysis.
def single_job_analysis(analyzer):
    """  
    Args:
        analyzer: The analyzer instance
    """
    print("\n Single Job Posting Analysis ")
    print("Enter/Paste your job posting text (press Enter on an empty line to finish):")
    
    lines = []
    while True:
        line = input()
        if line:
            lines.append(line)
        else:
            break
    
    text = "\n".join(lines)
    if not text.strip():
        print("No text provided. Returning to main menu.")
        return
    
    result = analyzer.analyze_text(text)
    analyzer.analysis_results.append(result)  # Save for later reporting
    
    print("\n Analysis Results ")
    print(f"Roles: {', '.join(result['roles']) if result['roles'] else 'None found'}")
    print(f"Technologies: {', '.join(result['technologies']) if result['technologies'] else 'None found'}")
    print(f"Salaries: {', '.join(result['salaries']) if result['salaries'] else 'None found'}")
    print(f"Locations: {', '.join(result['locations']) if result['locations'] else 'None found'}")
    print("\nRequirements:")
    for i, req in enumerate(result["requirements"], 1):
        print(f"{i}. {req}")
    print("\nBenefits:")
    print(", ".join(result["benefits"]) if result["benefits"] else "None found")

# Handle batch analysis from a file with support for multiple formats.
# Now specifically handles the provided dataset structure.
def file_batch_analysis(analyzer):
    """
    Args:
        analyzer: The analyzer instance
    """
    print("\n Batch Job Posting Analysis ")
    print("Supported file formats:")
    print("- CSV file (.csv) - with columns: Job Title, Company, Location, Posted Date, Job Types")
    print("- JSON file (.json) - array of job postings with similar structure")
    print("- Text file (.txt) - one job posting per line (simple format)")
    
    filepath = input("\nEnter file path: ").strip()
    
    if not os.path.exists(filepath):
        print("File not found. Please check the path.")
        return
    
    try:
        if filepath.endswith('.json'):
            with open(filepath, 'r') as f:
                data = json.load(f)
            
            if isinstance(data, list):
                # Process JSON array with expected structure
                texts = []
                for job in data:
                    # Construct a text blob from available fields
                    text_parts = [
                        f"Job Title: {job.get('Job Title', '')}",
                        f"Company: {job.get('Company', '')}",
                        f"Location: {job.get('Location', '')}",
                        f"Job Types: {job.get('Job Types', '')}",
                        f"Posted Date: {job.get('Posted Date', '')}"
                    ]
                    texts.append("\n".join(text_parts))
            else:
                print("JSON file should contain an array of job postings.")
                return
        
        elif filepath.endswith('.csv'):
            df = pd.read_csv(filepath)
            
            # Process CSV with the specific structure from your example
            texts = []
            for _, row in df.iterrows():
                text_parts = [
                    f"Job Title: {row.get('Job Title', '')}",
                    f"Company: {row.get('Company', '')}",
                    f"Location: {row.get('Location', '')}",
                    f"Job Types: {row.get('Job Types', '')}",
                    f"Posted Date: {row.get('Posted Date', '')}"
                ]
                texts.append("\n".join(text_parts))
        
        elif filepath.endswith('.txt'):
            with open(filepath, 'r') as f:
                texts = [line.strip() for line in f if line.strip()]
        
        else:
            print("Unsupported file format.")
            return
        
        print(f"\nFound {len(texts)} job postings to analyze.")
        if len(texts) > 100:
            print("Warning: Large number of postings. This may take a while.")
        
        confirm = input("Proceed with analysis? (y/n): ").lower()
        if confirm != 'y':
            return
        
        results = analyzer.batch_analyze(texts)
        analyzer.analysis_results.extend(results)
        
        print("\nAnalysis complete. Results saved for reporting.")
        print(f"Analyzed {len(results)} job postings successfully.")
    
    except Exception as e:
        print(f"Error processing file: {str(e)}")

# Manage custom entity recognition patterns.
def manage_patterns(analyzer):
    """  
    Args:
        analyzer: The analyzer instance
    """
    print("\n Custom Entity Patterns ")
    print("Current custom patterns:")
    for i, pattern in enumerate(analyzer.custom_patterns, 1):
        print(f"{i}. {pattern.get('label')} - {pattern.get('pattern')}")
    
    print("\nOptions:")
    print("1. Add new pattern")
    print("2. Remove pattern")
    print("3. Back to main menu")
    
    choice = input("\nEnter your choice (1-3): ")
    
    if choice == "1":
        print("\nAdd New Pattern")
        print("Pattern format is spaCy's Matcher pattern syntax")
        print("Example: {'label': 'TECHNOLOGY', 'pattern': [{'LOWER': 'python'}]}")
        
        try:
            label = input("Enter entity label (e.g., TECHNOLOGY, BENEFIT): ").strip().upper()
            pattern_str = input("Enter pattern (as Python dict): ").strip()
            
            # Convert string pattern to dict
            pattern = eval(pattern_str)  # Caution: eval can be dangerous in production
            
            # Validate pattern
            if not isinstance(pattern, list):
                pattern = [pattern]
            
            new_pattern = {"label": label, "pattern": pattern}
            analyzer.custom_patterns.append(new_pattern)
            
            # Update the entity ruler
            ruler = nlp.get_pipe("entity_ruler")
            ruler.add_patterns([new_pattern])
            
            print("Pattern added successfully.")
        
        except Exception as e:
            print(f"Error adding pattern: {str(e)}")
    
    elif choice == "2":
        if not analyzer.custom_patterns:
            print("No patterns to remove.")
            return
        
        try:
            index = int(input("Enter pattern number to remove: ")) - 1
            if 0 <= index < len(analyzer.custom_patterns):
                removed = analyzer.custom_patterns.pop(index)
                
                # Need to completely rebuild the entity ruler
                nlp.remove_pipe("entity_ruler")
                new_ruler = nlp.add_pipe("entity_ruler", before="ner")
                new_ruler.add_patterns(analyzer.custom_patterns)
                
                print(f"Removed pattern: {removed}")
            else:
                print("Invalid pattern number.")
        except ValueError:
            print("Please enter a valid number.")

# Handle export of analysis results.
def export_menu(analyzer):
    """    
    Args:
        analyzer: The analyzer instance
    """
    if not analyzer.analysis_results:
        print("No analysis results to export.")
        return
    
    print("\n Export Analysis Results ")
    print(f"You have {len(analyzer.analysis_results)} analyses to export.")
    print("\nExport formats:")
    print("1. JSON (structured data)")
    print("2. CSV (spreadsheet)")
    print("3. Excel (spreadsheet)")
    print("4. Back to main menu")
    
    choice = input("\nEnter your choice (1-4): ")
    
    if choice in ["1", "2", "3"]:
        format_map = {"1": "json", "2": "csv", "3": "excel"}
        analyzer.export_results(analyzer.analysis_results, format=format_map[choice])
    else:
        return

# Handle entity visualization.
def visualize_entities_menu(analyzer):
    """    
    Args:
        analyzer: The analyzer instance
    """
    print("\n Entity Visualization ")
    print("Enter/Paste your job posting text to visualize entities:")
    print("(press Enter on an empty line to finish)")
    
    lines = []
    while True:
        line = input()
        if line:
            lines.append(line)
        else:
            break
    
    text = "\n".join(lines)
    if not text.strip():
        print("No text provided. Returning to main menu.")
        return
    
    print("\nGenerating visualization... (this may open in your browser)")
    analyzer.visualize_entities(text)

def main():
    analyzer = JobPostingAnalyzer()
    
    print("Welcome to JobPostingNER by David Caleb")
    print("A comprehensive tool for analyzing job postings and extracting key entities.")
    
    while True:
        choice = display_menu()
        
        if choice == "1":
            single_job_analysis(analyzer)
        elif choice == "2":
            file_batch_analysis(analyzer)
        elif choice == "3":
            manage_patterns(analyzer)
        elif choice == "4":
            analyzer.generate_report(analyzer.analysis_results)
        elif choice == "5":
            export_menu(analyzer)
        elif choice == "6":
            visualize_entities_menu(analyzer)
        elif choice == "7":
            print("\nSettings:")
            print("Current settings options would be configured here.")
            print("(Implementation details would be added in a production system)")
        elif choice == "8":
            print("\nThank you for using JobPostingNER. Goodbye!")
            break
        else:
            print("\nInvalid choice. Please enter a number between 1 and 8.")
        
        input("\nPress Enter to continue...")

if __name__ == "__main__":
    main()
# Import necessary libraries
import re
from typing import List, Dict
import sqlite3
import matplotlib.pyplot as plt
from tkinter import Tk, Label, Text, Button, filedialog, messagebox, Frame

# A Named Entity Recognition (NER) system for extracting medical-related entities
# such as diseases, medications, symptoms, and medical procedures from text.
class MedNER:
    # Initialize the MedNER system with predefined patterns for medical entities.
    def __init__(self):
        # Define regex patterns for medical entities
        self.patterns = {
            "DISEASE": r"\b(?:cancer|diabetes|hypertension|asthma|alzheimer|parkinson)\b",
            "MEDICATION": r"\b(?:aspirin|ibuprofen|paracetamol|insulin|metformin)\b",
            "SYMPTOM": r"\b(?:headache|fever|cough|fatigue|nausea|dizziness)\b",
            "PROCEDURE": r"\b(?:surgery|biopsy|chemotherapy|radiotherapy|endoscopy)\b",
        }
        # Initialize database connection
        self.conn = sqlite3.connect('medner.db')
        self.create_table()

    # Create a table to store extracted entities
    def create_table(self):
        with self.conn:
            self.conn.execute('''
                CREATE TABLE IF NOT EXISTS entities (
                    id INTEGER PRIMARY KEY AUTOINCREMENT,
                    category TEXT,
                    entity TEXT
                )
            ''')

    # Extract medical entities from the input text.
    def extract_entities(self, text: str) -> Dict[str, List[str]]:
        """
        Args:
            text: The input text to analyze.
        Returns:
            Dict[str, List[str]]: A dictionary containing lists of extracted entities
                                for each category (DISEASE, MEDICATION, SYMPTOM, PROCEDURE).
        """
        entities = {category: [] for category in self.patterns}

        # Iterate through each category and find matches in the text
        for category, pattern in self.patterns.items():
            matches = re.findall(pattern, text, flags=re.IGNORECASE)
            entities[category] = list(set(matches))  # Remove duplicates

        return entities

    # Store extracted entities in the database
    def store_entities(self, entities: Dict[str, List[str]]):
        with self.conn:
            for category, matches in entities.items():
                for entity in matches:
                    self.conn.execute('INSERT INTO entities (category, entity) VALUES (?, ?)', (category, entity))

    # Analyze the input text and print the extracted medical entities.
    def analyze_text(self, text: str) -> None:
        """
        Args:
            text: The input text to analyze.
        """
        entities = self.extract_entities(text)
        self.store_entities(entities)

        # Print the results
        print("Extracted Medical Entities:")
        for category, matches in entities.items():
            print(f"{category}: {', '.join(matches)}")

    # Visualize the frequency of extracted entities
    def visualize_entities(self):
        with self.conn:
            cursor = self.conn.execute('SELECT category, COUNT(*) FROM entities GROUP BY category')
            categories = []
            counts = []
            for row in cursor:
                categories.append(row[0])
                counts.append(row[1])

            plt.bar(categories, counts, color='skyblue')
            plt.xlabel('Categories', color='white')
            plt.ylabel('Frequency', color='white')
            plt.title('Frequency of Extracted Medical Entities', color='white')
            plt.gca().set_facecolor('#2E2E2E')  # Dark background for the plot
            plt.gcf().set_facecolor('#2E2E2E')  # Dark background for the figure
            plt.xticks(color='white')
            plt.yticks(color='white')
            plt.show()

# GUI for MedNER
class MedNERApp:
    def __init__(self, root):
        self.root = root
        self.root.title("MedNER - Medical Named Entity Recognition by David Caleb")
        self.root.configure(bg='#2E2E2E')
        self.med_ner = MedNER()

        # Create a frame to hold the UI elements
        self.frame = Frame(root, bg='#2E2E2E')
        self.frame.pack(pady=20)

        # Create UI elements
        self.label = Label(self.frame, text="Enter text or upload a file to analyze:", bg='#2E2E2E', fg='white', font=('Arial', 12))
        self.label.pack()

        self.text_area = Text(self.frame, height=10, width=50, bg='#424242', fg='white', insertbackground='white')
        self.text_area.pack(pady=10)

        self.analyze_button = Button(self.frame, text="Analyze Text", command=self.analyze_text, bg='#555555', fg='white', font=('Arial', 10), relief='flat')
        self.analyze_button.pack(pady=5)

        self.upload_button = Button(self.frame, text="Upload File", command=self.upload_file, bg='#555555', fg='white', font=('Arial', 10), relief='flat')
        self.upload_button.pack(pady=5)

        self.visualize_button = Button(self.frame, text="Visualize Entities", command=self.visualize_entities, bg='#555555', fg='white', font=('Arial', 10), relief='flat')
        self.visualize_button.pack(pady=5)

    def analyze_text(self):
        text = self.text_area.get("1.0", "end-1c")
        if text.strip():
            self.med_ner.analyze_text(text)
            messagebox.showinfo("Analysis Complete", "Entities extracted and stored in the database.")
        else:
            messagebox.showwarning("Input Error", "Please enter some text to analyze.")

    def upload_file(self):
        file_path = filedialog.askopenfilename(filetypes=[("Text Files", "*.txt"), ("PDF Files", "*.pdf")])
        if file_path:
            with open(file_path, 'r') as file:
                text = file.read()
                self.text_area.delete("1.0", "end")
                self.text_area.insert("1.0", text)
                self.med_ner.analyze_text(text)
                messagebox.showinfo("Analysis Complete", "Entities extracted and stored in the database.")

    def visualize_entities(self):
        self.med_ner.visualize_entities()

# Example usage
if __name__ == "__main__":
    # Create the main application window
    root = Tk()
    app = MedNERApp(root)
    root.mainloop()
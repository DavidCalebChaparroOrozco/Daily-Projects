# Import necessary libraries
import spacy
import random
from spacy.util import minibatch
from spacy.training.example import Example

# Define training data for tourist locations NER
train_data = [
    ("During my trip to Paris, I visited the Eiffel Tower and enjoyed a walking tour.", {
        "entities": [
            (18, 24, "CITY"),
            (36, 47, "MONUMENT"),
            (62, 75, "ACTIVITY")
        ]
    }),
    ("Tokyo offers amazing experiences like climbing Mount Fuji and exploring local markets.", {
        "entities": [
            (0, 5, "CITY"),
            (32, 42, "MONUMENT"),
            (47, 64, "ACTIVITY")
        ]
    }),
    ("In Rome, I took a historical tour of the Colosseum and tried a food tour.", {
        "entities": [
            (3, 7, "CITY"),
            (31, 40, "MONUMENT"),
            (45, 55, "ACTIVITY")
        ]
    }),
    ("Barcelona's architectural wonders include the Sagrada Familia and a street art tour.", {
        "entities": [
            (0, 9, "CITY"),
            (37, 53, "MONUMENT"),
            (58, 73, "ACTIVITY")
        ]
    })
]

# Load the medium-sized English model
nlp = spacy.load("en_core_web_md")

# Add NER component if not already present
if 'ner' not in nlp.pipe_names:
    ner = nlp.add_pipe("ner", last=True)
else:
    ner = nlp.get_pipe("ner")

# Add custom labels to NER component
for _, annotations in train_data:
    for ent in annotations.get('entities', []):
        if ent[2] not in ner.labels:
            ner.add_label(ent[2])

# Training configuration

# Train NER model on custom tourist location data
def train_ner_model(nlp, train_data, epochs=50):
    """    
    Args:
        nlp: SpaCy language model
        train_data: Training data with text and entity annotations
        epochs: Number of training iterations
    """
    # Disable other pipeline components during training
    other_pipes = [pipe for pipe in nlp.pipe_names if pipe != 'ner']
    with nlp.disable_pipes(*other_pipes):
        optimizer = nlp.begin_training()
        
        for epoch in range(epochs):
            random.shuffle(train_data)
            losses = {}
            batches = minibatch(train_data, size=2)
            
            for batch in batches:
                examples = []
                for text, annotations in batch:
                    doc = nlp.make_doc(text)
                    example = Example.from_dict(doc, annotations)
                    examples.append(example)
                
                # Update model with examples
                nlp.update(examples, drop=0.5, losses=losses)
            
            print(f"Epoch {epoch + 1}, Losses: {losses}")
    
    return nlp

# Train the NER model
trained_nlp = train_ner_model(nlp, train_data)

# Save the trained model
trained_nlp.to_disk("tourist_location_ner_model")

# Test the trained model
def test_ner_model(nlp, test_texts):
    """
    Args:
        nlp: Trained SpaCy language model
        test_texts: List of texts to test NER
    """
    for text in test_texts:
        doc = nlp(text)
        print(f"Text: {text}")
        print("Entities:", [(ent.text, ent.label_) for ent in doc.ents])
        print()

# Sample test texts
test_texts = [
    "I want to explore New York City and visit the Statue of Liberty.",
    "A hiking tour in Rio de Janeiro near Christ the Redeemer sounds amazing.",
    "Venice offers beautiful canal tours and historic architecture.",
    "Enjoy the Flower Fair in Medellin"
]

# Run NER tests
test_ner_model(trained_nlp, test_texts)
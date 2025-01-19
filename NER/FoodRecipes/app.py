# Importing necessary libraries
import spacy
import random
from spacy.util import minibatch
from spacy.training.example import Example

# Defining the training data with recipes and their corresponding entities
train_data = [
    ("200g of flour", {"entities": [(0, 7, "QUANTITY"), (10, 15, "INGREDIENT")]}),
    ("1 cup of sugar", {"entities": [(0, 1, "QUANTITY"), (4, 9, "INGREDIENT")]}),
    ("Bake for 30 minutes", {"entities": [(0, 4, "METHOD"), (10, 12, "QUANTITY")]}),
    ("Fry the vegetables", {"entities": [(0, 4, "METHOD")]}),
    ("Add 2 eggs", {"entities": [(4, 5, "QUANTITY"), (6, 10, "INGREDIENT")]}),
    ("Mix well", {"entities": [(0, 4, "METHOD")]}),
    ("Chop the onions finely", {"entities": [(0, 4, "METHOD")]}),
    ("Simmer for 15 minutes", {"entities": [(0, 6, "METHOD"), (12, 14, "QUANTITY")]}),
]

# Loading the medium-sized English model from spaCy
nlp = spacy.load("en_core_web_md")

# Checking if the NER component is already in the pipeline; if not, add it.
if 'ner' not in nlp.pipe_names:
    # Adding NER as the last component
    ner = nlp.add_pipe("ner", last=True)
else:
    # Getting the existing NER component
    ner = nlp.get_pipe("ner")

# Adding labels to the NER component based on the training data
for _, annotations in train_data:
    for ent in annotations['entities']:
        # Check if label is already present
        if ent[2] not in ner.labels:
            # Add new label
            ner.add_label(ent[2])

# Disabling other pipeline components during training to focus on NER
other_pipes = [pipe for pipe in nlp.pipe_names if pipe != 'ner']
# Disable all pipes except NER
with nlp.disable_pipes(*other_pipes):
    # Initialize the optimizer for training
    optimizer = nlp.begin_training()
    epochs = 50

    # Shuffle training data at each epoch
    for epoch in range(epochs):
        random.shuffle(train_data)
        losses = {}
        batches = minibatch(train_data, size=2)
        for batch in batches:
            examples = []
            for text, annotations in batch:
                # Create a document from text
                doc = nlp.make_doc(text)
                # Create an Example object
                example = Example.from_dict(doc, annotations)
                examples.append(example)
            # Update model with examples and compute losses
            nlp.update(examples, drop=0.5, losses=losses)
        print(f"Epoch {epoch + 1}, Losses: {losses}")

# Saving the trained model to disk
nlp.to_disk("custom_ner_model")

# Loading the trained model from disk for testing
trained_nlp = spacy.load("custom_ner_model")

# Defining test texts to evaluate the trained model
test_texts = [
    "Use 200g of flour and bake for 30 minutes.",
    "Fry the onions and add 1 cup of sugar.",
    "Simmer for 15 minutes after adding salt."
]

# Loop through each test text and print recognized entities
for text in test_texts:
    # Process text with the trained model
    doc = trained_nlp(text)  
    # Print original text
    print(f"Text: {text}")  
    # Print detected entities and their labels
    print("Entities:", [(ent.text, ent.label_) for ent in doc.ents])  
    # Print a newline for better readability
    print()  

# # text = 'John goes ffor a walk in Berlin'
# # text = 'What is the price of 20 bananas?' # intent: price question
# text = 'Give me the value of 40 bananas' # intent: price question

# # Person -> John
# # Location -> Berlin


# def get_price_of_product(quantity, product):
#     # pass

# Importing necessary libraries
# import spacy

# texts = [
#     'What is the price of 4 bananas?',
#     'How much are 16 chairs?',
#     'Give me the value of 5 laptops?',
#     'Give me the value of five laptops?',
#     # 'John goes for a walk in Berlin',
#     # 'Mike is going to the store',
#     # 'Elon Musk is the CEO at Twitter',
#     # 'Bob Smith is the guy behind XYZ-Soft Inc.',
#     # 'Floarian Dedov is the guy behind NeuralNine'
# ]

# nlp = spacy.load("en_core_web_md")

# # ner_labels = nlp.get_pipe('ner').labels
# # print(ner_labels)

# categories = ['ORG', 'PERSON', 'LOC']

# docs = [nlp(text) for text in texts]

# for doc in docs:
#     entities = []
#     for ent in doc.ents:
#         # if ent.label_ in categories:
#         #     entities.append((ent.text, ent.label_))
#         entities.append((ent.text, ent.label_))

#     print(entities)






# Importing necessary libraries
import spacy
import random
from spacy.util import minibatch
from spacy.training.example import Example

# Defining the training data with questions and their corresponding entities
train_data = [
    ("What is the price of 10 bananas?", {"entities": [(21, 23, "QUANTITY"), (24, 31, "PRODUCT")]}),
    ("Can you tell me the cost of 5 apples?", {"entities": [(27, 28, "QUANTITY"), (29, 35, "PRODUCT")]}),
    ("How much for 3 oranges?", {"entities": [(13, 14, "QUANTITY"), (15, 22, "PRODUCT")]}),
    ("I'd like to know the price of 12 grapes.", {"entities": [(28, 30, "QUANTITY"), (31, 37, "PRODUCT")]}),
    ("What is the total for 2 pineapples?", {"entities": [(21, 22, "QUANTITY"), (23, 33, "PRODUCT")]}),
    ("Give me the cost for 7 lemons.", {"entities": [(20, 21, "QUANTITY"), (22, 28, "PRODUCT")]}),
    ("How much would 4 watermelons cost?", {"entities": [(16, 17, "QUANTITY"), (18, 29, "PRODUCT")]}),
    ("Tell me the price of 15 peaches.", {"entities": [(21, 23, "QUANTITY"), (24, 31, "PRODUCT")]}),
    ("What do 9 strawberries cost?", {"entities": [(8, 9, "QUANTITY"), (10, 21, "PRODUCT")]}),
    ("How much for 8 cherries?", {"entities": [(13, 14, "QUANTITY"), (15, 23, "PRODUCT")]}),
    ("Can you calculate the price of 6 kiwis?", {"entities": [(30, 31, "QUANTITY"), (32, 37, "PRODUCT")]}),
    ("I need the cost for 20 plums.", {"entities": [(21, 23, "QUANTITY"), (24, 29, "PRODUCT")]}),
    ("What is the price of 3 mangoes?", {"entities": [(21, 22, "QUANTITY"), (23, 30, "PRODUCT")]}),
    ("Can you tell me how much 14 pears cost?", {"entities": [(25, 27, "QUANTITY"), (28, 33, "PRODUCT")]}),
    ("How much do 11 avocados cost?", {"entities": [(12, 14, "QUANTITY"), (15, 23, "PRODUCT")]}),
    ("What's the cost of 1 coconut?", {"entities": [(20, 21, "QUANTITY"), (22, 29, "PRODUCT")]}),
    ("Tell me the price for 18 blueberries.", {"entities": [(23, 25, "QUANTITY"), (26, 36, "PRODUCT")]}),
    ("How much is 25 papayas?", {"entities": [(12, 14, "QUANTITY"), (15, 22, "PRODUCT")]}),
    ("What is the total price for 10 pineapples?", {"entities": [(28, 30, "QUANTITY"), (31, 41, "PRODUCT")]}),
    ("Give me the price of 4 watermelons.", {"entities": [(20, 21, "QUANTITY"), (22, 33, "PRODUCT")]}),
    ("How much do 7 melons cost?", {"entities": [(12, 13, "QUANTITY"), (14, 20, "PRODUCT")]}),
    ("What's the price for 19 limes?", {"entities": [(21, 23, "QUANTITY"), (24, 29, "PRODUCT")]}),
    ("Can you tell me the cost of 13 apples?", {"entities": [(27, 29, "QUANTITY"), (30, 36, "PRODUCT")]}),
    ("I'd like to know the price of 2 bananas.", {"entities": [(28, 29, "QUANTITY"), (30, 37, "PRODUCT")]}),
    ("What do 6 coconuts cost?", {"entities": [(8, 9, "QUANTITY"), (10, 18, "PRODUCT")]}),
    ("How much is the price for 15 peaches?", {"entities": [(26, 28, "QUANTITY"), (29, 36, "PRODUCT")]}),
    ("Can you calculate the cost of 8 cherries?", {"entities": [(29, 30, "QUANTITY"), (31, 39, "PRODUCT")]}),
    ("I need to know the price of 3 papayas.", {"entities": [(28, 29, "QUANTITY"), (30, 37, "PRODUCT")]}),
    ("What is the cost for 9 mangoes?", {"entities": [(21, 22, "QUANTITY"), (23, 30, "PRODUCT")]}),
    ("How much do 5 strawberries cost?", {"entities": [(12, 13, "QUANTITY"), (14, 25, "PRODUCT")]}),
    ("What's the total price for 16 grapes?", {"entities": [(28, 30, "QUANTITY"), (31, 37, "PRODUCT")]}),
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
for _ , annotations in train_data:
    for ent in annotations['entities']:
        # Check if label is already present
        if ent[2] not in ner.labels:
            # Add new label
            ner.add_labels(ent[2])

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
    "How much for 3 oranges?",
    "I want 15 limes for the conference.",
    "Can you give me the price for 3 strawberries?"
]

# Loop through each test text and print recognized entities
for text in test_texts:
    # Process text with the trained model
    doc = trained_nlp(text)  
    # Print original text
    print(f"Text: {text}")  
    # Print detected entities and their labels
    print("Entities", [(ent.text, ent.label_) for ent in doc.ents])  
    # Print a newline for better readability
    print()  
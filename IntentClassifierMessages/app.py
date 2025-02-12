# Import necessary libraries
import numpy as np
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.naive_bayes import MultinomialNB
from sklearn.pipeline import make_pipeline
from sklearn.metrics import classification_report, accuracy_score, confusion_matrix
import nltk
from nltk.corpus import stopwords
import string
import matplotlib.pyplot as plt
import seaborn as sns
import joblib
from sklearn.model_selection import GridSearchCV

# Download NLTK stopwords (only required once)
nltk.download('stopwords')

# Sample dataset of messages and their corresponding intents
data = {
    "message": [
        "I want to buy a product",
        "Can you help me?",
        "How do I reset my password?",
        "I need assistance",
        "Where can I find the pricing?",
        "I'd like to make a purchase",
        "What are your business hours?",
        "Is there a discount available?",
        "I have a question",
        "Can you provide more details?",
        "I want to order something",
        "How can I contact support?",
        "What is the return policy?",
        "I need help with my order",
        "Do you offer refunds?",
        "How do I track my shipment?",
        "I want to cancel my subscription",
        "Can I change my delivery address?",
        "What payment methods do you accept?",
        "I have a billing issue"
    ],
    "intent": [
        "purchase",
        "help",
        "question",
        "help",
        "question",
        "purchase",
        "question",
        "question",
        "question",
        "help",
        "purchase",
        "help",
        "question",
        "help",
        "question",
        "question",
        "purchase",
        "question",
        "question",
        "help"
    ]
}

# Convert the dataset into a pandas DataFrame
df = pd.DataFrame(data)

# Preprocessing function to clean and tokenize text
def preprocess_text(text):
    # Convert to lowercase
    text = text.lower()
    # Remove punctuation
    text = text.translate(str.maketrans("", "", string.punctuation))
    # Remove stopwords
    stop_words = set(stopwords.words("english"))
    text = " ".join([word for word in text.split() if word not in stop_words])
    return text

# Apply preprocessing to the messages
df["cleaned_message"] = df["message"].apply(preprocess_text)

# Split the dataset into training and testing sets
X_train, X_test, y_train, y_test = train_test_split(
    df["cleaned_message"], df["intent"], test_size=0.2, random_state=42
)

# Create a pipeline with TF-IDF vectorizer and Naive Bayes classifier
model = make_pipeline(TfidfVectorizer(), MultinomialNB())

# Hyperparameter tuning using GridSearchCV
param_grid = {
    'tfidfvectorizer__max_features': [1000, 2000, 3000],
    'multinomialnb__alpha': [0.1, 0.5, 1.0]
}
grid_search = GridSearchCV(model, param_grid, cv=3, n_jobs=-1)
grid_search.fit(X_train, y_train)

# Best model after hyperparameter tuning
best_model = grid_search.best_estimator_

# Predict on the test set
y_pred = best_model.predict(X_test)

# Evaluate the model
print("Best Parameters:", grid_search.best_params_)
print("Accuracy:", accuracy_score(y_test, y_pred))
print("\nClassification Report:\n", classification_report(y_test, y_pred))

# Confusion Matrix
conf_matrix = confusion_matrix(y_test, y_pred)
plt.figure(figsize=(8, 6))
sns.heatmap(conf_matrix, annot=True, fmt='d', cmap='Blues', xticklabels=best_model.classes_, yticklabels=best_model.classes_)
plt.xlabel('Predicted')
plt.ylabel('Actual')
plt.title('Confusion Matrix')
plt.show()

# Save the trained model to a file
model_filename = "intent_classifier_model.pkl"
joblib.dump(best_model, model_filename)
print(f"Model saved to {model_filename}")

# Load the model from the file (for demonstration)
loaded_model = joblib.load(model_filename)

# Function to classify a new message
def classify_intent(message):
    cleaned_message = preprocess_text(message)
    intent = loaded_model.predict([cleaned_message])[0]
    return intent

# Test the classifier with new messages
test_messages = [
    "I want to buy something",
    "Can you help me with my account?",
    "What is the price of this item?",
    "How do I cancel my order?",
    "Do you have a customer service number?"
]

print("\nTesting the Classifier with New Messages:")
for msg in test_messages:
    print(f"Message: {msg} -> Intent: {classify_intent(msg)}")
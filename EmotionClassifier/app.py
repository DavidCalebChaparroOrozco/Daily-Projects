# Import necessary libraries
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import accuracy_score, classification_report
from sklearn.utils import resample
import nltk
from nltk.corpus import stopwords
import spacy

# Download NLTK stopwords
nltk.download('stopwords')

# Load SpaCy's English model
try:
    nlp = spacy.load('en_core_web_sm')
except OSError:
    print("SpaCy model 'en_core_web_sm' not found. Please install it by running:")
    print("python -m spacy download en_core_web_sm")
    exit()

# Load the dataset
data = pd.read_csv('data/rotten_tomatoes_movies.csv')  # Replace with your dataset path

# Filter relevant columns: 'critics_consensus' and 'tomatometer_status'
data = data[['critics_consensus', 'tomatometer_status']]

# Drop rows with missing values
data = data.dropna()

# Map 'tomatometer_status' to sentiment labels
data['sentiment'] = data['tomatometer_status'].map({
    'Certified-Fresh': 'Positive',
    'Fresh': 'Positive',
    'Rotten': 'Negative'
})

# Balance the dataset by undersampling the majority class
data_majority = data[data['sentiment'] == 'Positive']
data_minority = data[data['sentiment'] == 'Negative']

# Undersample the majority class
data_majority_downsampled = resample(data_majority, replace=False, n_samples=len(data_minority), random_state=42)

# Combine the downsampled majority class with the minority class
balanced_data = pd.concat([data_majority_downsampled, data_minority])

# Shuffle the dataset
balanced_data = balanced_data.sample(frac=1, random_state=42)

# Preprocess the text data
def preprocess_text(text):
    # Convert to lowercase
    text = text.lower()
    
    # Remove stopwords using NLTK, but keep important sentiment words
    stop_words = set(stopwords.words('english')) - {'not', 'no', 'nor', 'neither', 'but', 'very', 'too', 'great', 'love', 'amazing'}
    text = ' '.join([word for word in text.split() if word not in stop_words])
    
    # Lemmatize using SpaCy
    doc = nlp(text)
    text = ' '.join([token.lemma_ for token in doc if token.pos_ in ['NOUN', 'ADJ', 'VERB', 'ADV']])  # Keep only nouns, adjectives, verbs, and adverbs
    
    return text

# Apply preprocessing to the 'critics_consensus' column
balanced_data['cleaned_text'] = balanced_data['critics_consensus'].apply(preprocess_text)

# Split the balanced dataset into training and testing sets
X_train, X_test, y_train, y_test = train_test_split(balanced_data['cleaned_text'], balanced_data['sentiment'], test_size=0.2, random_state=42)

# Convert text to numerical features using TF-IDF
vectorizer = TfidfVectorizer(max_features=25000, ngram_range=(1, 3))  # Use unigrams, bigrams, and trigrams
X_train_tfidata = vectorizer.fit_transform(X_train)
X_test_tfidata = vectorizer.transform(X_test)

# Train a Logistic Regression classifier with class weights
classifier = LogisticRegression(max_iter=1000, class_weight='balanced', random_state=42)
classifier.fit(X_train_tfidata, y_train)

# Make predictions on the test set
y_pred = classifier.predict(X_test_tfidata)

# Evaluate the model
accuracy = accuracy_score(y_test, y_pred)
print(f"Accuracy: {accuracy:.2f}")
print("\nClassification Report:")
print(classification_report(y_test, y_pred))

# Function to classify new text
def classify_sentiment(text):
    cleaned_text = preprocess_text(text)
    text_tfidata = vectorizer.transform([cleaned_text])
    prediction = classifier.predict(text_tfidata)
    return prediction[0]

# Test with multiple sample texts
sample_texts = [
    "This movie is great! I loved every moment of it.",  # Positive
    "The film was terrible and boring. I hated it.",     # Negative
    "An amazing experience with brilliant performances.",  # Positive
    "Worst movie I've ever seen. Waste of time.",        # Negative
    "The movie was okay, but nothing special.",          # Neutral (might be misclassified)
    "I absolutely adored this film! It was breathtaking.",  # Strong Positive
    "This was the most disappointing movie of the year.",  # Strong Negative
    "The acting was superb, but the plot was weak.",      # Mixed Sentiment
    "A masterpiece that left me speechless.",             # Strong Positive
    "I couldn't stand this movie. It was awful.",         # Strong Negative
]

for text in sample_texts:
    predicted_sentiment = classify_sentiment(text)
    print(f"Predicted Sentiment for '{text}': {predicted_sentiment}")
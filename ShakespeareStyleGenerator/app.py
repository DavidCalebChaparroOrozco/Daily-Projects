# Import necessary libraries
import tensorflow as tf
from tensorflow.keras.models import Sequential
from tensorflow.keras.layers import LSTM, Dense, Embedding
from tensorflow.keras.preprocessing.sequence import pad_sequences
from tensorflow.keras.utils import to_categorical
import numpy as np
import random

# Load Shakespeare dataset
def load_shakespeare_data(file_path):
    """
    Args:
        file_path: Path to the text file.
    Returns:
        str: The text data as a single string.
    """
    with open(file_path, 'r', encoding='utf-8') as file:
        text = file.read()
    return text

# Preprocess the text data by creating sequences of characters and their corresponding labels.
def preprocess_text(text, seq_length=100):
    """
    Args:
        text: The input text data.
        seq_length: Length of each input sequence.
    Returns:
        tuple: (input_sequences, labels, char_to_idx, idx_to_char, num_unique_chars)
    """
    # Extract unique characters from the text
    chars = sorted(list(set(text)))
    num_unique_chars = len(chars)
    
    # Create character-to-index and index-to-character mappings
    char_to_idx = {char: idx for idx, char in enumerate(chars)}
    idx_to_char = {idx: char for idx, char in enumerate(chars)}
    
    # Convert the entire text into a sequence of indices
    text_as_int = np.array([char_to_idx[char] for char in text])
    
    # Create input sequences and corresponding labels
    input_sequences = []
    labels = []
    for i in range(0, len(text_as_int) - seq_length):
        input_seq = text_as_int[i:i + seq_length]
        label = text_as_int[i + seq_length]
        input_sequences.append(input_seq)
        labels.append(label)
    
    # Convert lists to numpy arrays
    input_sequences = np.array(input_sequences)
    labels = np.array(labels)
    
    # One-hot encode the labels
    labels = to_categorical(labels, num_classes=num_unique_chars)
    
    return input_sequences, labels, char_to_idx, idx_to_char, num_unique_chars

# Build the LSTM model
def build_lstm_model(num_unique_chars, seq_length):
    """
    Build an LSTM model for text generation.
    Args:
        num_unique_chars: Number of unique characters in the text.
        seq_length: Length of input sequences.
    Returns:
        model: A compiled Keras model.
    """
    model = Sequential([
        Embedding(input_dim=num_unique_chars, output_dim=128, input_length=seq_length), 
        LSTM(256, return_sequences=True), 
        LSTM(256),
        Dense(128, activation='relu'),  
        Dense(num_unique_chars, activation='softmax')
    ])
    
    # Compile the model
    model.compile(optimizer='adam', loss='categorical_crossentropy', metrics=['accuracy'])
    return model

# Generate text using the trained model
def generate_text(model, seed_text, char_to_idx, idx_to_char, seq_length, num_chars_to_generate=500):
    """
    Generate text using the trained LSTM model.
    Args:
        model: Trained Keras model.
        seed_text: Initial seed text to start generation.
        char_to_idx: Character-to-index mapping.
        idx_to_char: Index-to-character mapping.
        seq_length: Length of input sequences.
        num_chars_to_generate: Number of characters to generate.
    Returns:
        str: Generated text.
    """
    generated_text = seed_text
    for _ in range(num_chars_to_generate):
        # Convert the seed text to a sequence of indices
        input_seq = [char_to_idx[char] for char in seed_text]
        input_seq = pad_sequences([input_seq], maxlen=seq_length, padding='pre')
        
        # Predict the next character
        predicted_probs = model.predict(input_seq, verbose=0)[0]
        predicted_idx = np.argmax(predicted_probs)
        predicted_char = idx_to_char[predicted_idx]
        
        # Append the predicted character to the generated text and update the seed text
        generated_text += predicted_char
        seed_text = seed_text[1:] + predicted_char
    
    return generated_text

# Main function
def main():
    # Load and preprocess the Shakespeare text
    file_path = 'shakespeare.txt'
    text = load_shakespeare_data(file_path)
    seq_length = 100
    input_sequences, labels, char_to_idx, idx_to_char, num_unique_chars = preprocess_text(text, seq_length)
    
    # Build and train the LSTM model
    model = build_lstm_model(num_unique_chars, seq_length)
    model.fit(input_sequences, labels, batch_size=128, epochs=20)
    
    # Generate text using the trained model
    seed_text = "To be, or not to be: that is the question:\n"
    generated_text = generate_text(model, seed_text, char_to_idx, idx_to_char, seq_length)
    print("Generated Text:\n", generated_text)

# Run the program
if __name__ == "__main__":
    main()
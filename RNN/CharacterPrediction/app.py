# Import necessary libraries
import numpy as np
import tensorflow as tf
from tensorflow.keras.models import Sequential
from tensorflow.keras.layers import Embedding, SimpleRNN, Dense

# Sample text for training the model
text = """
Hello family,
How are you all doing? Greetings from my daily projects. Today, on Day 108, I have created a simple character-level language model to predict the next character in a sequence.
Best regards,
David Caleb
"""

# Create a mapping from characters to indices
chars = sorted(set(text))
char_to_idx = {char: idx for idx, char in enumerate(chars)}
idx_to_char = {idx: char for char, idx in char_to_idx.items()}

# Prepare the dataset
# Length of the sequences for training
maxlen = 3  
# Step size for moving the training window
step = 1  
sequences = []
next_chars = []
for i in range(0, len(text) - maxlen, step):
    sequences.append(text[i: i + maxlen])
    next_chars.append(text[i + maxlen])
    
X = np.zeros((len(sequences), maxlen), dtype=np.int32)
y = np.zeros((len(sequences), len(chars)), dtype=np.int32)

for i, seq in enumerate(sequences):
    for t, char in enumerate(seq):
        X[i, t] = char_to_idx[char]
    y[i, char_to_idx[next_chars[i]]] = 1

# Build the RNN model
model = Sequential()
model.add(Embedding(input_dim=len(chars), output_dim=32, input_length=maxlen))
model.add(SimpleRNN(units=32))
model.add(Dense(len(chars), activation='softmax'))

# Compile the model
model.compile(loss='categorical_crossentropy', optimizer='adam', metrics=['accuracy'])

# Train the model
model.fit(X, y, batch_size=2, epochs=100)

# Function to predict the next character given a sequence
def predict_next_char(sequence):
    # Use only the last maxlen characters for prediction
    sequence = sequence[-maxlen:]
    x = np.zeros((1, maxlen), dtype=np.int32)
    for t, char in enumerate(sequence):
        x[0, t] = char_to_idx[char]
    preds = model.predict(x, verbose=0)[0]
    next_index = np.argmax(preds)
    return idx_to_char[next_index]

# Testing the model
test_seq = "Greetings from my "
predicted_char = predict_next_char(test_seq)
print(f"Given sequence: {test_seq}, predicted next character: {predicted_char}")
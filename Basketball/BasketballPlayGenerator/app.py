# Import necessary libraries
import numpy as np
import tensorflow as tf
from tensorflow.keras.models import Sequential
from tensorflow.keras.layers import Dense, LSTM, Embedding, Dropout, Concatenate, Input
from tensorflow.keras.preprocessing.sequence import pad_sequences
from tensorflow.keras.models import Model
import random
import matplotlib.pyplot as plt
import seaborn as sns
from sklearn.metrics import confusion_matrix

# Define the possible basketball actions
ACTIONS = [
    "Pick and Roll",
    "Pick and Pop",
    "Screen",
    "Pass",
    "Drive to the Basket",
    "Shoot a Three-pointer",
    "Cut to the Basket",
    "Post Up",
    "Isolation Play",
    "Fast Break"
]

# Define the positions on the basketball court
POSITIONS = [
    "Point Guard (PG)",
    "Shooting Guard (SG)",
    "Small Forward (SF)",
    "Power Forward (PF)",
    "Center (C)"
]

# Simulate a realistic dataset of basketball plays with offensive sequences
def generate_simulated_data(num_plays=30000):
    """
    Generates a simulated dataset of basketball plays with actions linked to positions.
    Each play is a sequence of 3-5 actions, and each action is associated with a position.
    """
    data = []
    for _ in range(num_plays):
        play_length = random.randint(3, 5)
        play = []
        for step in range(play_length):
            # Assign actions to positions based on realistic basketball scenarios
            position = POSITIONS[step % len(POSITIONS)]  
            if position == "Point Guard (PG)":
                action = random.choices(
                    ["Pick and Roll", "Pass", "Drive to the Basket", "Shoot a Three-pointer"],
                    weights=[10, 30, 30, 30],  
                    k=1
                )[0]
            elif position == "Shooting Guard (SG)":
                action = random.choices(
                    ["Shoot a Three-pointer", "Cut to the Basket", "Screen", "Pass"],
                    weights=[40, 20, 10, 30],  
                    k=1
                )[0]
            elif position == "Small Forward (SF)":
                action = random.choices(
                    ["Cut to the Basket", "Post Up", "Isolation Play", "Pass"],
                    weights=[25, 25, 25, 25], 
                    k=1
                )[0]
            elif position == "Power Forward (PF)":
                action = random.choices(
                    ["Pick and Pop", "Post Up", "Screen", "Pass"],
                    weights=[20, 30, 20, 30],  
                    k=1
                )[0]
            elif position == "Center (C)":
                action = random.choices(
                    ["Pick and Roll", "Post Up", "Screen", "Pass"],
                    weights=[20, 40, 10, 30],  
                    k=1
                )[0]
            play.append((position, action))
        data.append(play)
    return data

# Preprocess the data for training
def preprocess_data(data):
    """
    Converts the list of plays into numerical sequences and prepares them for training.
    """
    # Create dictionaries to map actions and positions to integers
    action_to_idx = {action: idx for idx, action in enumerate(ACTIONS)}
    position_to_idx = {position: idx for idx, position in enumerate(POSITIONS)}
    
    # Convert plays to numerical sequences
    numerical_data = []
    for play in data:
        numerical_play = [(position_to_idx[position], action_to_idx[action]) for position, action in play]
        numerical_data.append(numerical_play)
    
    # Pad sequences to ensure uniform length
    padded_data = pad_sequences(numerical_data, maxlen=5, padding='post', dtype='int32')
    
    # Prepare input (X) and output (y) for training
    X_position = padded_data[:, :-1, 0]  
    X_action = padded_data[:, :-1, 1]   
    y = padded_data[:, -1, 1]           
    
    # Convert y to one-hot encoding
    y = tf.keras.utils.to_categorical(y, num_classes=len(ACTIONS))
    
    return X_position, X_action, y, position_to_idx, action_to_idx

# Build the TensorFlow model with positions and actions as inputs
def build_model(input_shape, num_positions, num_actions):
    """
    Builds a neural network that takes both positions and actions as inputs.
    """
    # Input for positions
    position_input = Input(shape=(input_shape,), name="position_input")
    position_embedding = Embedding(input_dim=num_positions, output_dim=10)(position_input)
    
    # Input for actions
    action_input = Input(shape=(input_shape,), name="action_input")
    action_embedding = Embedding(input_dim=num_actions, output_dim=10)(action_input)
    
    # Concatenate position and action embeddings
    concatenated = Concatenate()([position_embedding, action_embedding])
    
    # LSTM layer
    lstm_out = LSTM(128, return_sequences=False, dropout=0.3)(concatenated)
    
    # Dense layers
    dense_out = Dense(128, activation='relu')(lstm_out)
    dense_out = Dropout(0.3)(dense_out)
    output = Dense(num_actions, activation='softmax')(dense_out)
    
    # Define the model
    model = Model(inputs=[position_input, action_input], outputs=output)
    model.compile(optimizer='adam', loss='categorical_crossentropy', metrics=['accuracy'])
    return model

# Generate a new play using the trained model
def generate_play(model, position_to_idx, action_to_idx, seed_play, max_length=5, temperature=1.0):
    """
    Generates a new basketball play using the trained model with temperature-based sampling.
    Higher temperature increases randomness.
    """
    idx_to_action = {idx: action for action, idx in action_to_idx.items()}
    idx_to_position = {idx: position for position, idx in position_to_idx.items()}
    
    # Convert seed play to numerical format
    seed_positions = [position_to_idx[position] for position, _ in seed_play]
    seed_actions = [action_to_idx[action] for _, action in seed_play]
    
    # Generate the play step by step
    for _ in range(max_length - len(seed_play)):
        padded_positions = pad_sequences([seed_positions], maxlen=max_length-1, padding='post')
        padded_actions = pad_sequences([seed_actions], maxlen=max_length-1, padding='post')
        
        # Predict the next action
        predicted_probabilities = model.predict([padded_positions, padded_actions], verbose=0)[0]
        
        # Apply temperature to the probabilities
        predicted_probabilities = np.log(predicted_probabilities) / temperature
        predicted_probabilities = np.exp(predicted_probabilities)
        predicted_probabilities = predicted_probabilities / np.sum(predicted_probabilities)
        
        # Sample the next action based on the adjusted probabilities
        predicted_action_idx = np.random.choice(len(ACTIONS), p=predicted_probabilities)
        
        # Assign the new action to the next position in the sequence
        new_position_idx = (len(seed_play) % len(POSITIONS))
        new_position = idx_to_position[new_position_idx]
        
        seed_positions.append(new_position_idx)
        seed_actions.append(predicted_action_idx)
        seed_play.append((new_position, idx_to_action[predicted_action_idx])) # Keep track of generated play
    
    # Convert the numerical sequence back to actions and positions
    generated_play = seed_play # Return the complete play including the seed
    return generated_play

# Visualize the distribution of actions in the dataset
def visualize_action_distribution(data):
    """
    Plots the distribution of actions in the dataset.
    """
    action_counts = {action: 0 for action in ACTIONS}
    for play in data:
        for _, action in play:
            action_counts[action] += 1
    
    plt.figure(figsize=(10, 6))
    plt.bar(action_counts.keys(), action_counts.values(), color='skyblue')
    plt.title("Distribution of Actions in the Dataset")
    plt.xlabel("Actions")
    plt.ylabel("Frequency")
    plt.xticks(rotation=45)
    plt.show()

# Visualize the accuracy and loss during training
def visualize_training_history(history):
    plt.figure(figsize=(12, 5))
    
    # Plot accuracy
    plt.subplot(1, 2, 1)
    plt.plot(history.history['accuracy'], label='Training Accuracy')
    plt.title('Training Accuracy')
    plt.xlabel('Epoch')
    plt.ylabel('Accuracy')
    plt.legend()
    
    # Plot loss
    plt.subplot(1, 2, 2)
    plt.plot(history.history['loss'], label='Training Loss', color='orange')
    plt.title('Training Loss')
    plt.xlabel('Epoch')
    plt.ylabel('Loss')
    plt.legend()
    
    plt.show()

# Visualize the confusion matrix
def visualize_confusion_matrix(y_true, y_pred, action_to_idx):
    # Convert predictions from one-hot encoding to class labels
    y_true_labels = np.argmax(y_true, axis=1)
    y_pred_labels = np.argmax(y_pred, axis=1)
    
    # Compute the confusion matrix
    cm = confusion_matrix(y_true_labels, y_pred_labels)
    
    # Plot the confusion matrix
    plt.figure(figsize=(10, 8))
    sns.heatmap(cm, annot=True, fmt='d', cmap='Blues', xticklabels=ACTIONS, yticklabels=ACTIONS)
    plt.title('Confusion Matrix')
    plt.xlabel('Predicted Actions')
    plt.ylabel('True Actions')
    plt.xticks(rotation=45)
    plt.yticks(rotation=0)
    plt.show()

# Main function to run the play generator
def main():
    # Step 1: Generate simulated data
    print("Generating simulated data...")
    data = generate_simulated_data(num_plays=30000)
    
    # Step 2: Visualize action distribution
    print("Visualizing action distribution...")
    visualize_action_distribution(data)
    
    # Step 3: Preprocess the data
    print("Preprocessing data...")
    X_position, X_action, y, position_to_idx, action_to_idx = preprocess_data(data)
    
    # Step 4: Build and train the model
    print("Building and training the model...")
    model = build_model(input_shape=X_position.shape[1], num_positions=len(POSITIONS), num_actions=len(ACTIONS))
    history = model.fit([X_position, X_action], y, epochs=50, batch_size=64, verbose=1)
    
    # Step 5: Visualize training history
    print("Visualizing training history...")
    visualize_training_history(history)
    
    # Step 6: Generate a new play
    print("\nGenerating a new basketball play...")
    seed_play = [("Point Guard (PG)", "Pick and Roll"), ("Shooting Guard (SG)", "Pass")]
    generated_play = generate_play(model, position_to_idx, action_to_idx, seed_play, temperature=1.0)
    
    # Display the generated play
    print("\nGenerated Basketball Play:")
    print("=".center(50, "="))
    for position, action in generated_play:
        print(f"{position}: {action}")
    print("=".center(50, "="))
    
    # Step 7: Visualize the confusion matrix
    print("\nVisualizing confusion matrix...")
    y_pred = model.predict([X_position, X_action])
    visualize_confusion_matrix(y, y_pred, action_to_idx)

# Run the program
if __name__ == "__main__":
    main()
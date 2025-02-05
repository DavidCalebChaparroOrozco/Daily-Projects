# Import necessary libraries
import numpy as np
import random
from tensorflow.keras.models import Sequential
from tensorflow.keras.layers import Dense
from tensorflow.keras.optimizers import Adam

# Define the maze dimensions and symbols
MAZE_SIZE = 9
START = 'S'
DESTINATION = 'D'
WALL = '#'
PATH = '.'
VISITED = '*'

# Generate a random maze
def generate_maze(size):
    maze = [[PATH for _ in range(size)] for _ in range(size)]
    # Add walls randomly
    for i in range(size):
        for j in range(size):
            if random.random() < 0.2:  # 20% chance of being a wall
                maze[i][j] = WALL
    # Set start and destination points
    maze[0][0] = START
    maze[size-1][size-1] = DESTINATION
    return maze

# Print the maze
def print_maze(maze):
    for row in maze:
        print(" ".join(row))

# Convert the maze to a numerical format for the neural network
def maze_to_input(maze):
    input_data = []
    for row in maze:
        for cell in row:
            if cell == START:
                input_data.append(0)  # Start
            elif cell == DESTINATION:
                input_data.append(1)  # Destination
            elif cell == WALL:
                input_data.append(2)  # Wall
            else:
                input_data.append(3)  # Path
    # Reshape to (1, 25)
    return np.array(input_data).reshape(1, -1)  

# Define the neural network model
def build_model(input_size):
    model = Sequential([
        Dense(64, activation='relu', input_shape=(input_size,)),  # Hidden layer
        Dense(64, activation='relu'),  # Hidden layer
        Dense(4, activation='softmax')  # Output layer (4 possible moves: up, down, left, right)
    ])
    model.compile(optimizer=Adam(), loss='categorical_crossentropy', metrics=['accuracy'])
    return model

# Train the neural network
def train_model(model, mazes, labels, epochs=10):
    # Convert mazes and labels to numpy arrays
    mazes = np.array(mazes).reshape(-1, MAZE_SIZE * MAZE_SIZE)  # Reshape to (num_samples, 25)
    labels = np.array(labels)
    model.fit(mazes, labels, epochs=epochs, verbose=1)

# Recursive pathfinding algorithm with Deep Learning integration
def find_path(maze, row, col, current_path, destination, visited, model):
    # Base case: if the destination is reached, return the current path
    if (row, col) == destination:
        return current_path + [(row, col)]
    
    # Mark the current cell as visited
    visited.add((row, col))
    
    # Predict the next move using the neural network
    input_data = maze_to_input(maze)
    predictions = model.predict(input_data, verbose=0)[0]
    
    # Possible moves: up, down, left, right
    moves = [(-1, 0), (1, 0), (0, -1), (0, 1)]
    
    # Sort moves based on the neural network's predictions (highest probability first)
    sorted_moves = [move for _, move in sorted(zip(predictions, moves), reverse=True)]
    
    # Explore the moves recursively
    for (dr, dc) in sorted_moves:
        new_row, new_col = row + dr, col + dc
        if (0 <= new_row < len(maze) and 
            0 <= new_col < len(maze[0]) and 
            maze[new_row][new_col] != WALL and 
            (new_row, new_col) not in visited):
            
            # Recursive call
            result = find_path(maze, new_row, new_col, 
                            current_path + [(row, col)], destination, visited, model)
            if result:
                return result
    
    # If no path is found, return None
    return None

# Main function
def main():
    # Generate a maze
    maze = generate_maze(MAZE_SIZE)
    print("Generated Maze:")
    print_maze(maze)
    
    # Define the start and destination points
    start = (0, 0)
    destination = (MAZE_SIZE-1, MAZE_SIZE-1)
    
    # Build and train the neural network
    input_size = MAZE_SIZE * MAZE_SIZE
    model = build_model(input_size)
    
    # Generate training data (mazes and their optimal paths)
    # Note: In a real-world scenario, this data would be pre-collected or generated using a solver.
    mazes = []
    labels = []
    for _ in range(100):  # Generate 100 training examples
        maze = generate_maze(MAZE_SIZE)
        mazes.append(maze_to_input(maze).flatten())  # Flatten to (25,)
        # Dummy labels for demonstration (replace with actual optimal paths)
        labels.append(np.random.rand(4))  # 4 possible moves
    
    # Train the model
    train_model(model, mazes, labels, epochs=10)
    
    # Find the path using the recursive algorithm with Deep Learning
    visited = set()
    path = find_path(maze, start[0], start[1], [], destination, visited, model)
    
    # Display the result
    if path:
        print("\nPath Found:")
        for (row, col) in path:
            if maze[row][col] != START and maze[row][col] != DESTINATION:
                maze[row][col] = VISITED
        print_maze(maze)
    else:
        print("\nNo Path Found.")

# Run the program
if __name__ == "__main__":
    main()
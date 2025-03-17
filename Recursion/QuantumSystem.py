# Importing necessary libraries
import random

# Define a class to represent the quantum system
class QuantumSystem:
    # Initialize the quantum system with a list of possible states.
    # Each state is represented as a tuple (state_name, probability).
    def __init__(self, states):
        self.states = states
        self.collapsed_state = None  # The state after collapse

    # Normalize the probabilities of the states so they sum to 1.
    def normalize_probabilities(self):
        total_probability = sum(prob for _, prob in self.states)
        self.states = [(state, prob / total_probability) for state, prob in self.states]

    # Simulate the collapse of the wave function into one of the possible states.
    # Uses recursion to explore the probability distribution.
    def collapse_wave_function(self):
        self.normalize_probabilities()  # Ensure probabilities are normalized
        self.collapsed_state = self._recursive_collapse(self.states, random.random())
        return self.collapsed_state

    # Recursively determine the collapsed state based on the random value and probabilities.
    def _recursive_collapse(self, states, random_value, index=0, accumulated_prob=0):
        if index >= len(states):
            raise ValueError("No state found for the given random value.")

        state, prob = states[index]
        accumulated_prob += prob

        # If the random value falls within the current probability range, return the state
        if random_value <= accumulated_prob:
            return state
        else:
            # Otherwise, continue to the next state
            return self._recursive_collapse(states, random_value, index + 1, accumulated_prob)

    # Return a string representation of the quantum system.
    def __str__(self):
        if self.collapsed_state is None:
            return "Quantum System (Uncollapsed): " + ", ".join([f"{state} ({prob:.2f})" for state, prob in self.states])
        else:
            return f"Quantum System (Collapsed): {self.collapsed_state}"


# Example usage
if __name__ == "__main__":
    # Define a quantum system with possible states and their probabilities
    states = [
        # State A with 30% probability
        ("State A", 0.3),  
        # State B with 50% probability
        ("State B", 0.5),  
        # State C with 20% probability
        ("State C", 0.2),  
    ]

    # Create a quantum system
    quantum_system = QuantumSystem(states)

    # Print the initial state of the system
    print("Initial Quantum System:")
    print(quantum_system)

    # Simulate the collapse of the wave function
    collapsed_state = quantum_system.collapse_wave_function()

    # Print the result after collapse
    print("\nAfter Wave Function Collapse:")
    print(quantum_system)
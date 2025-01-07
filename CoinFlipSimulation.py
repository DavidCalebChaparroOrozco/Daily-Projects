# Import necessary libraries
import matplotlib.pyplot as plt
import numpy as np

# Function to simulate coin flips recursively
def flip_coin(n, current_sequence="", results=None):
    if results is None:
        results = []
    
    # Base case: if n flips are done, add the sequence to results
    if n == 0:
        results.append(current_sequence)
        return results
    
    # Recursive case: flip the coin for heads (H) and tails (T)
    flip_coin(n - 1, current_sequence + "H", results)  # Add Heads
    flip_coin(n - 1, current_sequence + "T", results)  # Add Tails
    
    return results

# Function to count combinations with more heads or more tails
def count_combinations(sequences):
    more_heads = 0
    more_tails = 0
    
    for sequence in sequences:
        heads_count = sequence.count('H')
        tails_count = sequence.count('T')
        
        if heads_count > tails_count:
            more_heads += 1
        elif tails_count > heads_count:
            more_tails += 1
            
    return more_heads, more_tails

# Function to visualize the coin flips
def visualize_coin_flips(sequences):
    # Count heads and tails for visualization
    heads_counts = [seq.count('H') for seq in sequences]
    tails_counts = [seq.count('T') for seq in sequences]
    
    # Create a bar chart
    x = np.arange(len(sequences))
    
    plt.bar(x - 0.2, heads_counts, width=0.4, label='Heads', color='blue')
    plt.bar(x + 0.2, tails_counts, width=0.4, label='Tails', color='orange')
    
    plt.xlabel('Sequences')
    plt.ylabel('Count')
    plt.title('Coin Flip Simulation Results')
    plt.xticks(x, sequences)
    plt.legend()
    
    plt.show()

# Main function to execute the simulation
def main():
    n = int(input("Enter the number of coin flips: "))  # Number of flips
    sequences = flip_coin(n)  # Generate all sequences
    
    # Count combinations with more heads or tails
    more_heads, more_tails = count_combinations(sequences)
    
    print(f"Total sequences: {len(sequences)}")
    print(f"Combinations with more heads: {more_heads}")
    print(f"Combinations with more tails: {more_tails}")
    
    # Visualize the results
    visualize_coin_flips(sequences)

# Run the main function
if __name__ == "__main__":
    main()
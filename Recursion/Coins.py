# Generate all possible coin toss sequences using recursion.
def generate_coin_toss_sequences(n):
    """    
    Args:
        n: Number of coin tosses    
    Returns:
        list: All possible coin toss sequences
    """
    def recursive_toss(current_sequence, remaining_tosses):
        # Base case: if no more tosses remain, return the current sequence
        if remaining_tosses == 0:
            return [current_sequence]
        
        # Recursive cases: add 'H' (Heads) and 'T' (Tails)
        heads_sequence = recursive_toss(current_sequence + ['H'], remaining_tosses - 1)
        tails_sequence = recursive_toss(current_sequence + ['T'], remaining_tosses - 1)
        
        return heads_sequence + tails_sequence

    # Start the recursive generation with an empty sequence
    return recursive_toss([], n)

# Count sequences with more heads or more tails.
def count_unbalanced_sequences(sequences):
    """    
    Args:
        sequences (list): List of coin toss sequences    
    Returns:
        dict: Count of unbalanced sequences
    """
    unbalanced_count = {
        'more_heads': 0,
        'more_tails': 0
    }
    
    for sequence in sequences:
        heads_count = sequence.count('H')
        tails_count = sequence.count('T')
        
        if heads_count > tails_count:
            unbalanced_count['more_heads'] += 1
        elif tails_count > heads_count:
            unbalanced_count['more_tails'] += 1
    
    return unbalanced_count

def main():
    # Number of coin tosses
    n = 5
    
    # Generate all possible sequences
    sequences = generate_coin_toss_sequences(n)
    
    # Print total number of sequences
    print(f"Total sequences for {n} tosses: {len(sequences)}")
    
    # Print all sequences
    print("\nAll Sequences:")
    for seq in sequences:
        print(''.join(seq))
    
    # Count unbalanced sequences
    unbalanced_results = count_unbalanced_sequences(sequences)
    
    print("\nUnbalanced Sequence Analysis:")
    print(f"Sequences with more heads: {unbalanced_results['more_heads']}")
    print(f"Sequences with more tails: {unbalanced_results['more_tails']}")

if __name__ == "__main__":
    main()

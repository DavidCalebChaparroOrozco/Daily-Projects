# Generates all possible valid single-letter mutations from start_sequence to target_sequence.
def generate_mutations(start_sequence, target_sequence):
    """    
    Args:
        start_sequence: Initial DNA sequence (uppercase, only contains A, T, C, G)
        target_sequence: Target DNA sequence (same length as start_sequence)
    
    Returns:
        list: List of mutation paths from start to target sequence
    """
    
    # Validate input sequences
    if len(start_sequence) != len(target_sequence):
        raise ValueError("Start and target sequences must be of equal length")
    
    valid_nucleotides = {'A', 'T', 'C', 'G'}
    for seq in [start_sequence, target_sequence]:
        if not all(nucleotide in valid_nucleotides for nucleotide in seq):
            raise ValueError("Sequences can only contain A, T, C, G nucleotides")
    
    # If sequences are already the same
    if start_sequence == target_sequence:
        return [[start_sequence]]
    
    # Initialize variables for BFS (Breadth-First Search)
    from collections import deque
    queue = deque()
    queue.append([start_sequence])
    found_paths = []
    
    while queue:
        current_path = queue.popleft()
        last_sequence = current_path[-1]
        
        # Generate all possible next mutations
        for i in range(len(last_sequence)):
            if last_sequence[i] != target_sequence[i]:
                # Only mutate to the target nucleotide at this position
                mutated_sequence = (
                    last_sequence[:i] + target_sequence[i] + last_sequence[i+1:]
                )
                
                # Avoid cycles by checking if this sequence is already in the path
                if mutated_sequence not in current_path:
                    new_path = current_path.copy()
                    new_path.append(mutated_sequence)
                    
                    # Check if we've reached the target
                    if mutated_sequence == target_sequence:
                        found_paths.append(new_path)
                    else:
                        queue.append(new_path)
    
    return found_paths

# Prints all mutation paths in a readable format.
def print_mutation_paths(mutation_paths):
    """    
    Args:
        mutation_paths: List of mutation paths to print
    """
    if not mutation_paths:
        print("No valid mutation paths found.")
        return
    
    print(f"Found {len(mutation_paths)} possible mutation path(s):")
    for i, path in enumerate(mutation_paths, 1):
        print(f"\nPath {i}:")
        for step, sequence in enumerate(path):
            if step == 0:
                print(f"Start: {sequence}")
            else:
                # Highlight the changed nucleotide
                prev_seq = path[step-1]
                changed_pos = [j for j in range(len(sequence)) if sequence[j] != prev_seq[j]][0]
                highlighted = (
                    sequence[:changed_pos] + 
                    f"[{sequence[changed_pos]}]" + 
                    sequence[changed_pos+1:]
                )
                print(f"Step {step}: {highlighted} (changed position {changed_pos+1})")

def main():
    # Example sequences
    start_seq = "ATCG"
    target_seq = "GCTA"
    
    print(f"Generating mutations from {start_seq} to {target_seq}...\n")
    
    try:
        mutation_paths = generate_mutations(start_seq, target_seq)
        print_mutation_paths(mutation_paths)
    except ValueError as e:
        print(f"Error: {e}")

if __name__ == "__main__":
    main()
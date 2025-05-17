"""
The Hot Hand refers to the belief that a player who has made several successful shots 
in a row has a higher probability of making the next shot.

The program uses recursion to check for sequences of consecutive successful shots 
and determines if they exceed the expected probability.
"""

# Import necessary libraries
import random
from collections import defaultdict

# Generate a random sequence of shot outcomes (H for hit, M for miss).
def generate_shooting_sequence(length, success_prob):
    """    
    Parameters:
    length: Number of shots in the sequence
    success_prob: Probability of making a single shot (0 to 1)
    
    Returns:
    list: Sequence of 'H' and 'M' characters
    """
    return ['H' if random.random() < success_prob else 'M' for _ in range(length)]

# Recursively find all streaks of consecutive hits in a shot sequence.
def find_consecutive_hits(sequence, min_streak_length, current_streak=0, streaks=None):
    """    
    Parameters:
    sequence: Remaining shot sequence to analyze
    min_streak_length: Minimum streak length to count
    current_streak: Current streak length (used in recursion)
    streaks: List of found streaks (used in recursion)
    
    Returns:
    list: List of streak lengths that meet the minimum requirement
    """
    if streaks is None:
        streaks = []
    
    # Base case: empty sequence
    if not sequence:
        if current_streak >= min_streak_length:
            streaks.append(current_streak)
        return streaks
    
    current_shot = sequence[0]
    remaining_sequence = sequence[1:]
    
    if current_shot == 'H':
        # Continue the current streak
        return find_consecutive_hits(remaining_sequence, min_streak_length, current_streak + 1, streaks)
    else:
        # Streak ended
        if current_streak >= min_streak_length:
            streaks.append(current_streak)
        return find_consecutive_hits(remaining_sequence, min_streak_length, 0, streaks)

# Calculate the probability of making a shot after a streak of hits.
def calculate_streak_probability(sequence, streak_length):
    """    
    Parameters:
    sequence: Shot sequence to analyze
    streak_length: Length of streak to consider
    
    Returns:
    float: Probability of making next shot after streak
    """
    opportunities = 0
    successes = 0
    
    for i in range(len(sequence) - streak_length):
        # Check if we have a streak of the required length
        if all(shot == 'H' for shot in sequence[i:i+streak_length]):
            opportunities += 1
            if sequence[i+streak_length] == 'H':
                successes += 1
    
    return successes / opportunities if opportunities > 0 else 0.0

# Analyze a shot sequence for evidence of the Hot Hand effect.
def analyze_hot_hand(sequence, success_prob, min_streak_length=3):
    """    
    Parameters:
    sequence: Shot sequence to analyze
    success_prob: Baseline probability of making a shot
    min_streak_length: Minimum streak length to consider
    
    Returns:
    dict: Analysis results including streaks found and probabilities
    """
    results = {
        'total_shots': len(sequence),
        'success_prob': success_prob,
        'observed_success_rate': sequence.count('H') / len(sequence),
        'min_streak_length': min_streak_length,
        'streaks_found': [],
        'streak_probabilities': defaultdict(float)
    }
    
    # Find all streaks of the minimum length or longer
    streaks = find_consecutive_hits(sequence, min_streak_length)
    results['streaks_found'] = streaks
    
    # Calculate probabilities for different streak lengths
    for length in range(min_streak_length, min_streak_length + 3):
        if len(sequence) > length:
            prob = calculate_streak_probability(sequence, length)
            results['streak_probabilities'][length] = prob
    
    return results

# Print the results of the Hot Hand analysis in a readable format.
def print_analysis_results(results):
    print("\nHot Hand Effect Analysis")
    print("=".center(50, "="))
    print(f"Total shots: {results['total_shots']}")
    print(f"Expected success probability: {results['success_prob']:.2f}")
    print(f"Observed success rate: {results['observed_success_rate']:.2f}")
    print(f"\nMinimum streak length analyzed: {results['min_streak_length']}")
    print(f"Number of streaks found: {len(results['streaks_found'])}")
    if results['streaks_found']:
        print(f"Streak lengths: {sorted(results['streaks_found'], reverse=True)}")
    
    print("\nConditional Probabilities:")
    for length, prob in results['streak_probabilities'].items():
        print(f"After {length} hits: {prob:.2f} (Expected: {results['success_prob']:.2f})")
        if prob > results['success_prob']:
            print("  → Potential Hot Hand detected!")
        elif prob < results['success_prob']:
            print("  → Potential Cold Hand detected!")
        else:
            print("  → No significant effect detected.")

def main():
    # Simulation parameters

    # Number of shots in the sequence
    num_shots = 100       
    # Baseline probability of making a shot
    success_prob = 0.7
    # Minimum streak length to analyze
    min_streak = 3        
    
    # Generate a random shooting sequence
    print("Generating shot sequence...")
    shot_sequence = generate_shooting_sequence(num_shots, success_prob)
    print("Sample sequence:", ''.join(shot_sequence[:20]) + "...")
    
    # Analyze the sequence for Hot Hand effect
    results = analyze_hot_hand(shot_sequence, success_prob, min_streak)
    
    # Print the results
    print_analysis_results(results)

if __name__ == "__main__":
    main()
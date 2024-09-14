# Crossing the River Problem using recursion
# We have a boat, a farmer, a wolf, a goat, and a cabbage
# The goal is to get all of them across the river with constraints:
# - The wolf can't be left alone with the goat
# - The goat can't be left alone with the cabbage
# - Only two items can be in the boat at a time (including the farmer)

# Define the initial state of the riverbank
initial_state = {
    'left': ['farmer', 'wolf', 'goat', 'cabbage'],
    'right': []
}

# Function to check if the current state is valid (no illegal pairings)
def is_valid_state(state):
    left_bank = state['left']
    right_bank = state['right']
    
    # Check the left bank for illegal pairings
    if 'wolf' in left_bank and 'goat' in left_bank and 'farmer' not in left_bank:
        return False  # The wolf will eat the goat
    if 'goat' in left_bank and 'cabbage' in left_bank and 'farmer' not in left_bank:
        return False  # The goat will eat the cabbage
    
    # Check the right bank for illegal pairings
    if 'wolf' in right_bank and 'goat' in right_bank and 'farmer' not in right_bank:
        return False  # The wolf will eat the goat
    if 'goat' in right_bank and 'cabbage' in right_bank and 'farmer' not in right_bank:
        return False  # The goat will eat the cabbage
    
    return True

# Function to move items between the riverbanks
def move_item(state, item):
    new_state = {
        'left': state['left'].copy(),
        'right': state['right'].copy()
    }
    
    if 'farmer' in new_state['left']:  # Farmer is on the left bank
        new_state['left'].remove('farmer')
        new_state['right'].append('farmer')
        if item:
            new_state['left'].remove(item)
            new_state['right'].append(item)
    else:  # Farmer is on the right bank
        new_state['right'].remove('farmer')
        new_state['left'].append('farmer')
        if item:
            new_state['right'].remove(item)
            new_state['left'].append(item)
    
    return new_state

# Recursive function to solve the problem
def solve(state, path=[]):
    # Check if the goal has been reached (all items on the right bank)
    if set(state['right']) == {'farmer', 'wolf', 'goat', 'cabbage'}:
        return path + [state]
    
    # Check if the state is valid before proceeding
    if not is_valid_state(state):
        return None
    
    # Try all possible moves
    for item in [None, 'wolf', 'goat', 'cabbage']:
        # Skip if the item is not on the same side as the farmer
        if item and item not in state['left'] and 'farmer' in state['left']:
            continue
        if item and item not in state['right'] and 'farmer' in state['right']:
            continue
        
        # Move the farmer and possibly an item
        new_state = move_item(state, item)
        
        # Avoid revisiting the same state
        if new_state in path:
            continue
        
        # Recursively attempt to solve from the new state
        solution = solve(new_state, path + [state])
        if solution:
            return solution
    
    return None

# Main function to run the recursive solution
def main():
    solution_path = solve(initial_state)
    if solution_path:
        print("Solution found:")
        for step, state in enumerate(solution_path):
            print(f"Step {step + 1}: Left bank: {state['left']}, Right bank: {state['right']}")
    else:
        print("No solution found.")

# Execute the program
if __name__ == "__main__":
    main()

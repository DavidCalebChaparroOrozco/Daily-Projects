# Function to move a block from one position to another
def move_block(tower, from_pos, to_pos):
    block = tower[from_pos].pop()
    tower[to_pos].append(block)
    print(f"Move block {block} from {from_pos} to {to_pos}")

# Recursive function to build the tower
def build_tower(tower, n, from_pos, to_pos, aux_pos):
    # Base case: if only one block is left, move it to the target position
    if n == 1:
        move_block(tower, from_pos, to_pos)
        return
    
    # Move the top n-1 blocks from the initial position to the auxiliary position
    build_tower(tower, n-1, from_pos, aux_pos, to_pos)
    
    # Move the nth block to the target position
    move_block(tower, from_pos, to_pos)
    
    # Move the n-1 blocks from the auxiliary position to the target position
    build_tower(tower, n-1, aux_pos, to_pos, from_pos)

# Function to initiate the tower building process
def tower_of_babel(n):
    # Initialize the tower with n blocks in the first position
    tower = {0: list(range(n, 0, -1)), 1: [], 2: []}
    print("Initial tower state:", tower)
    
    # Start the recursive process to build the tower
    build_tower(tower, n, 0, 2, 1)
    
    # Final state of the tower
    print("Final tower state:", tower)

# Example of use:
tower_of_babel(4)

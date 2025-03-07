# Calculate the number of complete levels that can be formed in a pyramid
# given a certain number of blocks.

# Each level of the pyramid is a square, and the number of blocks required
# for a level is the square of its level number. For example:
# - Level 1: 1 block (1^2)
# - Level 2: 4 blocks (2^2)
# - Level 3: 9 blocks (3^2)
# - and so on...
def pyramid_levels(blocks):
    """
    Args:
        blocks: The total number of blocks available.

    Returns:
        int: The number of complete levels that can be formed.
    """
    # Initialize the level counter
    level = 0  
    while True:
        # Move to the next level
        level += 1  
        # Calculate blocks needed for the current level
        blocks_needed = level ** 2  
        if blocks >= blocks_needed:
            # Subtract the blocks used for this level
            blocks -= blocks_needed  
        else:
            # If not enough blocks, revert to the previous level
            level -= 1  
            break
    return level


# Draw a pyramid using ASCII art based on the number of levels.
def draw_pyramid(levels):
    """
    Args:
        levels: The number of levels in the pyramid.
    """
    for i in range(1, levels + 1):
        # Print spaces to center the blocks in the pyramid
        print(" " * (levels - i), end="")
        # Print the blocks for the current level
        print("[]" * i)


# Example usage
if __name__ == "__main__":
    # Input: Number of blocks
    blocks = int(input("Enter the number of blocks: "))
    
    # Calculate the number of complete levels
    levels = pyramid_levels(blocks)
    
    # Output the result
    print(f"Number of complete levels: {levels}")
    
    # Draw the pyramid
    if levels > 0:
        print("\nPyramid Structure:")
        draw_pyramid(levels)
    else:
        print("Not enough blocks to build a pyramid.")
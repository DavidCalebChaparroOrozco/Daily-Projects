# Import necessary libraries
from typing import List, Tuple, Set

# Simulate pouring from one jug to another
def pour(jugs: List[int], capacities: List[int], from_idx: int, to_idx: int) -> List[int]:
    new_jugs = jugs.copy()
    transfer_amount = min(jugs[from_idx], capacities[to_idx] - jugs[to_idx])
    new_jugs[from_idx] -= transfer_amount
    new_jugs[to_idx] += transfer_amount
    return new_jugs

# Recursive search for all valid combinations
def solve(jugs: List[int], capacities: List[int], target: int,
            visited: Set[Tuple[int]], path: List[List[int]], solutions: List[List[List[int]]]):

    state = tuple(jugs)
    if state in visited:
        return
    visited.add(state)

    # If any jug contains the target volume, store the current path
    if target in jugs:
        solutions.append(path.copy())
        return

    num_jugs = len(jugs)

    # Try pouring from every jug to every other jug
    for i in range(num_jugs):
        for j in range(num_jugs):
            if i != j and jugs[i] > 0 and jugs[j] < capacities[j]:
                next_state = pour(jugs, capacities, i, j)
                path.append(next_state)
                solve(next_state, capacities, target, visited, path, solutions)
                path.pop()

# Entry point to the liquid pouring puzzle
def liquid_pouring_puzzle(capacities: List[int], initial: List[int], target: int) -> List[List[List[int]]]:
    visited = set()
    solutions = []
    solve(initial, capacities, target, visited, [initial], solutions)
    return solutions

# Menu to allow user interaction
def show_menu():
    print("🔷 Liquid Pouring Puzzle 🔷")
    try:
        num_jugs = int(input("Enter the number of jugs: "))
        capacities = []
        initial = []

        for i in range(num_jugs):
            cap = int(input(f"Enter capacity for jug {i + 1}: "))
            capacities.append(cap)

        for i in range(num_jugs):
            init = int(input(f"Enter initial amount in jug {i + 1} (≤ {capacities[i]}): "))
            if init > capacities[i]:
                print("Initial amount cannot exceed capacity.")
                return
            initial.append(init)

        target = int(input("Enter the target volume to measure: "))

        print("\nSearching for all possible solutions...\n")
        solutions = liquid_pouring_puzzle(capacities, initial, target)

        if not solutions:
            print("❌ No solution found.")
        else:
            for idx, solution in enumerate(solutions, 1):
                print(f"\nSolution: {idx} ")
                for step in solution:
                    print(step)
    except ValueError:
        print("Please enter valid integer inputs.")

# Run the menu when script is executed
if __name__ == "__main__":
    show_menu()

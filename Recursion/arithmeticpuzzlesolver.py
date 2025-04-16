# Import necessary libraries
import matplotlib.pyplot as plt
from typing import List, Optional

# Recursive backtracking function to generate all permutations of digits without repetition
def generate_permutations(path: List[str], used: List[bool], digits: List[str], result: List[List[str]]):
    if len(path) == len(digits):
        result.append(path[:])
        return
    for i in range(len(digits)):
        if not used[i]:
            used[i] = True
            path.append(digits[i])
            generate_permutations(path, used, digits, result)
            path.pop()
            used[i] = False

# Function to evaluate the arithmetic expression
def evaluate_expression(numbers: List[str], pattern: str, operator: str) -> Optional[str]:
    try:
        parts = pattern.split(operator)
        if '=' not in parts[1]:
            return None
        left, right = parts[0], parts[1].split('=')[0]
        result = parts[1].split('=')[1]

        # Replace placeholders with actual numbers
        mapping = {}
        idx = 0
        for ch in pattern:
            if ch.isalpha() and ch not in mapping:
                mapping[ch] = numbers[idx]
                idx += 1

        def map_str(s):
            return int(''.join(mapping[c] for c in s))

        A = map_str(left)
        B = map_str(right)
        C = map_str(result)

        # Perform the operation
        if operator == '+':
            return f"{A} + {B} = {C}" if A + B == C else None
        elif operator == '-':
            return f"{A} - {B} = {C}" if A - B == C else None
        elif operator == '*':
            return f"{A} * {B} = {C}" if A * B == C else None
        elif operator == '/':
            return f"{A} / {B} = {C}" if B != 0 and A / B == C else None
        elif operator == '//':
            return f"{A} // {B} = {C}" if B != 0 and A // B == C else None
    except:
        return None
    return None

# Function to solve the arithmetic puzzle given a pattern and operator
def solve_arithmetic_puzzle(pattern: str, operator: str):
    # Extract unique letters from the pattern
    letters = sorted(set([c for c in pattern if c.isalpha()]))
    if len(letters) > 9:
        print("Too many unique letters (max 9).")
        return

    digits = ['1','2','3','4','5','6','7','8','9']
    permutations = []
    generate_permutations([], [False]*len(digits), digits, permutations)

    for p in permutations:
        result = evaluate_expression(p, pattern, operator)
        if result:
            print(f"Solution Found: {result}")
            return

    print("No solution found.")

# Visualization of dummy data showing number of solutions per operator type
def plot_operator_solution_frequency():
    operators = ['+', '-', '*', '/', '//']
    # Example dummy data
    solutions_found = [3, 1, 2, 0, 1]  

    plt.figure(figsize=(8, 5))
    plt.bar(operators, solutions_found, color='skyblue')
    plt.title('Number of Solutions Found by Operator Type')
    plt.xlabel('Operator')
    plt.ylabel('Solutions Found')
    plt.grid(axis='y', linestyle='--', alpha=0.7)
    plt.tight_layout()
    plt.show()

# User CLI interface
def user_interface():
    print("Arithmetic Puzzle Solver")
    print("Enter the pattern using uppercase letters and an operator (e.g., ABC+DEF=GHI)")
    pattern = input("Enter the pattern: ").strip()
    operator = input("Enter the operator (+, -, *, /, //): ").strip()

    if operator not in ['+', '-', '*', '/', '//']:
        print("Invalid operator.")
        return

    solve_arithmetic_puzzle(pattern, operator)
    plot_operator_solution_frequency()

if __name__ == "__main__":
    user_interface()

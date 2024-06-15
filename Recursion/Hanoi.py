# Function to solve the Tower of Hanoi problem.
def hanoi(n, source, target, auxiliary):
    # Base case: if there is only one disk, move it directly.
    if n == 1:
        print(f"Move disk 1 from {source} to {target}")
        return
    # Recursively move n-1 disks from the source to the auxiliary.
    hanoi(n-1, source, auxiliary, target)
    # Move the nth disk from the source to the target.
    print(f"Move disk {n} from {source} to {target}")
    # Recursively move the n-1 disks from the auxiliary to the target.
    hanoi(n-1, auxiliary, target, source)

# Example of use:
n = 7 # Number of disks
hanoi(n, 'A', 'C', 'B')
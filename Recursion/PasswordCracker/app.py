# Import necessary libraries
import itertools
import time

class PasswordCracker:
    # Initialize the password cracker with character set and constraints.
    def __init__(self, charset, max_length, prefix="", suffix=""):
        """    
        Args:
            charset: Characters to use in combinations (e.g., "abc123")
            max_length: Maximum password length to attempt
            prefix: Known prefix of the password (if any)
            suffix: Known suffix of the password (if any)
        """
        self.charset = charset
        self.max_length = max_length
        self.prefix = prefix
        self.suffix = suffix
        self.attempts = 0
        self.found = False
        self.password = None

    # Check if the candidate matches the known constraints (prefix/suffix).
    # This is where we implement intelligent pruning.
    def is_possible_password(self, candidate):
        """    
        Args:
            candidate: The generated password candidate
            
        Returns:
            bool: True if candidate matches known constraints
        """
        # Check prefix match (early pruning)
        if self.prefix and not candidate.startswith(self.prefix):
            return False
            
        # Check suffix match (only when candidate is long enough)
        if self.suffix and len(candidate) >= len(self.suffix):
            if not candidate.endswith(self.suffix):
                return False
        return True

    # Recursive function to generate and test password combinations.
    def crack_recursive(self, current, target_length, check_password_callback):
        """    
        Args:
            current: Current string being built
            target_length: Desired password length
            check_password_callback (function): Function to test if password is correct
        """
        # Base case: if we've reached the target length
        if len(current) == target_length:
            self.attempts += 1
            
            # Check if this candidate matches all constraints
            if self.is_possible_password(current):
                if check_password_callback(current):
                    self.found = True
                    self.password = current
            return
            
        # Recursive case: build longer combinations
        for char in self.charset:
            if self.found:  # Early exit if password found
                return
                
            new_current = current + char
            
            # Prune the search tree if the current path can't possibly be valid
            if self.is_possible_password(new_current):
                self.crack_recursive(new_current, target_length, check_password_callback)

    # Main cracking method that tries passwords of increasing lengths.
    def crack(self, check_password_callback):
        """    
        Args:
            check_password_callback (function): Function that returns True if password is correct
            
        Returns:
            tuple: (found_password, attempts_made) or (None, attempts_made) if not found
        """
        start_time = time.time()
        
        # Try all lengths up to max_length
        for length in range(1, self.max_length + 1):
            if self.found:
                break
                
            # Only try lengths that make sense with prefix/suffix
            min_needed_length = len(self.prefix) + len(self.suffix)
            if min_needed_length > 0 and length < min_needed_length:
                continue
                
            self.crack_recursive("", length, check_password_callback)
        
        end_time = time.time()
        print(f"Cracking completed in {end_time - start_time:.2f} seconds")
        print(f"Total attempts: {self.attempts}")
        
        return self.password if self.found else None, self.attempts

# Example usage
if __name__ == "__main__":
    # Simulated password checker 
    def simulate_password_check(guess):
        # This is just for demonstration - in reality, you'd check against a real system
        real_password = "a1b2"
        return guess == real_password

    # Define the character set to use (could include letters, numbers, symbols)
    charset = "abcdefghijklmnopqrstuvwxyz0123456789"
    
    # Create cracker instance with constraints
    cracker = PasswordCracker(
        charset=charset,
        max_length=4,
        # We "know" the password starts with 'a'
        prefix="a",  
        # No known suffix in this example
        suffix=""     
    )
    
    # Start the cracking process
    password, attempts = cracker.crack(simulate_password_check)
    
    if password:
        print(f"Password found: {password} after {attempts} attempts")
    else:
        print(f"Password not found after {attempts} attempts")

    # More complex example with prefix and suffix
    print("\nTrying more complex example with prefix and suffix...")
    
    def simulate_complex_check(guess):
        real_password = "david!"
        return guess == real_password
    
    cracker = PasswordCracker(
        charset="abcdefghijklmnopqrstuvwxyz0123456789!@#$",
        max_length=10,
        # We "know" it starts with 'admin'
        prefix="admin",  
        # And ends with '!'
        suffix="!"       
    )
    
    password, attempts = cracker.crack(simulate_complex_check)
    
    if password:
        print(f"Password found: {password} after {attempts} attempts")
    else:
        print(f"Password not found after {attempts} attempts")
# Import necessary libraries
import random

# Implementation of Shamir's Secret Sharing scheme
class ShamirSecretSharing:
    """
    Implements Shamir's Secret Sharing algorithm which allows
    splitting a secret into multiple shares and reconstructing it from a subset.
    """
    # Initialize the scheme with a large prime number.
    def __init__(self, prime: int = 2**127 - 1):
        """
        Default is 2^127 - 1 (a Mersenne prime) which is large enough for most purposes.
        """
        self.prime = prime
    
    # Evaluates a polynomial at point x using Horner's method.
    @staticmethod
    def _evaluate_polynomial(coefficients: list, x: int, prime: int) -> int:
        """
        coefficients: List of polynomial coefficients [a0, a1, ..., ak]
        x: Point at which to evaluate the polynomial
        prime: Prime number for modulo operation
        Returns: Polynomial value at x (mod prime)
        """
        result = 0
        for coefficient in reversed(coefficients):
            result = (result * x + coefficient) % prime
        return result
    
    # Splits a secret into n shares with threshold k.
    def split_secret(self, secret: int, n: int, k: int) -> list:
        """
        secret: The secret number to split
        n: Total number of shares to generate
        k: Minimum number of shares required to reconstruct
        Returns: List of tuples (x, y) representing the shares
        """
        if k > n:
            raise ValueError("k must be less than or equal to n")
        if secret >= self.prime:
            raise ValueError("Secret must be smaller than the prime number")
        
        # Generate random coefficients for the polynomial (degree k-1)
        coefficients = [secret] + [random.randint(1, self.prime - 1) for _ in range(k - 1)]
        shares = []
        
        # Generate shares by evaluating the polynomial at points 1..n
        for x in range(1, n + 1):
            y = self._evaluate_polynomial(coefficients, x, self.prime)
            shares.append((x, y))
        
        return shares
    
    # Reconstructs the original secret from given shares using Lagrange interpolation.
    def reconstruct_secret(self, shares: list) -> int:
        """
        shares: List of share tuples (x, y)
        Returns: Reconstructed secret number
        """
        if not shares:
            raise ValueError("No shares provided")
        
        secret = 0
        x_values = [x for x, y in shares]
        
        # Perform Lagrange interpolation
        for i, (xi, yi) in enumerate(shares):
            numerator = 1
            denominator = 1
            
            # Calculate the Lagrange basis polynomial
            for j, (xj, _) in enumerate(shares):
                if i != j:
                    numerator = (numerator * (-xj)) % self.prime
                    denominator = (denominator * (xi - xj)) % self.prime
            
            # Compute the Lagrange coefficient and add its contribution
            lagrange_coeff = (numerator * pow(denominator, -1, self.prime)) % self.prime
            secret = (secret + yi * lagrange_coeff) % self.prime
        
        return secret


# Interactive menu system for Shamir's Secret Sharing operations
class ShamirSecretSharingMenu:
    """
    A menu-driven interface for interacting with the Shamir's Secret Sharing implementation.
    Provides options to split secrets, reconstruct them, and view shares.
    """
    def __init__(self):
        """Initialize the menu system with a new ShamirSecretSharing instance"""
        self.scheme = ShamirSecretSharing()
        self.current_shares = []  # Stores the currently generated shares
        self.current_secret = None  # Stores the original secret for verification
    
    # Displays the main menu options
    @staticmethod
    def display_menu():
        print("\nShamir's Secret Sharing System by David Caleb")
        print("1. Split a secret into shares")
        print("2. Reconstruct secret from shares")
        print("3. View current shares")
        print("4. Generate demo example")
        print("5. Exit")
    
    def run(self):
        while True:
            self.display_menu()
            choice = input("Enter your choice (1-5): ")
            
            if choice == "1":
                self.split_secret_menu()
            elif choice == "2":
                self.reconstruct_secret_menu()
            elif choice == "3":
                self.view_shares_menu()
            elif choice == "4":
                self.generate_demo_menu()
            elif choice == "5":
                print("Exiting the program. Goodbye!")
                break
            else:
                print("Invalid choice. Please enter a number between 1 and 5.")
    
    # Handles the secret splitting operation
    def split_secret_menu(self):
        print("\nSplit Secret ")
        try:
            # Get user input for secret splitting
            secret = int(input("Enter the secret number: "))
            n = int(input("Enter total number of shares to create: "))
            k = int(input("Enter minimum shares needed for reconstruction: "))
            
            if k > n:
                print("Error: Minimum shares needed cannot be greater than total shares.")
                return
            
            # Generate and store shares
            self.current_shares = self.scheme.split_secret(secret, n, k)
            self.current_secret = secret
            print(f"\nSuccessfully generated {n} shares. At least {k} shares are needed for reconstruction.")
        except ValueError:
            print("Invalid input. Please enter integers only.")
    
    # Handles the secret reconstruction operation
    def reconstruct_secret_menu(self):
        print("\nReconstruct Secret ")
        
        if not self.current_shares:
            print("No shares available. Please split a secret first or generate a demo.")
            return
        
        # Display available shares
        print(f"Available shares (total {len(self.current_shares)}):")
        for idx, (x, y) in enumerate(self.current_shares, 1):
            print(f"{idx}. Share {x}: {y}")
        
        try:
            # Get user input for which shares to use
            selected_indices = input("\nEnter the indices of shares to use (comma-separated, e.g. 1,3,5): ")
            indices = [int(i.strip()) - 1 for i in selected_indices.split(",")]
            
            # Reconstruct the secret
            selected_shares = [self.current_shares[i] for i in indices]
            secret = self.scheme.reconstruct_secret(selected_shares)
            
            # Display results and verify against original secret if available
            print(f"\nReconstructed secret: {secret}")
            if self.current_secret and secret == self.current_secret:
                print("Verification: This matches the original secret!")
            elif self.current_secret:
                print("Warning: This doesn't match the original secret (or none was stored).")
        except (ValueError, IndexError):
            print("Invalid selection. Please enter valid share indices.")
    
    # Displays all currently stored shares
    def view_shares_menu(self):
        print("\nCurrent Shares ")
        if not self.current_shares:
            print("No shares currently stored.")
            return
        
        # Print all shares
        for x, y in self.current_shares:
            print(f"Share {x}: {y}")
        
        # Print original secret if available
        if self.current_secret:
            print(f"\nOriginal secret (for verification): {self.current_secret}")
    
    # Generates a demonstration example with preset values
    def generate_demo_menu(self):
        print("\nDemo Example ")
        demo_secret = 42
        n = 4
        k = 2
        
        # Generate demo shares
        self.current_shares = self.scheme.split_secret(demo_secret, n, k)
        self.current_secret = demo_secret
        
        print(f"Generated demo with secret={demo_secret}, {n} shares, and threshold={k}.")
        print("Now you can try reconstructing the secret with different share combinations.")


if __name__ == "__main__":
    # Create and run the menu interface
    menu = ShamirSecretSharingMenu()
    menu.run()
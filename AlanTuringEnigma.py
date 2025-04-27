# Represents a single rotor in the Enigma machine with specific wiring and rotation behavior
class Rotor:
    
    # Initialize a rotor with specific wiring and notch position
    def __init__(self, wiring, notch):
        """        
        Args:
            wiring: The wiring configuration (e.g., 'EKMFLGDQVZNTOWYHXUSPAIBRCJ')
            notch: The turnover position where it causes the next rotor to rotate (e.g., 'Q')
        """
        self.wiring = wiring
        self.notch = notch
        # Current rotation position (0-25 representing A-Z)
        self.position = 0  
        self.alphabet = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
        
    # Encrypt a character in the forward direction (right to left through rotors)
    def forward(self, char):
        """
        Args:
            char: Single character to encrypt
        """
        index = (self.alphabet.index(char) + self.position) % 26
        encrypted_char = self.wiring[index]
        return self.alphabet[(self.alphabet.index(encrypted_char) - self.position) % 26]
    
    # Encrypt a character in the backward direction (after reflection)
    def backward(self, char):
        """        
        Args:
            char: Single character to encrypt            
        """
        index = (self.alphabet.index(char) + self.position) % 26
        encrypted_char = self.alphabet[self.wiring.index(self.alphabet[index])]
        return self.alphabet[(self.alphabet.index(encrypted_char) - self.position) % 26]
    
    # Rotate the rotor by one position and check if next rotor should rotate
    def rotate(self):
        self.position = (self.position + 1) % 26
        return self.position == self.alphabet.index(self.notch)

# Represents the fixed reflector that bounces the signal back through the rotors
class Reflector:
    
    # Initialize the reflector with specific wiring
    def __init__(self, wiring):
        """    
        Args:
            wiring: The fixed wiring configuration (e.g., 'YRUHQSLDPXNGOKMIEBFZCWVJAT')
        """
        self.wiring = wiring
        self.alphabet = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
        
    # Reflect a character back through the rotors using fixed wiring
    def reflect(self, char):
        """        
        Args:
            char: Character to reflect
        """
        return self.wiring[self.alphabet.index(char)]

# Represents the plugboard that swaps pairs of letters before and after rotor processing
class Plugboard:
    # Initialize the plugboard with letter pairs to swap
    def __init__(self, pairs):
        """    
        Args:
            pairs: List of letter pairs to swap (e.g., ['AB', 'CD'])
        """
        self.mapping = {}
        # Create a bidirectional mapping for each pair
        for pair in pairs:
            if len(pair) == 2:  # Ensure valid pair
                a, b = pair[0].upper(), pair[1].upper()
                self.mapping[a] = b
                self.mapping[b] = a
                
    # Swap characters according to plugboard settings if configured
    def swap(self, char):
        """    
        Args:
            char: Character to potentially swap
        """
        return self.mapping.get(char.upper(), char.upper())

# Main class representing the complete Enigma machine with user interface
class EnigmaMachine:    
    def __init__(self):
        """Initialize the Enigma machine with default settings"""
        # Historical rotor wirings (simplified)
        self.ROTOR_I = 'EKMFLGDQVZNTOWYHXUSPAIBRCJ'
        self.ROTOR_II = 'AJDKSIRUXBLHWTMCQGZNPYFVOE'
        self.ROTOR_III = 'BDFHJLCPRTXVZNYEIWGAKMUSQO'
        
        # Historical reflector wiring
        self.REFLECTOR_B = 'YRUHQSLDPXNGOKMIEBFZCWVJAT'
        
        # Initialize components with default settings
        self.rotor1 = Rotor(self.ROTOR_I, 'Q')
        self.rotor2 = Rotor(self.ROTOR_II, 'E')
        self.rotor3 = Rotor(self.ROTOR_III, 'V')
        self.reflector = Reflector(self.REFLECTOR_B)
        # Empty plugboard by default
        self.plugboard = Plugboard([])  
        
        # Current machine state
        self.message_history = []
    
    # Display the main menu and get user selection
    def display_main_menu(self):
        """    
        Returns:
            str: User's menu selection
        """
        print("\nAlan Turing's Enigma Machine Simulator by David Caleb")
        print("1. Configure Rotor Settings")
        print("2. Configure Plugboard")
        print("3. Encrypt/Decrypt Message")
        print("4. View Message History")
        print("5. Reset Machine Settings")
        print("6. Exit")
        return input("Please select an option (1-6): ")
    
    # Display rotor configuration menu and handle user input
    def display_rotor_menu(self):
        while True:
            print("\n Rotor Configuration ")
            print(f"Current Positions: Rotor1={chr(65+self.rotor1.position)}, "
                    f"Rotor2={chr(65+self.rotor2.position)}, "
                    f"Rotor3={chr(65+self.rotor3.position)}")
            print("1. Set Rotor Starting Positions")
            print("2. View Rotor Wiring")
            print("3. Return to Main Menu")
            choice = input("Select option (1-3): ")
            
            if choice == '1':
                self.set_rotor_positions()
            elif choice == '2':
                self.view_rotor_wiring()
            elif choice == '3':
                break
            else:
                print("Invalid option. Please try again.")
    
    # Set the initial positions for all three rotors
    def set_rotor_positions(self):
        print("\nSet Rotor Starting Positions (A-Z):")
        try:
            pos1 = input("Enter position for Rotor 1 (A-Z): ").upper()
            pos2 = input("Enter position for Rotor 2 (A-Z): ").upper()
            pos3 = input("Enter position for Rotor 3 (A-Z): ").upper()
            
            if len(pos1) == 1 and pos1 in 'ABCDEFGHIJKLMNOPQRSTUVWXYZ':
                self.rotor1.position = ord(pos1) - ord('A')
            if len(pos2) == 1 and pos2 in 'ABCDEFGHIJKLMNOPQRSTUVWXYZ':
                self.rotor2.position = ord(pos2) - ord('A')
            if len(pos3) == 1 and pos3 in 'ABCDEFGHIJKLMNOPQRSTUVWXYZ':
                self.rotor3.position = ord(pos3) - ord('A')
                
            print("Rotor positions updated successfully.")
        except:
            print("Invalid input. Positions must be single letters A-Z.")
    
    # Display the wiring configuration of all rotors
    def view_rotor_wiring(self):
        print("\nRotor Wiring Configurations:")
        print(f"Rotor I:  {self.ROTOR_I}")
        print(f"Rotor II: {self.ROTOR_II}")
        print(f"Rotor III: {self.ROTOR_III}")
        print("\nNote: These are historical wiring configurations and cannot be modified.")
    
    # Configure the plugboard connections
    def configure_plugboard(self):
        print("\nPlugboard Configuration")
        print("Current connections:", [f"{k}<->{v}" for k,v in self.plugboard.mapping.items() if k < v])
        print("Enter letter pairs to swap (e.g., AB CD EF), or 'clear' to reset:")
        user_input = input("> ").upper()
        
        if user_input.strip() == 'CLEAR':
            self.plugboard = Plugboard([])
            print("Plugboard connections cleared.")
        else:
            # Validate input and create pairs
            pairs = []
            valid = True
            for pair in user_input.split():
                if len(pair) == 2 and pair[0] in 'ABCDEFGHIJKLMNOPQRSTUVWXYZ' and pair[1] in 'ABCDEFGHIJKLMNOPQRSTUVWXYZ':
                    pairs.append(pair)
                else:
                    valid = False
                    break
            
            if valid:
                self.plugboard = Plugboard(pairs)
                print(f"Plugboard updated with {len(pairs)} connections.")
            else:
                print("Invalid input. Each connection must be two distinct letters (e.g., AB CD).")
    
    # Encrypt or decrypt a message using the current Enigma settings
    def encrypt_message(self, message):
        """
        Args:
            message: The message to process
        """
        encrypted = []
        for char in message.upper():
            if char in 'ABCDEFGHIJKLMNOPQRSTUVWXYZ':
                # Rotate rotors before processing each character
                rotate_next = True
                for i in [2, 1, 0]:  
                    # Right to left (rotor3, rotor2, rotor1)
                    if rotate_next:
                        rotate_next = self.rotors[i].rotate()
                        # Handle double-stepping anomaly
                        if i > 0 and self.rotors[i-1].notch == self.rotors[i-1].alphabet[self.rotors[i-1].position]:
                            rotate_next = True
                
                # Pass through plugboard
                char = self.plugboard.swap(char)
                
                # Pass through rotors right to left
                for rotor in reversed(self.rotors):
                    char = rotor.forward(char)
                
                # Pass through reflector
                char = self.reflector.reflect(char)
                
                # Pass back through rotors left to right
                for rotor in self.rotors:
                    char = rotor.backward(char)
                
                # Pass back through plugboard
                char = self.plugboard.swap(char)
                
                encrypted.append(char)
            else:
                # Non-alphabetic characters pass through unchanged
                encrypted.append(char)
        
        return ''.join(encrypted)
    
    # Handle message encryption/decryption through user interface
    def process_message(self):
        print("\n Message Processing")
        print("Note: The same process encrypts and decrypts when using the same settings")
        message = input("Enter message to process: ")
        
        # Store original settings to reset after processing
        original_positions = [self.rotor1.position, self.rotor2.position, self.rotor3.position]
        
        # Process the message
        result = self.encrypt_message(message)
        
        # Display results
        print("\nProcessing Results:")
        print(f"Original: {message}")
        print(f"Result:   {result}")
        
        # Add to history
        self.message_history.append({
            'original': message,
            'processed': result,
            'settings': {
                'rotor_positions': [chr(p + ord('A')) for p in original_positions],
                'plugboard': [f"{k}<->{v}" for k,v in self.plugboard.mapping.items() if k < v]
            }
        })
        
        # Reset rotor positions to original state
        self.rotor1.position, self.rotor2.position, self.rotor3.position = original_positions
    
    # Display previous message processing history
    def view_history(self):
        print("\nMessage History ")
        if not self.message_history:
            print("No messages processed yet.")
            return
        
        for i, entry in enumerate(self.message_history, 1):
            print(f"\nEntry {i}:")
            print(f"Original: {entry['original']}")
            print(f"Processed: {entry['processed']}")
            print(f"Settings: Rotors={entry['settings']['rotor_positions']}, "
                    f"Plugboard={entry['settings']['plugboard']}")
    
    # Reset all machine settings to defaults
    def reset_settings(self):
        self.rotor1.position = 0
        self.rotor2.position = 0
        self.rotor3.position = 0
        self.plugboard = Plugboard([])
        print("\nAll settings reset to defaults:")
        print("Rotor positions: A A A")
        print("Plugboard: No connections")
    
    # Main execution loop for the Enigma machine interface
    def run(self):
        print("Welcome to Alan Turing's Enigma Machine Simulator")
        print("This simulator demonstrates how the WWII Enigma machine worked")
        
        # Initialize rotors list for easy access
        self.rotors = [self.rotor1, self.rotor2, self.rotor3]
        
        while True:
            choice = self.display_main_menu()
            
            if choice == '1':
                self.display_rotor_menu()
            elif choice == '2':
                self.configure_plugboard()
            elif choice == '3':
                self.process_message()
            elif choice == '4':
                self.view_history()
            elif choice == '5':
                self.reset_settings()
            elif choice == '6':
                print("\nThank you for using the Enigma Machine Simulator. Goodbye!")
                break
            else:
                print("Invalid selection. Please choose 1-6.")

# Run the program
if __name__ == "__main__":
    enigma = EnigmaMachine()
    enigma.run()
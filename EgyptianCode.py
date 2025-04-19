# Extended hieroglyph dictionary using Unicode Egyptian Hieroglyphs block
HIEROGLYPH_DICT = {
    # Uppercase letters
    'A': '\U00013000',  
    'B': '\U00013001',
    'C': '\U00013002',
    'D': '\U00013003',
    'E': '\U00013004',
    'F': '\U00013005',
    'G': '\U00013006',
    'H': '\U00013007',
    'I': '\U00013008',
    'J': '\U00013009',
    'K': '\U0001300A',
    'L': '\U0001300B',
    'M': '\U0001300C',
    'N': '\U0001300D',
    'O': '\U0001300E',
    'P': '\U0001300F',
    'Q': '\U00013010',
    'R': '\U00013011',
    'S': '\U00013012',
    'T': '\U00013013',
    'U': '\U00013014',
    'V': '\U00013015',
    'W': '\U00013016',
    'X': '\U00013017',
    'Y': '\U00013018',
    'Z': '\U00013019',
    
    # Numbers
    '0': '\U0001301A',
    '1': '\U0001301B',
    '2': '\U0001301C',
    '3': '\U0001301D',
    '4': '\U0001301E',
    '5': '\U0001301F',
    '6': '\U00013020',
    '7': '\U00013021',
    '8': '\U00013022',
    '9': '\U00013023',
    
    # Punctuation
    '.': '\U00013024',
    ',': '\U00013025',
    '!': '\U00013026',
    '?': '\U00013027',
    "'": '\U00013028',
    '"': '\U00013029',
    
    # Space
    ' ': ' ',
    
    # Default fallback character (unknown)
    '?': '\U0001302A'
}

# Create the reverse dictionary for decoding
REVERSE_HIEROGLYPH_DICT = {v: k for k, v in HIEROGLYPH_DICT.items()}

# Convert a plain message into hieroglyphs using substitution cipher.
def encode_message(message):
    """    
    Args:
        message (str): The text to be encoded
        
    Returns:
        str: The encoded hieroglyphic message
    """
    encoded = []
    for char in message.upper():
        # Use the character if found in dictionary, otherwise use fallback
        encoded_char = HIEROGLYPH_DICT.get(char, HIEROGLYPH_DICT['?'])
        encoded.append(encoded_char)
    return ''.join(encoded)

# Convert a hieroglyphic message back to readable text.
def decode_message(encoded_message):
    """    
    Args:
        encoded_message (str): The hieroglyphic message to decode
        
    Returns:
        str: The decoded plain text message
    """
    decoded = []
    for symbol in encoded_message:
        # Use the reverse lookup with fallback for unknown symbols
        decoded_char = REVERSE_HIEROGLYPH_DICT.get(symbol, '?')
        decoded.append(decoded_char)
    return ''.join(decoded)

# Display a reference chart of available hieroglyphs and their meanings.
def display_hieroglyph_chart():
    print("\nHieroglyph Reference Chart:")
    print("=" * 40)
    print("{:<10} {:<5} {:<20}".format("Character", "Glyph", "Unicode"))
    print("-" * 40)
    
    for char, glyph in sorted(HIEROGLYPH_DICT.items()):
        if char == ' ':  # Skip space
            continue
        print("{:<10} {:<5} {:<20}".format(
            repr(char)[1:-1],  # Remove quotes
            glyph,
            f"U+{ord(glyph):04X}" if glyph != ' ' else 'Space'
        ))
    print("=" * 40)

# Display the interactive menu for the Egyptian Code Book system.
def menu():
    # Handles user input and program flow.
    print("\n" + "🔐" * 10)
    print(" Egyptian Code Book ".center(20, '𓁹'))
    print("🔐" * 10)
    
    while True:
        print("\nMain Menu:")
        print("1. Encode a message")
        print("2. Decode a message")
        print("3. View hieroglyph chart")
        print("4. Exit")
        
        choice = input("\nEnter your choice (1-4): ").strip()
        
        if choice == '1':
            print("\nEncode Mode")
            print("=".center(20, '='))
            text = input("Enter your message to encode:\n> ")
            if not text:
                print("Error: Empty input")
                continue
                
            encoded = encode_message(text)
            print("\nEncoded Hieroglyphs:")
            print(encoded)
            
            # Offer to copy to clipboard if pyperclip is available
            try:
                import pyperclip
                pyperclip.copy(encoded)
                print("\n(Copied to clipboard!)")
            except ImportError:
                pass
            
        elif choice == '2':
            print("\nDecode Mode")
            print("=".center(20, '='))
            encoded_text = input("Enter hieroglyphic message to decode:\n> ")
            if not encoded_text:
                print("Error: Empty input")
                continue
                
            decoded = decode_message(encoded_text)
            print("\nDecoded Message:")
            print(decoded)
            
        elif choice == '3':
            display_hieroglyph_chart()
            
        elif choice == '4':
            print("\nThank you for using the Egyptian Code Book!")
            print("May the gods smile upon your cryptographic journeys! 𓁹")
            break
            
        else:
            print("Invalid option. Please select 1-4.")

# Main entry point for the Egyptian Code Book program.
def main():
    try:
        # Check if terminal supports Unicode properly
        print("Testing Unicode support...", end='')
        test_glyph = HIEROGLYPH_DICT['A']
        print(f" {test_glyph} OK!")
        
        # Display welcome message
        welcome_msg = " WELCOME TO THE EGYPTIAN CODE BOOK BY DAVID CALEB "
        print("\n" + "𓃭" * (len(welcome_msg) + 2))
        print(f"𓃭{welcome_msg.center(len(welcome_msg))}𓃭")
        print("𓃭" * (len(welcome_msg) + 2))
        
        menu()
    except UnicodeEncodeError:
        print("\nError: Your terminal doesn't support Egyptian hieroglyphs properly.")
        print("Please use a terminal with full Unicode support (like Windows Terminal).")
    except Exception as e:
        print(f"\nAn unexpected error occurred: {e}")

if __name__ == "__main__":
    main()
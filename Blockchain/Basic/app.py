# Import necessary libraries
import hashlib
import json
from time import time
from typing import List, Dict, Any

# A single block in our blockchain.
class Block:
    """
    Each block contains:
    - index
    - timestamp
    - data
    - previous hash
    - nonce (for proof-of-work)
    - its own hash
    """
    
    def __init__(self, index: int, timestamp: float, data: Any, previous_hash: str, nonce: int = 0):
        self.index = index
        self.timestamp = timestamp
        self.data = data
        self.previous_hash = previous_hash
        self.nonce = nonce
        self.hash = self.calculate_hash()
        
    # Calculate the SHA-256 hash of this block.
    # The hash is based on all block contents.
    def calculate_hash(self) -> str:
        block_string = json.dumps({
            "index": self.index,
            "timestamp": self.timestamp,
            "data": self.data,
            "previous_hash": self.previous_hash,
            "nonce": self.nonce
        }, sort_keys=True).encode()
        return hashlib.sha256(block_string).hexdigest()
    
    # Proof-of-work mining: find a nonce that makes the hash start with 'difficulty' zeros.
    def mine_block(self, difficulty: int):
        target = "0" * difficulty
        while self.hash[:difficulty] != target:
            self.nonce += 1
            self.hash = self.calculate_hash()
            
    def __str__(self) -> str:
        return f"Block #{self.index} [Hash: {self.hash}, Previous Hash: {self.previous_hash}, Nonce: {self.nonce}]"

# The blockchain class that maintains the chain of blocks.
class Blockchain:
    def __init__(self):
        self.chain: List[Block] = []
        # Number of leading zeros required for proof-of-work
        self.difficulty = 4  
        self.create_genesis_block()
        
    # Create the first block in the chain (genesis block).
    def create_genesis_block(self):
        genesis_block = Block(0, time(), "Genesis Block", "0")
        genesis_block.mine_block(self.difficulty)
        self.chain.append(genesis_block)
        
    # Get the most recent block in the chain.
    def get_latest_block(self) -> Block:
        return self.chain[-1]
    
    # Add a new block to the chain after mining it.
    def add_block(self, new_block: Block):
        new_block.previous_hash = self.get_latest_block().hash
        new_block.mine_block(self.difficulty)
        self.chain.append(new_block)
        
    # Validate the integrity of the blockchain:
    def is_chain_valid(self) -> bool:
        """
        1. Check if each block's hash is correct
        2. Check if each block points to the correct previous hash
        """
        for i in range(1, len(self.chain)):
            current_block = self.chain[i]
            previous_block = self.chain[i-1]
            
            # Verify current block's hash
            if current_block.hash != current_block.calculate_hash():
                print(f"Block #{current_block.index} has invalid hash!")
                return False
                
            # Verify link to previous block
            if current_block.previous_hash != previous_block.hash:
                print(f"Block #{current_block.index} has invalid previous hash!")
                return False
                
        return True
    
    def __str__(self) -> str:
        return "\n".join(str(block) for block in self.chain)

# Interactive menu system for the Minimalist Blockchain.
# Provides a user-friendly way to interact with the blockchain.
class BlockchainMenu:
    
    def __init__(self):
        # Now Blockchain class is defined
        self.blockchain = Blockchain()  
        self.running = True
    
    @staticmethod
    def display_menu():
        print("\nMinimalist Blockchain by David Caleb")
        print("1. Add a new block to the chain")
        print("2. View the entire blockchain")
        print("3. Validate blockchain integrity")
        print("4. View the latest block")
        print("5. Tamper with a block (demo)")
        print("6. Run demo sequence")
        print("7. Exit")
    
    def run(self):
        while self.running:
            self.display_menu()
            choice = input("Please enter your choice (1-7): ")
            
            if choice == "1":
                self.add_block_menu()
            elif choice == "2":
                self.view_blockchain()
            elif choice == "3":
                self.validate_chain()
            elif choice == "4":
                self.view_latest_block()
            elif choice == "5":
                self.tamper_demo()
            elif choice == "6":
                self.run_demo()
            elif choice == "7":
                self.exit_menu()
            else:
                print("Invalid choice. Please try again.")
    
    # Menu for adding a new block to the blockchain.
    def add_block_menu(self):
        print("\nAdd New Block ")
        try:
            data = input("Enter block data (can be any text or JSON): ")
            new_block = Block(
                index=len(self.blockchain.chain),
                timestamp=time(),
                data=data,
                previous_hash=""
            )
            self.blockchain.add_block(new_block)
            print(f"Block #{new_block.index} added successfully!")
            print(new_block)
        except Exception as e:
            print(f"Error adding block: {e}")
    
    # Display the entire blockchain.
    def view_blockchain(self):
        print("\nFull Blockchain ")
        if not self.blockchain.chain:
            print("Blockchain is empty!")
        else:
            print(self.blockchain)
    
    # Validate and display blockchain integrity status.
    def validate_chain(self):
        print("\nBlockchain Validation ")
        if self.blockchain.is_chain_valid():
            print("Blockchain is valid. No tampering detected.")
        else:
            print("WARNING: Blockchain is invalid! Tampering detected.")
    
    # Display the most recent block in the chain.
    def view_latest_block(self):
        print("\nLatest Block ")
        print(self.blockchain.get_latest_block())
    
    # Demonstration of how tampering is detected.
    def tamper_demo(self):
        print("\nTampering Demonstration ")
        if len(self.blockchain.chain) < 2:
            print("Need at least 2 blocks to demonstrate tampering.")
            return
        
        print("Current valid block:")
        print(self.blockchain.chain[1])
        
        print("\nTampering with block #1 data...")
        self.blockchain.chain[1].data = "Tampered data"
        
        print("\nBlock after tampering (without recalculating hash):")
        print(self.blockchain.chain[1])
        
        print("\nValidating chain...")
        self.validate_chain()
        
        # Reset the tampering for demo purposes
        self.blockchain.chain[1].data = {"amount": 4}
        self.blockchain.chain[1].hash = self.blockchain.chain[1].calculate_hash()
    
    # Run a complete demonstration sequence.
    def run_demo(self):
        print("\nRunning Blockchain Demo ")
        
        # Reset blockchain for clean demo
        self.blockchain = Blockchain()
        print("1. Created new blockchain with genesis block")
        print(self.blockchain.get_latest_block())
        
        print("\n2. Adding block #1 with transaction data...")
        self.blockchain.add_block(Block(1, time(), {"from": "Alice", "to": "Bob", "amount": 5}, ""))
        print(self.blockchain.get_latest_block())
        
        print("\n3. Adding block #2 with more data...")
        self.blockchain.add_block(Block(2, time(), {"from": "Bob", "to": "Charlie", "amount": 3}, ""))
        print(self.blockchain.get_latest_block())
        
        print("\n4. Validating chain...")
        self.validate_chain()
        
        print("\n5. Attempting to tamper with block #1...")
        self.tamper_demo()
        
        print("\nDemo complete!")
    
    # Clean exit from the menu system.
    def exit_menu(self):
        print("\nExiting the Blockchain Menu. Goodbye!")
        self.running = False


# To run the menu system:
if __name__ == "__main__":
    menu = BlockchainMenu()
    menu.run()

# Test:
# {"from": "Test01", "to": "Caleb", "amount": 10}
# {"from": "Caleb", "to": "Test02", "amount": 5}
# "Hello Blockchain! This is a test by David Caleb."

# Complex JSON data:
# {"contract": "ERC20", "action": "transfer", "params": {"to": "0x123...", "value": 100}}

# Numbers:
# 42

# List of strings:
# ["vote", "candidate1", "2025-05-06T14:00:00Z"]

# Error:
# {}
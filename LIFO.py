# Node class for singly linked list
class Node:
    def __init__(self, data):
        # Store the data
        self.data = data  
        # Pointer to the next node
        self.next = None  

# Singly linked list class
class SinglyLinkedList:
    def __init__(self):
        # Initialize head of the list
        self.head = None  

    # Insert a new node at the end of the list.
    def insert(self, data):
        new_node = Node(data)
        if not self.head:
            # If list is empty, set head to new node
            self.head = new_node  
            return
        last_node = self.head
        # Traverse to the end of the list
        while last_node.next:  
            last_node = last_node.next
        # Link the new node
        last_node.next = new_node  

    # Display all nodes in the list.
    def display(self):
        current = self.head
        while current:
            # Print current node's data
            print(current.data)  
            # Move to next node
            current = current.next  

# Stack class
class Stack:
    def __init__(self):
        # Initialize an empty stack
        self.items = []  

    # Push an item onto the stack.
    def push(self, item):
        self.items.append(item)

    # Pop an item from the stack.
    def pop(self):
        if not self.is_empty():
            # Remove and return top item
            return self.items.pop()  
        return None

    # Return the top item of the stack without removing it.
    def peek(self):
        if not self.is_empty():
            return self.items[-1]
        return None

    # Check if the stack is empty.
    def is_empty(self):
        return len(self.items) == 0

# Function to display the menu
def display_menu():
    print("\nData Structure Menu by David Caleb")
    print("1. Add player to linked list")
    print("2. Display players in linked list")
    print("3. Push player onto stack")
    print("4. Pop player from stack")
    print("5. Peek at top player in stack")
    print("6. Exit")
    print("=".center(50, "="))
    return input("Select an option: ")

# Main function to run the menu and handle user input
def main():
    linked_list = SinglyLinkedList()
    stack = Stack()
    
    while True:
        # Display menu and get user choice
        choice = display_menu()  
        
        if choice == '1':
            player_name = input("Enter player's name: ")
            # Add player to linked list
            linked_list.insert(player_name)  
            
        elif choice == '2':
            print("Players in linked list:")
            # Display players
            linked_list.display()  
            
        elif choice == '3':
            player_name = input("Enter player's name to push onto stack: ")
            # Push player onto stack
            stack.push(player_name)  
            
        elif choice == '4':
            # Pop player from stack
            popped_player = stack.pop()
            if popped_player:
                print(f"Popped player: {popped_player}")
            else:
                print("Stack is empty!")
                
        elif choice == '5':
            # Peek at top player in stack
            top_player = stack.peek()  
            if top_player:
                print(f"Top player in stack: {top_player}")
            else:
                print("Stack is empty!")
                
        elif choice == '6':
            print("Exiting program.")
            break
            
        else:
            print("Invalid option, please try again.")

# Entry point of the program
if __name__ == "__main__":
    main()
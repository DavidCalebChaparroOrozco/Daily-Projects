class Node:
    # Doubly linked list node class to store key-value pairs# 
    def __init__(self, key=0, value=0):
        # Key stored in the node
        self.key = key      
        # Value stored in the node
        self.value = value  
        # Pointer to previous node
        self.prev = None    
        # Pointer to next node
        self.next = None    

# LRU Cache implementation using hash map and doubly linked list
class LRUCache:
    
    # Initialize the LRU cache with given capacity
    def __init__(self, capacity: int):
        # Maximum capacity of the cache
        self.capacity = capacity          
        # Hash map to store key-node pairs
        self.cache = {}                   
        # Dummy head node of the doubly linked list
        self.head = Node()                
        # Dummy tail node of the doubly linked list
        self.tail = Node()                
        # Connect head to tail
        self.head.next = self.tail        
        # Connect tail to head
        self.tail.prev = self.head        
        # Current size of the cache
        self.size = 0                     

    # Add a node right after the head (most recently used)
    def _add_node(self, node: Node) -> None:
        # Set node's next to what was after head
        node.next = self.head.next
        # Set node's prev to head
        node.prev = self.head
        # Update the old first node's prev pointer
        self.head.next.prev = node
        # Update head's next pointer
        self.head.next = node

    # Remove a node from the linked list
    def _remove_node(self, node: Node) -> None:
        # Get the nodes before and after the node to remove
        prev_node = node.prev
        next_node = node.next
        # Link them together, bypassing the node to remove
        prev_node.next = next_node
        next_node.prev = prev_node

    # Move a node to the head position (most recently used)
    def _move_to_head(self, node: Node) -> None:
        # Remove from current position
        self._remove_node(node)  
        self._add_node(node)     # Add to head position

    # Remove and return the node before the tail (least recently used)# 
    def _pop_tail(self) -> Node:
        # Get the node before tail
        node = self.tail.prev   
        # Remove it from the list
        self._remove_node(node) 
        return node

    def get(self, key: int) -> int:
        # Get the value of the key if it exists, otherwise return -1# 
        if key not in self.cache:
            return -1
        
        # Get the node from cache
        node = self.cache[key]
        # Move this node to head since it was recently used
        self._move_to_head(node)
        # Return the value
        return node.value

    def put(self, key: int, value: int) -> None:
        # Put a key-value pair into the cache
        if key in self.cache:
            # If key exists, update its value and move to head
            node = self.cache[key]
            node.value = value
            self._move_to_head(node)
        else:
            # Create new node
            new_node = Node(key, value)
            # Add to cache
            self.cache[key] = new_node
            # Add to head of linked list
            self._add_node(new_node)
            self.size += 1
            
            # Check if capacity is exceeded
            if self.size > self.capacity:
                # Remove the LRU item (before tail)
                tail = self._pop_tail()
                # Remove from cache
                del self.cache[tail.key]  
                self.size -= 1
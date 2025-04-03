"""
This module implements an LRU (Least Recently Used) Cache.
The cache has a fixed capacity and removes the least recently used item when full.
It uses a combination of a dictionary (for O(1) lookups) and a doubly linked list 
(for O(1) insertions/deletions to track usage order.
"""

# Node class for doubly linked list
class Node:
    def __init__(self, key=None, value=None):
        self.key = key
        self.value = value
        self.prev = None
        self.next = None

# LRU Cache implementation with usage tracking
class LRUCache:
    
    def __init__(self, capacity: int):
        if capacity <= 0:
            raise ValueError("Capacity must be a positive integer")
            
        self.capacity = capacity
        self.cache = {}
        self.size = 0
        
        # Dummy head and tail nodes
        self.head = Node()
        self.tail = Node()
        self.head.next = self.tail
        self.tail.prev = self.head
    
    # Add node right after head
    def _add_node(self, node: Node):
        node.prev = self.head
        node.next = self.head.next
        self.head.next.prev = node
        self.head.next = node
    
    # Remove node from linked list
    def _remove_node(self, node: Node):
        prev_node = node.prev
        next_node = node.next
        prev_node.next = next_node
        next_node.prev = prev_node
    
    # Move node to head position
    def _move_to_head(self, node: Node):
        self._remove_node(node)
        self._add_node(node)
    
    # Remove and return the tail node
    def _pop_tail(self) -> Node:
        node = self.tail.prev
        self._remove_node(node)
        return node
    
    # Get current cache state as MRU to LRU keys
    def get_current_state(self):
        state = []
        current = self.head.next
        while current != self.tail:
            state.append(current.key)
            current = current.next
        return state
    
    # Retrieve value for key
    def get(self, key) -> any:
        node = self.cache.get(key)
        if not node:
            return None
        self._move_to_head(node)
        return node.value
    
    # Add/update key-value pair
    def put(self, key, value):
        node = self.cache.get(key)
        
        if not node:
            new_node = Node(key, value)
            self.cache[key] = new_node
            self._add_node(new_node)
            self.size += 1
            
            if self.size > self.capacity:
                tail = self._pop_tail()
                del self.cache[tail.key]
                self.size -= 1
        else:
            node.value = value
            self._move_to_head(node)

# Visualize cache state history using matplotlib
def visualize_cache_history(history):
    import matplotlib.pyplot as plt
    
    operations = [entry[0] for entry in history]
    states = [entry[1] for entry in history]
    
    # Create figure
    fig, ax = plt.subplots(figsize=(10, 6))
    
    # Create data grid
    max_len = max(len(state) for state in states)
    grid_data = []
    for state in states:
        padded = list(state) + [''] * (max_len - len(state))
        grid_data.append(padded)
    
    # Create table
    table = ax.table(cellText=grid_data, 
                        rowLabels=operations,
                        colLabels=[f"Pos {i}" for i in range(max_len)],
                        loc='center',
                        cellLoc='center')
    
    # Style table
    table.auto_set_font_size(False)
    table.set_fontsize(12)
    table.scale(1.2, 1.2)
    
    # Configure plot
    ax.set_title("LRU Cache State Evolution", pad=20, fontsize=14)
    ax.axis('off')
    
    # Add legend
    ax.text(0.5, -0.1, 
            "Pos 0 = Most Recently Used\nPos N = Least Recently Used", 
            ha='center', va='center', transform=ax.transAxes)
    
    plt.tight_layout()
    plt.show()

if __name__ == "__main__":
    # Initialize cache and history tracker
    cache = LRUCache(3)
    history = []
    
    # Define helper function to track operations
    def track(op):
        history.append((op, cache.get_current_state()))
    
    # Perform cache operations
    cache.put('a', 1); track("Put 'a'")
    cache.put('b', 2); track("Put 'b'")
    cache.put('c', 3); track("Put 'c'")
    cache.get('b');     track("Get 'b'")
    cache.put('d', 4); track("Put 'd'")
    cache.get('a');     track("Get 'a'")
    
    # Generate visualization
    visualize_cache_history(history)
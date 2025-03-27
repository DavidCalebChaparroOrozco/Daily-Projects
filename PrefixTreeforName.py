# Import necessary libraries
import matplotlib.pyplot as plt
import networkx as nx
from collections import deque

# A node in the prefix tree (trie) structure.
class TrieNode:
    def __init__(self, char=None):
        self.children = {}
        self.is_end = False
        # Store character for visualization
        self.char = char  
        
    def __repr__(self):
        return f"TrieNode('{self.char}')"


# Enhanced prefix tree (trie) implementation with visualization capabilities.
class NameSearchTrie:
    # Initialize the trie with an empty root node.
    def __init__(self):
        self.root = TrieNode()
        self.total_names = 0
        # Count the root node
        self.total_nodes = 1  
        
    # Insert a name into the trie.
    def insert(self, name):
        if not name:
            return
            
        node = self.root
        for char in name.lower():
            if char not in node.children:
                node.children[char] = TrieNode(char)
                self.total_nodes += 1
            node = node.children[char]
        
        if not node.is_end:  # Only count if it's a new name
            node.is_end = True
            self.total_names += 1
    
    # Search for all names that start with the given prefix.
    def search(self, prefix):
        if not prefix:
            return []
            
        node = self.root
        prefix = prefix.lower()
        
        # Traverse to the end of the prefix
        for char in prefix:
            if char not in node.children:
                return []
            node = node.children[char]
        
        # Collect all names with this prefix
        names = []
        self._collect_names(node, prefix, names)
        return sorted(names)
    
    # Helper method to recursively collect all names starting from a given node.
    def _collect_names(self, node, current_prefix, names):
        if node.is_end:
            names.append(current_prefix)
        
        for char, child_node in node.children.items():
            self._collect_names(child_node, current_prefix + char, names)
    
    # Visualize the trie structure using matplotlib and networkx.
    def visualize(self, max_depth=5, max_children=10):
        G = nx.DiGraph()
        pos = {}
        labels = {}
        queue = deque()
        
        # Add root node
        root_id = id(self.root)
        G.add_node(root_id)
        pos[root_id] = (0, 0)
        labels[root_id] = "ROOT"
        queue.append((self.root, 0, 0, 0))
        
        # BFS to build the graph
        while queue:
            node, x, y, depth = queue.popleft()
            node_id = id(node)
            
            if depth >= max_depth:
                continue
                
            # Sort children for consistent visualization
            children = sorted(node.children.items(), key=lambda item: item[0])
            
            # Limit number of children shown
            if max_children and len(children) > max_children:
                children = children[:max_children]
            
            # Calculate positions for children
            num_children = len(children)
            x_start = x - (num_children - 1) / 2
            child_y = y - 1
            
            for i, (char, child_node) in enumerate(children):
                child_id = id(child_node)
                child_x = x_start + i
                
                G.add_node(child_id)
                G.add_edge(node_id, child_id)
                pos[child_id] = (child_x, child_y)
                
                # Use different colors for end nodes
                node_color = 'red' if child_node.is_end else 'skyblue'
                labels[child_id] = (char.upper(), node_color)
                
                queue.append((child_node, child_x, child_y, depth + 1))
        
        # Draw the graph
        plt.figure(figsize=(12, 8))
        
        # Draw nodes with different colors
        for node_id in G.nodes():
            if node_id == root_id:
                nx.draw_networkx_nodes(G, pos, nodelist=[node_id], node_size=1000, 
                                        node_color='green', alpha=0.8)
            else:
                label, node_color = labels[node_id]
                nx.draw_networkx_nodes(G, pos, nodelist=[node_id], node_size=800, 
                                        node_color=node_color, alpha=0.8)
        
        # Draw edges
        nx.draw_networkx_edges(G, pos, arrowstyle='-|>', arrowsize=15, 
                                edge_color='gray', width=1.5)
        
        # Draw labels
        for node_id in G.nodes():
            if node_id == root_id:
                plt.text(pos[node_id][0], pos[node_id][1], labels[node_id], 
                            ha='center', va='center', fontsize=12, fontweight='bold')
            else:
                char, _ = labels[node_id]
                plt.text(pos[node_id][0], pos[node_id][1], char, 
                            ha='center', va='center', fontsize=10)
        
        plt.title(f"Trie Structure (Depth: {max_depth}, Showing {max_children} children max)")
        plt.axis('off')
        plt.tight_layout()
        plt.show()
    
    # Get statistics about the trie.
    def get_stats(self):
        return {
            'total_names': self.total_names,
            'total_nodes': self.total_nodes,
            'average_name_length': self._calculate_avg_length(),
            'compression_ratio': self.total_nodes / (sum(len(name) for name in self.get_all_names()) + 1)
        }
    
    # Calculate average length of names in the trie.
    def _calculate_avg_length(self):
        names = self.get_all_names()
        if not names:
            return 0
        return sum(len(name) for name in names) / len(names)
    
    # Retrieve all names stored in the trie.
    def get_all_names(self):
        names = []
        self._collect_names(self.root, "", names)
        return sorted(names)


# Load names from a text file (one name per line).
def load_names_from_file(filename):
    try:
        with open(filename, 'r') as file:
            return [line.strip() for line in file if line.strip()]
    except FileNotFoundError:
        print(f"Error: File '{filename}' not found.")
        return []


# Interactive demo with menu options for trie operations.
def interactive_demo():
    trie = NameSearchTrie()
    
    # Sample data for demonstration
    sample_names = [
        "Alice", "Bob", "Charlie", "David", "Eve",
        "Frank", "Grace", "Heidi", "Ivan", "Judy",
        "Kevin", "Linda", "Mike", "Nancy", "Oscar",
        "Peter", "Quinn", "Rachel", "Steve", "Tina",
        "Ursula", "Victor", "Wendy", "Xavier", "Yvonne", "Zack",
        "Anna", "Annie", "Anne", "Andy", "Anderson"
    ]
    
    while True:
        print("\n Name Search Trie by David Caleb")
        print("1. Load sample names")
        print("2. Load names from file")
        print("3. Search names by prefix")
        print("4. View all names")
        print("5. Visualize trie structure")
        print("6. Show trie statistics")
        print("7. Exit")
        
        choice = input("Enter your choice (1-7): ").strip()
        
        if choice == '1':
            for name in sample_names:
                trie.insert(name)
            print(f"Loaded {len(sample_names)} sample names.")
        
        elif choice == '2':
            filename = input("Enter filename (e.g., names.txt): ").strip()
            names = load_names_from_file(filename)
            if names:
                for name in names:
                    trie.insert(name)
                print(f"Loaded {len(names)} names from file.")
        
        elif choice == '3':
            prefix = input("Enter prefix to search: ").strip()
            results = trie.search(prefix)
            if results:
                print(f"\nFound {len(results)} matches:")
                for i, name in enumerate(results, 1):
                    print(f"{i}. {name.capitalize()}")
            else:
                print("No matches found.")
        
        elif choice == '4':
            names = trie.get_all_names()
            if names:
                print("\nAll names in trie:")
                for i, name in enumerate(names, 1):
                    print(f"{i}. {name.capitalize()}")
            else:
                print("Trie is empty.")
        
        elif choice == '5':
            print("Generating visualization...")
            try:
                trie.visualize(max_depth=5, max_children=8)
            except ImportError:
                print("Visualization requires matplotlib and networkx. Install with:")
                print("pip install matplotlib networkx")
        
        elif choice == '6':
            stats = trie.get_stats()
            print("\nTrie Statistics:")
            print(f"- Total names: {stats['total_names']}")
            print(f"- Total nodes: {stats['total_nodes']}")
            print(f"- Average name length: {stats['average_name_length']:.2f}")
            print(f"- Compression ratio: {stats['compression_ratio']:.2f}")
        
        elif choice == '7':
            print("Exiting...")
            break
        
        else:
            print("Invalid choice. Please enter a number 1-7.")


if __name__ == "__main__":
    print("Name Search Trie with Visualization")
    print("=".center(40,"="))
    interactive_demo()
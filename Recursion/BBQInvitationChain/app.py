# Import necessary libraries
import networkx as nx
import matplotlib.pyplot as plt
from collections import deque

class Guest:
    def __init__(self, name, level):
        # Name of the guest
        self.name = name  
        # Depth level in the invitation chain
        self.level = level  
        # Who invited this guest
        self.invited_by = None  
        # List of people this guest invited
        self.invitees = []  

class BBQInvitationTree:
    def __init__(self):
        # The initial host of the BBQ
        self.root = None  
        # Counter for total guests
        self.total_guests = 0  
        # Tracks the deepest level of invitation
        self.max_depth = 0  
    
    # Add a new guest to the invitation tree
    def add_guest(self, name, inviter_name=None):
        if not self.root:
            # First guest is the host
            self.root = Guest(name, 0)
            self.total_guests = 1
            self.max_depth = 0
            return self.root
        
        # Find the inviter in the tree using BFS
        inviter = self._find_guest(inviter_name)
        if not inviter:
            print(f"Inviter {inviter_name} not found. Guest not added.")
            return None
        
        # Create new guest and update relationships
        new_guest = Guest(name, inviter.level + 1)
        new_guest.invited_by = inviter
        inviter.invitees.append(new_guest)
        
        # Update statistics
        self.total_guests += 1
        self.max_depth = max(self.max_depth, new_guest.level)
        
        return new_guest
    
    # BFS helper to find a guest by name
    def _find_guest(self, name):
        if not self.root:
            return None
        if self.root.name == name:
            return self.root
            
        queue = deque([self.root])
        while queue:
            current = queue.popleft()
            if current.name == name:
                return current
            for invitee in current.invitees:
                queue.append(invitee)
        return None
    
    # Print the invitation tree with indentation showing levels
    def print_tree(self):
        if not self.root:
            print("No guests in the BBQ yet!")
            return
        
        self._print_guest(self.root, 0)
        print(f"\nTotal guests: {self.total_guests}")
        print(f"Maximum invitation depth: {self.max_depth}")
    
    # Recursive helper to print guest tree
    def _print_guest(self, guest, indent):
        print(' ' * indent * 4 + f"└── {guest.name} (Level {guest.level})")
        for invitee in guest.invitees:
            self._print_guest(invitee, indent + 1)
    
    # Create a visual graph of the invitation tree
    def visualize_tree(self):
        if not self.root:
            print("No guests to visualize!")
            return
        
        G = nx.DiGraph()
        self._add_edges_to_graph(G, self.root)
        
        pos = nx.spring_layout(G)
        plt.figure(figsize=(10, 8))
        
        # Draw nodes with different colors based on level
        node_colors = [self._get_color_for_level(G.nodes[node]['level']) 
                        for node in G.nodes]
        
        nx.draw(G, pos, with_labels=True, node_size=2000, node_color=node_colors,
                font_size=10, font_weight='bold', arrowsize=20)
        
        plt.title("BBQ Invitation Tree Visualization")
        plt.show()
    
    # Recursive helper to build the networkx graph
    def _add_edges_to_graph(self, graph, guest):
        graph.add_node(guest.name, level=guest.level)
        for invitee in guest.invitees:
            graph.add_edge(guest.name, invitee.name)
            self._add_edges_to_graph(graph, invitee)
    
    # Helper to assign colors based on invitation level
    def _get_color_for_level(self, level):
        colors = ['#FF9999', '#66B2FF', '#99FF99', '#FFCC99', 
                 '#FF99FF', '#FFFF99', '#99FFFF']
        return colors[level % len(colors)]

# Example usage
if __name__ == "__main__":
    bbq = BBQInvitationTree()
    
    # The host starts the BBQ
    bbq.add_guest("Caleb")
    
    # First level invitations
    bbq.add_guest("Alba", "Caleb")
    bbq.add_guest("Jose", "Caleb")
    
    # Second level invitations
    bbq.add_guest("Maxi", "Alba")
    bbq.add_guest("Andrea", "Alba")
    bbq.add_guest("Santiago", "Jose")
    
    # Third level invitations
    bbq.add_guest("Sofia", "Maxi")
    bbq.add_guest("Diego", "Andrea")
    # This will fail (intentional typo)
    bbq.add_guest("Laura", "Santiago")  
    
    # Print the invitation tree
    bbq.print_tree()
    
    # Visualize the tree
    bbq.visualize_tree()
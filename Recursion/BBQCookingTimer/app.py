# Import necessary libraries
import time
from typing import Dict, List, Optional
import matplotlib.pyplot as plt
import networkx as nx

# A recursive BBQ cooking timer that simulates cooking different cuts of meat,
# where some cuts start cooking while others are already in process.
class BBQTimer:
    """
    Attributes:
        cuts: Dictionary of meat cuts and their cooking times in minutes
        grill_state: Current state of the grill with cooking items
        graph: Directed graph to visualize cooking process
        node_counter: Counter for unique node IDs in the graph
    """
    
    # Initialize the BBQ timer with default meat cuts and cooking times.
    def __init__(self):
        self.cuts = {
            # 2 hours
            "ribs": 120,        
            # 30 minutes
            "sausage": 30,     
            # 45 minutes
            "blood_sausage": 45,  
            # 1 hour
            "chicken": 60,      
            # 3 hours
            "brisket": 180      
        }
        self.grill_state = []
        self.graph = nx.DiGraph()
        self.node_counter = 0
        
    # Add a meat cut to the grill with its start time.
    def add_to_grill(self, cut_name: str, start_time: float) -> Dict:
        """    
        Args:
            cut_name: Name of the meat cut
            start_time: Time when the cut was added to the grill
        Returns:
            Dictionary representing the meat cut on the grill
        """
        if cut_name not in self.cuts:
            raise ValueError(f"Unknown cut: {cut_name}")
            
        item = {
            "name": cut_name,
            "start_time": start_time,
            # Convert to seconds
            "end_time": start_time + self.cuts[cut_name] * 60,  
            "done": False
        }
        self.grill_state.append(item)
        return item
    
    # Recursively cook meat cuts, adding new cuts while others are cooking.
    def cook_recursive(self, cuts_to_cook: List[str], current_time: float = None, parent_node: Optional[int] = None) -> None:
        """    
        Args:
            cuts_to_cook: List of meat cuts to cook
            current_time: Simulation time in seconds since start
            parent_node: Parent node ID in the visualization graph
        """
        if current_time is None:
            current_time = time.time()  # Use current system time if not specified
            
        if not cuts_to_cook:
            return
            
        # Get next cut to cook
        current_cut = cuts_to_cook[0]
        remaining_cuts = cuts_to_cook[1:]
        
        # Add to grill and create graph node
        item = self.add_to_grill(current_cut, current_time)
        current_node = self.node_counter
        self.graph.add_node(current_node, 
                            label=f"{current_cut}\nStart: {self.format_time(current_time)}\nEnd: {self.format_time(item['end_time'])}")
        
        # Connect to parent node if exists
        if parent_node is not None:
            self.graph.add_edge(parent_node, current_node)
            
        self.node_counter += 1
        
        print(f"Started cooking {current_cut} at {self.format_time(current_time)}")
        
        # Simulate cooking time (in real app this would be actual waiting)
        done_time = item['end_time']
        
        # While cooking, check if we should add more items
        if remaining_cuts:
            # Decide when to add next cut (here we use half of current cut's cooking time)
            next_cut_time = current_time + (self.cuts[current_cut] * 60) / 2
            
            # Recursively add next cut
            self.cook_recursive(remaining_cuts, next_cut_time, current_node)
        
        # Mark as done
        item['done'] = True
        print(f"Finished cooking {current_cut} at {self.format_time(done_time)}")
        
    # Format timestamp as readable time.
    def format_time(self, timestamp: float) -> str:
        """    
        Args:
            timestamp: Time in seconds
            
        Returns:
            Formatted time string (HH:MM:SS)
        """
        return time.strftime("%H:%M:%S", time.localtime(timestamp))
    
    # Visualize the cooking process as a tree using matplotlib.
    def visualize_grill(self) -> None:
        try:
            plt.figure(figsize=(12, 8))
            
            # Try different layout methods if graphviz isn't available
            try:
                from networkx.drawing.nx_pydot import graphviz_layout
                pos = graphviz_layout(self.graph, prog="dot")
            except ImportError:
                print("Graphviz/pydot not available - using spring layout instead")
                pos = nx.spring_layout(self.graph, seed=42)  # seed for reproducibility
            
            # Draw nodes with labels
            labels = nx.get_node_attributes(self.graph, 'label')
            nx.draw(self.graph, pos, with_labels=True, labels=labels, node_size=3000, 
                    node_color="lightblue", font_size=10, arrows=True)
            
            plt.title("BBQ Cooking Process Tree")
            plt.tight_layout()
            plt.show()
        except Exception as e:
            print(f"Could not generate visualization: {e}")
            print("Here's the text representation instead:")
            self.print_graph_text()
    
    # Print a text representation of the cooking graph.
    def print_graph_text(self) -> None:
        print("\nCooking Process Tree:")
        print("=".center(40, "="))
        for node in self.graph.nodes:
            print(f"Node {node}: {self.graph.nodes[node]['label']}")
            for successor in self.graph.successors(node):
                print(f"  -> Node {successor}")
        print()
    
    # Print current state of all items on the grill.
    def print_grill_state(self) -> None:
        print("\nCurrent Grill State:")
        print("=".center(40, "="))
        for item in sorted(self.grill_state, key=lambda x: x['start_time']):
            status = "DONE" if item['done'] else "COOKING"
            print(f"{item['name'].ljust(15)} {self.format_time(item['start_time'])} - {self.format_time(item['end_time'])} [{status}]")
        print()

if __name__ == "__main__":
    # Create and run the BBQ timer
    bbq = BBQTimer()
    
    # Define the order of cuts to cook
    cuts_sequence = ["ribs", "sausage", "blood_sausage", "chicken"]
    
    # Start cooking recursively
    print("🚀 Starting BBQ Cooking Process 🚀")
    bbq.cook_recursive(cuts_sequence)
    
    # Show results
    bbq.print_grill_state()
    bbq.visualize_grill()
# Import necessary libraries
import matplotlib.pyplot as plt
import networkx as nx
from typing import List, Tuple

class ProbabilityNode:
    #  Initializes a probability node.
    def __init__(self, name: str, probability: float, children: List['ProbabilityNode'] = None):        
        self.name = name
        self.probability = probability
        self.children = children if children else []

    # Check if the node is a leaf (has no children).
    def is_leaf(self) -> bool:
        return len(self.children) == 0

# Recursively creates a probability tree from user input.
def create_tree_interactively(node_name="Start", prob=1.0) -> ProbabilityNode:
    print(f"\nNode: {node_name} (Probability from parent: {prob})")
    try:
        num_children = int(input(f"How many children does '{node_name}' have? (0 if leaf): "))
    except ValueError:
        print("Invalid input. Assuming 0 children.")
        num_children = 0

    children = []
    for i in range(num_children):
        child_name = input(f"Enter name for child {i+1} of '{node_name}': ")
        while True:
            try:
                child_prob = float(input(f"Enter probability to '{child_name}' (0.0 to 1.0): "))
                if 0 <= child_prob <= 1:
                    break
                else:
                    print("Probability must be between 0 and 1.")
            except ValueError:
                print("Invalid number. Please enter a valid float.")
        child_node = create_tree_interactively(child_name, child_prob)
        child_node.probability = child_prob
        children.append(child_node)

    return ProbabilityNode(node_name, prob, children)

# Recursively traverse the probability tree and collect paths.
def traverse_tree(node: ProbabilityNode, path: List[str], prob: float,
                    results: List[Tuple[List[str], float]], G: nx.DiGraph, parent: str = None):
    new_path = path + [node.name]
    new_prob = prob * node.probability

    G.add_node(node.name, label=f"{node.name}\nP={node.probability}")
    if parent:
        G.add_edge(parent, node.name, weight=node.probability)

    if node.is_leaf():
        results.append((new_path, new_prob))
    else:
        for child in node.children:
            traverse_tree(child, new_path, new_prob, results, G, node.name)

# Display all paths to the leaves with their total probabilities.
def display_results(results: List[Tuple[List[str], float]]):
    print("\n Probability Paths to Leaves")
    for path, prob in results:
        print(" -> ".join(path) + f" = {prob:.6f}")

# Draw the tree using networkx and matplotlib.
def draw_tree(G: nx.DiGraph):
    pos = nx.spring_layout(G, seed=42)
    labels = nx.get_node_attributes(G, 'label')
    edge_labels = nx.get_edge_attributes(G, 'weight')

    plt.figure(figsize=(10, 6))
    nx.draw(G, pos, with_labels=True, labels=labels, node_size=2000,
            node_color="lightgreen", font_size=8, font_weight='bold', arrows=True)
    nx.draw_networkx_edge_labels(G, pos,
                                    edge_labels={k: f"P={v:.2f}" for k, v in edge_labels.items()},
                                    font_color='blue')
    plt.title("Recursive Probability Tree")
    plt.tight_layout()
    plt.show()

# Main program
if __name__ == "__main__":
    print("📊 Recursive Probability Tree Builder")
    print("You will now create a tree where each node has probabilities and child decisions.")

    # Step 1: Create the tree from user input
    root = create_tree_interactively()

    # Step 2: Traverse and analyze
    results = []
    G = nx.DiGraph()
    traverse_tree(root, [], 1.0, results, G)

    # Step 3: Display output
    display_results(results)
    draw_tree(G)

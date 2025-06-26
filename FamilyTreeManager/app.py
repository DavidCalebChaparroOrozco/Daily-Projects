# Import necessary libraries
import pandas as pd
import matplotlib.pyplot as plt
import networkx as nx 
from collections import defaultdict, deque

# Class to represent a family member with a name and list of children.
class FamilyMember:
    def __init__(self, name):
        self.name = name
        self.children = []

# Class to represent and manipulate the family tree.
class FamilyTree:
    def __init__(self):
        self.members = {}
        self.root = None

    # Add a member to the family tree.
    def add_member(self, name, parent_name=None):
        if name in self.members:
            print(f"Member '{name}' already exists.")
            return

        new_member = FamilyMember(name)
        self.members[name] = new_member

        if parent_name:
            if parent_name in self.members:
                self.members[parent_name].children.append(new_member)
            else:
                print(f"Parent '{parent_name}' not found. Adding '{name}' without parent.")
        else:
            if self.root is None:
                self.root = new_member
            else:
                print("Root already exists. Only one root is allowed.")

    # Display the family tree using matplotlib.
    def display_tree(self):
        if self.root is None:
            print("No root defined. Cannot draw tree.")
            return

        G = nx.DiGraph()
        pos = {}
        labels = {}

        def dfs(member, x=0, y=0, depth=0):
            pos[member.name] = (x, -y)
            labels[member.name] = member.name
            G.add_node(member.name)

            for i, child in enumerate(member.children):
                G.add_edge(member.name, child.name)
                dfs(child, x + i - len(member.children) / 2, y + 1, depth + 1)

        dfs(self.root)

        plt.figure(figsize=(10, 6))
        nx.draw(G, pos, with_labels=True, arrows=False, node_size=3000, node_color='lightblue')
        nx.draw_networkx_labels(G, pos, labels)
        plt.title("Family Tree")
        plt.show()

    # Export generation data to an Excel file.
    def export_generations_to_excel(self, filename="generations.xlsx"):
        if not self.root:
            print("Cannot export. No root defined.")
            return

        generation_data = defaultdict(int)
        queue = deque([(self.root, 0)])

        while queue:
            member, generation = queue.popleft()
            generation_data[generation] += 1

            for child in member.children:
                queue.append((child, generation + 1))

        df = pd.DataFrame(list(generation_data.items()), columns=['Generation', 'Number of Individuals'])
        df.to_excel(filename, index=False)
        print(f"Generation data exported to '{filename}'.")

# Class to handle the menu interface.
class Menu:
    def __init__(self):
        self.family_tree = FamilyTree()

    @staticmethod
    def display_menu():
        print("\nWelcome to the Family Tree Manager")
        print("1. Add family member")
        print("2. View family tree")
        print("3. Export generation data to Excel")
        print("4. Exit")

    def run(self):
        while True:
            self.display_menu()
            choice = input("Choose an option: ")

            if choice == '1':
                name = input("Enter the name of the family member: ")
                parent = input("Enter the name of the parent (leave blank if root): ")
                parent = parent if parent.strip() else None
                self.family_tree.add_member(name, parent)

            elif choice == '2':
                self.family_tree.display_tree()

            elif choice == '3':
                self.family_tree.export_generations_to_excel()

            elif choice == '4':
                print("Exiting... Goodbye!")
                break

            else:
                print("Invalid choice. Please select again.")

if __name__ == "__main__":
    menu = Menu()
    menu.run()
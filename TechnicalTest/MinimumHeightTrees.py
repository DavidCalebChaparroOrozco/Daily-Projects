# A tree is an undirected graph in which any two vertices are connected by exactly one path. 
# In other words, any connected graph without simple cycles is a tree.
# Given a tree of n nodes labelled from 0 to n - 1, and an array of n - 1 edges where 
# edges[i] = [ai, bi] indicates that there is an undirected edge between the two nodes ai and bi in
# the tree, you can choose any node of the tree as the root. When you select a node x as the root, 
# the result tree has height h. Among all possible rooted trees, those with minimum height 
# (i.e. min(h)) are called minimum height trees (MHTs).
# Return a list of all MHTs' root labels. You can return the answer in any order.
# The height of a rooted tree is the number of edges on the longest downward path between the root and a leaf.

from collections import defaultdict

class Solution(object):
    def findMinHeightTrees(self, n, edges):
        if n == 1:
            # Special case: only one node
            return [0]  

        # Create an adjacency list representation of the graph
        adjacency_list = defaultdict(set)
        for u, v in edges:
            adjacency_list[u].add(v)
            adjacency_list[v].add(u)

        # Find the leaf nodes (nodes with only one connection)
        leaves = [node for node in adjacency_list if len(adjacency_list[node]) == 1]

        # Repeat the process until we have 1 or 2 nodes left
        while n > 2:
            n -= len(leaves)
            new_leaves = []
            for leaf in leaves:
                # Remove leaf node and update its adjacent node
                neighbor = adjacency_list[leaf].pop()
                adjacency_list[neighbor].remove(leaf)
                if len(adjacency_list[neighbor]) == 1:
                    new_leaves.append(neighbor)
            leaves = new_leaves

        # The remaining nodes are the roots of minimum height trees
        return leaves


# Create an instance of the Solution class
sol1 = Solution()

# Define the number of nodes and edges of the graph
n = 4
edges = [[1,0],[1,2],[1,3]]

# Call the findMinHeightTrees function and display the result in the output
print(sol1.findMinHeightTrees(n, edges))
print("=".center(50,"="))


# Create an instance of the Solution class
sol2 = Solution()

# Define the number of nodes and edges of the graph
n = 6
edges = [[3, 0], [3, 1], [3, 2], [3, 4], [5, 4]]

# Call the findMinHeightTrees function and display the result in the output
print(sol2.findMinHeightTrees(n, edges))
print("=".center(50,"="))
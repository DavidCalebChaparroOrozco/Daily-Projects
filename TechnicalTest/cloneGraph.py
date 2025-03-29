from typing import Optional

# Definition for a Node.
class Node:
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []


class Solution:
    def cloneGraph(self, node: Optional['Node']) -> Optional['Node']:
        if not node:
            return None
        
        # Dictionary to save the visited nodes and their clones to avoid cycles.
        visited = {}
        
        def dfs(original_node):
            if original_node in visited:
                return visited[original_node]
            
            # Create a clone of the original node.
            clone_node = Node(original_node.val)
            visited[original_node] = clone_node
            
            # Iterate through the neighbors to clone them.
            for neighbor in original_node.neighbors:
                clone_node.neighbors.append(dfs(neighbor))
            
            return clone_node
        
        return dfs(node)

# Function to build a graph from an adjacency list.
def buildGraph(adjList):
    if not adjList:
        return None
    
    nodes = {}
    for i in range(len(adjList)):
        nodes[i+1] = Node(i+1)
    
    for i in range(len(adjList)):
        for neighbor_val in adjList[i]:
            nodes[i+1].neighbors.append(nodes[neighbor_val])
    
    return nodes[1] if nodes else None

# Create an instance of the Solution class
sol = Solution()

# Example 1
print("=".center(50, "="))
adjList1 = [[2,4],[1,3],[2,4],[1,3]]
print("Example 1:")
print("Input adjList1:", adjList1)
graph1 = buildGraph(adjList1)
sol1 = sol.cloneGraph(graph1)
print("Output:", sol1.val if sol1 else None)
print("=".center(50, "="))

# Example 2
adjList2 = [[]]
print("Example 2:")
print("Input adjList2:", adjList2)
graph2 = buildGraph(adjList2)
sol2 = sol.cloneGraph(graph2)
print("Output:", sol2.val if sol2 else None)
print("=".center(50, "="))

# Example 3
adjList3 = []
print("Example 3:")
print("Input adjList3:", adjList3)
graph3 = buildGraph(adjList3)
sol3 = sol.cloneGraph(graph3)
print("Output:", sol3.val if sol3 else None)
print("=".center(50, "="))
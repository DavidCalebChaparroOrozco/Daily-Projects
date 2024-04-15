import heapq

def dijkstra(graph, start):

# Check if the start node exists in the graph
    if start not in graph:
        raise ValueError("The starting node does not exist in the graph.")

    # Dictionary to store the distance from start to each node
    distances = {node: float('inf') for node in graph}
    # Distance from start to itself is 0
    distances[start] = 0  

    # Priority queue to store nodes to visit, with their current distance from start
    # (distance, node)
    queue = [(0, start)]  
    
    while queue:
        # Pop the node with the smallest distance
        current_distance, current_node = heapq.heappop(queue)  
        if current_distance > distances[current_node]:
        # Skip if we have already found a shorter path to this node
            continue  
        for neighbor, weight in graph[current_node].items():
            distance = current_distance + weight
            if distance < distances[neighbor]:
                distances[neighbor] = distance
                heapq.heappush(queue, (distance, neighbor))
    
    return distances

# Example graph representation (adjacency list)
graph = {
    'A': {'B': 2, 'C': 1},
    'B': {'A': 2, 'D': 3, 'E': 1},
    'C': {'A': 1, 'F': 4},
    'D': {'B': 3, 'E': 2, 'G': 1},
    'E': {'B': 1, 'D': 2, 'H': 3},
    'F': {'C': 4, 'I': 5},
    'G': {'D': 1, 'H': 2},
    'H': {'E': 3, 'G': 2, 'I': 1},
    'I': {'F': 5, 'H': 1}
}

start_node = 'A'
try:
    distances = dijkstra(graph, start_node)
    print("Shortest distances from node", start_node)
    for node, distance in distances.items():
        print("Node:", node, ", Distance:", distance)
except ValueError as e:
    print(e)

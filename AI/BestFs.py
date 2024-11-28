from queue import PriorityQueue

def best_first_search(graph, start, goal, heuristic):
    # Priority Queue to store nodes with their heuristic value
    pq = PriorityQueue()
    pq.put((heuristic[start], start, [start]))  # (heuristic value, current node, path)
    visited = set()

    while not pq.empty():
        _, node, path = pq.get()  # Get the node with the lowest heuristic value

        if node in visited:  # Skip if already visited
            continue
        visited.add(node)

        if node == goal:  # Stop when goal is reached
            return path

        for neighbor in graph[node]:  # Explore neighbors
            if neighbor not in visited:
                pq.put((heuristic[neighbor], neighbor, path + [neighbor]))

    return []  # Return empty if no path is found

# Example graph (edges are unweighted for Best First Search)
graph = {
    'A': ['B', 'C'],
    'B': ['D', 'E'],
    'C': ['F'],
    'D': [],
    'E': ['F'],
    'F': []
}

# Heuristic values (estimated distance to goal)
heuristic = {
    'A': 6,
    'B': 8,
    'C': 5,
    'D': 2,
    'E': 1,
    'F': 0
}

# Example usage
path = best_first_search(graph, 'A', 'F', heuristic)
if path:
    print(f"Path: {path}")
else:
    print("No path found.")

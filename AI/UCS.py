from queue import PriorityQueue

def uniform_cost_search(graph, start, goal):
    
    # Priority Queue to store nodes with their cumulative cost
    pq = PriorityQueue()
    pq.put((0, start, [start]))  # (current cost, current node, path)
    visited = set()

    while not pq.empty():
        cost, node, path = pq.get()  # Get node with the smallest cost

        if node in visited:  # Skip if already visited
            continue
        visited.add(node)

        if node == goal:  # Stop when goal is reached
            return cost, path

        for neighbor, weight in graph[node]:  # Explore neighbors
            if neighbor not in visited:
                pq.put((cost + weight, neighbor, path + [neighbor]))

    return -1, []  # Return -1 if goal is not reachable


# Example graph as a dictionary
graph = {
    'A': [('B', 1), ('C', 1)],
    'B': [('A', 1), ('C', 2), ('D', 5)],
    'C': [('A', 1), ('B', 2), ('D', 2)],
    'D': [('B', 5), ('C', 2), ('E', 3)],
    'E': [('D', 3)]
}

# Example usage
cost, path = uniform_cost_search(graph, 'A', 'E')
if path:
    print(f"Path: {path}, Cost: {cost}")
else:
    print("No path found.")

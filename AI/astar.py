from queue import PriorityQueue


def astar_algorithm(graph, start, goal, heuristic):
   
    open_list = PriorityQueue()
    open_list.put((0, start))  
    
    # Dictionary to store the g-costs (cost to reach each node)
    g_costs = {start: 0}
    
    # Dictionary to store the parent of each node (for path reconstruction)
    parent = {start: None}
    
    # Set to keep track of visited nodes (closed list)
    closed_list = set()
    
    while not open_list.empty():
        # Get the node with the lowest f-cost
        current_f, current_node = open_list.get()
        
        # If goal is reached, reconstruct and return the path
        if current_node == goal:
            path = []
            while current_node:
                path.append(current_node)
                current_node = parent[current_node]
            return path[::-1]  # Return the path in reverse order
        
        # Add current node to the closed list
        closed_list.add(current_node)
        
        # Explore neighbors
        for neighbor, cost in graph[current_node]:
            if neighbor in closed_list:
                continue
            
            # Calculate tentative g-cost
            tentative_g = g_costs[current_node] + cost
            
            # If neighbor is not in g_costs or we found a cheaper path
            if neighbor not in g_costs or tentative_g < g_costs[neighbor]:
                g_costs[neighbor] = tentative_g
                f_cost = tentative_g + heuristic[neighbor]
                open_list.put((f_cost, neighbor))
                parent[neighbor] = current_node
    
    return None  # Return None if no path is found

# Example graph (adjacency list with weights)
graph = {
    'A': [('B', 1), ('C', 9)],
    'B': [('A', 1), ('C', 2), ('D', 5)],
    'C': [('A', 4), ('B', 2), ('D', 1)],
    'D': [('B', 5), ('C', 1)]
}

# Heuristic values for each node (example values)
heuristic = {
    'A': 7,
    'B': 6,
    'C': 2,
    'D': 0  # Goal node
}

# Run the A* algorithm
start_node = 'A'
goal_node = 'D'
path = astar_algorithm(graph, start_node, goal_node, heuristic)

# Output the result
if path:
    print(f"Shortest path from {start_node} to {goal_node}: {' -> '.join(path)}")
else:
    print(f"No path found from {start_node} to {goal_node}")

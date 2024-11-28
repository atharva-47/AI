from queue import LifoQueue

def depth_limited_search(graph, start, goal, depth_limit):
    
    stack = LifoQueue()  # Stack for DFS
    stack.put((start, [start], 0))  # (current_node, path, current_depth)

    while not stack.empty():
        current_node, path, current_depth = stack.get()

        # Check if the current node is the goal
        if current_node == goal:
            return path

        # If within depth limit, explore neighbors
        if current_depth < depth_limit:
            for neighbor in graph[current_node]:
                if neighbor not in path:  # Avoid cycles
                    stack.put((neighbor, path + [neighbor], current_depth + 1))

    return None  # Return None if goal is not found within depth limit


# Example usage:
if __name__ == "__main__":
    # Define a sample graph as an adjacency list
    graph = {
        'A': ['B', 'C', 'D'],
        'B': ['E', 'C'],
        'C': ['F'],
        'D': [],
        'E': [],
        'F': ['H'],
        'G': [],
        'H': []
    }

    start_node = 'A'
    goal_node = 'H'
    depth_limit = 4

    result = depth_limited_search(graph, start_node, goal_node, depth_limit)
    if result:
        print("Path to goal:", result)
    else:
        print(f"Goal '{goal_node}' not found within depth limit {depth_limit}.")

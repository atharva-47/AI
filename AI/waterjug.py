#6.
from collections import deque

def water_jug_problem(capacity_a, capacity_b, target):
    
    # To track visited states
    visited = set()
    # Queue for BFS: holds tuples of (current amount in Jug A, current amount in Jug B, steps)
    queue = deque()
    queue.append((0, 0, []))  # Start with both jugs empty

    while queue:
        a, b, steps = queue.popleft()
        
        # If we reach the target
        if a == target:
            steps.append((a, 0))
            return f"Target achieved! Steps: {steps}"
        if b == target:
            steps.append((0, b))
            return f"Target achieved! Steps: {steps}"

        # If the state has been visited, skip it
        if (a, b) in visited:
            continue
        visited.add((a, b))

        # Possible actions
        actions = [
            (capacity_a, b),  # Fill Jug A
            (a, capacity_b),  # Fill Jug B
            (0, b),           # Empty Jug A
            (a, 0),           # Empty Jug B
            (max(a - (capacity_b - b), 0), min(b + a, capacity_b)),  # Pour A to B
            (min(a + b, capacity_a), max(b - (capacity_a - a), 0))   # Pour B to A
        ]

        for new_a, new_b in actions:
            if (new_a, new_b) not in visited:
                queue.append((new_a, new_b, steps + [(new_a, new_b)]))
    
    return "Target not achievable."

# Example usage
capacity_a = 4  # Capacity of Jug A
capacity_b = 3  # Capacity of Jug B
target = 2     # Desired amount

result = water_jug_problem(capacity_a, capacity_b, target)
print(result)

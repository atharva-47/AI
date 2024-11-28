def count_goal_states(states, goal_state):
    
    goal_count = 0
    for state in states:
        if state == goal_state:
            goal_count += 1
    return goal_count

# Example usage
states = [
    [1, 2, 3], 
    [4, 5, 6], 
    [1, 2, 3],   # Goal state example
    [7, 8, 9]
]
goal_state = [1, 2, 3]  # Define the goal state

# Count how many times the goal state appears in the list of states
goal_count = count_goal_states(states, goal_state)
print(f"Total number of goal states: {goal_count}")

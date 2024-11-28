import queue

def dfs(graph,start):
    visited = set()
    stack = queue.LifoQueue()
    stack.put(start)

    while not stack.empty():
        node = stack.get()
        if node not in visited:
            visited.add(node)
            print(node)
            for neighbor in graph[node]:
                stack.put(neighbor)

graph = {
    'A':['B','C'],
    'B':['D','E'],
    'C':['F'],
    'D':[],
    'E':[],
    'F':[]
}

dfs(graph,'A')
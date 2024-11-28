graph = {
    'A': [('B', 1), ('C', 1)],
    'B': [('A', 1), ('C', 2), ('D', 5)],
    'C': [('A', 1), ('B', 2), ('D', 2)],
    'D': [('B', 5), ('C', 2), ('E', 3)],
    'E': [('D', 3)]
}

from queue import PriorityQueue

def ucs(graph,start,goal):

    pq = PriorityQueue()
    
print("04_Jayprabha Nadar")
graph = {
    'A': set(['B', 'C']),
    'B': set(['A', 'D', 'E']),
    'C': set(['A', 'F']),
    'D': set(['B']),
    'E': set(['B', 'F']),
    'F': set(['C', 'E'])
}

# Implementing BFS Logic
def bfs(start):
    queue = [start]
    levels = {}  # Keeps track of levels (distance from start)
    levels[start] = 0  # Depth of start node is 0
    visited = set([start])  # Corrected this line
    
    while queue:
        node = queue.pop(0)
        neighbours = graph[node]
        
        for neighbor in neighbours:
            if neighbor not in visited:
                queue.append(neighbor)
                visited.add(neighbor)
                levels[neighbor] = levels[node] + 1
    
    print(levels)
    return visited

print(str(bfs('A')))

# For finding all BFS paths from start to goal
def bfs_paths(graph, start, goal):
    queue = [(start, [start])]
    
    while queue:
        (vertex, path) = queue.pop(0)
        
        for next in graph[vertex] - set(path):
            if next == goal:
                yield path + [next]
            else:
                queue.append((next, path + [next]))

result = list(bfs_paths(graph, 'A', 'F'))
print(result)

# For finding the shortest path using BFS
def shortest_path(graph, start, goal):
    try:
        return next(bfs_paths(graph, start, goal))
    except StopIteration:
        return None

result1 = shortest_path(graph, 'A', 'F')
print(result1)

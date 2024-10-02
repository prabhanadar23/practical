# Graph represented as an adjacency list using sets
print("04_Jayprabha Nadar")

graph1 = { 
    'A': set(['B', 'C']), 
    'B': set(['A', 'D', 'E']), 
    'C': set(['A', 'F']), 
    'D': set(['B']), 
    'E': set(['B', 'F']), 
    'F': set(['C', 'E']) 
}

# Depth-First Search (DFS) function
def dfs(graph, node, visited):
    if node not in visited:
        visited.append(node)  # Mark node as visited
        for n in graph[node]:  # Explore neighbors
            dfs(graph, n, visited)
    return visited

# Initialize DFS with an empty visited list
visited = dfs(graph1, 'A', [])

# Output the result
print(visited)

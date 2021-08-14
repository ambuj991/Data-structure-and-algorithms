# depth first traversal

graph = {
    'A' : ['B','C'],
    'B' : ['D', 'E'],
    'C' : ['F'],
    'D' : [],
    'E' : ['F'],
    'F' : []
}
visited = set()

def dft(visited, graph, node):
    if node not in visited:
        print(node, end=' ')
        visited.add(node)
        for i in graph[node]:
            dft(visited, graph, i)

dft(visited, graph, 'A')

# O(V+E), where V is the number of vertices and E is the number of edges

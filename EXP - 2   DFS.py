class Graph:
    def __init__(self, vertices):
        self.vertices = vertices
        self.graph = {i: [] for i in range(vertices)}
    def add_edge(self, u, v):
        self.graph[u].append(v)
        self.graph[v].append(u)

    def dfs(self, v, visited):
        print(v, end=" ")  
        visited[v] = True  

        for neighbor in self.graph[v]:
            if not visited[neighbor]:
                self.dfs(neighbor, visited)
def depth_first_search():
    vertices = int(input("Enter the number of vertices: "))
    g = Graph(vertices)
    edges = int(input("Enter the number of edges: "))
    for _ in range(edges):
        u, v = map(int, input("Enter edge (u v): ").split())
        g.add_edge(u, v)
    visited = [False] * g.vertices
    start_node = int(input("Enter the starting node for DFS: "))
    print(f"Depth First Search starting from vertex {start_node}:")
    g.dfs(start_node, visited)
    
depth_first_search()

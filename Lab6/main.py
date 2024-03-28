from edgegraph import *

def bfs(graph: GraphEL, start: VertexEL) -> list:
    if graph is None or start is None or start not in graph.vertices():
        return []
    
    print("end of bfs")

graph = GraphEL()
vertex1 = VertexEL("1")
vertex2 = VertexEL("2")

graph.add_vertex(vertex1)

bfs(graph, vertex1)
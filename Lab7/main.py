from edgegraph import *


def bellman_ford(graph: GraphEL, start: VertexEL, end: VertexEL) -> list:
    if graph is None or start is None or end is None:
        return []
    if start not in graph.vertices() or end not in graph.vertices():
        return []
    
    # Logic for returning a path from a vertex to itself?
    
    
    
    
    

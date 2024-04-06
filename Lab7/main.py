from edgegraph import *
import sys


def bellman_ford(graph: GraphEL, start: VertexEL, end: VertexEL) -> list:
    if not validate_args(graph, start, end):
        if start == end:
            return [start]
        else:
            return []
    
    vertex_dictionary, vertex_path = {}, {}
    
    for i in graph.vertices():
        vertex_dictionary[i.name] = sys.maxsize
        
    vertex_dictionary[start.name] = 0
    
    for i in range(graph.num_vertices() - 1):
        for j in graph.edges():
            if j.get_value() <= 0:
                return []
            edge_relax(j, vertex_dictionary, vertex_path)
            
    shortest_path = [end]
    search = end
    
    while search != start:
        search = vertex_path[search.name]
        shortest_path.append(search)
      
    shortest_path.reverse()  
    return shortest_path            
            

def edge_relax(edge, dict, path):
    current_distance = dict[edge.tail().name]
    compare_distance = dict[edge.head().name]
    
    if (current_distance + edge.get_value()) < compare_distance:
        dict[edge.head().name] = current_distance + edge.get_value()
        path[edge.head().name] = edge.tail()
     
        
def validate_args(graph, start, end):
    if not isinstance(graph, GraphEL) \
            or not isinstance(start, VertexEL) \
            or not isinstance(end, VertexEL):
        return False
    
    if start == end \
            or start not in graph.vertices() \
            or end not in graph.vertices():
        return False
    
    return True

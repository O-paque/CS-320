from edgegraph import *
import sys


def bellman_ford(graph: GraphEL, start: VertexEL, end: VertexEL) -> list:
    if graph is None or start is None or end is None:
        return []
    if start not in graph.vertices():
        return []
    if start == end:
        return [start]
    
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
    
    # print("Dictionary: " , vertex_dictionary)
    # print("Path: " , vertex_path)
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

# graph = GraphEL()
# vertex1 = VertexEL("1")
# vertex2 = VertexEL("2")
# vertex3 = VertexEL("3")
# vertex4 = VertexEL("4")
# vertex5 = VertexEL("5")
# vertex6 = VertexEL("6")
# vertex7 = VertexEL("7")

# edgeA12 = EdgeEL("A12", vertex1, vertex2)
# edgeB23 = EdgeEL("B23", vertex2, vertex3)
# edgeC34 = EdgeEL("C34", vertex3, vertex4)
# edgeD45 = EdgeEL("D45", vertex4, vertex5)
# edgeE56 = EdgeEL("E56", vertex5, vertex6)
# edgeF61 = EdgeEL("F61", vertex6, vertex1)
# edgeG14 = EdgeEL("G14", vertex1, vertex4)
# edgeH37 = EdgeEL("H37", vertex3, vertex7)

# edgeF16 = EdgeEL("F16", vertex1, vertex6)
# edgeE65 = EdgeEL("E65", vertex6, vertex5)
# edgeD54 = EdgeEL("D54", vertex5, vertex4)
# edgeC43 = EdgeEL("C43", vertex4, vertex3)

# edgeA12.set_value(1)
# edgeB23.set_value(10)
# edgeC34.set_value(1)
# edgeD45.set_value(1)
# edgeE56.set_value(1)
# edgeF61.set_value(1)
# edgeG14.set_value(4)
# edgeH37.set_value(2)

# edgeF16.set_value(1)
# edgeE65.set_value(1)
# edgeD54.set_value(1)
# edgeC43.set_value(1)

# graph.add_edge(edgeA12)
# graph.add_edge(edgeB23)
# graph.add_edge(edgeC34)
# graph.add_edge(edgeD45)
# graph.add_edge(edgeE56)
# graph.add_edge(edgeF61)
# graph.add_edge(edgeG14)
# graph.add_edge(edgeH37)

# graph.add_edge(edgeF16)
# graph.add_edge(edgeE65)
# graph.add_edge(edgeD54)
# graph.add_edge(edgeC43)

# print("Graph: " , graph)

# result = bellman_ford(graph, vertex1, vertex7)

# print("Result: " , result)

from edgegraph import *

def bfs(graph: GraphEL, start: VertexEL) -> list:
    if graph is None or start is None or start not in graph.vertices():
        return []
    
    searched_list, current_list = [], []
    searched_list.append(start)
    current_list.append(start)
    
    while len(current_list) > 0:
        adjacent = graph.adjacent_vertices(current_list.pop(0))
        print(adjacent)
    
    
    print("end of bfs")

graph = GraphEL()
vertex1 = VertexEL("1")
vertex2 = VertexEL("2")
vertex3 = VertexEL("3")
vertex4 = VertexEL("4")
vertex5 = VertexEL("5")
vertex6 = VertexEL("6")
vertex7 = VertexEL("7")

edgeA = EdgeEL("A", vertex1, vertex2)
edgeB = EdgeEL("B", vertex2, vertex3)
edgeC = EdgeEL("C", vertex3, vertex4)
edgeD = EdgeEL("D", vertex4, vertex5)
edgeE = EdgeEL("E", vertex5, vertex6)
edgeF = EdgeEL("F", vertex6, vertex1)
edgeG = EdgeEL("G", vertex1, vertex4)
edgeH = EdgeEL("H", vertex3, vertex7)

graph.add_edge(edgeA)
graph.add_edge(edgeB)
graph.add_edge(edgeC)
graph.add_edge(edgeD)
graph.add_edge(edgeE)
graph.add_edge(edgeF)
graph.add_edge(edgeG)
graph.add_edge(edgeH)

print(graph)

bfs(graph, vertex1)
from edgegraph import *


def bfs(graph: GraphEL, start: VertexEL) -> list:
    if graph is None or start is None or start not in graph.vertices():
        return []
    
    searched_list, current_list = [], []
    searched_list.append(start)
    current_list.append(start)
    
    while len(current_list) > 0:
        adjacent = graph.adjacent_vertices(current_list.pop(0))

        while len(adjacent) > 0:
            temp_vertex = adjacent.pop(0)

            if temp_vertex not in searched_list:
                searched_list.append(temp_vertex)
                current_list.append(temp_vertex)

    return searched_list

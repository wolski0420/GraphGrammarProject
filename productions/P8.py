from utils.SameCoordsMatcher import SameCoordsMatcher
from utils.StandardizedGraph import StandardizedGraph, Vert

def P8(graph: StandardizedGraph, v0_group: list, v1_group: list):

    for idx, x in enumerate(v1_group):
        for z in v0_group:
            if x==z:
                v0 = x
                idx0 = idx
    # idx0 = v0_group.index(v0)
    print(idx0)
    if idx0 == 0:
        v1_vertices = [v0_group[1]] + [v1_group[1]]
        v2_vertices = [v0_group[2]] + [v1_group[2]]
    else:
        v1_vertices = [v0_group[1]] + [v1_group[1]]
        v2_vertices = [v0_group[0]] + [v1_group[0]]

    v1_0_neigh = (graph.get_neighbours(v1_vertices[0], v1_vertices[0].level(), label="I") +
                  graph.get_neighbours(v1_vertices[0], v1_vertices[0].level(), label="E"))
    v1_0_neigh.remove(v0.underlying)
    v1_0_neigh.remove(v2_vertices[0].underlying)

    v2_0_neigh = (graph.get_neighbours(v2_vertices[0], v2_vertices[0].level(), label="I") +
                  graph.get_neighbours(v2_vertices[0], v2_vertices[0].level(), label="E"))
    v2_0_neigh.remove(v1_vertices[0].underlying)

    graph.remove_vertex(v1_vertices[0])
    graph.remove_vertex(v2_vertices[0])


    for neigh_1 in v1_0_neigh:
        graph.add_edge(v1_vertices[1], Vert(graph.underlying, neigh_1))

    for neigh_2 in v2_0_neigh:
        graph.add_edge(v2_vertices[1], Vert(graph.underlying, neigh_2))

    return graph

def match_P8(graph: StandardizedGraph, level: int):
    matcher = SameCoordsMatcher(2)    
    return matcher.match(graph, level)

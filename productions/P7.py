from utils.SameCoordsMatcher import SameCoordsMatcher
from utils.StandardizedGraph import StandardizedGraph, Vert

def P7(graph: StandardizedGraph, v0_group: list, v1_group: list):

    # # find vertices on the same position
    v0_vertices = [v0_group[0]] + [v1_group[0]]
    v1_vertices = [v0_group[1]] + [v1_group[1]]
    v2_vertices = [v0_group[2]] + [v1_group[2]]

    # find neighbours of one vertex on each position
    v0_0_neigh = (graph.get_neighbours(v0_vertices[0], v0_vertices[0].level(), label = "I") +
                 graph.get_neighbours(v0_vertices[0], v0_vertices[0].level(), label = "E"))
    v0_0_neigh.remove(v1_vertices[0].underlying)

    v1_0_neigh = (graph.get_neighbours(v1_vertices[0], v1_vertices[0].level(), label="I") +
                  graph.get_neighbours(v1_vertices[0], v1_vertices[0].level(), label="E"))
    v1_0_neigh.remove(v0_vertices[0].underlying)
    v1_0_neigh.remove(v2_vertices[0].underlying)

    v2_0_neigh = (graph.get_neighbours(v2_vertices[0], v2_vertices[0].level(), label="I") +
                 graph.get_neighbours(v2_vertices[0], v2_vertices[0].level(), label="E"))
    v2_0_neigh.remove(v1_vertices[0].underlying)

    # remove one repeated vertex
    graph.remove_vertex(v0_vertices[0])
    graph.remove_vertex(v1_vertices[0])
    graph.remove_vertex(v2_vertices[0])

    # add edges for remaining vertex
    for neigh_0 in v0_0_neigh:
        graph.add_edge(v0_vertices[1], Vert(graph.underlying, neigh_0))

    for neigh_1 in v1_0_neigh:
        graph.add_edge(v1_vertices[1], Vert(graph.underlying, neigh_1))

    for neigh_2 in v2_0_neigh:
        graph.add_edge(v2_vertices[1], Vert(graph.underlying, neigh_2))

    return graph

def get_e_neighs(graph, i):
    e = []
    for child in graph.get_neighbours(i, i.level+1, 'I'):
        e += graph.get_neighbours(child, child.level, 'E')
        
    return list(set(e))

def match_P7(graph: StandardizedGraph, level:int):
    matcher = SameCoordsMatcher(3)    
    return matcher.match(graph, level)

       

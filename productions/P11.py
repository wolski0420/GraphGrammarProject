from utils.SameCoordsOneEdgeBrokenMatcher import SameCoordsMatcherOneEdgeBroken
from utils.StandardizedGraph import StandardizedGraph, Vert

def P11(graph: StandardizedGraph, v0_group: list, v1_group: list):

    # # find vertices on the same position
    v0_vertices = [v0_group[0]] + [v1_group[0]]
    v1_vertices = [v0_group[1]] + [v1_group[1]]
    # v2_vertices = [v0_group[2]] + [v1_group[2]]

    # find neighbours of one vertex on each position
    v0_1_neigh = (graph.get_neighbours(v1_vertices[0], v1_vertices[0].level(), label = "I") +
                 graph.get_neighbours(v1_vertices[0], v1_vertices[0].level(), label = "E"))
    v0_1_neigh.remove(v1_vertices[1].underlying)

    v1_1_neigh = (graph.get_neighbours(v1_vertices[1], v1_vertices[1].level(), label="I") +
                  graph.get_neighbours(v1_vertices[1], v1_vertices[1].level(), label="E"))
    v1_1_neigh.remove(v1_vertices[0].underlying)

    # remove one repeated vertex
    graph.remove_vertex(v1_vertices[0])
    graph.remove_vertex(v1_vertices[1])

    # add edges for remaining vertex
    for neigh_0 in v0_1_neigh:
        graph.add_edge(v0_vertices[0], Vert(graph.underlying, neigh_0))

    for neigh_1 in v1_1_neigh:
        graph.add_edge(v0_vertices[1], Vert(graph.underlying, neigh_1))

    return graph

def match_P11(graph: StandardizedGraph, level:int):
    matcher = SameCoordsMatcherOneEdgeBroken(2)    
    return matcher.match(graph, level)

       

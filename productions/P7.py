from utils.StandardizedGraph import StandardizedGraph, Vert

def P7(graph: StandardizedGraph, v0: Vert, v1: Vert,v2: Vert ):

    # find vertices on the same position
    v0_vertices = graph.find_by_pos(v0.pos_x(), v0.pos_y())
    v1_vertices = graph.find_by_pos(v1.pos_x(), v1.pos_y())
    v2_vertices = graph.find_by_pos(v2.pos_x(), v2.pos_y())

    # find neighbours of one vertex on each position
    v0_0_neigh = (graph.get_neighbours(v0_vertices[0], v0.level(), label = "I") +
                 graph.get_neighbours(v0_vertices[0], v0.level(), label = "E"))
    v0_0_neigh.remove(v1_vertices[0].underlying)

    v1_0_neigh = (graph.get_neighbours(v1_vertices[0], v1.level(), label="I") +
                  graph.get_neighbours(v1_vertices[0], v1.level(), label="E"))
    v1_0_neigh.remove(v0_vertices[0].underlying)
    v1_0_neigh.remove(v2_vertices[0].underlying)

    v2_0_neigh = (graph.get_neighbours(v2_vertices[0], v2.level(), label="I") +
                 graph.get_neighbours(v2_vertices[0], v2.level(), label="E"))
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

def match_P7(graph: StandardizedGraph, level:int):
    # graph.in

    return []

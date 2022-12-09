from utils import StandardizedGraph

def P1(graph: StandardizedGraph):
    v0 = graph.find_by_label("El")[0]
    level = v0.level()

    graph.modify_label(v0, "el")

    v1 = graph.add_vert(pos_x = 0, pos_y = 0, level = level + 1, label = "I")
    v2 = graph.add_vert(pos_x = -10, pos_y = 10, level = level + 1, label = "E")
    v3 = graph.add_vert(pos_x = 10, pos_y = 10, level = level + 1, label = "E")
    v4 = graph.add_vert(pos_x = 10, pos_y = -10, level = level + 1, label = "E")
    v5 = graph.add_vert(pos_x = -10, pos_y = -10, level = level + 1, label = "E")

    graph.add_edges([(v1,v2), (v1,v3), (v1,v4), (v1,v5), (v2,v3), (v3,v4), (v4, v5), (v5, v2)])
    graph.add_edge(v0, v1)

    return graph

from utils.StandardizedGraph import StandardizedGraph, Vert


def P1(graph: StandardizedGraph, v0: Vert):
    level = v0.level()

    graph.modify_label(v0, "el")

    x, y = v0.pos_x(), v0.pos_y()

    v1 = graph.add_vert(pos_x=x, pos_y=y, level=level + 1, label="I")
    v2 = graph.add_vert(pos_x=x - 10, pos_y=y + 10, level=level + 1, label="E")
    v3 = graph.add_vert(pos_x=x + 10, pos_y=y + 10, level=level + 1, label="E")
    v4 = graph.add_vert(pos_x=x + 10, pos_y=y - 10, level=level + 1, label="E")
    v5 = graph.add_vert(pos_x=x - 10, pos_y=y - 10, level=level + 1, label="E")

    graph.add_edges([(v1, v2), (v1, v3), (v1, v4), (v1, v5), (v2, v3), (v3, v4), (v4, v5), (v5, v2)])
    graph.add_edge(v0, v1)

    return graph


def match_P1(graph: StandardizedGraph):
    return graph.find_by_label("El")

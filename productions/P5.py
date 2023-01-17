from utils.StandardizedGraph import StandardizedGraph, Vert
from utils.SurroundingMatcher import SurroundingMatcher


def P5(graph: StandardizedGraph, v: Vert):
    level = v.level()

    graph.modify_label(v, "i")

    e1_left, e2_left, e3_left, e4_left = get_surrounding_e_coordinates(graph, v)

    e1 = graph.add_vert(pos_x=e1_left.pos_x(), pos_y=e1_left.pos_y(), level=level + 1, label="E")
    e2 = graph.add_vert(pos_x=e2_left.pos_x(), pos_y=e2_left.pos_y(), level=level + 1, label="E")
    e3 = graph.add_vert(pos_x=e3_left.pos_x(), pos_y=e3_left.pos_y(), level=level + 1, label="E")
    e4 = graph.add_vert(pos_x=e4_left.pos_x(), pos_y=e4_left.pos_y(), level=level + 1, label="E")

    e12 = add_node_in_the_middle(graph, [e1, e2], level + 1, "E")
    graph.add_edges([(e1, e12), (e2, e12)])
    e23 = add_node_in_the_middle(graph, [e2, e3], level + 1, "E")
    graph.add_edges([(e2, e23), (e3, e23)])
    e14 = add_node_in_the_middle(graph, [e1, e4], level + 1, "E")
    graph.add_edges([(e1, e14), (e4, e14)])
    e34 = add_node_in_the_middle(graph, [e3, e4], level + 1, "E")
    graph.add_edges([(e3, e34), (e4, e34)])

    e1234 = add_node_in_the_middle(graph, [e1, e2, e3, e4], level + 1, "E")
    graph.add_edges([(e12, e1234), (e23, e1234), (e14, e1234), (e34, e1234)])

    i1 = add_node_in_the_middle(graph, [e1, e12, e14, e1234], level + 1, "I")
    graph.add_edges([
        (i1, e1), (i1, e12), (i1, e14), (i1, e1234),
        (v, i1)
    ])

    i2 = add_node_in_the_middle(graph, [e2, e12, e23, e1234], level + 1, "I")
    graph.add_edges([
        (i2, e2), (i2, e12), (i2, e23), (i2, e1234),
        (v, i2)
    ])

    i3 = add_node_in_the_middle(graph, [e4, e14, e34, e1234], level + 1, "I")
    graph.add_edges([
        (i3, e4), (i3, e14), (i3, e34), (i3, e1234),
        (v, i3)
    ])

    i4 = add_node_in_the_middle(graph, [e3, e23, e34, e1234], level + 1, "I")
    graph.add_edges([
        (i4, e3), (i4, e23), (i4, e34), (i4, e1234),
        (v, i4)
    ])
    return graph


def add_node_in_the_middle(graph, vertices, level, label):
    x, y = get_middle(vertices)
    return graph.add_vert(
        pos_x=x,
        pos_y=y,
        level=level,
        label=label
    )


def get_surrounding_e_coordinates(graph, i_vert):
    e_neighbours = graph.get_neighbours(i_vert, i_vert.level(), "E")
    return tuple(map(
        lambda neigh: Vert(graph.underlying, neigh),
        e_neighbours
    ))


def get_middle(e_verts):
    x_middle = sum(map(
        lambda vert: vert.pos_x(),
        e_verts
    )) / len(e_verts)

    y_middle = sum(map(
        lambda vert: vert.pos_y(),
        e_verts
    )) / len(e_verts)

    return x_middle, y_middle


def match_P5(graph: StandardizedGraph, level: int):
    matcher = SurroundingMatcher(3)
    return matcher.match(graph, level)

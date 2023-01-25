from utils.StandardizedGraph import StandardizedGraph, Vert
import networkx as nx
from networkx.algorithms.isomorphism import is_isomorphic


def P10(graph: StandardizedGraph, v: Vert):
    graph.modify_label(v, "i")

    v_level = v.level()
    old_lu, old_ru, old_ll, old_rl = _get_corner_vertices(graph, v)

    left_upper = graph.add_vert(old_lu.pos_x(), old_lu.pos_y(), old_lu.label(), v_level + 1)
    right_upper = graph.add_vert(old_ru.pos_x(), old_ru.pos_y(), old_ru.label(), v_level + 1)
    left_lower = graph.add_vert(old_ll.pos_x(), old_ll.pos_y(), old_ll.label(), v_level + 1)
    right_lower = graph.add_vert(old_rl.pos_x(), old_rl.pos_y(), old_rl.label(), v_level + 1)

    i_middle = _create_vertex_between(graph, left_upper, right_lower, label="I")

    graph.add_edges([
        (v, i_middle), (left_upper, right_upper), (right_upper, right_lower), (right_lower, left_lower), (left_lower, left_upper),
        (i_middle, left_upper), (i_middle, left_lower), (i_middle, right_lower), (i_middle, right_upper),
    ])

    return graph


def _get_corner_vertices(graph: StandardizedGraph, v: Vert):
    valid_v_neighbors = _get_valid_vertex_neighbours(graph, v)

    neighbors_as_vert = [Vert(graph.underlying, index) for index in valid_v_neighbors]
    neighbors_as_vert.sort(key=lambda n: (n.pos_x(), n.pos_y()))

    # left-to-right & up-to-down order
    return neighbors_as_vert[1], neighbors_as_vert[3], neighbors_as_vert[0], neighbors_as_vert[2]


def _create_vertex_between(graph: StandardizedGraph, v1: Vert, v2: Vert, label="E"):
    return graph.add_vert((v1.pos_x() + v2.pos_x()) / 2, (v1.pos_y() + v2.pos_y()) / 2, label, v1.level())


def match_P10(graph: StandardizedGraph, level: int):
    vertices = []

    for i in graph.find_by_label("I"):
        if i.level() != level:
            continue

        subgraph = _create_candidate(graph, i)
        expected_subgraph = _create_expected_subgraph()

        # checking labels is unnecessary because we are taking
        # appropriate vertices before isomorphism test
        if is_isomorphic(subgraph, expected_subgraph):
            vertices.append(i)

    return vertices


def _create_candidate(graph: StandardizedGraph, v: Vert):
    return graph.underlying.subgraph(_get_valid_vertex_neighbours(graph, v) + [v.underlying])


def _get_valid_vertex_neighbours(graph: StandardizedGraph, v: Vert):
    v_level = v.level()

    g = graph.underlying
    v_neighbors = g.neighbors(v.underlying)

    return [
        n for n in v_neighbors
        if nx.get_node_attributes(g, "level")[n] == v_level
        and nx.get_node_attributes(g, "label")[n] == "E"
    ]


def _create_expected_subgraph():
    g = nx.Graph()
    g.add_nodes_from([  # labels are not compared
        (0, {"label": "I"}),
        (1, {"label": "E"}),
        (2, {"label": "E"}),
        (3, {"label": "E"}),
        (4, {"label": "E"})
    ])
    g.add_edges_from([
        (0, 1), (0, 2), (0, 3), (0, 4), (1, 2), (2, 3), (3, 4), (4, 1)
    ])

    return g

from utils.StandardizedGraph import StandardizedGraph, Vert
import networkx as nx
import unittest
from utils.SurroundingMatcher import SurroundingMatcher
from utils.vis import visualise_graph


def P3(graph: StandardizedGraph, v: Vert):
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
    e_neighbours = get_neighbours(graph, i_vert, i_vert.level(), "E")
    return tuple(map(
        lambda neigh: Vert(graph.underlying, neigh),
        e_neighbours
    ))


def get_neighbours(graph, vertex, level: int, label: str):
    return list(filter(
        lambda neigh: nx.get_node_attributes(graph.underlying, "level")[neigh] == level \
                      and nx.get_node_attributes(graph.underlying, "label")[neigh] == label,
        graph.underlying.neighbors(vertex.underlying)
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


def match_P3(graph: StandardizedGraph, level: int):
    matcher = SurroundingMatcher(1)
    return matcher.match(graph, level)


class TestP3(unittest.TestCase):
    def test_match_P3_correct(self):
        level = 0
        base_graph = StandardizedGraph()
        e1 = base_graph.add_vert(pos_x=-4, pos_y=4, level=level, label="E")
        e2 = base_graph.add_vert(pos_x=4, pos_y=4, level=level, label="E")
        e3 = base_graph.add_vert(pos_x=4, pos_y=-4, level=level, label="E")
        e4 = base_graph.add_vert(pos_x=-4, pos_y=-4, level=level, label="E")
        e5 = base_graph.add_vert(pos_x=-4, pos_y=0, level=level, label="E")
        i1 = base_graph.add_vert(pos_x=0, pos_y=0, level=level, label="I")
        base_graph.add_edges([(e1, e2), (e2, e3), (e3, e4), (e4, e5), (e5, e1)])
        base_graph.add_edges([(i1, e1), (i1, e2), (i1, e3), (i1, e4)])
        
        # for debugging
        # visualise_graph(base_graph, level)

        i_match = match_P3(base_graph, level)[0]
        self.assertEqual(i_match, i1)

        new_graph = P3(base_graph, i_match)

        expected_graph = StandardizedGraph()
        old_e1 = expected_graph.add_vert(pos_x=-4, pos_y=4, level=level, label="E")
        old_e2 = expected_graph.add_vert(pos_x=4, pos_y=4, level=level, label="E")
        old_e3 = expected_graph.add_vert(pos_x=4, pos_y=-4, level=level, label="E")
        old_e4 = expected_graph.add_vert(pos_x=-4, pos_y=-4, level=level, label="E")
        old_e5 = expected_graph.add_vert(pos_x=-4, pos_y=0, level=level, label="E")
        # small 'i', because this is the right side of production
        old_i1 = expected_graph.add_vert(pos_x=0, pos_y=0, level=level, label="i")
        expected_graph.add_edges(
            [(old_e1, old_e2), (old_e2, old_e3), (old_e3, old_e4), (old_e4, old_e5), (old_e5, old_e1)])
        expected_graph.add_edges([(old_i1, old_e1), (old_i1, old_e2), (old_i1, old_e3), (old_i1, old_e4)])

        e1 = expected_graph.add_vert(pos_x=-4, pos_y=4, level=level + 1, label="E")
        e2 = expected_graph.add_vert(pos_x=4, pos_y=4, level=level + 1, label="E")
        e3 = expected_graph.add_vert(pos_x=4, pos_y=-4, level=level + 1, label="E")
        e4 = expected_graph.add_vert(pos_x=-4, pos_y=-4, level=level + 1, label="E")

        e12 = expected_graph.add_vert(pos_x=0, pos_y=4, level=level + 1, label="E")
        e23 = expected_graph.add_vert(pos_x=4, pos_y=0, level=level + 1, label="E")
        e34 = expected_graph.add_vert(pos_x=0, pos_y=-4, level=level + 1, label="E")
        e14 = expected_graph.add_vert(pos_x=-4, pos_y=0, level=level + 1, label="E")
        e1234 = expected_graph.add_vert(pos_x=0, pos_y=0, level=level + 1, label="E")

        expected_graph.add_edges([
            (e1, e12), (e2, e12),
            (e2, e23), (e3, e23),
            (e1, e14), (e4, e14),
            (e3, e34), (e4, e34),
            (e12, e1234), (e23, e1234), (e14, e1234), (e34, e1234)
        ])

        i1 = expected_graph.add_vert(pos_x=-2, pos_y=2, level=level + 1, label="I")
        expected_graph.add_edges([(i1, e1), (i1, e12), (i1, e14), (i1, e1234), (old_i1, i1)])

        i2 = expected_graph.add_vert(pos_x=2, pos_y=2, level=level + 1, label="I")
        expected_graph.add_edges([(i2, e2), (i2, e12), (i2, e23), (i2, e1234), (old_i1, i2)])

        i3 = expected_graph.add_vert(pos_x=2, pos_y=-2, level=level + 1, label="I")
        expected_graph.add_edges([(i3, e3), (i3, e23), (i3, e34), (i3, e1234), (old_i1, i3)])

        i4 = expected_graph.add_vert(pos_x=-2, pos_y=-2, level=level + 1, label="I")
        expected_graph.add_edges([(i4, e4), (i4, e14), (i4, e34), (i4, e1234), (old_i1, i4)])
        
        # for debugging
        # visualise_graph(new_graph, level + 1)
        # visualise_graph(expected_graph, level + 1)

        self.assertEqual(new_graph, expected_graph)

    def test_match_P3_correct_rotated(self):
        level = 0
        base_graph = StandardizedGraph()
        e1 = base_graph.add_vert(pos_x=-4, pos_y=4, level=level, label="E")
        e2 = base_graph.add_vert(pos_x=4, pos_y=4, level=level, label="E")
        e3 = base_graph.add_vert(pos_x=4, pos_y=-4, level=level, label="E")
        e4 = base_graph.add_vert(pos_x=-4, pos_y=-4, level=level, label="E")
        e5 = base_graph.add_vert(pos_x=0, pos_y=4, level=level, label="E")
        i1 = base_graph.add_vert(pos_x=0, pos_y=0, level=level, label="I")
        base_graph.add_edges([(e1, e5), (e5, e2), (e2, e3), (e3, e4), (e4, e1)])
        base_graph.add_edges([(i1, e1), (i1, e2), (i1, e3), (i1, e4)])

        # for debugging
        # visualise_graph(base_graph, level)

        i_match = match_P3(base_graph, level)[0]
        self.assertEqual(i_match, i1)

        new_graph = P3(base_graph, i_match)

        expected_graph = StandardizedGraph()
        old_e1 = expected_graph.add_vert(pos_x=-4, pos_y=4, level=level, label="E")
        old_e2 = expected_graph.add_vert(pos_x=4, pos_y=4, level=level, label="E")
        old_e3 = expected_graph.add_vert(pos_x=4, pos_y=-4, level=level, label="E")
        old_e4 = expected_graph.add_vert(pos_x=-4, pos_y=-4, level=level, label="E")
        old_e5 = expected_graph.add_vert(pos_x=0, pos_y=4, level=level, label="E")
        # small 'i', because this is the right side of production
        old_i1 = expected_graph.add_vert(pos_x=0, pos_y=0, level=level, label="i")
        expected_graph.add_edges(
            [(old_e1, old_e5), (old_e5, old_e2), (old_e2, old_e3), (old_e3, old_e4), (old_e4, old_e1)])
        expected_graph.add_edges([(old_i1, old_e1), (old_i1, old_e2), (old_i1, old_e3), (old_i1, old_e4)])

        e1 = expected_graph.add_vert(pos_x=-4, pos_y=4, level=level + 1, label="E")
        e2 = expected_graph.add_vert(pos_x=4, pos_y=4, level=level + 1, label="E")
        e3 = expected_graph.add_vert(pos_x=4, pos_y=-4, level=level + 1, label="E")
        e4 = expected_graph.add_vert(pos_x=-4, pos_y=-4, level=level + 1, label="E")

        e12 = expected_graph.add_vert(pos_x=0, pos_y=4, level=level + 1, label="E")
        e23 = expected_graph.add_vert(pos_x=4, pos_y=0, level=level + 1, label="E")
        e34 = expected_graph.add_vert(pos_x=0, pos_y=-4, level=level + 1, label="E")
        e14 = expected_graph.add_vert(pos_x=-4, pos_y=0, level=level + 1, label="E")
        e1234 = expected_graph.add_vert(pos_x=0, pos_y=0, level=level + 1, label="E")

        expected_graph.add_edges([
            (e1, e12), (e2, e12),
            (e2, e23), (e3, e23),
            (e1, e14), (e4, e14),
            (e3, e34), (e4, e34),
            (e12, e1234), (e23, e1234), (e14, e1234), (e34, e1234)
        ])

        i1 = expected_graph.add_vert(pos_x=-2, pos_y=2, level=level + 1, label="I")
        expected_graph.add_edges([(i1, e1), (i1, e12), (i1, e14), (i1, e1234), (old_i1, i1)])

        i2 = expected_graph.add_vert(pos_x=2, pos_y=2, level=level + 1, label="I")
        expected_graph.add_edges([(i2, e2), (i2, e12), (i2, e23), (i2, e1234), (old_i1, i2)])

        i3 = expected_graph.add_vert(pos_x=2, pos_y=-2, level=level + 1, label="I")
        expected_graph.add_edges([(i3, e3), (i3, e23), (i3, e34), (i3, e1234), (old_i1, i3)])

        i4 = expected_graph.add_vert(pos_x=-2, pos_y=-2, level=level + 1, label="I")
        expected_graph.add_edges([(i4, e4), (i4, e14), (i4, e34), (i4, e1234), (old_i1, i4)])

        # for debugging
        # visualise_graph(new_graph, level + 1)
        # visualise_graph(expected_graph, level + 1)

        self.assertEqual(new_graph, expected_graph)

    def test_match_P3_incorrect_pos(self):
        level = 0
        base_graph = StandardizedGraph()
        e1 = base_graph.add_vert(pos_x=-4, pos_y=4, level=level, label="E")
        e2 = base_graph.add_vert(pos_x=4, pos_y=4, level=level, label="E")
        e3 = base_graph.add_vert(pos_x=4, pos_y=-4, level=level, label="E")
        e4 = base_graph.add_vert(pos_x=-4, pos_y=-4, level=level, label="E")
        e5 = base_graph.add_vert(pos_x=-4, pos_y=2, level=level, label="E")
        i1 = base_graph.add_vert(pos_x=0, pos_y=0, level=level, label="I")
        base_graph.add_edges([(e1, e2), (e2, e3), (e3, e4), (e4, e5), (e5, e1)])
        base_graph.add_edges([(i1, e1), (i1, e2), (i1, e3), (i1, e4)])
        
        # for debugging
        # visualise_graph(base_graph, level)

        i_match = match_P3(base_graph, level)
        self.assertEqual(i_match, [])

    def test_match_P3_incorrect_missing(self):
        level = 0
        base_graph = StandardizedGraph()
        e1 = base_graph.add_vert(pos_x=-4, pos_y=4, level=level, label="E")
        e2 = base_graph.add_vert(pos_x=4, pos_y=4, level=level, label="E")
        e3 = base_graph.add_vert(pos_x=4, pos_y=-4, level=level, label="E")
        e4 = base_graph.add_vert(pos_x=-4, pos_y=-4, level=level, label="E")
        i1 = base_graph.add_vert(pos_x=0, pos_y=0, level=level, label="I")
        base_graph.add_edges([(e1, e2), (e2, e3), (e3, e4), (e4, e1)])
        base_graph.add_edges([(i1, e1), (i1, e2), (i1, e3), (i1, e4)])
        
        # for debugging
        # visualise_graph(base_graph, level)

        i_match = match_P3(base_graph, level)
        self.assertEqual(i_match, [])

    def test_match_P3_incorrect_too_many(self):
        level = 0
        base_graph = StandardizedGraph()
        e1 = base_graph.add_vert(pos_x=-4, pos_y=4, level=level, label="E")
        e2 = base_graph.add_vert(pos_x=4, pos_y=4, level=level, label="E")
        e3 = base_graph.add_vert(pos_x=4, pos_y=-4, level=level, label="E")
        e4 = base_graph.add_vert(pos_x=-4, pos_y=-4, level=level, label="E")
        e5 = base_graph.add_vert(pos_x=-4, pos_y=0, level=level, label="E")
        e6 = base_graph.add_vert(pos_x=0, pos_y=4, level=level, label="E")
        i1 = base_graph.add_vert(pos_x=0, pos_y=0, level=level, label="I")
        base_graph.add_edges([(e1, e6), (e6, e2), (e2, e3), (e3, e4), (e4, e5), (e5, e1)])
        base_graph.add_edges([(i1, e1), (i1, e2), (i1, e3), (i1, e4)])
        
        # for debugging
        # visualise_graph(base_graph, level)

        i_match = match_P3(base_graph, level)
        self.assertEqual(i_match, [])

    def test_match_P3_correct_large(self):
        level = 0
        base_graph = StandardizedGraph()
        e1 = base_graph.add_vert(pos_x=-4, pos_y=4, level=level, label="E")
        e2 = base_graph.add_vert(pos_x=4, pos_y=4, level=level, label="E")
        e3 = base_graph.add_vert(pos_x=4, pos_y=-4, level=level, label="E")
        e4 = base_graph.add_vert(pos_x=-4, pos_y=-4, level=level, label="E")
        e5 = base_graph.add_vert(pos_x=-4, pos_y=0, level=level, label="E")
        i1 = base_graph.add_vert(pos_x=0, pos_y=0, level=level, label="I")
        e6 = base_graph.add_vert(pos_x=-12, pos_y=-4, level=level, label="E")
        e7 = base_graph.add_vert(pos_x=-12, pos_y=4, level=level, label="E")
        i2 = base_graph.add_vert(pos_x=-8, pos_y=0, level=level, label="I")
        base_graph.add_edges([(e1, e2), (e2, e3), (e3, e4), (e4, e5), (e5, e1), (e4, e6), (e6, e7), (e7, e1)])
        base_graph.add_edges([(i1, e1), (i1, e2), (i1, e3), (i1, e4)])
        base_graph.add_edges([(i2, e1), (i2, e4), (i2, e6), (i2, e7)])
        
        # for debugging
        # visualise_graph(base_graph, level)

        i_match = match_P3(base_graph, level)
        self.assertEqual(len(i_match), 2)
        self.assertTrue(i1 in i_match and i2 in i_match)

        new_graph = P3(base_graph, i1)

        expected_graph = StandardizedGraph()
        old_e1 = expected_graph.add_vert(pos_x=-4, pos_y=4, level=level, label="E")
        old_e2 = expected_graph.add_vert(pos_x=4, pos_y=4, level=level, label="E")
        old_e3 = expected_graph.add_vert(pos_x=4, pos_y=-4, level=level, label="E")
        old_e4 = expected_graph.add_vert(pos_x=-4, pos_y=-4, level=level, label="E")
        old_e5 = expected_graph.add_vert(pos_x=-4, pos_y=0, level=level, label="E")
        # small 'i', because this is the right side of production
        old_i1 = expected_graph.add_vert(pos_x=0, pos_y=0, level=level, label="i")
        old_e6 = expected_graph.add_vert(pos_x=-12, pos_y=-4, level=level, label="E")
        old_e7 = expected_graph.add_vert(pos_x=-12, pos_y=4, level=level, label="E")
        old_i2 = expected_graph.add_vert(pos_x=-8, pos_y=0, level=level, label="I")
        expected_graph.add_edges(
            [(old_e1, old_e2), (old_e2, old_e3), (old_e3, old_e4), (old_e4, old_e5),
             (old_e5, old_e1), (old_e4, old_e6), (old_e6, old_e7), (old_e7, old_e1)])
        expected_graph.add_edges([(old_i1, old_e1), (old_i1, old_e2), (old_i1, old_e3), (old_i1, old_e4)])
        expected_graph.add_edges([(old_i2, old_e1), (old_i2, old_e4), (old_i2, old_e6), (old_i2, old_e7)])

        e1 = expected_graph.add_vert(pos_x=-4, pos_y=4, level=level + 1, label="E")
        e2 = expected_graph.add_vert(pos_x=4, pos_y=4, level=level + 1, label="E")
        e3 = expected_graph.add_vert(pos_x=4, pos_y=-4, level=level + 1, label="E")
        e4 = expected_graph.add_vert(pos_x=-4, pos_y=-4, level=level + 1, label="E")

        e12 = expected_graph.add_vert(pos_x=0, pos_y=4, level=level + 1, label="E")
        e23 = expected_graph.add_vert(pos_x=4, pos_y=0, level=level + 1, label="E")
        e34 = expected_graph.add_vert(pos_x=0, pos_y=-4, level=level + 1, label="E")
        e14 = expected_graph.add_vert(pos_x=-4, pos_y=0, level=level + 1, label="E")
        e1234 = expected_graph.add_vert(pos_x=0, pos_y=0, level=level + 1, label="E")

        expected_graph.add_edges([
            (e1, e12), (e2, e12),
            (e2, e23), (e3, e23),
            (e1, e14), (e4, e14),
            (e3, e34), (e4, e34),
            (e12, e1234), (e23, e1234), (e14, e1234), (e34, e1234)
        ])

        i1 = expected_graph.add_vert(pos_x=-2, pos_y=2, level=level + 1, label="I")
        expected_graph.add_edges([(i1, e1), (i1, e12), (i1, e14), (i1, e1234), (old_i1, i1)])

        i2 = expected_graph.add_vert(pos_x=2, pos_y=2, level=level + 1, label="I")
        expected_graph.add_edges([(i2, e2), (i2, e12), (i2, e23), (i2, e1234), (old_i1, i2)])

        i3 = expected_graph.add_vert(pos_x=2, pos_y=-2, level=level + 1, label="I")
        expected_graph.add_edges([(i3, e3), (i3, e23), (i3, e34), (i3, e1234), (old_i1, i3)])

        i4 = expected_graph.add_vert(pos_x=-2, pos_y=-2, level=level + 1, label="I")
        expected_graph.add_edges([(i4, e4), (i4, e14), (i4, e34), (i4, e1234), (old_i1, i4)])
        
        # for debugging
        # visualise_graph(new_graph, level + 1)
        # visualise_graph(expected_graph, level + 1)

        self.assertEqual(new_graph, expected_graph)

    def test_match_P3_correct_large_rotated(self):
        level = 0
        base_graph = StandardizedGraph()
        e1 = base_graph.add_vert(pos_x=-4, pos_y=4, level=level, label="E")
        e2 = base_graph.add_vert(pos_x=4, pos_y=4, level=level, label="E")
        e3 = base_graph.add_vert(pos_x=4, pos_y=-4, level=level, label="E")
        e4 = base_graph.add_vert(pos_x=-4, pos_y=-4, level=level, label="E")
        e5 = base_graph.add_vert(pos_x=0, pos_y=4, level=level, label="E")
        i1 = base_graph.add_vert(pos_x=0, pos_y=0, level=level, label="I")
        e6 = base_graph.add_vert(pos_x=-12, pos_y=-4, level=level, label="E")
        e7 = base_graph.add_vert(pos_x=-12, pos_y=4, level=level, label="E")
        i2 = base_graph.add_vert(pos_x=-8, pos_y=0, level=level, label="I")
        base_graph.add_edges([(e1, e5), (e5, e2), (e2, e3), (e3, e4), (e4, e1), (e4, e6), (e6, e7), (e7, e1)])
        base_graph.add_edges([(i1, e1), (i1, e2), (i1, e3), (i1, e4)])
        base_graph.add_edges([(i2, e1), (i2, e4), (i2, e6), (i2, e7)])
        
        # for debugging
        # visualise_graph(base_graph, level)

        i_match = match_P3(base_graph, level)
        self.assertEqual(len(i_match), 1)
        self.assertEqual(i_match[0], i1)

        new_graph = P3(base_graph, i_match[0])

        expected_graph = StandardizedGraph()
        old_e1 = expected_graph.add_vert(pos_x=-4, pos_y=4, level=level, label="E")
        old_e2 = expected_graph.add_vert(pos_x=4, pos_y=4, level=level, label="E")
        old_e3 = expected_graph.add_vert(pos_x=4, pos_y=-4, level=level, label="E")
        old_e4 = expected_graph.add_vert(pos_x=-4, pos_y=-4, level=level, label="E")
        old_e5 = expected_graph.add_vert(pos_x=0, pos_y=4, level=level, label="E")
        # small 'i', because this is the right side of production
        old_i1 = expected_graph.add_vert(pos_x=0, pos_y=0, level=level, label="i")
        old_e6 = expected_graph.add_vert(pos_x=-12, pos_y=-4, level=level, label="E")
        old_e7 = expected_graph.add_vert(pos_x=-12, pos_y=4, level=level, label="E")
        old_i2 = expected_graph.add_vert(pos_x=-8, pos_y=0, level=level, label="I")
        expected_graph.add_edges(
            [(old_e1, old_e5), (old_e5, old_e2), (old_e2, old_e3), (old_e3, old_e4),
             (old_e4, old_e1), (old_e4, old_e6), (old_e6, old_e7), (old_e7, old_e1)])
        expected_graph.add_edges([(old_i1, old_e1), (old_i1, old_e2), (old_i1, old_e3), (old_i1, old_e4)])
        expected_graph.add_edges([(old_i2, old_e1), (old_i2, old_e4), (old_i2, old_e6), (old_i2, old_e7)])

        e1 = expected_graph.add_vert(pos_x=-4, pos_y=4, level=level + 1, label="E")
        e2 = expected_graph.add_vert(pos_x=4, pos_y=4, level=level + 1, label="E")
        e3 = expected_graph.add_vert(pos_x=4, pos_y=-4, level=level + 1, label="E")
        e4 = expected_graph.add_vert(pos_x=-4, pos_y=-4, level=level + 1, label="E")

        e12 = expected_graph.add_vert(pos_x=0, pos_y=4, level=level + 1, label="E")
        e23 = expected_graph.add_vert(pos_x=4, pos_y=0, level=level + 1, label="E")
        e34 = expected_graph.add_vert(pos_x=0, pos_y=-4, level=level + 1, label="E")
        e14 = expected_graph.add_vert(pos_x=-4, pos_y=0, level=level + 1, label="E")
        e1234 = expected_graph.add_vert(pos_x=0, pos_y=0, level=level + 1, label="E")

        expected_graph.add_edges([
            (e1, e12), (e2, e12),
            (e2, e23), (e3, e23),
            (e1, e14), (e4, e14),
            (e3, e34), (e4, e34),
            (e12, e1234), (e23, e1234), (e14, e1234), (e34, e1234)
        ])

        i1 = expected_graph.add_vert(pos_x=-2, pos_y=2, level=level + 1, label="I")
        expected_graph.add_edges([(i1, e1), (i1, e12), (i1, e14), (i1, e1234), (old_i1, i1)])

        i2 = expected_graph.add_vert(pos_x=2, pos_y=2, level=level + 1, label="I")
        expected_graph.add_edges([(i2, e2), (i2, e12), (i2, e23), (i2, e1234), (old_i1, i2)])

        i3 = expected_graph.add_vert(pos_x=2, pos_y=-2, level=level + 1, label="I")
        expected_graph.add_edges([(i3, e3), (i3, e23), (i3, e34), (i3, e1234), (old_i1, i3)])

        i4 = expected_graph.add_vert(pos_x=-2, pos_y=-2, level=level + 1, label="I")
        expected_graph.add_edges([(i4, e4), (i4, e14), (i4, e34), (i4, e1234), (old_i1, i4)])
        
        # for debugging
        # visualise_graph(new_graph, level + 1)
        # visualise_graph(expected_graph, level + 1)

        self.assertEqual(new_graph, expected_graph)

    def test_match_P3_correct_only_one_large(self):
        level = 0
        base_graph = StandardizedGraph()
        e1 = base_graph.add_vert(pos_x=-4, pos_y=4, level=level, label="E")
        e2 = base_graph.add_vert(pos_x=4, pos_y=4, level=level, label="E")
        e3 = base_graph.add_vert(pos_x=4, pos_y=-4, level=level, label="E")
        e4 = base_graph.add_vert(pos_x=-4, pos_y=-4, level=level, label="E")
        e5 = base_graph.add_vert(pos_x=-4, pos_y=0, level=level, label="E")
        e6 = base_graph.add_vert(pos_x=0, pos_y=4, level=level, label="E")
        i1 = base_graph.add_vert(pos_x=0, pos_y=0, level=level, label="I")
        e7 = base_graph.add_vert(pos_x=-12, pos_y=-4, level=level, label="E")
        e8 = base_graph.add_vert(pos_x=-12, pos_y=4, level=level, label="E")
        i2 = base_graph.add_vert(pos_x=-8, pos_y=0, level=level, label="I")
        base_graph.add_edges([(e1, e6), (e6, e2), (e2, e3), (e3, e4), (e4, e5), (e5, e1), (e4, e7), (e7, e8), (e8, e1)])
        base_graph.add_edges([(i1, e1), (i1, e2), (i1, e3), (i1, e4)])
        base_graph.add_edges([(i2, e1), (i2, e4), (i2, e7), (i2, e8)])
        
        # for debugging
        # visualise_graph(base_graph, level)

        i_match = match_P3(base_graph, level)[0]
        self.assertEqual(i_match, i2)

        new_graph = P3(base_graph, i_match)

        expected_graph = StandardizedGraph()
        old_e1 = expected_graph.add_vert(pos_x=-4, pos_y=4, level=level, label="E")
        old_e2 = expected_graph.add_vert(pos_x=4, pos_y=4, level=level, label="E")
        old_e3 = expected_graph.add_vert(pos_x=4, pos_y=-4, level=level, label="E")
        old_e4 = expected_graph.add_vert(pos_x=-4, pos_y=-4, level=level, label="E")
        old_e5 = expected_graph.add_vert(pos_x=0, pos_y=4, level=level, label="E")
        old_e6 = expected_graph.add_vert(pos_x=0, pos_y=4, level=level, label="E")
        # small 'i', because this is the right side of production
        old_i1 = expected_graph.add_vert(pos_x=0, pos_y=0, level=level, label="i")
        old_e7 = expected_graph.add_vert(pos_x=-12, pos_y=-4, level=level, label="E")
        old_e8 = expected_graph.add_vert(pos_x=-12, pos_y=4, level=level, label="E")
        old_i2 = expected_graph.add_vert(pos_x=0, pos_y=0, level=level, label="I")
        expected_graph.add_edges(
            [(old_e1, old_e6), (old_e6, old_e2), (old_e2, old_e3), (old_e3, old_e4), (old_e4, old_e5),
             (old_e5, old_e1), (old_e4, old_e7), (old_e7, old_e8), (old_e8, old_e1)])
        expected_graph.add_edges([(old_i1, old_e1), (old_i1, old_e2), (old_i1, old_e3), (old_i1, old_e4)])
        expected_graph.add_edges([(old_i2, old_e1), (old_i2, old_e4), (old_i2, old_e7), (old_i2, old_e8)])

        e1 = expected_graph.add_vert(pos_x=-4, pos_y=4, level=level + 1, label="E")
        e2 = expected_graph.add_vert(pos_x=4, pos_y=4, level=level + 1, label="E")
        e3 = expected_graph.add_vert(pos_x=4, pos_y=-4, level=level + 1, label="E")
        e4 = expected_graph.add_vert(pos_x=-4, pos_y=-4, level=level + 1, label="E")

        e12 = expected_graph.add_vert(pos_x=0, pos_y=4, level=level + 1, label="E")
        e23 = expected_graph.add_vert(pos_x=4, pos_y=0, level=level + 1, label="E")
        e34 = expected_graph.add_vert(pos_x=0, pos_y=-4, level=level + 1, label="E")
        e14 = expected_graph.add_vert(pos_x=-4, pos_y=0, level=level + 1, label="E")
        e1234 = expected_graph.add_vert(pos_x=0, pos_y=0, level=level + 1, label="E")

        expected_graph.add_edges([
            (e1, e12), (e2, e12),
            (e2, e23), (e3, e23),
            (e1, e14), (e4, e14),
            (e3, e34), (e4, e34),
            (e12, e1234), (e23, e1234), (e14, e1234), (e34, e1234)
        ])

        i1 = expected_graph.add_vert(pos_x=-2, pos_y=2, level=level + 1, label="I")
        expected_graph.add_edges([(i1, e1), (i1, e12), (i1, e14), (i1, e1234), (old_i2, i1)])

        i2 = expected_graph.add_vert(pos_x=2, pos_y=2, level=level + 1, label="I")
        expected_graph.add_edges([(i2, e2), (i2, e12), (i2, e23), (i2, e1234), (old_i2, i2)])

        i3 = expected_graph.add_vert(pos_x=2, pos_y=-2, level=level + 1, label="I")
        expected_graph.add_edges([(i3, e4), (i3, e14), (i3, e34), (i3, e1234), (old_i2, i3)])

        i4 = expected_graph.add_vert(pos_x=-2, pos_y=-2, level=level + 1, label="I")
        expected_graph.add_edges([(i4, e3), (i4, e23), (i4, e34), (i4, e1234), (old_i2, i4)])
        
        # for debugging
        # visualise_graph(new_graph, level + 1)
        # visualise_graph(expected_graph, level + 1)

        self.assertEqual(new_graph, expected_graph)

    def test_match_P3_incorrect_too_many_large(self):
        level = 0
        base_graph = StandardizedGraph()
        e1 = base_graph.add_vert(pos_x=-4, pos_y=4, level=level, label="E")
        e2 = base_graph.add_vert(pos_x=4, pos_y=4, level=level, label="E")
        e3 = base_graph.add_vert(pos_x=4, pos_y=-4, level=level, label="E")
        e4 = base_graph.add_vert(pos_x=-4, pos_y=-4, level=level, label="E")
        e5 = base_graph.add_vert(pos_x=-4, pos_y=0, level=level, label="E")
        e6 = base_graph.add_vert(pos_x=0, pos_y=4, level=level, label="E")
        i1 = base_graph.add_vert(pos_x=0, pos_y=0, level=level, label="I")
        e7 = base_graph.add_vert(pos_x=-12, pos_y=-4, level=level, label="E")
        e8 = base_graph.add_vert(pos_x=-12, pos_y=0, level=level, label="E")
        e9 = base_graph.add_vert(pos_x=-12, pos_y=4, level=level, label="E")
        i2 = base_graph.add_vert(pos_x=-8, pos_y=0, level=level, label="I")
        base_graph.add_edges(
            [(e1, e6), (e6, e2), (e2, e3), (e3, e4), (e4, e5),
             (e5, e1), (e4, e7), (e7, e8), (e8, e9), (e9, e1)])
        base_graph.add_edges([(i1, e1), (i1, e2), (i1, e3), (i1, e4)])
        base_graph.add_edges([(i2, e1), (i2, e4), (i2, e7), (i2, e9)])
        
        # for debugging
        # visualise_graph(base_graph, level)

        i_match = match_P3(base_graph, level)
        self.assertEqual(i_match, [])

    def test_match_P3_incorrect_pos_large(self):
        level = 0
        base_graph = StandardizedGraph()
        e1 = base_graph.add_vert(pos_x=-4, pos_y=4, level=level, label="E")
        e2 = base_graph.add_vert(pos_x=4, pos_y=4, level=level, label="E")
        e3 = base_graph.add_vert(pos_x=4, pos_y=-4, level=level, label="E")
        e4 = base_graph.add_vert(pos_x=-4, pos_y=-4, level=level, label="E")
        e5 = base_graph.add_vert(pos_x=-4, pos_y=2, level=level, label="E")
        i1 = base_graph.add_vert(pos_x=0, pos_y=0, level=level, label="I")
        e6 = base_graph.add_vert(pos_x=-12, pos_y=-4, level=level, label="E")
        e7 = base_graph.add_vert(pos_x=-12, pos_y=4, level=level, label="E")
        i2 = base_graph.add_vert(pos_x=-8, pos_y=0, level=level, label="I")
        base_graph.add_edges([(e1, e2), (e2, e3), (e3, e4), (e4, e5), (e5, e1), (e4, e6), (e6, e7), (e7, e1)])
        base_graph.add_edges([(i1, e1), (i1, e2), (i1, e3), (i1, e4)])
        base_graph.add_edges([(i2, e1), (i2, e4), (i2, e6), (i2, e7)])
        
        # for debugging
        # visualise_graph(base_graph, level)

        i_match = match_P3(base_graph, level)
        self.assertEqual(i_match, [])

    def test_match_P3_incorrect_missing_large(self):
        level = 0
        base_graph = StandardizedGraph()
        e1 = base_graph.add_vert(pos_x=-4, pos_y=4, level=level, label="E")
        e2 = base_graph.add_vert(pos_x=4, pos_y=4, level=level, label="E")
        e3 = base_graph.add_vert(pos_x=4, pos_y=-4, level=level, label="E")
        e4 = base_graph.add_vert(pos_x=-4, pos_y=-4, level=level, label="E")
        i1 = base_graph.add_vert(pos_x=0, pos_y=0, level=level, label="I")
        e6 = base_graph.add_vert(pos_x=-12, pos_y=-4, level=level, label="E")
        e7 = base_graph.add_vert(pos_x=-12, pos_y=4, level=level, label="E")
        i2 = base_graph.add_vert(pos_x=-8, pos_y=0, level=level, label="I")
        base_graph.add_edges([(e1, e2), (e2, e3), (e3, e4), (e4, e1), (e4, e6), (e6, e7), (e7, e1)])
        base_graph.add_edges([(i1, e1), (i1, e2), (i1, e3), (i1, e4)])
        base_graph.add_edges([(i2, e1), (i2, e4), (i2, e6), (i2, e7)])
        
        # for debugging
        # visualise_graph(base_graph, level)

        i_match = match_P3(base_graph, level)
        self.assertEqual(i_match, [])

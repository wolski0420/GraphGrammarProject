import unittest
from utils.vis import visualise_graph
from utils.StandardizedGraph import StandardizedGraph, Vert
from .P5 import match_P5, P5



class TestP5(unittest.TestCase):
    def test_match_P5_correct(self):
        level = 0
        base_graph = StandardizedGraph()
        e1 = base_graph.add_vert(pos_x=-4, pos_y=4, level=level, label="E")
        e2 = base_graph.add_vert(pos_x=4, pos_y=4, level=level, label="E")
        e3 = base_graph.add_vert(pos_x=4, pos_y=-4, level=level, label="E")
        e4 = base_graph.add_vert(pos_x=-4, pos_y=-4, level=level, label="E")
        e5 = base_graph.add_vert(pos_x=-4, pos_y=0, level=level, label="E")
        e6 = base_graph.add_vert(pos_x=0, pos_y=4, level=level, label="E")
        e7 = base_graph.add_vert(pos_x=4, pos_y=0, level=level, label="E")
        i1 = base_graph.add_vert(pos_x=0, pos_y=0, level=level, label="I")
        base_graph.add_edges([(e1, e6), (e2, e6), (e2, e7), (e3, e7), (e3, e4), (e4, e5), (e5, e1)])
        base_graph.add_edges([(i1, e1), (i1, e2), (i1, e3), (i1, e4)])

        # for debugging
        # visualise_graph(base_graph, level)

        i_match = match_P5(base_graph, level)[0]
        self.assertEqual(i_match, i1)

        new_graph = P5(base_graph, i_match)

        expected_graph = StandardizedGraph()
        old_e1 = expected_graph.add_vert(pos_x=-4, pos_y=4, level=level, label="E")
        old_e2 = expected_graph.add_vert(pos_x=4, pos_y=4, level=level, label="E")
        old_e3 = expected_graph.add_vert(pos_x=4, pos_y=-4, level=level, label="E")
        old_e4 = expected_graph.add_vert(pos_x=-4, pos_y=-4, level=level, label="E")
        old_e5 = expected_graph.add_vert(pos_x=-4, pos_y=0, level=level, label="E")
        old_e6 = expected_graph.add_vert(pos_x=0, pos_y=4, level=level, label="E")
        old_e7 = expected_graph.add_vert(pos_x=4, pos_y=0, level=level, label="E")
        # small 'i', because this is the right side of production
        old_i1 = expected_graph.add_vert(pos_x=0, pos_y=0, level=level, label="i")
        expected_graph.add_edges(
            [(old_e1, old_e6), (old_e2, old_e6), (old_e2, old_e7), (old_e3, old_e7), (old_e3, old_e4), (old_e4, old_e5), (old_e5, old_e1)])
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

    def test_match_P5_correct_rotated(self):
        level = 0
        base_graph = StandardizedGraph()
        e1 = base_graph.add_vert(pos_x=-4, pos_y=4, level=level, label="E")
        e2 = base_graph.add_vert(pos_x=4, pos_y=4, level=level, label="E")
        e3 = base_graph.add_vert(pos_x=4, pos_y=-4, level=level, label="E")
        e4 = base_graph.add_vert(pos_x=-4, pos_y=-4, level=level, label="E")
        e5 = base_graph.add_vert(pos_x=0, pos_y=4, level=level, label="E")
        e6 = base_graph.add_vert(pos_x=4, pos_y=0, level=level, label="E")
        e7 = base_graph.add_vert(pos_x=0, pos_y=-4, level=level, label="E")
        i1 = base_graph.add_vert(pos_x=0, pos_y=0, level=level, label="I")
        base_graph.add_edges([(e1, e5), (e5, e2), (e2, e6), (e6, e3), (e3, e7), (e7, e4), (e4, e1)])
        base_graph.add_edges([(i1, e1), (i1, e2), (i1, e3), (i1, e4)])

        # for debugging
        # visualise_graph(base_graph, level)

        i_match = match_P5(base_graph, level)[0]
        self.assertEqual(i_match, i1)

        new_graph = P5(base_graph, i_match)

        expected_graph = StandardizedGraph()
        old_e1 = expected_graph.add_vert(pos_x=-4, pos_y=4, level=level, label="E")
        old_e2 = expected_graph.add_vert(pos_x=4, pos_y=4, level=level, label="E")
        old_e3 = expected_graph.add_vert(pos_x=4, pos_y=-4, level=level, label="E")
        old_e4 = expected_graph.add_vert(pos_x=-4, pos_y=-4, level=level, label="E")
        old_e5 = expected_graph.add_vert(pos_x=0, pos_y=4, level=level, label="E")
        old_e6 = expected_graph.add_vert(pos_x=4, pos_y=0, level=level, label="E")
        old_e7 = expected_graph.add_vert(pos_x=0, pos_y=-4, level=level, label="E")
        # small 'i', because this is the right side of production
        old_i1 = expected_graph.add_vert(pos_x=0, pos_y=0, level=level, label="i")
        expected_graph.add_edges(
            [(old_e1, old_e5), (old_e5, old_e2), (old_e2, old_e6), (old_e6, old_e3), (old_e3, old_e7), (old_e7, old_e4), (old_e4, old_e1)])
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

    def test_match_P5_incorrect_pos(self):
        level = 0
        base_graph = StandardizedGraph()
        e1 = base_graph.add_vert(pos_x=-4, pos_y=4, level=level, label="E")
        e2 = base_graph.add_vert(pos_x=4, pos_y=4, level=level, label="E")
        e3 = base_graph.add_vert(pos_x=4, pos_y=-4, level=level, label="E")
        e4 = base_graph.add_vert(pos_x=-4, pos_y=-4, level=level, label="E")
        e5 = base_graph.add_vert(pos_x=-4, pos_y=2, level=level, label="E")
        e6 = base_graph.add_vert(pos_x=0, pos_y=4, level=level, label="E")
        e7 = base_graph.add_vert(pos_x=4, pos_y=0, level=level, label="E")
        i1 = base_graph.add_vert(pos_x=0, pos_y=0, level=level, label="I")
        base_graph.add_edges([(e1, e6), (e6, e2), (e2, e7), (e7, e3), (e3, e4), (e4, e5), (e5, e1)])
        base_graph.add_edges([(i1, e1), (i1, e2), (i1, e3), (i1, e4)])

        # for debugging
        # visualise_graph(base_graph, level)

        i_match = match_P5(base_graph, level)
        self.assertEqual(i_match, [])

    def test_match_P5_incorrect_missing(self):
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

        i_match = match_P5(base_graph, level)
        self.assertEqual(i_match, [])

    def test_match_P5_incorrect_too_many(self):
        level = 0
        base_graph = StandardizedGraph()
        e1 = base_graph.add_vert(pos_x=-4, pos_y=4, level=level, label="E")
        e2 = base_graph.add_vert(pos_x=4, pos_y=4, level=level, label="E")
        e3 = base_graph.add_vert(pos_x=4, pos_y=-4, level=level, label="E")
        e4 = base_graph.add_vert(pos_x=-4, pos_y=-4, level=level, label="E")
        e5 = base_graph.add_vert(pos_x=-4, pos_y=0, level=level, label="E")
        e6 = base_graph.add_vert(pos_x=0, pos_y=4, level=level, label="E")
        e7 = base_graph.add_vert(pos_x=4, pos_y=0, level=level, label="E")
        e8 = base_graph.add_vert(pos_x=0, pos_y=-4, level=level, label="E")
        i1 = base_graph.add_vert(pos_x=0, pos_y=0, level=level, label="I")
        base_graph.add_edges([(e1, e6), (e6, e2), (e2, e7), (e7, e3), (e3, e8), (e8, e4), (e4, e5), (e5, e1)])
        base_graph.add_edges([(i1, e1), (i1, e2), (i1, e3), (i1, e4)])

        # for debugging
        # visualise_graph(base_graph, level)

        i_match = match_P5(base_graph, level)
        self.assertEqual(i_match, [])

    def test_match_P5_incorrect_label(self):
        level = 0
        base_graph = StandardizedGraph()
        e1 = base_graph.add_vert(pos_x=-4, pos_y=4, level=level, label="F")
        e2 = base_graph.add_vert(pos_x=4, pos_y=4, level=level, label="E")
        e3 = base_graph.add_vert(pos_x=4, pos_y=-4, level=level, label="E")
        e4 = base_graph.add_vert(pos_x=-4, pos_y=-4, level=level, label="E")
        e5 = base_graph.add_vert(pos_x=-4, pos_y=0, level=level, label="E")
        e6 = base_graph.add_vert(pos_x=0, pos_y=4, level=level, label="E")
        e7 = base_graph.add_vert(pos_x=4, pos_y=0, level=level, label="E")
        i1 = base_graph.add_vert(pos_x=0, pos_y=0, level=level, label="I")
        base_graph.add_edges([(e1, e6), (e6, e2), (e2, e7), (e7, e3), (e3, e4), (e4, e5), (e5, e1)])
        base_graph.add_edges([(i1, e1), (i1, e2), (i1, e3), (i1, e4)])

        # for debugging
        # visualise_graph(base_graph, level)

        i_match = match_P5(base_graph, level)
        self.assertEqual(i_match, [])

    def test_match_P5_missing_edge(self):
        level = 0
        base_graph = StandardizedGraph()
        e1 = base_graph.add_vert(pos_x=-4, pos_y=4, level=level, label="E")
        e2 = base_graph.add_vert(pos_x=4, pos_y=4, level=level, label="E")
        e3 = base_graph.add_vert(pos_x=4, pos_y=-4, level=level, label="E")
        e4 = base_graph.add_vert(pos_x=-4, pos_y=-4, level=level, label="E")
        e5 = base_graph.add_vert(pos_x=-4, pos_y=0, level=level, label="E")
        e6 = base_graph.add_vert(pos_x=0, pos_y=4, level=level, label="E")
        e7 = base_graph.add_vert(pos_x=4, pos_y=0, level=level, label="E")
        i1 = base_graph.add_vert(pos_x=0, pos_y=0, level=level, label="I")
        base_graph.add_edges([(e1, e6), (e2, e7), (e7, e3), (e3, e4), (e4, e5), (e5, e1)])
        base_graph.add_edges([(i1, e1), (i1, e2), (i1, e3), (i1, e4)])

        # for debugging
        # visualise_graph(base_graph, level)

        i_match = match_P5(base_graph, level)
        self.assertEqual(i_match, [])

    def test_match_P5_correct_large(self):
        level = 0
        base_graph = StandardizedGraph()
        e1 = base_graph.add_vert(pos_x=-4, pos_y=4, level=level, label="E")
        e2 = base_graph.add_vert(pos_x=4, pos_y=4, level=level, label="E")
        e3 = base_graph.add_vert(pos_x=4, pos_y=-4, level=level, label="E")
        e4 = base_graph.add_vert(pos_x=-4, pos_y=-4, level=level, label="E")
        e5 = base_graph.add_vert(pos_x=-4, pos_y=0, level=level, label="E")
        e6 = base_graph.add_vert(pos_x=0, pos_y=4, level=level, label="E")
        e7 = base_graph.add_vert(pos_x=4, pos_y=0, level=level, label="E")
        i1 = base_graph.add_vert(pos_x=0, pos_y=0, level=level, label="I")

        e8 = base_graph.add_vert(pos_x=-12, pos_y=-4, level=level, label="E")
        e9 = base_graph.add_vert(pos_x=-12, pos_y=4, level=level, label="E")
        e10 = base_graph.add_vert(pos_x=-8, pos_y=-4, level=level, label="E")
        e11 = base_graph.add_vert(pos_x=-8, pos_y=4, level=level, label="E")
        i2 = base_graph.add_vert(pos_x=-8, pos_y=0, level=level, label="I")
        base_graph.add_edges([(e1, e6), (e6, e2), (e2, e7), (e7, e3), (e3, e4), (e4, e5), (e5, e1), (e4, e10), (e10, e8), (e8, e9), (e9, e11), (e11, e1)])
        base_graph.add_edges([(i1, e1), (i1, e2), (i1, e3), (i1, e4)])
        base_graph.add_edges([(i2, e1), (i2, e4), (i2, e8), (i2, e9)])

        # for debugging
        # visualise_graph(base_graph, level)

        i_match = match_P5(base_graph, level)
        self.assertEqual(len(i_match), 2)
        self.assertTrue(i1 in i_match and i2 in i_match)

        new_graph = P5(base_graph, i1)
        new_graph = P5(new_graph, i2)

        expected_graph = StandardizedGraph()
        old_e1 = expected_graph.add_vert(pos_x=-4, pos_y=4, level=level, label="E")
        old_e2 = expected_graph.add_vert(pos_x=4, pos_y=4, level=level, label="E")
        old_e3 = expected_graph.add_vert(pos_x=4, pos_y=-4, level=level, label="E")
        old_e4 = expected_graph.add_vert(pos_x=-4, pos_y=-4, level=level, label="E")
        old_e5 = expected_graph.add_vert(pos_x=-4, pos_y=0, level=level, label="E")
        old_e6 = expected_graph.add_vert(pos_x=0, pos_y=4, level=level, label="E")
        old_e7 = expected_graph.add_vert(pos_x=4, pos_y=0, level=level, label="E")
        # small 'i', because this is the right side of production
        old_i1 = expected_graph.add_vert(pos_x=0, pos_y=0, level=level, label="i")
        old_e8 = expected_graph.add_vert(pos_x=-12, pos_y=-4, level=level, label="E")
        old_e9 = expected_graph.add_vert(pos_x=-12, pos_y=4, level=level, label="E")
        old_e10 = expected_graph.add_vert(pos_x=-8, pos_y=-4, level=level, label="E")
        old_e11 = expected_graph.add_vert(pos_x=-8, pos_y=4, level=level, label="E")
        old_i2 = expected_graph.add_vert(pos_x=-8, pos_y=0, level=level, label="I")
        expected_graph.add_edges(
            [(old_e1, old_e6), (old_e6, old_e2), (old_e2, old_e7), (old_e7, old_e3), 
             (old_e3, old_e4), (old_e4, old_e5), (old_e5, old_e1), (old_e4, old_e10), 
             (old_e10, old_e8), (old_e8, old_e9), (old_e9, old_e11), (old_e11, old_e1)])
        expected_graph.add_edges([(old_i1, old_e1), (old_i1, old_e2), (old_i1, old_e3), (old_i1, old_e4)])
        expected_graph.add_edges([(old_i2, old_e1), (old_i2, old_e4), (old_i2, old_e8), (old_i2, old_e9)])

        e1 = expected_graph.add_vert(pos_x=-4, pos_y=4, level=level + 1, label="E")
        e2 = expected_graph.add_vert(pos_x=4, pos_y=4, level=level + 1, label="E")
        e3 = expected_graph.add_vert(pos_x=4, pos_y=-4, level=level + 1, label="E")
        e4 = expected_graph.add_vert(pos_x=-4, pos_y=-4, level=level + 1, label="E")

        e12 = expected_graph.add_vert(pos_x=0, pos_y=4, level=level + 1, label="E")
        e23 = expected_graph.add_vert(pos_x=4, pos_y=0, level=level + 1, label="E")
        e34 = expected_graph.add_vert(pos_x=0, pos_y=-4, level=level + 1, label="E")
        e14 = expected_graph.add_vert(pos_x=-4, pos_y=0, level=level + 1, label="E")
        e1234 = expected_graph.add_vert(pos_x=0, pos_y=0, level=level + 1, label="E")

        e5 = expected_graph.add_vert(pos_x=-12, pos_y=4, level=level + 1, label="E")
        e6 = expected_graph.add_vert(pos_x=-4, pos_y=4, level=level + 1, label="E")
        e7 = expected_graph.add_vert(pos_x=-4, pos_y=-4, level=level + 1, label="E")
        e8 = expected_graph.add_vert(pos_x=-12, pos_y=-4, level=level + 1, label="E")

        e56 = expected_graph.add_vert(pos_x=-8, pos_y=4, level=level + 1, label="E")
        e67 = expected_graph.add_vert(pos_x=-4, pos_y=0, level=level + 1, label="E")
        e78 = expected_graph.add_vert(pos_x=-8, pos_y=-4, level=level + 1, label="E")
        e58 = expected_graph.add_vert(pos_x=-12, pos_y=0, level=level + 1, label="E")
        e5678 = expected_graph.add_vert(pos_x=-8, pos_y=0, level=level + 1, label="E")

        expected_graph.add_edges([
            (e1, e12), (e2, e12),
            (e2, e23), (e3, e23),
            (e1, e14), (e4, e14),
            (e3, e34), (e4, e34),
            (e12, e1234), (e23, e1234), (e14, e1234), (e34, e1234),

            (e5, e56), (e6, e56),
            (e6, e67), (e7, e67),
            (e5, e58), (e8, e58),
            (e7, e78), (e8, e78),
            (e56, e5678), (e67, e5678), (e58, e5678), (e78, e5678),
        ])

        i1 = expected_graph.add_vert(pos_x=-2, pos_y=2, level=level + 1, label="I")
        expected_graph.add_edges([(i1, e1), (i1, e12), (i1, e14), (i1, e1234), (old_i1, i1)])

        i2 = expected_graph.add_vert(pos_x=2, pos_y=2, level=level + 1, label="I")
        expected_graph.add_edges([(i2, e2), (i2, e12), (i2, e23), (i2, e1234), (old_i1, i2)])

        i3 = expected_graph.add_vert(pos_x=2, pos_y=-2, level=level + 1, label="I")
        expected_graph.add_edges([(i3, e3), (i3, e23), (i3, e34), (i3, e1234), (old_i1, i3)])

        i4 = expected_graph.add_vert(pos_x=-2, pos_y=-2, level=level + 1, label="I")
        expected_graph.add_edges([(i4, e4), (i4, e14), (i4, e34), (i4, e1234), (old_i1, i4)])

        i5 = expected_graph.add_vert(pos_x=-10, pos_y=2, level=level + 1, label="I")
        expected_graph.add_edges([(i5, e5), (i5, e56), (i5, e58), (i5, e5678), (old_i2, i5)])

        i6 = expected_graph.add_vert(pos_x=-6, pos_y=2, level=level + 1, label="I")
        expected_graph.add_edges([(i6, e6), (i6, e56), (i6, e67), (i6, e5678), (old_i2, i6)])

        i7 = expected_graph.add_vert(pos_x=-6, pos_y=-2, level=level + 1, label="I")
        expected_graph.add_edges([(i7, e7), (i7, e67), (i7, e78), (i7, e5678), (old_i2, i7)])

        i8 = expected_graph.add_vert(pos_x=-10, pos_y=-2, level=level + 1, label="I")
        expected_graph.add_edges([(i8, e8), (i8, e58), (i8, e78), (i8, e5678), (old_i2, i8)])

        # for debugging
        # visualise_graph(new_graph, level + 1)
        # visualise_graph(expected_graph, level + 1)

        self.assertEqual(new_graph, expected_graph)

    def test_match_P5_correct_large_rotated(self):
        level = 0
        base_graph = StandardizedGraph()
        e1 = base_graph.add_vert(pos_x=-4, pos_y=4, level=level, label="E")
        e2 = base_graph.add_vert(pos_x=4, pos_y=4, level=level, label="E")
        e3 = base_graph.add_vert(pos_x=4, pos_y=-4, level=level, label="E")
        e4 = base_graph.add_vert(pos_x=-4, pos_y=-4, level=level, label="E")
        e5 = base_graph.add_vert(pos_x=0, pos_y=-4, level=level, label="E")
        e6 = base_graph.add_vert(pos_x=0, pos_y=4, level=level, label="E")
        e7 = base_graph.add_vert(pos_x=4, pos_y=0, level=level, label="E")
        i1 = base_graph.add_vert(pos_x=0, pos_y=0, level=level, label="I")

        e8 = base_graph.add_vert(pos_x=-12, pos_y=-4, level=level, label="E")
        e9 = base_graph.add_vert(pos_x=-12, pos_y=4, level=level, label="E")
        e10 = base_graph.add_vert(pos_x=-8, pos_y=-4, level=level, label="E")
        e11 = base_graph.add_vert(pos_x=-8, pos_y=4, level=level, label="E")
        i2 = base_graph.add_vert(pos_x=-8, pos_y=0, level=level, label="I")
        base_graph.add_edges([(e1, e6), (e6, e2), (e2, e7), (e7, e3), (e3, e5), (e5, e4), (e4, e1), (e4, e10), (e10, e8), (e8, e9), (e9, e11), (e11, e1)])
        base_graph.add_edges([(i1, e1), (i1, e2), (i1, e3), (i1, e4)])
        base_graph.add_edges([(i2, e1), (i2, e4), (i2, e8), (i2, e9)])

        # for debugging
        # visualise_graph(base_graph, level)

        i_match = match_P5(base_graph, level)
        self.assertEqual(len(i_match), 1)
        self.assertEqual(i_match[0], i1)

        new_graph = P5(base_graph, i_match[0])

        expected_graph = StandardizedGraph()
        old_e1 = expected_graph.add_vert(pos_x=-4, pos_y=4, level=level, label="E")
        old_e2 = expected_graph.add_vert(pos_x=4, pos_y=4, level=level, label="E")
        old_e3 = expected_graph.add_vert(pos_x=4, pos_y=-4, level=level, label="E")
        old_e4 = expected_graph.add_vert(pos_x=-4, pos_y=-4, level=level, label="E")
        old_e5 = expected_graph.add_vert(pos_x=0, pos_y=-4, level=level, label="E")
        old_e6 = expected_graph.add_vert(pos_x=0, pos_y=4, level=level, label="E")
        old_e7 = expected_graph.add_vert(pos_x=4, pos_y=0, level=level, label="E")
        # small 'i', because this is the right side of production
        old_i1 = expected_graph.add_vert(pos_x=0, pos_y=0, level=level, label="i")
        old_e8 = expected_graph.add_vert(pos_x=-12, pos_y=-4, level=level, label="E")
        old_e9 = expected_graph.add_vert(pos_x=-12, pos_y=4, level=level, label="E")
        old_e10 = expected_graph.add_vert(pos_x=-8, pos_y=-4, level=level, label="E")
        old_e11 = expected_graph.add_vert(pos_x=-8, pos_y=4, level=level, label="E")
        old_i2 = expected_graph.add_vert(pos_x=-8, pos_y=0, level=level, label="I")
        expected_graph.add_edges(
            [(old_e1, old_e6), (old_e6, old_e2), (old_e2, old_e7), (old_e7, old_e3), 
             (old_e3, old_e5), (old_e5, old_e4), (old_e4, old_e1), (old_e4, old_e10), 
             (old_e10, old_e8), (old_e8, old_e9), (old_e9, old_e11), (old_e11, old_e1)])
        expected_graph.add_edges([(old_i1, old_e1), (old_i1, old_e2), (old_i1, old_e3), (old_i1, old_e4)])
        expected_graph.add_edges([(old_i2, old_e1), (old_i2, old_e4), (old_i2, old_e8), (old_i2, old_e9)])

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

    def test_match_P5_correct_only_one_large(self):
        level = 0
        base_graph = StandardizedGraph()
        e1 = base_graph.add_vert(pos_x=-4, pos_y=4, level=level, label="E")
        e2 = base_graph.add_vert(pos_x=4, pos_y=4, level=level, label="E")
        e3 = base_graph.add_vert(pos_x=4, pos_y=-4, level=level, label="E")
        e4 = base_graph.add_vert(pos_x=-4, pos_y=-4, level=level, label="E")
        e5 = base_graph.add_vert(pos_x=-4, pos_y=0, level=level, label="E")
        e6 = base_graph.add_vert(pos_x=0, pos_y=4, level=level, label="E")
        e7 = base_graph.add_vert(pos_x=4, pos_y=0, level=level, label="E")
        e12 = base_graph.add_vert(pos_x=0, pos_y=-4, level=level, label="E")
        i1 = base_graph.add_vert(pos_x=0, pos_y=0, level=level, label="I")

        e8 = base_graph.add_vert(pos_x=-12, pos_y=-4, level=level, label="E")
        e9 = base_graph.add_vert(pos_x=-12, pos_y=4, level=level, label="E")
        e10 = base_graph.add_vert(pos_x=-8, pos_y=-4, level=level, label="E")
        e11 = base_graph.add_vert(pos_x=-8, pos_y=4, level=level, label="E")
        i2 = base_graph.add_vert(pos_x=-8, pos_y=0, level=level, label="I")
        base_graph.add_edges([(e1, e6), (e6, e2), (e2, e7), (e7, e3), (e3, e12), (e12, e4), (e4, e5), (e5, e1), (e4, e10), (e10, e8), (e8, e9), (e9, e11), (e11, e1)])
        base_graph.add_edges([(i1, e1), (i1, e2), (i1, e3), (i1, e4)])
        base_graph.add_edges([(i2, e1), (i2, e4), (i2, e8), (i2, e9)])

        # for debugging
        # visualise_graph(base_graph, level)

        i_match = match_P5(base_graph, level)[0]
        self.assertEqual(i_match, i2)

        new_graph = P5(base_graph, i_match)

        expected_graph = StandardizedGraph()
        old_e1 = expected_graph.add_vert(pos_x=-4, pos_y=4, level=level, label="E")
        old_e2 = expected_graph.add_vert(pos_x=4, pos_y=4, level=level, label="E")
        old_e3 = expected_graph.add_vert(pos_x=4, pos_y=-4, level=level, label="E")
        old_e4 = expected_graph.add_vert(pos_x=-4, pos_y=-4, level=level, label="E")
        old_e5 = expected_graph.add_vert(pos_x=-4, pos_y=0, level=level, label="E")
        old_e6 = expected_graph.add_vert(pos_x=0, pos_y=4, level=level, label="E")
        old_e7 = expected_graph.add_vert(pos_x=4, pos_y=0, level=level, label="E")
        old_e12 = expected_graph.add_vert(pos_x=0, pos_y=-4, level=level, label="E")
        # small 'i', because this is the right side of production
        old_i1 = expected_graph.add_vert(pos_x=0, pos_y=0, level=level, label="i")
        old_e8 = expected_graph.add_vert(pos_x=-12, pos_y=-4, level=level, label="E")
        old_e9 = expected_graph.add_vert(pos_x=-12, pos_y=4, level=level, label="E")
        old_e10 = expected_graph.add_vert(pos_x=-8, pos_y=-4, level=level, label="E")
        old_e11 = expected_graph.add_vert(pos_x=-8, pos_y=4, level=level, label="E")
        old_i2 = expected_graph.add_vert(pos_x=-8, pos_y=0, level=level, label="I")
        expected_graph.add_edges(
            [(old_e1, old_e6), (old_e6, old_e2), (old_e2, old_e7), (old_e7, old_e3), 
             (old_e3, old_e12), (old_e12, old_e4), (old_e4, old_e5), (old_e5, old_e1), (old_e4, old_e10), 
             (old_e10, old_e8), (old_e8, old_e9), (old_e9, old_e11), (old_e11, old_e1)])
        expected_graph.add_edges([(old_i1, old_e1), (old_i1, old_e2), (old_i1, old_e3), (old_i1, old_e4)])
        expected_graph.add_edges([(old_i2, old_e1), (old_i2, old_e4), (old_i2, old_e8), (old_i2, old_e9)])

        e1 = expected_graph.add_vert(pos_x=-12, pos_y=4, level=level + 1, label="E")
        e2 = expected_graph.add_vert(pos_x=-4, pos_y=4, level=level + 1, label="E")
        e3 = expected_graph.add_vert(pos_x=-4, pos_y=-4, level=level + 1, label="E")
        e4 = expected_graph.add_vert(pos_x=-12, pos_y=-4, level=level + 1, label="E")

        e12 = expected_graph.add_vert(pos_x=-8, pos_y=4, level=level + 1, label="E")
        e23 = expected_graph.add_vert(pos_x=-4, pos_y=0, level=level + 1, label="E")
        e34 = expected_graph.add_vert(pos_x=-8, pos_y=-4, level=level + 1, label="E")
        e14 = expected_graph.add_vert(pos_x=-12, pos_y=0, level=level + 1, label="E")
        e1234 = expected_graph.add_vert(pos_x=-8, pos_y=0, level=level + 1, label="E")

        expected_graph.add_edges([
            (e1, e12), (e2, e12),
            (e2, e23), (e3, e23),
            (e1, e14), (e4, e14),
            (e3, e34), (e4, e34),
            (e12, e1234), (e23, e1234), (e14, e1234), (e34, e1234)
        ])

        i1 = expected_graph.add_vert(pos_x=-10, pos_y=2, level=level + 1, label="I")
        expected_graph.add_edges([(i1, e1), (i1, e12), (i1, e14), (i1, e1234), (old_i2, i1)])

        i2 = expected_graph.add_vert(pos_x=-6, pos_y=2, level=level + 1, label="I")
        expected_graph.add_edges([(i2, e2), (i2, e12), (i2, e23), (i2, e1234), (old_i2, i2)])

        i3 = expected_graph.add_vert(pos_x=-6, pos_y=-2, level=level + 1, label="I")
        expected_graph.add_edges([(i3, e3), (i3, e23), (i3, e34), (i3, e1234), (old_i2, i3)])

        i4 = expected_graph.add_vert(pos_x=-10, pos_y=-2, level=level + 1, label="I")
        expected_graph.add_edges([(i4, e4), (i4, e14), (i4, e34), (i4, e1234), (old_i2, i4)])

        # for debugging
        # visualise_graph(new_graph, level + 1)
        # visualise_graph(expected_graph, level + 1)

        self.assertEqual(new_graph, expected_graph)

    def test_match_P5_incorrect_too_many_large(self):
        level = 0
        base_graph = StandardizedGraph()
        e1 = base_graph.add_vert(pos_x=-4, pos_y=4, level=level, label="E")
        e2 = base_graph.add_vert(pos_x=4, pos_y=4, level=level, label="E")
        e3 = base_graph.add_vert(pos_x=4, pos_y=-4, level=level, label="E")
        e4 = base_graph.add_vert(pos_x=-4, pos_y=-4, level=level, label="E")
        e5 = base_graph.add_vert(pos_x=0, pos_y=-4, level=level, label="E")
        e6 = base_graph.add_vert(pos_x=0, pos_y=4, level=level, label="E")
        e7 = base_graph.add_vert(pos_x=4, pos_y=0, level=level, label="E")
        e12 = base_graph.add_vert(pos_x=-4, pos_y=0, level=level, label="E")
        i1 = base_graph.add_vert(pos_x=0, pos_y=0, level=level, label="I")

        e8 = base_graph.add_vert(pos_x=-12, pos_y=-4, level=level, label="E")
        e9 = base_graph.add_vert(pos_x=-12, pos_y=4, level=level, label="E")
        e10 = base_graph.add_vert(pos_x=-8, pos_y=-4, level=level, label="E")
        e11 = base_graph.add_vert(pos_x=-8, pos_y=4, level=level, label="E")
        e13 = base_graph.add_vert(pos_x=-12, pos_y=0, level=level, label="E")
        i2 = base_graph.add_vert(pos_x=-8, pos_y=0, level=level, label="I")
        base_graph.add_edges([(e1, e6), (e6, e2), (e2, e7), (e7, e3), (e3, e5), (e5, e4), (e4, e12), (e12, e1), (e4, e10), (e10, e8), (e8, e13), (e13, e9), (e9, e11), (e11, e1)])
        base_graph.add_edges([(i1, e1), (i1, e2), (i1, e3), (i1, e4)])
        base_graph.add_edges([(i2, e1), (i2, e4), (i2, e8), (i2, e9)])

        # for debugging
        # visualise_graph(base_graph, level)

        i_match = match_P5(base_graph, level)
        self.assertEqual(i_match, [])

    def test_match_P5_incorrect_pos_large(self):
        level = 0
        base_graph = StandardizedGraph()
        e1 = base_graph.add_vert(pos_x=-4, pos_y=4, level=level, label="E")
        e2 = base_graph.add_vert(pos_x=4, pos_y=4, level=level, label="E")
        e3 = base_graph.add_vert(pos_x=4, pos_y=-4, level=level, label="E")
        e4 = base_graph.add_vert(pos_x=-4, pos_y=-4, level=level, label="E")
        e5 = base_graph.add_vert(pos_x=-4, pos_y=-2, level=level, label="E")
        e6 = base_graph.add_vert(pos_x=0, pos_y=4, level=level, label="E")
        e7 = base_graph.add_vert(pos_x=4, pos_y=0, level=level, label="E")
        i1 = base_graph.add_vert(pos_x=0, pos_y=0, level=level, label="I")

        e8 = base_graph.add_vert(pos_x=-12, pos_y=-4, level=level, label="E")
        e9 = base_graph.add_vert(pos_x=-12, pos_y=4, level=level, label="E")
        e10 = base_graph.add_vert(pos_x=-8, pos_y=-4, level=level, label="E")
        e11 = base_graph.add_vert(pos_x=-8, pos_y=4, level=level, label="E")
        i2 = base_graph.add_vert(pos_x=-8, pos_y=0, level=level, label="I")
        base_graph.add_edges([(e1, e6), (e6, e2), (e2, e7), (e7, e3), (e3, e4), (e4, e5), (e5, e1), (e4, e10), (e10, e8), (e8, e9), (e9, e11), (e11, e1)])
        base_graph.add_edges([(i1, e1), (i1, e2), (i1, e3), (i1, e4)])
        base_graph.add_edges([(i2, e1), (i2, e4), (i2, e8), (i2, e9)])

        # for debugging
        # visualise_graph(base_graph, level)

        i_match = match_P5(base_graph, level)
        self.assertEqual(i_match, [])

    def test_match_P5_incorrect_missing_large(self):
        level = 0
        base_graph = StandardizedGraph()
        e1 = base_graph.add_vert(pos_x=-4, pos_y=4, level=level, label="E")
        e2 = base_graph.add_vert(pos_x=4, pos_y=4, level=level, label="E")
        e3 = base_graph.add_vert(pos_x=4, pos_y=-4, level=level, label="E")
        e4 = base_graph.add_vert(pos_x=-4, pos_y=-4, level=level, label="E")
        e6 = base_graph.add_vert(pos_x=0, pos_y=4, level=level, label="E")
        e7 = base_graph.add_vert(pos_x=4, pos_y=0, level=level, label="E")
        i1 = base_graph.add_vert(pos_x=0, pos_y=0, level=level, label="I")

        e8 = base_graph.add_vert(pos_x=-12, pos_y=-4, level=level, label="E")
        e9 = base_graph.add_vert(pos_x=-12, pos_y=4, level=level, label="E")
        e10 = base_graph.add_vert(pos_x=-8, pos_y=-4, level=level, label="E")
        e11 = base_graph.add_vert(pos_x=-8, pos_y=4, level=level, label="E")
        i2 = base_graph.add_vert(pos_x=-8, pos_y=0, level=level, label="I")
        base_graph.add_edges([(e1, e6), (e6, e2), (e2, e7), (e7, e3), (e3, e4), (e4, e1), (e4, e10), (e10, e8), (e8, e9), (e9, e11), (e11, e1)])
        base_graph.add_edges([(i1, e1), (i1, e2), (i1, e3), (i1, e4)])
        base_graph.add_edges([(i2, e1), (i2, e4), (i2, e8), (i2, e9)])

        # for debugging
        # visualise_graph(base_graph, level)

        i_match = match_P5(base_graph, level)
        self.assertEqual(i_match, [])

    def test_match_P5_incorrect_label_large(self):
        level = 0
        base_graph = StandardizedGraph()
        e1 = base_graph.add_vert(pos_x=-4, pos_y=4, level=level, label="F")
        e2 = base_graph.add_vert(pos_x=4, pos_y=4, level=level, label="E")
        e3 = base_graph.add_vert(pos_x=4, pos_y=-4, level=level, label="E")
        e4 = base_graph.add_vert(pos_x=-4, pos_y=-4, level=level, label="E")
        e5 = base_graph.add_vert(pos_x=-4, pos_y=0, level=level, label="E")
        e6 = base_graph.add_vert(pos_x=0, pos_y=4, level=level, label="E")
        e7 = base_graph.add_vert(pos_x=4, pos_y=0, level=level, label="E")
        i1 = base_graph.add_vert(pos_x=0, pos_y=0, level=level, label="I")

        e8 = base_graph.add_vert(pos_x=-12, pos_y=-4, level=level, label="E")
        e9 = base_graph.add_vert(pos_x=-12, pos_y=4, level=level, label="E")
        e10 = base_graph.add_vert(pos_x=-8, pos_y=-4, level=level, label="E")
        e11 = base_graph.add_vert(pos_x=-8, pos_y=4, level=level, label="E")
        i2 = base_graph.add_vert(pos_x=-8, pos_y=0, level=level, label="I")
        base_graph.add_edges([(e1, e6), (e6, e2), (e2, e7), (e7, e3), (e3, e4), (e4, e5), (e5, e1), (e4, e10), (e10, e8), (e8, e9), (e9, e11), (e11, e1)])
        base_graph.add_edges([(i1, e1), (i1, e2), (i1, e3), (i1, e4)])
        base_graph.add_edges([(i2, e1), (i2, e4), (i2, e8), (i2, e9)])

        # for debugging
        # visualise_graph(base_graph, level)

        i_match = match_P5(base_graph, level)
        self.assertEqual(i_match, [])

    def test_match_P5_missing_edge_large(self):
        level = 0
        base_graph = StandardizedGraph()
        e1 = base_graph.add_vert(pos_x=-4, pos_y=4, level=level, label="E")
        e2 = base_graph.add_vert(pos_x=4, pos_y=4, level=level, label="E")
        e3 = base_graph.add_vert(pos_x=4, pos_y=-4, level=level, label="E")
        e4 = base_graph.add_vert(pos_x=-4, pos_y=-4, level=level, label="E")
        e5 = base_graph.add_vert(pos_x=0, pos_y=-4, level=level, label="E")
        e6 = base_graph.add_vert(pos_x=0, pos_y=4, level=level, label="E")
        e7 = base_graph.add_vert(pos_x=4, pos_y=0, level=level, label="E")
        i1 = base_graph.add_vert(pos_x=0, pos_y=0, level=level, label="I")

        e8 = base_graph.add_vert(pos_x=-12, pos_y=-4, level=level, label="E")
        e9 = base_graph.add_vert(pos_x=-12, pos_y=4, level=level, label="E")
        e10 = base_graph.add_vert(pos_x=-8, pos_y=-4, level=level, label="E")
        e11 = base_graph.add_vert(pos_x=-8, pos_y=4, level=level, label="E")
        i2 = base_graph.add_vert(pos_x=-8, pos_y=0, level=level, label="I")
        base_graph.add_edges([(e6, e2), (e2, e7), (e7, e3), (e3, e5), (e5, e4), (e4, e1), (e4, e10), (e10, e8), (e8, e9), (e9, e11), (e11, e1)])
        base_graph.add_edges([(i1, e1), (i1, e2), (i1, e3), (i1, e4)])
        base_graph.add_edges([(i2, e1), (i2, e4), (i2, e8), (i2, e9)])

        # for debugging
        # visualise_graph(base_graph, level)

        i_match = match_P5(base_graph, level)
        self.assertEqual(i_match, [])


if __name__ == '__main__':
    unittest.main()

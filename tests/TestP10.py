import unittest

from networkx import is_isomorphic

from productions.P10 import match_P10, P10
from utils.vis import visualise_graph
from utils.StandardizedGraph import StandardizedGraph


class TestP10(unittest.TestCase):
    def test_match_correct(self):
        level = 0
        base_graph = StandardizedGraph()

        e1 = base_graph.add_vert(pos_x=-4, pos_y=4, level=level, label="E")
        e2 = base_graph.add_vert(pos_x=4, pos_y=4, level=level, label="E")
        e3 = base_graph.add_vert(pos_x=4, pos_y=-4, level=level, label="E")
        e4 = base_graph.add_vert(pos_x=-4, pos_y=-4, level=level, label="E")

        i = base_graph.add_vert(pos_x=0, pos_y=0, level=level, label="I")
        base_graph.add_edges([(e1, e2), (e2, e3), (e3, e4), (e4, e1)])
        base_graph.add_edges([(i, e1), (i, e2), (i, e3), (i, e4)])

        # for debugging
        visualise_graph(base_graph, level)

        matched = match_P10(base_graph, level)
        self.assertEqual([i.underlying], [vert.underlying for vert in matched])

        new_graph = P10(base_graph, matched[0])

        expected_graph = StandardizedGraph()
        old_e1 = expected_graph.add_vert(pos_x=-4, pos_y=4, level=level, label="E")
        old_e2 = expected_graph.add_vert(pos_x=4, pos_y=4, level=level, label="E")
        old_e3 = expected_graph.add_vert(pos_x=4, pos_y=-4, level=level, label="E")
        old_e4 = expected_graph.add_vert(pos_x=-4, pos_y=-4, level=level, label="E")

        # small 'i', because this is the right side of production
        old_i = expected_graph.add_vert(pos_x=0, pos_y=0, level=level, label="i")
        expected_graph.add_edges(
            [(old_e1, old_e2), (old_e2, old_e3), (old_e3, old_e4), (old_e4, old_e1)])
        expected_graph.add_edges([(old_i, old_e1), (old_i, old_e2), (old_i, old_e3), (old_i, old_e4)])

        e1 = expected_graph.add_vert(pos_x=-4, pos_y=4, level=level + 1, label="E")
        e2 = expected_graph.add_vert(pos_x=4, pos_y=4, level=level + 1, label="E")
        e3 = expected_graph.add_vert(pos_x=4, pos_y=-4, level=level + 1, label="E")
        e4 = expected_graph.add_vert(pos_x=-4, pos_y=-4, level=level + 1, label="E")

        expected_graph.add_edges([
            (e1, e2),
            (e2, e3),
            (e3, e4),
            (e4, e1)
        ])

        i = expected_graph.add_vert(pos_x=0, pos_y=0, level=level + 1, label="I")
        expected_graph.add_edges([(i, e1), (i, e2), (i, e3), (i, e4), (old_i, i)])

        # for debugging
        visualise_graph(new_graph, level + 1)
        visualise_graph(expected_graph, level + 1)

        self.assertTrue(is_isomorphic(new_graph.underlying, expected_graph.underlying))

    def test_without_E_vertex(self):
        level = 0
        base_graph = StandardizedGraph()

        e1 = base_graph.add_vert(pos_x=-4, pos_y=4, level=level, label="E")
        e2 = base_graph.add_vert(pos_x=4, pos_y=4, level=level, label="E")
        e3 = base_graph.add_vert(pos_x=4, pos_y=-4, level=level, label="E")

        i = base_graph.add_vert(pos_x=0, pos_y=0, level=level, label="I")
        base_graph.add_edges([(e1, e2), (e2, e3)])
        base_graph.add_edges([(i, e1), (i, e2), (i, e3)])

        # for debugging
        visualise_graph(base_graph, level)

        matched = match_P10(base_graph, level)
        self.assertEqual([], [vert.underlying for vert in matched])

    def test_without_I_vertex(self):
        level = 0
        base_graph = StandardizedGraph()

        e1 = base_graph.add_vert(pos_x=-4, pos_y=4, level=level, label="E")
        e2 = base_graph.add_vert(pos_x=4, pos_y=4, level=level, label="E")
        e3 = base_graph.add_vert(pos_x=4, pos_y=-4, level=level, label="E")
        e4 = base_graph.add_vert(pos_x=-4, pos_y=-4, level=level, label="E")

        base_graph.add_edges([(e1, e2), (e2, e3), (e3, e4), (e4, e1)])

        # for debugging
        visualise_graph(base_graph, level)

        matched = match_P10(base_graph, level)
        self.assertEqual([], [vert.underlying for vert in matched])

    def test_without_E_to_E_edge(self):
        level = 0
        base_graph = StandardizedGraph()

        e1 = base_graph.add_vert(pos_x=-4, pos_y=4, level=level, label="E")
        e2 = base_graph.add_vert(pos_x=4, pos_y=4, level=level, label="E")
        e3 = base_graph.add_vert(pos_x=4, pos_y=-4, level=level, label="E")
        e4 = base_graph.add_vert(pos_x=-4, pos_y=-4, level=level, label="E")

        i = base_graph.add_vert(pos_x=0, pos_y=0, level=level, label="I")
        base_graph.add_edges([(e2, e3), (e3, e4), (e4, e1)])
        base_graph.add_edges([(i, e1), (i, e2), (i, e3), (i, e4)])

        # for debugging
        visualise_graph(base_graph, level)

        matched = match_P10(base_graph, level)
        self.assertEqual([], [vert.underlying for vert in matched])

    def test_without_E_to_I_edge(self):
        level = 0
        base_graph = StandardizedGraph()

        e1 = base_graph.add_vert(pos_x=-4, pos_y=4, level=level, label="E")
        e2 = base_graph.add_vert(pos_x=4, pos_y=4, level=level, label="E")
        e3 = base_graph.add_vert(pos_x=4, pos_y=-4, level=level, label="E")
        e4 = base_graph.add_vert(pos_x=-4, pos_y=-4, level=level, label="E")

        i = base_graph.add_vert(pos_x=0, pos_y=0, level=level, label="I")
        base_graph.add_edges([(e1, e2), (e2, e3), (e3, e4), (e4, e1)])
        base_graph.add_edges([(i, e2), (i, e3), (i, e4)])

        # for debugging
        visualise_graph(base_graph, level)

        matched = match_P10(base_graph, level)
        self.assertEqual([], [vert.underlying for vert in matched])

    def test_with_wrong_label(self):
        level = 0
        base_graph = StandardizedGraph()

        e1 = base_graph.add_vert(pos_x=-4, pos_y=4, level=level, label="E")
        e2 = base_graph.add_vert(pos_x=4, pos_y=4, level=level, label="E")
        e3 = base_graph.add_vert(pos_x=4, pos_y=-4, level=level, label="E")
        e4 = base_graph.add_vert(pos_x=-4, pos_y=-4, level=level, label="Z")

        i = base_graph.add_vert(pos_x=0, pos_y=0, level=level, label="I")
        base_graph.add_edges([(e1, e2), (e2, e3), (e3, e4), (e4, e1)])
        base_graph.add_edges([(i, e1), (i, e2), (i, e3), (i, e4)])

        # for debugging
        visualise_graph(base_graph, level)

        matched = match_P10(base_graph, level)
        self.assertEqual([], [vert.underlying for vert in matched])

    def test_with_addition_vertex(self):
        level = 0
        base_graph = StandardizedGraph()

        e1 = base_graph.add_vert(pos_x=-4, pos_y=4, level=level, label="E")
        e2 = base_graph.add_vert(pos_x=4, pos_y=4, level=level, label="E")
        e3 = base_graph.add_vert(pos_x=4, pos_y=-4, level=level, label="E")
        e4 = base_graph.add_vert(pos_x=-4, pos_y=-4, level=level, label="E")
        e5 = base_graph.add_vert(pos_x=-4, pos_y=0, level=level, label="E")

        i = base_graph.add_vert(pos_x=0, pos_y=0, level=level, label="I")
        base_graph.add_edges([(e1, e2), (e2, e3), (e3, e4), (e4, e5), (e5, e1)])
        base_graph.add_edges([(i, e1), (i, e2), (i, e3), (i, e4)])

        # for debugging
        visualise_graph(base_graph, level)

        matched = match_P10(base_graph, level)
        self.assertEqual([], [vert.underlying for vert in matched])

    def test_with_addition_edge(self):
        level = 0
        base_graph = StandardizedGraph()

        e1 = base_graph.add_vert(pos_x=-4, pos_y=4, level=level, label="E")
        e2 = base_graph.add_vert(pos_x=4, pos_y=4, level=level, label="E")
        e3 = base_graph.add_vert(pos_x=4, pos_y=-4, level=level, label="E")
        e4 = base_graph.add_vert(pos_x=-4, pos_y=-4, level=level, label="E")

        i = base_graph.add_vert(pos_x=0, pos_y=0, level=level, label="I")
        base_graph.add_edges([(e1, e2), (e2, e3), (e3, e4), (e4, e1), (e1, e3)])
        base_graph.add_edges([(i, e1), (i, e2), (i, e3), (i, e4)])

        # for debugging
        visualise_graph(base_graph, level)

        matched = match_P10(base_graph, level)
        self.assertEqual([], [vert.underlying for vert in matched])

    def test_match_correct_double(self):
        level = 0
        base_graph = StandardizedGraph()

        e1 = base_graph.add_vert(pos_x=-4, pos_y=4, level=level, label="E")
        e2 = base_graph.add_vert(pos_x=4, pos_y=4, level=level, label="E")
        e3 = base_graph.add_vert(pos_x=4, pos_y=-4, level=level, label="E")
        e4 = base_graph.add_vert(pos_x=-4, pos_y=-4, level=level, label="E")

        e5 = base_graph.add_vert(pos_x=-12, pos_y=4, level=level, label="E")
        e6 = base_graph.add_vert(pos_x=-12, pos_y=-4, level=level, label="E")

        i = base_graph.add_vert(pos_x=0, pos_y=0, level=level, label="I")
        i2 = base_graph.add_vert(pos_x=-8, pos_y=0, level=level, label="I")

        base_graph.add_edges([(e1, e2), (e2, e3), (e3, e4), (e4, e1)])
        base_graph.add_edges([(i, e1), (i, e2), (i, e3), (i, e4)])
        base_graph.add_edges([(e4, e6), (e6, e5), (e5, e1)])
        base_graph.add_edges([(i2, e1), (i2, e4), (i2, e5), (i2, e6)])

        # for debugging
        visualise_graph(base_graph, level)

        matched = match_P10(base_graph, level)
        new_graph = P10(base_graph, matched[0])

        expected_graph = StandardizedGraph()
        old_e1 = expected_graph.add_vert(pos_x=-4, pos_y=4, level=level, label="E")
        old_e2 = expected_graph.add_vert(pos_x=4, pos_y=4, level=level, label="E")
        old_e3 = expected_graph.add_vert(pos_x=4, pos_y=-4, level=level, label="E")
        old_e4 = expected_graph.add_vert(pos_x=-4, pos_y=-4, level=level, label="E")

        old_e5 = expected_graph.add_vert(pos_x=-12, pos_y=4, level=level, label="E")
        old_e6 = expected_graph.add_vert(pos_x=-12, pos_y=-4, level=level, label="E")

        old_i = expected_graph.add_vert(pos_x=0, pos_y=0, level=level, label="I")
        # small 'i', because this is the right side of production
        old_i2 = expected_graph.add_vert(pos_x=-8, pos_y=0, level=level, label="i")

        expected_graph.add_edges(
            [(old_e1, old_e2), (old_e2, old_e3), (old_e3, old_e4), (old_e4, old_e1)])
        expected_graph.add_edges([(old_i, old_e1), (old_i, old_e2), (old_i, old_e3), (old_i, old_e4)])

        expected_graph.add_edges([(old_e4, old_e6), (old_e6, old_e5), (old_e5, old_e1)])
        expected_graph.add_edges([(old_i2, old_e1), (old_i2, old_e4), (old_i2, old_e5), (old_i2, old_e6)])

        e1 = expected_graph.add_vert(pos_x=-4, pos_y=4, level=level + 1, label="E")
        e2 = expected_graph.add_vert(pos_x=4, pos_y=4, level=level + 1, label="E")
        e3 = expected_graph.add_vert(pos_x=4, pos_y=-4, level=level + 1, label="E")
        e4 = expected_graph.add_vert(pos_x=-4, pos_y=-4, level=level + 1, label="E")

        expected_graph.add_edges([
            (e1, e2),
            (e2, e3),
            (e3, e4),
            (e4, e1)
        ])

        i = expected_graph.add_vert(pos_x=0, pos_y=0, level=level + 1, label="I")
        expected_graph.add_edges([(i, e1), (i, e2), (i, e3), (i, e4), (old_i, i)])

        visualise_graph(new_graph, level + 1)
        visualise_graph(expected_graph, level + 1)
        self.assertTrue(is_isomorphic(new_graph.underlying, expected_graph.underlying))

    def test_not_match_double_without_E_common_vertex(self):
        level = 0
        base_graph = StandardizedGraph()

        e1 = base_graph.add_vert(pos_x=-4, pos_y=4, level=level, label="E")
        e2 = base_graph.add_vert(pos_x=4, pos_y=4, level=level, label="E")
        e3 = base_graph.add_vert(pos_x=4, pos_y=-4, level=level, label="E")

        e5 = base_graph.add_vert(pos_x=-12, pos_y=4, level=level, label="E")
        e6 = base_graph.add_vert(pos_x=-12, pos_y=-4, level=level, label="E")

        i = base_graph.add_vert(pos_x=0, pos_y=0, level=level, label="I")
        i2 = base_graph.add_vert(pos_x=-8, pos_y=0, level=level, label="I")

        base_graph.add_edges([(e1, e2), (e2, e3)])
        base_graph.add_edges([(i, e1), (i, e2), (i, e3)])
        base_graph.add_edges([(e6, e5), (e5, e1)])
        base_graph.add_edges([(i2, e1), (i2, e5), (i2, e6)])

        # for debugging
        visualise_graph(base_graph, level)

        matched = match_P10(base_graph, level)
        self.assertEqual([], [vert.underlying for vert in matched])

    def test_not_match_double_without_common_edge(self):
        level = 0
        base_graph = StandardizedGraph()

        e1 = base_graph.add_vert(pos_x=-4, pos_y=4, level=level, label="E")
        e2 = base_graph.add_vert(pos_x=4, pos_y=4, level=level, label="E")
        e3 = base_graph.add_vert(pos_x=4, pos_y=-4, level=level, label="E")
        e4 = base_graph.add_vert(pos_x=-4, pos_y=-4, level=level, label="E")

        e5 = base_graph.add_vert(pos_x=-12, pos_y=4, level=level, label="E")
        e6 = base_graph.add_vert(pos_x=-12, pos_y=-4, level=level, label="E")

        i = base_graph.add_vert(pos_x=0, pos_y=0, level=level, label="I")
        i2 = base_graph.add_vert(pos_x=-8, pos_y=0, level=level, label="I")

        base_graph.add_edges([(e1, e2), (e2, e3), (e3, e4)])
        base_graph.add_edges([(i, e1), (i, e2), (i, e3), (i, e4)])
        base_graph.add_edges([(e4, e6), (e6, e5), (e5, e1)])
        base_graph.add_edges([(i2, e1), (i2, e4), (i2, e5), (i2, e6)])

        # for debugging
        visualise_graph(base_graph, level)

        matched = match_P10(base_graph, level)
        self.assertEqual([], [vert.underlying for vert in matched])

    def test_not_match_double_with_additional_vertex_on_common_edge(self):
        level = 0
        base_graph = StandardizedGraph()

        e1 = base_graph.add_vert(pos_x=-4, pos_y=4, level=level, label="E")
        e2 = base_graph.add_vert(pos_x=4, pos_y=4, level=level, label="E")
        e3 = base_graph.add_vert(pos_x=4, pos_y=-4, level=level, label="E")
        e4 = base_graph.add_vert(pos_x=-4, pos_y=-4, level=level, label="Z")

        e5 = base_graph.add_vert(pos_x=-12, pos_y=4, level=level, label="E")
        e6 = base_graph.add_vert(pos_x=-12, pos_y=-4, level=level, label="E")
        e7 = base_graph.add_vert(pos_x=-4, pos_y=0, level=level, label="E")

        i = base_graph.add_vert(pos_x=0, pos_y=0, level=level, label="I")
        i2 = base_graph.add_vert(pos_x=-8, pos_y=0, level=level, label="I")

        base_graph.add_edges([(e1, e2), (e2, e3), (e3, e4), (e4, e7), (e7, e1)])
        base_graph.add_edges([(i, e1), (i, e2), (i, e3), (i, e4)])
        base_graph.add_edges([(e4, e6), (e6, e5), (e5, e1)])
        base_graph.add_edges([(i2, e1), (i2, e4), (i2, e5), (i2, e6)])

        # for debugging
        visualise_graph(base_graph, level)

        matched = match_P10(base_graph, level)
        self.assertEqual([], [vert.underlying for vert in matched])

    def test_not_match_double_with_additional_edges(self):
        level = 0
        base_graph = StandardizedGraph()

        e1 = base_graph.add_vert(pos_x=-4, pos_y=4, level=level, label="E")
        e2 = base_graph.add_vert(pos_x=4, pos_y=4, level=level, label="E")
        e3 = base_graph.add_vert(pos_x=4, pos_y=-4, level=level, label="E")
        e4 = base_graph.add_vert(pos_x=-4, pos_y=-4, level=level, label="E")

        e5 = base_graph.add_vert(pos_x=-12, pos_y=4, level=level, label="E")
        e6 = base_graph.add_vert(pos_x=-12, pos_y=-4, level=level, label="E")

        i = base_graph.add_vert(pos_x=0, pos_y=0, level=level, label="I")
        i2 = base_graph.add_vert(pos_x=-8, pos_y=0, level=level, label="I")

        base_graph.add_edges([(e1, e2), (e2, e3), (e3, e4), (e4, e1)])
        base_graph.add_edges([(i, e1), (i, e2), (i, e3), (i, e4)])
        base_graph.add_edges([(e4, e6), (e6, e5), (e5, e1)])
        base_graph.add_edges([(i2, e1), (i2, e4), (i2, e5), (i2, e6)])
        base_graph.add_edges([(e1, e3), (e1, e6)])

        # for debugging
        visualise_graph(base_graph, level)

        matched = match_P10(base_graph, level)
        self.assertEqual([], [vert.underlying for vert in matched])

    def test_match_correct_double_with_additional_edge(self):
        level = 0
        base_graph = StandardizedGraph()

        e1 = base_graph.add_vert(pos_x=-4, pos_y=4, level=level, label="E")
        e2 = base_graph.add_vert(pos_x=4, pos_y=4, level=level, label="E")
        e3 = base_graph.add_vert(pos_x=4, pos_y=-4, level=level, label="E")
        e4 = base_graph.add_vert(pos_x=-4, pos_y=-4, level=level, label="E")

        e5 = base_graph.add_vert(pos_x=-12, pos_y=4, level=level, label="E")
        e6 = base_graph.add_vert(pos_x=-12, pos_y=-4, level=level, label="E")

        i = base_graph.add_vert(pos_x=0, pos_y=0, level=level, label="I")
        i2 = base_graph.add_vert(pos_x=-8, pos_y=0, level=level, label="I")

        base_graph.add_edges([(e1, e2), (e2, e3), (e3, e4), (e4, e1)])
        base_graph.add_edges([(i, e1), (i, e2), (i, e3), (i, e4)])
        base_graph.add_edges([(e4, e6), (e6, e5), (e5, e1)])
        base_graph.add_edges([(i2, e1), (i2, e4), (i2, e5), (i2, e6)])
        base_graph.add_edges([(e6, e1)])

        # for debugging
        visualise_graph(base_graph, level)

        matched = match_P10(base_graph, level)
        new_graph = P10(base_graph, matched[0])

        expected_graph = StandardizedGraph()
        old_e1 = expected_graph.add_vert(pos_x=-4, pos_y=4, level=level, label="E")
        old_e2 = expected_graph.add_vert(pos_x=4, pos_y=4, level=level, label="E")
        old_e3 = expected_graph.add_vert(pos_x=4, pos_y=-4, level=level, label="E")
        old_e4 = expected_graph.add_vert(pos_x=-4, pos_y=-4, level=level, label="E")

        old_e5 = expected_graph.add_vert(pos_x=-12, pos_y=4, level=level, label="E")
        old_e6 = expected_graph.add_vert(pos_x=-12, pos_y=-4, level=level, label="E")

        old_i = expected_graph.add_vert(pos_x=0, pos_y=0, level=level, label="I")
        # small 'i', because this is the right side of production
        old_i2 = expected_graph.add_vert(pos_x=-8, pos_y=0, level=level, label="i")

        expected_graph.add_edges(
            [(old_e1, old_e2), (old_e2, old_e3), (old_e3, old_e4), (old_e4, old_e1)])
        expected_graph.add_edges([(old_i, old_e1), (old_i, old_e2), (old_i, old_e3), (old_i, old_e4)])

        expected_graph.add_edges([(old_e4, old_e6), (old_e6, old_e5), (old_e5, old_e1)])
        expected_graph.add_edges([(old_i2, old_e1), (old_i2, old_e4), (old_i2, old_e5), (old_i2, old_e6)])
        expected_graph.add_edges([(old_e6, old_e1)])

        e1 = expected_graph.add_vert(pos_x=-4, pos_y=4, level=level + 1, label="E")
        e2 = expected_graph.add_vert(pos_x=4, pos_y=4, level=level + 1, label="E")
        e3 = expected_graph.add_vert(pos_x=4, pos_y=-4, level=level + 1, label="E")
        e4 = expected_graph.add_vert(pos_x=-4, pos_y=-4, level=level + 1, label="E")

        expected_graph.add_edges([
            (e1, e2),
            (e2, e3),
            (e3, e4),
            (e4, e1)
        ])

        i = expected_graph.add_vert(pos_x=0, pos_y=0, level=level + 1, label="I")
        expected_graph.add_edges([(i, e1), (i, e2), (i, e3), (i, e4), (old_i, i)])

        visualise_graph(new_graph, level + 1)
        visualise_graph(expected_graph, level + 1)
        self.assertTrue(is_isomorphic(new_graph.underlying, expected_graph.underlying))


if __name__ == '__main__':
    unittest.main()

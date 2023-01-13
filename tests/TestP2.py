from networkx.algorithms.isomorphism import is_isomorphic
from productions.P2 import match_P2, P2
from unittest import TestCase
from utils.StandardizedGraph import StandardizedGraph
from utils.vis import visualise_graph


class TestP2(TestCase):

    def test_typical_happy_path(self):
        level = 0
        graph = StandardizedGraph()

        left_upper = graph.add_vert(-10, 10, "E", level)
        right_upper = graph.add_vert(10, 10, "E", level)
        right_lower = graph.add_vert(10, -10, "E", level)
        left_lower = graph.add_vert(-10, -10, "E", level)
        i_middle = graph.add_vert(0, 0, "I", level)

        graph.add_edges([
            (i_middle, left_upper), (i_middle, right_upper), (i_middle, right_lower), (i_middle, left_lower),
            (left_upper, right_upper), (right_upper, right_lower), (right_lower, left_lower), (left_lower, left_upper)
        ])

        visualise_graph(graph, center_level=0, hist=[0])

        # check matched subgraph
        matched = match_P2(graph, 0)
        self.assertEqual([i_middle.underlying], [vert.underlying for vert in matched])

        # building expected result graph
        expected_result_graph_P2 = StandardizedGraph()
        exp_lu = expected_result_graph_P2.add_vert(-10, 10, "E", level)
        exp_ru = expected_result_graph_P2.add_vert(10, 10, "E", level)
        exp_rl = expected_result_graph_P2.add_vert(10, -10, "E", level)
        exp_ll = expected_result_graph_P2.add_vert(-10, -10, "E", level)
        exp_i_middle = expected_result_graph_P2.add_vert(0, 0, "I", level)

        exp_new_lu = expected_result_graph_P2.add_vert(-10, 10, "E", level + 1)
        exp_new_upper = expected_result_graph_P2.add_vert(0, 10, "E", level + 1)
        exp_new_ru = expected_result_graph_P2.add_vert(10, 10, "E", level + 1)
        exp_new_right = expected_result_graph_P2.add_vert(10, 0, "E", level + 1)
        exp_new_rl = expected_result_graph_P2.add_vert(10, -10, "E", level + 1)
        exp_new_lower = expected_result_graph_P2.add_vert(0, -10, "E", level + 1)
        exp_new_ll = expected_result_graph_P2.add_vert(-10, -10, "E", level + 1)
        exp_new_left = expected_result_graph_P2.add_vert(-10, 0, "E", level + 1)
        exp_new_middle = expected_result_graph_P2.add_vert(0, 0, "E", level + 1)

        exp_new_i_lu = expected_result_graph_P2.add_vert(-5, 5, "I", level + 1)
        exp_new_i_ru = expected_result_graph_P2.add_vert(5, 5, "I", level + 1)
        exp_new_i_rl = expected_result_graph_P2.add_vert(5, -5, "I", level + 1)
        exp_new_i_ll = expected_result_graph_P2.add_vert(-5, -5, "I", level + 1)

        expected_result_graph_P2.add_edges([
            (exp_i_middle, exp_lu), (exp_i_middle, exp_ru), (exp_i_middle, exp_rl), (exp_i_middle, exp_ll),
            (exp_lu, exp_ru), (exp_ru, exp_rl), (exp_rl, exp_ll), (exp_ll, exp_lu),

            (exp_i_middle, exp_new_i_lu), (exp_i_middle, exp_new_i_ru),
            (exp_i_middle, exp_new_i_rl), (exp_i_middle, exp_new_i_ll),

            (exp_new_i_lu, exp_new_lu), (exp_new_i_lu, exp_new_upper),
            (exp_new_i_lu, exp_new_middle), (exp_new_i_lu, exp_new_left),
            (exp_new_i_ru, exp_new_upper), (exp_new_i_ru, exp_new_ru),
            (exp_new_i_ru, exp_new_right), (exp_new_i_ru, exp_new_middle),

            (exp_new_i_rl, exp_new_middle), (exp_new_i_rl, exp_new_right),
            (exp_new_i_rl, exp_new_rl), (exp_new_i_rl, exp_new_lower),
            (exp_new_i_ll, exp_new_left), (exp_new_i_ll, exp_new_middle),
            (exp_new_i_ll, exp_new_lower), (exp_new_i_ll, exp_new_ll),

            (exp_new_middle, exp_new_left), (exp_new_middle, exp_new_upper),
            (exp_new_middle, exp_new_right), (exp_new_middle, exp_new_lower),

            (exp_new_lu, exp_new_upper), (exp_new_upper, exp_new_ru),
            (exp_new_ru, exp_new_right), (exp_new_right, exp_new_rl),
            (exp_new_rl, exp_new_lower), (exp_new_lower, exp_new_ll),
            (exp_new_ll, exp_new_left), (exp_new_left, exp_new_lu),
        ])

        # check created graph from production 2
        result_graph_P2 = P2(graph, matched[0])
        self.assertTrue(is_isomorphic(result_graph_P2.underlying, expected_result_graph_P2.underlying))

        visualise_graph(result_graph_P2)

    def test_typical_without_E_vertex(self):
        level = 0
        graph = StandardizedGraph()

        left_upper = graph.add_vert(-10, 10, "E", level)
        right_upper = graph.add_vert(10, 10, "E", level)
        left_lower = graph.add_vert(-10, -10, "E", level)
        i_middle = graph.add_vert(0, 0, "I", level)

        graph.add_edges([
            (i_middle, left_upper), (i_middle, right_upper), (i_middle, left_lower),
            (left_upper, right_upper), (left_lower, left_upper)
        ])

        visualise_graph(graph, center_level=0, hist=[0])

        # check matched subgraph
        matched = match_P2(graph, 0)
        self.assertEqual([], [vert.underlying for vert in matched])

    def test_typical_without_I_vertex(self):
        level = 0
        graph = StandardizedGraph()

        left_upper = graph.add_vert(-10, 10, "E", level)
        right_upper = graph.add_vert(10, 10, "E", level)
        right_lower = graph.add_vert(10, -10, "E", level)
        left_lower = graph.add_vert(-10, -10, "E", level)

        graph.add_edges([
            (left_upper, right_upper), (right_upper, right_lower), (right_lower, left_lower), (left_lower, left_upper)
        ])

        visualise_graph(graph, center_level=0, hist=[0])

        # check matched subgraph
        matched = match_P2(graph, 0)
        self.assertEqual([], [vert.underlying for vert in matched])

    def test_typical_without_E_to_E_edge(self):
        level = 0
        graph = StandardizedGraph()

        left_upper = graph.add_vert(-10, 10, "E", level)
        right_upper = graph.add_vert(10, 10, "E", level)
        right_lower = graph.add_vert(10, -10, "E", level)
        left_lower = graph.add_vert(-10, -10, "E", level)
        i_middle = graph.add_vert(0, 0, "I", level)

        graph.add_edges([
            (i_middle, left_upper), (i_middle, right_upper), (i_middle, right_lower), (i_middle, left_lower),
            (left_upper, right_upper), (right_upper, right_lower), (left_lower, left_upper)
        ])

        visualise_graph(graph, center_level=0, hist=[0])

        # check matched subgraph
        matched = match_P2(graph, 0)
        self.assertEqual([], [vert.underlying for vert in matched])

    def test_typical_without_I_to_E_edge(self):
        level = 0
        graph = StandardizedGraph()

        left_upper = graph.add_vert(-10, 10, "E", level)
        right_upper = graph.add_vert(10, 10, "E", level)
        right_lower = graph.add_vert(10, -10, "E", level)
        left_lower = graph.add_vert(-10, -10, "E", level)
        i_middle = graph.add_vert(0, 0, "I", level)

        graph.add_edges([
            (i_middle, left_upper), (i_middle, right_upper), (i_middle, left_lower),
            (left_upper, right_upper), (right_upper, right_lower), (right_lower, left_lower), (left_lower, left_upper)
        ])

        visualise_graph(graph, center_level=0, hist=[0])

        # check matched subgraph
        matched = match_P2(graph, 0)
        self.assertEqual([], [vert.underlying for vert in matched])

    def test_typical_wrong_label(self):
        level = 0
        graph = StandardizedGraph()

        left_upper = graph.add_vert(-10, 10, "E", level)
        right_upper = graph.add_vert(10, 10, "E", level)
        right_lower = graph.add_vert(10, -10, "I", level)
        left_lower = graph.add_vert(-10, -10, "E", level)
        i_middle = graph.add_vert(0, 0, "I", level)

        graph.add_edges([
            (i_middle, left_upper), (i_middle, right_upper), (i_middle, right_lower), (i_middle, left_lower),
            (left_upper, right_upper), (right_upper, right_lower), (right_lower, left_lower), (left_lower, left_upper)
        ])

        visualise_graph(graph, center_level=0, hist=[0])

        # check matched subgraph
        matched = match_P2(graph, 0)
        self.assertEqual([], [vert.underlying for vert in matched])

    def test_typical_too_many_vertices(self):
        level = 0
        graph = StandardizedGraph()

        left_upper = graph.add_vert(-10, 10, "E", level)
        right_upper = graph.add_vert(10, 10, "E", level)
        right_lower = graph.add_vert(10, -10, "E", level)
        left_lower = graph.add_vert(-10, -10, "E", level)
        additional = graph.add_vert(0, 10, "E", level)
        i_middle = graph.add_vert(0, 0, "I", level)

        graph.add_edges([
            (i_middle, left_upper), (i_middle, right_upper), (i_middle, right_lower), (i_middle, left_lower),
            (left_upper, additional), (additional, right_upper), (i_middle, additional),
            (right_upper, right_lower), (right_lower, left_lower), (left_lower, left_upper),
        ])

        visualise_graph(graph, center_level=0, hist=[0])

        # check matched subgraph
        matched = match_P2(graph, 0)
        self.assertEqual([], [vert.underlying for vert in matched])

    def test_typical_too_many_edges(self):
        level = 0
        graph = StandardizedGraph()

        left_upper = graph.add_vert(-10, 10, "E", level)
        right_upper = graph.add_vert(10, 10, "E", level)
        right_lower = graph.add_vert(10, -10, "E", level)
        left_lower = graph.add_vert(-10, -10, "E", level)
        i_middle = graph.add_vert(0, 0, "I", level)

        graph.add_edges([
            (i_middle, left_upper), (i_middle, right_upper), (i_middle, right_lower), (i_middle, left_lower),
            (left_upper, right_upper), (right_upper, right_lower), (right_lower, left_lower), (left_lower, left_upper),
            (left_upper, right_lower)
        ])

        visualise_graph(graph, center_level=0, hist=[0])

        # check matched subgraph
        matched = match_P2(graph, 0)
        self.assertEqual([], [vert.underlying for vert in matched])

    def test_extended_happy_path(self):
        level = 0
        graph = StandardizedGraph()

        left_upper = graph.add_vert(-10, 10, "E", level)
        right_upper = graph.add_vert(10, 10, "E", level)
        right_lower = graph.add_vert(10, -10, "E", level)
        left_lower = graph.add_vert(-10, -10, "E", level)
        left_left_upper = graph.add_vert(-20, 10, "E", level)
        left_left_lower = graph.add_vert(-20, -10, "E", level)
        i_middle = graph.add_vert(0, 0, "I", level)

        graph.add_edges([
            (i_middle, left_upper), (i_middle, right_upper), (i_middle, right_lower), (i_middle, left_lower),
            (left_upper, right_upper), (right_upper, right_lower), (right_lower, left_lower), (left_lower, left_upper),
            (left_left_upper, left_upper), (left_left_lower, left_lower), (left_left_lower, left_left_upper)
        ])

        visualise_graph(graph, center_level=0, hist=[0])

        # check matched subgraph
        matched = match_P2(graph, 0)
        self.assertEqual([i_middle.underlying], [vert.underlying for vert in matched])

        # building expected result graph
        expected_result_graph_P2 = StandardizedGraph()
        exp_lu = expected_result_graph_P2.add_vert(-10, 10, "E", level)
        exp_ru = expected_result_graph_P2.add_vert(10, 10, "E", level)
        exp_rl = expected_result_graph_P2.add_vert(10, -10, "E", level)
        exp_ll = expected_result_graph_P2.add_vert(-10, -10, "E", level)
        exp_llu = expected_result_graph_P2.add_vert(-20, 10, "E", level)
        exp_lll = expected_result_graph_P2.add_vert(-20, -10, "E", level)
        exp_i_middle = expected_result_graph_P2.add_vert(0, 0, "I", level)

        exp_new_lu = expected_result_graph_P2.add_vert(-10, 10, "E", level + 1)
        exp_new_upper = expected_result_graph_P2.add_vert(0, 10, "E", level + 1)
        exp_new_ru = expected_result_graph_P2.add_vert(10, 10, "E", level + 1)
        exp_new_right = expected_result_graph_P2.add_vert(10, 0, "E", level + 1)
        exp_new_rl = expected_result_graph_P2.add_vert(10, -10, "E", level + 1)
        exp_new_lower = expected_result_graph_P2.add_vert(0, -10, "E", level + 1)
        exp_new_ll = expected_result_graph_P2.add_vert(-10, -10, "E", level + 1)
        exp_new_left = expected_result_graph_P2.add_vert(-10, 0, "E", level + 1)
        exp_new_middle = expected_result_graph_P2.add_vert(0, 0, "E", level + 1)

        exp_new_i_lu = expected_result_graph_P2.add_vert(-5, 5, "I", level + 1)
        exp_new_i_ru = expected_result_graph_P2.add_vert(5, 5, "I", level + 1)
        exp_new_i_rl = expected_result_graph_P2.add_vert(5, -5, "I", level + 1)
        exp_new_i_ll = expected_result_graph_P2.add_vert(-5, -5, "I", level + 1)

        expected_result_graph_P2.add_edges([
            (exp_i_middle, exp_lu), (exp_i_middle, exp_ru), (exp_i_middle, exp_rl), (exp_i_middle, exp_ll),
            (exp_lu, exp_ru), (exp_ru, exp_rl), (exp_rl, exp_ll), (exp_ll, exp_lu),
            (exp_lll, exp_ll), (exp_llu, exp_lu), (exp_lll, exp_llu),

            (exp_i_middle, exp_new_i_lu), (exp_i_middle, exp_new_i_ru),
            (exp_i_middle, exp_new_i_rl), (exp_i_middle, exp_new_i_ll),

            (exp_new_i_lu, exp_new_lu), (exp_new_i_lu, exp_new_upper),
            (exp_new_i_lu, exp_new_middle), (exp_new_i_lu, exp_new_left),
            (exp_new_i_ru, exp_new_upper), (exp_new_i_ru, exp_new_ru),
            (exp_new_i_ru, exp_new_right), (exp_new_i_ru, exp_new_middle),

            (exp_new_i_rl, exp_new_middle), (exp_new_i_rl, exp_new_right),
            (exp_new_i_rl, exp_new_rl), (exp_new_i_rl, exp_new_lower),
            (exp_new_i_ll, exp_new_left), (exp_new_i_ll, exp_new_middle),
            (exp_new_i_ll, exp_new_lower), (exp_new_i_ll, exp_new_ll),

            (exp_new_middle, exp_new_left), (exp_new_middle, exp_new_upper),
            (exp_new_middle, exp_new_right), (exp_new_middle, exp_new_lower),

            (exp_new_lu, exp_new_upper), (exp_new_upper, exp_new_ru),
            (exp_new_ru, exp_new_right), (exp_new_right, exp_new_rl),
            (exp_new_rl, exp_new_lower), (exp_new_lower, exp_new_ll),
            (exp_new_ll, exp_new_left), (exp_new_left, exp_new_lu),
        ])

        # check created graph from production 2
        result_graph_P2 = P2(graph, matched[0])
        self.assertTrue(is_isomorphic(result_graph_P2.underlying, expected_result_graph_P2.underlying))

        visualise_graph(result_graph_P2)

    def test_doubled_happy_path(self):
        level = 0
        graph = StandardizedGraph()

        left_upper = graph.add_vert(-10, 10, "E", level)
        right_upper = graph.add_vert(10, 10, "E", level)
        right_lower = graph.add_vert(10, -10, "E", level)
        left_lower = graph.add_vert(-10, -10, "E", level)
        left_left_upper = graph.add_vert(-30, 10, "E", level)
        left_left_lower = graph.add_vert(-30, -10, "E", level)
        i_left_left = graph.add_vert(-20, 0, "I", level)
        i_middle = graph.add_vert(0, 0, "I", level)

        graph.add_edges([
            (i_middle, left_upper), (i_middle, right_upper), (i_middle, right_lower), (i_middle, left_lower),
            (left_upper, right_upper), (right_upper, right_lower), (right_lower, left_lower), (left_lower, left_upper),
            (left_left_upper, left_upper), (left_left_lower, left_lower), (left_left_lower, left_left_upper),
            (i_left_left, left_left_upper), (i_left_left, left_upper),
            (i_left_left, left_lower), (i_left_left, left_left_lower)
        ])

        visualise_graph(graph, center_level=0, hist=[0])

        # check matched subgraph
        matched = match_P2(graph, 0)
        self.assertEqual([i_left_left.underlying, i_middle.underlying], [vert.underlying for vert in matched])

        # building expected result graph
        expected_result_graph_P2 = StandardizedGraph()
        exp_lu = expected_result_graph_P2.add_vert(-10, 10, "E", level)
        exp_ru = expected_result_graph_P2.add_vert(10, 10, "E", level)
        exp_rl = expected_result_graph_P2.add_vert(10, -10, "E", level)
        exp_ll = expected_result_graph_P2.add_vert(-10, -10, "E", level)
        exp_llu = expected_result_graph_P2.add_vert(-30, 10, "E", level)
        exp_lll = expected_result_graph_P2.add_vert(-30, -10, "E", level)
        exp_i_ll = expected_result_graph_P2.add_vert(-20, 0, "I", level)
        exp_i_middle = expected_result_graph_P2.add_vert(0, 0, "I", level)

        exp_new_lu = expected_result_graph_P2.add_vert(-30, 10, "E", level + 1)
        exp_new_upper = expected_result_graph_P2.add_vert(-20, 10, "E", level + 1)
        exp_new_ru = expected_result_graph_P2.add_vert(-10, 10, "E", level + 1)
        exp_new_right = expected_result_graph_P2.add_vert(-10, 0, "E", level + 1)
        exp_new_rl = expected_result_graph_P2.add_vert(-10, -10, "E", level + 1)
        exp_new_lower = expected_result_graph_P2.add_vert(-20, -10, "E", level + 1)
        exp_new_ll = expected_result_graph_P2.add_vert(-30, -10, "E", level + 1)
        exp_new_left = expected_result_graph_P2.add_vert(-30, 0, "E", level + 1)
        exp_new_middle = expected_result_graph_P2.add_vert(-20, 0, "E", level + 1)

        exp_new_i_lu = expected_result_graph_P2.add_vert(-5, 5, "I", level + 1)
        exp_new_i_ru = expected_result_graph_P2.add_vert(5, 5, "I", level + 1)
        exp_new_i_rl = expected_result_graph_P2.add_vert(5, -5, "I", level + 1)
        exp_new_i_ll = expected_result_graph_P2.add_vert(-5, -5, "I", level + 1)

        expected_result_graph_P2.add_edges([
            (exp_i_middle, exp_lu), (exp_i_middle, exp_ru), (exp_i_middle, exp_rl), (exp_i_middle, exp_ll),
            (exp_lu, exp_ru), (exp_ru, exp_rl), (exp_rl, exp_ll), (exp_ll, exp_lu),
            (exp_lll, exp_ll), (exp_llu, exp_lu), (exp_lll, exp_llu),

            (exp_i_ll, exp_llu), (exp_i_ll, exp_lu), (exp_i_ll, exp_ll), (exp_i_ll, exp_lll),

            (exp_i_ll, exp_new_i_lu), (exp_i_ll, exp_new_i_ru),
            (exp_i_ll, exp_new_i_rl), (exp_i_ll, exp_new_i_ll),

            (exp_new_i_lu, exp_new_lu), (exp_new_i_lu, exp_new_upper),
            (exp_new_i_lu, exp_new_middle), (exp_new_i_lu, exp_new_left),
            (exp_new_i_ru, exp_new_upper), (exp_new_i_ru, exp_new_ru),
            (exp_new_i_ru, exp_new_right), (exp_new_i_ru, exp_new_middle),

            (exp_new_i_rl, exp_new_middle), (exp_new_i_rl, exp_new_right),
            (exp_new_i_rl, exp_new_rl), (exp_new_i_rl, exp_new_lower),
            (exp_new_i_ll, exp_new_left), (exp_new_i_ll, exp_new_middle),
            (exp_new_i_ll, exp_new_lower), (exp_new_i_ll, exp_new_ll),

            (exp_new_middle, exp_new_left), (exp_new_middle, exp_new_upper),
            (exp_new_middle, exp_new_right), (exp_new_middle, exp_new_lower),

            (exp_new_lu, exp_new_upper), (exp_new_upper, exp_new_ru),
            (exp_new_ru, exp_new_right), (exp_new_right, exp_new_rl),
            (exp_new_rl, exp_new_lower), (exp_new_lower, exp_new_ll),
            (exp_new_ll, exp_new_left), (exp_new_left, exp_new_lu),
        ])

        # check created graph from production 2
        result_graph_P2 = P2(graph, matched[0])
        self.assertTrue(is_isomorphic(result_graph_P2.underlying, expected_result_graph_P2.underlying))

        visualise_graph(result_graph_P2)

    def test_doubled_without_common_E_vertex(self):
        level = 0
        graph = StandardizedGraph()

        left_upper = graph.add_vert(-10, 10, "E", level)
        right_upper = graph.add_vert(10, 10, "E", level)
        right_lower = graph.add_vert(10, -10, "E", level)
        left_left_upper = graph.add_vert(-30, 10, "E", level)
        left_left_lower = graph.add_vert(-30, -10, "E", level)
        i_left_left = graph.add_vert(-20, 0, "I", level)
        i_middle = graph.add_vert(0, 0, "I", level)

        graph.add_edges([
            (i_middle, left_upper), (i_middle, right_upper), (i_middle, right_lower),
            (left_upper, right_upper), (right_upper, right_lower),
            (left_left_upper, left_upper), (left_left_lower, left_left_upper),
            (i_left_left, left_left_upper), (i_left_left, left_upper),
            (i_left_left, left_left_lower)
        ])

        visualise_graph(graph, center_level=0, hist=[0])

        # check matched subgraph
        matched = match_P2(graph, 0)
        self.assertEqual([], [vert.underlying for vert in matched])

    def test_doubled_without_common_edge(self):
        level = 0
        graph = StandardizedGraph()

        left_upper = graph.add_vert(-10, 10, "E", level)
        right_upper = graph.add_vert(10, 10, "E", level)
        right_lower = graph.add_vert(10, -10, "E", level)
        left_lower = graph.add_vert(-10, -10, "E", level)
        left_left_upper = graph.add_vert(-30, 10, "E", level)
        left_left_lower = graph.add_vert(-30, -10, "E", level)
        i_left_left = graph.add_vert(-20, 0, "I", level)
        i_middle = graph.add_vert(0, 0, "I", level)

        graph.add_edges([
            (i_middle, left_upper), (i_middle, right_upper), (i_middle, right_lower), (i_middle, left_lower),
            (left_upper, right_upper), (right_upper, right_lower), (right_lower, left_lower),
            (left_left_upper, left_upper), (left_left_lower, left_lower), (left_left_lower, left_left_upper),
            (i_left_left, left_left_upper), (i_left_left, left_upper),
            (i_left_left, left_lower), (i_left_left, left_left_lower)
        ])

        visualise_graph(graph, center_level=0, hist=[0])

        # check matched subgraph
        matched = match_P2(graph, 0)
        self.assertEqual([], [vert.underlying for vert in matched])

    def test_doubled_wrong_label_on_common_vertex(self):
        level = 0
        graph = StandardizedGraph()

        left_upper = graph.add_vert(-10, 10, "E", level)
        right_upper = graph.add_vert(10, 10, "E", level)
        right_lower = graph.add_vert(10, -10, "E", level)
        left_lower = graph.add_vert(-10, -10, "I", level)
        left_left_upper = graph.add_vert(-30, 10, "E", level)
        left_left_lower = graph.add_vert(-30, -10, "E", level)
        i_left_left = graph.add_vert(-20, 0, "I", level)
        i_middle = graph.add_vert(0, 0, "I", level)

        graph.add_edges([
            (i_middle, left_upper), (i_middle, right_upper), (i_middle, right_lower), (i_middle, left_lower),
            (left_upper, right_upper), (right_upper, right_lower), (right_lower, left_lower), (left_lower, left_upper),
            (left_left_upper, left_upper), (left_left_lower, left_lower), (left_left_lower, left_left_upper),
            (i_left_left, left_left_upper), (i_left_left, left_upper),
            (i_left_left, left_lower), (i_left_left, left_left_lower)
        ])

        visualise_graph(graph, center_level=0, hist=[0])

        # check matched subgraph
        matched = match_P2(graph, 0)
        self.assertEqual([], [vert.underlying for vert in matched])

    def test_doubled_too_many_vertices(self):
        level = 0
        graph = StandardizedGraph()

        left_upper = graph.add_vert(-10, 10, "E", level)
        right_upper = graph.add_vert(10, 10, "E", level)
        right_lower = graph.add_vert(10, -10, "E", level)
        left_lower = graph.add_vert(-10, -10, "E", level)
        left_middle = graph.add_vert(-10, 0, "E", level)
        left_left_upper = graph.add_vert(-30, 10, "E", level)
        left_left_lower = graph.add_vert(-30, -10, "E", level)
        i_left_left = graph.add_vert(-20, 0, "I", level)
        i_middle = graph.add_vert(0, 0, "I", level)

        graph.add_edges([
            (i_middle, left_upper), (i_middle, right_upper), (i_middle, right_lower),
            (i_middle, left_lower), (i_middle, left_middle),
            (left_upper, right_upper), (right_upper, right_lower), (right_lower, left_lower),
            (left_lower, left_middle), (left_middle, left_upper),
            (left_left_upper, left_upper), (left_left_lower, left_lower), (left_left_lower, left_left_upper),
            (i_left_left, left_left_upper), (i_left_left, left_upper),
            (i_left_left, left_lower), (i_left_left, left_left_lower), (i_left_left, left_middle)
        ])

        visualise_graph(graph, center_level=0, hist=[0])

        # check matched subgraph
        matched = match_P2(graph, 0)
        self.assertEqual([], [vert.underlying for vert in matched])

    def test_doubled_too_many_edges(self):
        level = 0
        graph = StandardizedGraph()

        left_upper = graph.add_vert(-10, 10, "E", level)
        right_upper = graph.add_vert(10, 10, "E", level)
        right_lower = graph.add_vert(10, -10, "E", level)
        left_lower = graph.add_vert(-10, -10, "E", level)
        left_left_upper = graph.add_vert(-30, 10, "E", level)
        left_left_lower = graph.add_vert(-30, -10, "E", level)
        i_left_left = graph.add_vert(-20, 0, "I", level)
        i_middle = graph.add_vert(0, 0, "I", level)

        graph.add_edges([
            (i_middle, left_upper), (i_middle, right_upper), (i_middle, right_lower), (i_middle, left_lower),
            (left_upper, right_upper), (right_upper, right_lower), (right_lower, left_lower), (left_lower, left_upper),
            (left_left_upper, left_upper), (left_left_lower, left_lower), (left_left_lower, left_left_upper),
            (i_left_left, left_left_upper), (i_left_left, left_upper),
            (i_left_left, left_lower), (i_left_left, left_left_lower),
            (left_left_upper, left_lower), (left_upper, right_lower)
        ])

        visualise_graph(graph, center_level=0, hist=[0])

        # check matched subgraph
        matched = match_P2(graph, 0)
        self.assertEqual([], [vert.underlying for vert in matched])

    def test_doubled_happy_path_with_additional_edge(self):
        level = 0
        graph = StandardizedGraph()

        left_upper = graph.add_vert(-10, 10, "E", level)
        right_upper = graph.add_vert(10, 10, "E", level)
        right_lower = graph.add_vert(10, -10, "E", level)
        left_lower = graph.add_vert(-10, -10, "E", level)
        left_left_upper = graph.add_vert(-30, 10, "E", level)
        left_left_lower = graph.add_vert(-30, -10, "E", level)
        i_left_left = graph.add_vert(-20, 0, "I", level)
        i_middle = graph.add_vert(0, 0, "I", level)

        graph.add_edges([
            (i_middle, left_upper), (i_middle, right_upper), (i_middle, right_lower), (i_middle, left_lower),
            (left_upper, right_upper), (right_upper, right_lower), (right_lower, left_lower), (left_lower, left_upper),
            (left_left_upper, left_upper), (left_left_lower, left_lower), (left_left_lower, left_left_upper),
            (i_left_left, left_left_upper), (i_left_left, left_upper),
            (i_left_left, left_lower), (i_left_left, left_left_lower),
            (left_left_upper, right_lower)
        ])

        visualise_graph(graph, center_level=0, hist=[0])

        # check matched subgraph
        matched = match_P2(graph, 0)
        self.assertEqual([i_left_left.underlying, i_middle.underlying], [vert.underlying for vert in matched])

        # building expected result graph
        expected_result_graph_P2 = StandardizedGraph()
        exp_lu = expected_result_graph_P2.add_vert(-10, 10, "E", level)
        exp_ru = expected_result_graph_P2.add_vert(10, 10, "E", level)
        exp_rl = expected_result_graph_P2.add_vert(10, -10, "E", level)
        exp_ll = expected_result_graph_P2.add_vert(-10, -10, "E", level)
        exp_llu = expected_result_graph_P2.add_vert(-30, 10, "E", level)
        exp_lll = expected_result_graph_P2.add_vert(-30, -10, "E", level)
        exp_i_ll = expected_result_graph_P2.add_vert(-20, 0, "I", level)
        exp_i_middle = expected_result_graph_P2.add_vert(0, 0, "I", level)

        exp_new_lu = expected_result_graph_P2.add_vert(-30, 10, "E", level + 1)
        exp_new_upper = expected_result_graph_P2.add_vert(-20, 10, "E", level + 1)
        exp_new_ru = expected_result_graph_P2.add_vert(-10, 10, "E", level + 1)
        exp_new_right = expected_result_graph_P2.add_vert(-10, 0, "E", level + 1)
        exp_new_rl = expected_result_graph_P2.add_vert(-10, -10, "E", level + 1)
        exp_new_lower = expected_result_graph_P2.add_vert(-20, -10, "E", level + 1)
        exp_new_ll = expected_result_graph_P2.add_vert(-30, -10, "E", level + 1)
        exp_new_left = expected_result_graph_P2.add_vert(-30, 0, "E", level + 1)
        exp_new_middle = expected_result_graph_P2.add_vert(-20, 0, "E", level + 1)

        exp_new_i_lu = expected_result_graph_P2.add_vert(-5, 5, "I", level + 1)
        exp_new_i_ru = expected_result_graph_P2.add_vert(5, 5, "I", level + 1)
        exp_new_i_rl = expected_result_graph_P2.add_vert(5, -5, "I", level + 1)
        exp_new_i_ll = expected_result_graph_P2.add_vert(-5, -5, "I", level + 1)

        expected_result_graph_P2.add_edges([
            (exp_i_middle, exp_lu), (exp_i_middle, exp_ru), (exp_i_middle, exp_rl), (exp_i_middle, exp_ll),
            (exp_lu, exp_ru), (exp_ru, exp_rl), (exp_rl, exp_ll), (exp_ll, exp_lu),
            (exp_lll, exp_ll), (exp_llu, exp_lu), (exp_lll, exp_llu),

            (exp_i_ll, exp_llu), (exp_i_ll, exp_lu), (exp_i_ll, exp_ll), (exp_i_ll, exp_lll),

            (exp_i_ll, exp_new_i_lu), (exp_i_ll, exp_new_i_ru),
            (exp_i_ll, exp_new_i_rl), (exp_i_ll, exp_new_i_ll),

            (exp_new_i_lu, exp_new_lu), (exp_new_i_lu, exp_new_upper),
            (exp_new_i_lu, exp_new_middle), (exp_new_i_lu, exp_new_left),
            (exp_new_i_ru, exp_new_upper), (exp_new_i_ru, exp_new_ru),
            (exp_new_i_ru, exp_new_right), (exp_new_i_ru, exp_new_middle),

            (exp_new_i_rl, exp_new_middle), (exp_new_i_rl, exp_new_right),
            (exp_new_i_rl, exp_new_rl), (exp_new_i_rl, exp_new_lower),
            (exp_new_i_ll, exp_new_left), (exp_new_i_ll, exp_new_middle),
            (exp_new_i_ll, exp_new_lower), (exp_new_i_ll, exp_new_ll),

            (exp_new_middle, exp_new_left), (exp_new_middle, exp_new_upper),
            (exp_new_middle, exp_new_right), (exp_new_middle, exp_new_lower),

            (exp_new_lu, exp_new_upper), (exp_new_upper, exp_new_ru),
            (exp_new_ru, exp_new_right), (exp_new_right, exp_new_rl),
            (exp_new_rl, exp_new_lower), (exp_new_lower, exp_new_ll),
            (exp_new_ll, exp_new_left), (exp_new_left, exp_new_lu),

            (exp_llu, exp_rl)
        ])

        # check created graph from production 2
        result_graph_P2 = P2(graph, matched[0])
        self.assertTrue(is_isomorphic(result_graph_P2.underlying, expected_result_graph_P2.underlying))

        visualise_graph(result_graph_P2)

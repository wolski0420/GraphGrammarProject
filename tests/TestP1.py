from networkx.algorithms.isomorphism import is_isomorphic
from productions.P1 import match_P1, P1
from unittest import TestCase
from utils.StandardizedGraph import StandardizedGraph
from utils.vis import visualise_graph


class TestP1(TestCase):
    def test_typical_happy_path(self):
        level = 0
        graph = StandardizedGraph()
        el = graph.add_vert(0, 0, "El", level)

        visualise_graph(graph, center_level=0, hist=[0])

        # check matched subgraph
        matched = match_P1(graph)
        self.assertEqual([el.underlying], [vert.underlying for vert in matched])

        # building expected result graph
        expected_result_graph_P1 = StandardizedGraph()
        exp_el = expected_result_graph_P1.add_vert(0, 0, "el", level)
        exp_i = expected_result_graph_P1.add_vert(0, 0, "I", level + 1)
        exp_lu = expected_result_graph_P1.add_vert(-10, 10, "E", level + 1)
        exp_ru = expected_result_graph_P1.add_vert(10, 10, "E", level + 1)
        exp_rl = expected_result_graph_P1.add_vert(10, -10, "E", level + 1)
        exp_ll = expected_result_graph_P1.add_vert(-10, -10, "E", level + 1)

        expected_result_graph_P1.add_edges([
            (exp_i, exp_lu), (exp_i, exp_ru), (exp_i, exp_rl), (exp_i, exp_ll),
            (exp_lu, exp_ru), (exp_ru, exp_rl), (exp_rl, exp_ll), (exp_ll, exp_lu),
            (exp_el, exp_i)
        ])

        # check created graph from production 1
        result_graph_P1 = P1(graph, matched[0])
        self.assertTrue(is_isomorphic(result_graph_P1.underlying, expected_result_graph_P1.underlying))

        visualise_graph(result_graph_P1)

    def test_typical_wrong_label(self):
        level = 0
        graph = StandardizedGraph()
        el = graph.add_vert(0, 0, "el", level)

        visualise_graph(graph, center_level=0, hist=[0])

        # check matched subgraph
        matched = match_P1(graph)
        self.assertEqual([], [vert.underlying for vert in matched])

    def test_doubled_happy_path(self):
        level = 0
        graph = StandardizedGraph()
        el = graph.add_vert(0, 0, "El", level)
        el2 = graph.add_vert(10, 0, "El", level)

        graph.add_edges([(el, el2)])

        visualise_graph(graph, center_level=0, hist=[0])

        # check matched subgraph
        matched = match_P1(graph)
        self.assertEqual([el.underlying, el2.underlying], [vert.underlying for vert in matched])

        # building expected result graph
        expected_result_graph_P1 = StandardizedGraph()
        exp_el = expected_result_graph_P1.add_vert(0, 0, "el", level)
        exp_el2 = expected_result_graph_P1.add_vert(10, 0, "El", level)
        exp_i = expected_result_graph_P1.add_vert(0, 0, "I", level + 1)
        exp_lu = expected_result_graph_P1.add_vert(-10, 10, "E", level + 1)
        exp_ru = expected_result_graph_P1.add_vert(10, 10, "E", level + 1)
        exp_rl = expected_result_graph_P1.add_vert(10, -10, "E", level + 1)
        exp_ll = expected_result_graph_P1.add_vert(-10, -10, "E", level + 1)

        expected_result_graph_P1.add_edges([
            (exp_i, exp_lu), (exp_i, exp_ru), (exp_i, exp_rl), (exp_i, exp_ll),
            (exp_lu, exp_ru), (exp_ru, exp_rl), (exp_rl, exp_ll), (exp_ll, exp_lu),
            (exp_el, exp_i), (exp_el2, exp_el)
        ])

        # check created graph from production 1
        result_graph_P1 = P1(graph, matched[0])
        self.assertTrue(is_isomorphic(result_graph_P1.underlying, expected_result_graph_P1.underlying))

        visualise_graph(result_graph_P1)

    def test_doubled_with_only_one_correct(self):
        level = 0
        graph = StandardizedGraph()
        el = graph.add_vert(0, 0, "el", level)
        el2 = graph.add_vert(10, 0, "El", level)

        graph.add_edges([(el, el2)])

        visualise_graph(graph, center_level=0, hist=[0])

        # check matched subgraph
        matched = match_P1(graph)
        self.assertEqual([el2.underlying], [vert.underlying for vert in matched])

        # building expected result graph
        expected_result_graph_P1 = StandardizedGraph()
        exp_el = expected_result_graph_P1.add_vert(0, 0, "el", level)
        exp_el2 = expected_result_graph_P1.add_vert(10, 0, "El", level)
        exp_i = expected_result_graph_P1.add_vert(10, 0, "I", level + 1)
        exp_lu = expected_result_graph_P1.add_vert(0, 10, "E", level + 1)
        exp_ru = expected_result_graph_P1.add_vert(20, 10, "E", level + 1)
        exp_rl = expected_result_graph_P1.add_vert(20, -10, "E", level + 1)
        exp_ll = expected_result_graph_P1.add_vert(0, -10, "E", level + 1)

        expected_result_graph_P1.add_edges([
            (exp_i, exp_lu), (exp_i, exp_ru), (exp_i, exp_rl), (exp_i, exp_ll),
            (exp_lu, exp_ru), (exp_ru, exp_rl), (exp_rl, exp_ll), (exp_ll, exp_lu),
            (exp_el2, exp_i), (exp_el2, exp_el)
        ])

        # check created graph from production 1
        result_graph_P1 = P1(graph, matched[0])
        self.assertTrue(is_isomorphic(result_graph_P1.underlying, expected_result_graph_P1.underlying))

        visualise_graph(result_graph_P1)

    def test_doubled_wrong_label_both(self):
        level = 0
        graph = StandardizedGraph()
        el = graph.add_vert(0, 0, "el", level)
        el2 = graph.add_vert(10, 0, "el", level)

        graph.add_edges([(el, el2)])

        visualise_graph(graph, center_level=0, hist=[0])

        # check matched subgraph
        matched = match_P1(graph)
        self.assertEqual([], [vert.underlying for vert in matched])


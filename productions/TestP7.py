import unittest
from utils.vis import visualise_graph
from utils.StandardizedGraph import StandardizedGraph, Vert
from .P7 import match_P7, P7


class TestP7(unittest.TestCase):
    def test_match_P7_correct(self):
        level = 0
        base_graph = StandardizedGraph()
        i1 = base_graph.add_vert(pos_x=-4, pos_y=0, level=level, label="i")
        i2 = base_graph.add_vert(pos_x=4, pos_y=0, level=level, label="i")
        I1 = base_graph.add_vert(pos_x=-2, pos_y=2, level=level, label="I")
        I2 = base_graph.add_vert(pos_x=-2, pos_y=-2, level=level, label="I")
        I3 = base_graph.add_vert(pos_x=2, pos_y=2, level=level, label="I")
        I4 = base_graph.add_vert(pos_x=2, pos_y=-2, level=level, label="I")
        e1 = base_graph.add_vert(pos_x=0, pos_y=4, level=level, label="E")
        e2 = base_graph.add_vert(pos_x=0, pos_y=0, level=level, label="E")
        e3 = base_graph.add_vert(pos_x=0, pos_y=-4, level=level, label="E")
        e4 = base_graph.add_vert(pos_x=0, pos_y=4, level=level, label="E")
        e5 = base_graph.add_vert(pos_x=0, pos_y=0, level=level, label="E")
        e6 = base_graph.add_vert(pos_x=0, pos_y=-4, level=level, label="E")
        base_graph.add_edges([(i1, I1), (i1, I2), (i2, I3), (i2, I4)])
        base_graph.add_edges([(I1, e4), (I1, e5), (I2, e6), (I2, e5), (I3, e1), (I3, e2), (I4, e2), (I4, e3)])
        base_graph.add_edges([(e4, e5), (e6, e5), (e1, e2), (e2, e3)])


        # for debugging
        # visualise_graph(base_graph, level)

        i_match0, i_match1 = match_P7(base_graph, level)

        new_graph = P7(base_graph, i_match0, i_match1)

        expected_graph = StandardizedGraph()
        i1 = expected_graph.add_vert(pos_x=-4, pos_y=0, level=level, label="i")
        i2 = expected_graph.add_vert(pos_x=4, pos_y=0, level=level, label="i")
        I1 = expected_graph.add_vert(pos_x=-2, pos_y=2, level=level, label="I")
        I2 = expected_graph.add_vert(pos_x=-2, pos_y=-2, level=level, label="I")
        I3 = expected_graph.add_vert(pos_x=2, pos_y=2, level=level, label="I")
        I4 = expected_graph.add_vert(pos_x=2, pos_y=-2, level=level, label="I")
        e1 = expected_graph.add_vert(pos_x=0, pos_y=4, level=level, label="E")
        e2 = expected_graph.add_vert(pos_x=0, pos_y=0, level=level, label="E")
        e3 = expected_graph.add_vert(pos_x=0, pos_y=-4, level=level, label="E")
        expected_graph.add_edges([(i1, I1), (i1, I2), (i2, I3), (i2, I4)])
        expected_graph.add_edges([(I1, e1), (I1, e2), (I2, e3), (I2, e2), (I3, e1), (I3, e2), (I4, e2), (I4, e3)])
        expected_graph.add_edges([(e1, e2), (e2, e3)])

        # for debugging
        # visualise_graph(new_graph, level)
        # visualise_graph(expected_graph, level)

        self.assertEqual(new_graph, expected_graph)

    def test_match_P7_correct_rotated(self):
        level = 0
        base_graph = StandardizedGraph()
        i1 = base_graph.add_vert(pos_x=0, pos_y=-4, level=level, label="i")
        i2 = base_graph.add_vert(pos_x=0, pos_y=4, level=level, label="i")
        I1 = base_graph.add_vert(pos_x=2, pos_y=-2, level=level, label="I")
        I2 = base_graph.add_vert(pos_x=-2, pos_y=-2, level=level, label="I")
        I3 = base_graph.add_vert(pos_x=2, pos_y=2, level=level, label="I")
        I4 = base_graph.add_vert(pos_x=-2, pos_y=2, level=level, label="I")
        e1 = base_graph.add_vert(pos_x=4, pos_y=0, level=level, label="E")
        e2 = base_graph.add_vert(pos_x=0, pos_y=0, level=level, label="E")
        e3 = base_graph.add_vert(pos_x=-4, pos_y=0, level=level, label="E")
        e4 = base_graph.add_vert(pos_x=4, pos_y=0, level=level, label="E")
        e5 = base_graph.add_vert(pos_x=0, pos_y=0, level=level, label="E")
        e6 = base_graph.add_vert(pos_x=-4, pos_y=0, level=level, label="E")
        base_graph.add_edges([(i1, I1), (i1, I2), (i2, I3), (i2, I4)])
        base_graph.add_edges([(I1, e4), (I1, e5), (I2, e6), (I2, e5), (I3, e1), (I3, e2), (I4, e2), (I4, e3)])
        base_graph.add_edges([(e4, e5), (e6, e5), (e1, e2), (e2, e3)])

        # for debugging
        # visualise_graph(base_graph, level)

        i_match0, i_match1 = match_P7(base_graph, level)

        new_graph = P7(base_graph, i_match0, i_match1)

        expected_graph = StandardizedGraph()
        i1 = expected_graph.add_vert(pos_x=0, pos_y=-4, level=level, label="i")
        i2 = expected_graph.add_vert(pos_x=0, pos_y=4, level=level, label="i")
        I1 = expected_graph.add_vert(pos_x=2, pos_y=-2, level=level, label="I")
        I2 = expected_graph.add_vert(pos_x=-2, pos_y=-2, level=level, label="I")
        I3 = expected_graph.add_vert(pos_x=2, pos_y=2, level=level, label="I")
        I4 = expected_graph.add_vert(pos_x=-2, pos_y=2, level=level, label="I")
        e1 = expected_graph.add_vert(pos_x=4, pos_y=0, level=level, label="E")
        e2 = expected_graph.add_vert(pos_x=0, pos_y=0, level=level, label="E")
        e3 = expected_graph.add_vert(pos_x=-4, pos_y=0, level=level, label="E")
        expected_graph.add_edges([(i1, I1), (i1, I2), (i2, I3), (i2, I4)])
        expected_graph.add_edges([(I1, e1), (I1, e2), (I2, e3), (I2, e2), (I3, e1), (I3, e2), (I4, e2), (I4, e3)])
        expected_graph.add_edges([(e1, e2), (e2, e3)])

        # for debugging
        # visualise_graph(new_graph, level)
        # visualise_graph(expected_graph, level)

        self.assertEqual(new_graph, expected_graph)

    def test_match_P7_incorrect_pos(self):
        level = 0
        base_graph = StandardizedGraph()
        i1 = base_graph.add_vert(pos_x=-4, pos_y=0, level=level, label="i")
        i2 = base_graph.add_vert(pos_x=4, pos_y=0, level=level, label="i")
        I1 = base_graph.add_vert(pos_x=-2, pos_y=2, level=level, label="I")
        I2 = base_graph.add_vert(pos_x=-2, pos_y=-2, level=level, label="I")
        I3 = base_graph.add_vert(pos_x=2, pos_y=2, level=level, label="I")
        I4 = base_graph.add_vert(pos_x=2, pos_y=-2, level=level, label="I")
        e1 = base_graph.add_vert(pos_x=0, pos_y=4, level=level, label="E")
        e2 = base_graph.add_vert(pos_x=0, pos_y=-1, level=level, label="E")  # incorrect one
        e3 = base_graph.add_vert(pos_x=0, pos_y=-4, level=level, label="E")
        e4 = base_graph.add_vert(pos_x=0, pos_y=4, level=level, label="E")
        e5 = base_graph.add_vert(pos_x=0, pos_y=0, level=level, label="E")
        e6 = base_graph.add_vert(pos_x=0, pos_y=-4, level=level, label="E")
        base_graph.add_edges([(i1, I1), (i1, I2), (i2, I3), (i2, I4)])
        base_graph.add_edges([(I1, e4), (I1, e5), (I2, e6), (I2, e5), (I3, e1), (I3, e2), (I4, e2), (I4, e3)])
        base_graph.add_edges([(e4, e5), (e6, e5), (e1, e2), (e2, e3)])

        # for debugging
        visualise_graph(base_graph, level)

        i_match0, i_match1 = match_P7(base_graph, level)
        self.assertEqual(i_match0, [])
        self.assertEqual(i_match1, [])

    def test_match_P7_incorrect_missing(self):
        level = 0
        base_graph = StandardizedGraph()
        i1 = base_graph.add_vert(pos_x=-4, pos_y=0, level=level, label="i")
        i2 = base_graph.add_vert(pos_x=4, pos_y=0, level=level, label="i")
        I1 = base_graph.add_vert(pos_x=-2, pos_y=2, level=level, label="I")
        I2 = base_graph.add_vert(pos_x=-2, pos_y=-2, level=level, label="I")
        I3 = base_graph.add_vert(pos_x=2, pos_y=2, level=level, label="I")
        I4 = base_graph.add_vert(pos_x=2, pos_y=-2, level=level, label="I")
        e1 = base_graph.add_vert(pos_x=0, pos_y=4, level=level, label="E")
        e2 = base_graph.add_vert(pos_x=0, pos_y=0, level=level, label="E")
        e3 = base_graph.add_vert(pos_x=0, pos_y=-4, level=level, label="E")
        e4 = base_graph.add_vert(pos_x=0, pos_y=4, level=level, label="E")
        e5 = base_graph.add_vert(pos_x=0, pos_y=0, level=level, label="E")
        base_graph.add_edges([(i1, I1), (i1, I2), (i2, I3), (i2, I4)])
        base_graph.add_edges([(I1, e4), (I1, e5), (I2, e5), (I3, e1), (I3, e2), (I4, e2), (I4, e3)])
        base_graph.add_edges([(e4, e5), (e1, e2), (e2, e3)])

        # for debugging
        # visualise_graph(base_graph, level)

        i_match0, i_match1 = match_P7(base_graph, level)
        self.assertEqual(i_match0, [])
        self.assertEqual(i_match1, [])

    def test_match_P7_correct_large(self):
        level = 0
        base_graph = StandardizedGraph()
        i1 = base_graph.add_vert(pos_x=-4, pos_y=2, level=level, label="i")
        i2 = base_graph.add_vert(pos_x=4, pos_y=2, level=level, label="i")
        I1 = base_graph.add_vert(pos_x=-2, pos_y=3, level=level, label="I")
        I2 = base_graph.add_vert(pos_x=-2, pos_y=1, level=level, label="I")
        I3 = base_graph.add_vert(pos_x=2, pos_y=3, level=level, label="I")
        I4 = base_graph.add_vert(pos_x=2, pos_y=1, level=level, label="I")
        e1 = base_graph.add_vert(pos_x=0, pos_y=4, level=level, label="E")
        e2 = base_graph.add_vert(pos_x=0, pos_y=2, level=level, label="E")
        e3 = base_graph.add_vert(pos_x=0, pos_y=0, level=level, label="E")
        e4 = base_graph.add_vert(pos_x=0, pos_y=4, level=level, label="E")
        e5 = base_graph.add_vert(pos_x=0, pos_y=2, level=level, label="E")
        e6 = base_graph.add_vert(pos_x=0, pos_y=0, level=level, label="E")

        i3 = base_graph.add_vert(pos_x=-4, pos_y=-2, level=level, label="i")
        i4 = base_graph.add_vert(pos_x=4, pos_y=-2, level=level, label="i")
        I6 = base_graph.add_vert(pos_x=-2, pos_y=-3, level=level, label="I")
        I5 = base_graph.add_vert(pos_x=-2, pos_y=-1, level=level, label="I")
        I8 = base_graph.add_vert(pos_x=2, pos_y=-3, level=level, label="I")
        I7 = base_graph.add_vert(pos_x=2, pos_y=-1, level=level, label="I")
        e7 = base_graph.add_vert(pos_x=0, pos_y=0, level=level, label="E")
        e8 = base_graph.add_vert(pos_x=0, pos_y=-2, level=level, label="E")
        e9 = base_graph.add_vert(pos_x=0, pos_y=-4, level=level, label="E")
        e10 = base_graph.add_vert(pos_x=0, pos_y=0, level=level, label="E")
        e11 = base_graph.add_vert(pos_x=0, pos_y=-2, level=level, label="E")
        e12 = base_graph.add_vert(pos_x=0, pos_y=-4, level=level, label="E")

        base_graph.add_edges([(i1, I1), (i1, I2), (i2, I3), (i2, I4), (i3, I5), (i3, I6), (i4, I7), (i4, I8)])
        base_graph.add_edges([(I1, e4), (I1, e5), (I2, e6), (I2, e5), (I3, e1), (I3, e2), (I4, e2), (I4, e3)])
        base_graph.add_edges([(I5, e7), (I5, e8), (I6, e8), (I6, e9), (I7, e10), (I7, e11), (I8, e12), (I8, e11)])
        base_graph.add_edges([(e4, e5), (e6, e5), (e1, e2), (e2, e3), (e7, e8), (e8, e9), (e10, e11), (e11, e12)])

        # for debugging
        visualise_graph(base_graph, level)

        i_match0, i_match1 = match_P7(base_graph, level)

        new_graph = P7(base_graph, i_match0, i_match1)

        expected_graph = StandardizedGraph()
        i1 = expected_graph.add_vert(pos_x=-4, pos_y=2, level=level, label="i")
        i2 = expected_graph.add_vert(pos_x=4, pos_y=2, level=level, label="i")
        I1 = expected_graph.add_vert(pos_x=-2, pos_y=3, level=level, label="I")
        I2 = expected_graph.add_vert(pos_x=-2, pos_y=1, level=level, label="I")
        I3 = expected_graph.add_vert(pos_x=2, pos_y=3, level=level, label="I")
        I4 = expected_graph.add_vert(pos_x=2, pos_y=1, level=level, label="I")
        e1 = expected_graph.add_vert(pos_x=0, pos_y=4, level=level, label="E")
        e2 = expected_graph.add_vert(pos_x=0, pos_y=2, level=level, label="E")
        e3 = expected_graph.add_vert(pos_x=0, pos_y=0, level=level, label="E")

        i3 = expected_graph.add_vert(pos_x=-4, pos_y=-2, level=level, label="i")
        i4 = expected_graph.add_vert(pos_x=4, pos_y=-2, level=level, label="i")
        I6 = expected_graph.add_vert(pos_x=-2, pos_y=-3, level=level, label="I")
        I5 = expected_graph.add_vert(pos_x=-2, pos_y=-1, level=level, label="I")
        I8 = expected_graph.add_vert(pos_x=2, pos_y=-3, level=level, label="I")
        I7 = expected_graph.add_vert(pos_x=2, pos_y=-1, level=level, label="I")
        e8 = expected_graph.add_vert(pos_x=0, pos_y=-2, level=level, label="E")
        e9 = expected_graph.add_vert(pos_x=0, pos_y=-4, level=level, label="E")
        e11 = expected_graph.add_vert(pos_x=0, pos_y=-2, level=level, label="E")
        e12 = expected_graph.add_vert(pos_x=0, pos_y=-4, level=level, label="E")

        expected_graph.add_edges([(i1, I1), (i1, I2), (i2, I3), (i2, I4), (i3, I5), (i3, I6), (i4, I7), (i4, I8)])
        expected_graph.add_edges([(I1, e1), (I1, e2), (I2, e2), (I2, e3), (I3, e1), (I3, e2), (I4, e2), (I4, e3)])
        expected_graph.add_edges([(I5, e3), (I5, e8), (I6, e8), (I6, e9), (I7, e3), (I7, e11), (I8, e12), (I8, e11)])
        expected_graph.add_edges([(e1, e2), (e2, e3), (e3, e8), (e8, e9), (e3, e11), (e11, e12)])

        # for debugging
        # visualise_graph(new_graph, level)
        # visualise_graph(expected_graph, level)

        self.assertEqual(new_graph, expected_graph)
    def test_match_P7_correct_too_much(self):
        level = 0
        base_graph = StandardizedGraph()
        i1 = base_graph.add_vert(pos_x=-4, pos_y=0, level=level, label="i")
        i2 = base_graph.add_vert(pos_x=4, pos_y=0, level=level, label="i")
        I1 = base_graph.add_vert(pos_x=-2, pos_y=2, level=level, label="I")
        I2 = base_graph.add_vert(pos_x=-2, pos_y=-2, level=level, label="I")
        I3 = base_graph.add_vert(pos_x=2, pos_y=2, level=level, label="I")
        I4 = base_graph.add_vert(pos_x=2, pos_y=-2, level=level, label="I")
        e1 = base_graph.add_vert(pos_x=0, pos_y=4, level=level, label="E")
        e2 = base_graph.add_vert(pos_x=0, pos_y=0, level=level, label="E")
        e3 = base_graph.add_vert(pos_x=0, pos_y=-4, level=level, label="E")
        e3_1 = base_graph.add_vert(pos_x=0, pos_y=-6, level=level, label="E")
        e4 = base_graph.add_vert(pos_x=0, pos_y=4, level=level, label="E")
        e5 = base_graph.add_vert(pos_x=0, pos_y=0, level=level, label="E")
        e6 = base_graph.add_vert(pos_x=0, pos_y=-4, level=level, label="E")
        e6_1 = base_graph.add_vert(pos_x=0, pos_y=-6, level=level, label="E")
        base_graph.add_edges([(i1, I1), (i1, I2), (i2, I3), (i2, I4)])
        base_graph.add_edges([(I1, e4), (I1, e5), (I2, e6), (I2, e5), (I3, e1), (I3, e2), (I4, e2), (I4, e3), (I4, e3_1), (I2, e6_1)])
        base_graph.add_edges([(e4, e5), (e6, e5), (e1, e2), (e2, e3), (e3_1, e3), (e6, e6_1)])

        # for debugging
        # visualise_graph(base_graph, level)

        i_match0, i_match1 = match_P7(base_graph, level)

        new_graph = P7(base_graph, i_match0, i_match1)

        expected_graph = StandardizedGraph()
        i1 = expected_graph.add_vert(pos_x=-4, pos_y=0, level=level, label="i")
        i2 = expected_graph.add_vert(pos_x=4, pos_y=0, level=level, label="i")
        I1 = expected_graph.add_vert(pos_x=-2, pos_y=2, level=level, label="I")
        I2 = expected_graph.add_vert(pos_x=-2, pos_y=-2, level=level, label="I")
        I3 = expected_graph.add_vert(pos_x=2, pos_y=2, level=level, label="I")
        I4 = expected_graph.add_vert(pos_x=2, pos_y=-2, level=level, label="I")
        e1 = expected_graph.add_vert(pos_x=0, pos_y=4, level=level, label="E")
        e2 = expected_graph.add_vert(pos_x=0, pos_y=0, level=level, label="E")
        e3 = expected_graph.add_vert(pos_x=0, pos_y=-4, level=level, label="E")
        e3_1 = base_graph.add_vert(pos_x=0, pos_y=-6, level=level, label="E")
        e6_1 = base_graph.add_vert(pos_x=0, pos_y=-6, level=level, label="E")
        expected_graph.add_edges([(i1, I1), (i1, I2), (i2, I3), (i2, I4)])
        expected_graph.add_edges([(I1, e1), (I1, e2), (I2, e3), (I2, e2), (I3, e1), (I3, e2), (I4, e2), (I4, e3), (I4, e3_1), (I2, e6_1)])
        expected_graph.add_edges([(e1, e2), (e2, e3), (e3_1, e3), (e3, e6_1)])

        # for debugging
        # visualise_graph(new_graph, level)
        # visualise_graph(expected_graph, level)

        self.assertEqual(new_graph, expected_graph)


if __name__ == '__main__':
    unittest.main()

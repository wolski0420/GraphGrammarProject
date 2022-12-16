import networkx as nx
import utils.vis as vis
from productions.P7 import P7
from productions.P8 import P8
from utils.StandardizedGraph import StandardizedGraph
from productions.P1 import P1
from productions.P2 import match_P2
from productions.P3 import match_P3, P3
from productions.P4 import match_P4, P4
import matplotlib.pyplot as plt
from networkx.algorithms.isomorphism import is_isomorphic
from itertools import combinations
from productions.P5 import match_P5, P5
from productions.P6 import match_P6, P6

def test_P7():
    graph = StandardizedGraph()

    i1 = graph.add_vert(pos_x=5, pos_y=5, level=0, label="I")
    i2 = graph.add_vert(pos_x=-5, pos_y=5, level=0, label="I")
    i3 = graph.add_vert(pos_x=-5, pos_y=-5, level=0, label="I")
    i4 = graph.add_vert(pos_x=5, pos_y=-5, level=0, label="I")

    e1 = graph.add_vert(pos_x=-10, pos_y=0, level=0, label="E")
    e2 = graph.add_vert(pos_x=10, pos_y=0, level=0, label="E")
    e3 = graph.add_vert(pos_x=0, pos_y=0, level=0, label="E")

    e4 = graph.add_vert(pos_x=-10, pos_y=0, level=0, label="E")
    e5 = graph.add_vert(pos_x=10, pos_y=0, level=0, label="E")
    e6 = graph.add_vert(pos_x=0, pos_y=0, level=0, label="E")

    graph.add_edges([
        (e1, e3), (e3, e2),
        (e4, e6), (e6, e5),
        (e1, i2), (e3, i2), (e3, i1), (e2, i1),
        (e4, i3), (e6, i3), (e6, i4), (e5, i4)
    ])

    vis.visualise_graph(graph, center_level=1)

    graph = P7(graph, e1, e3, e2)

    vis.visualise_graph(graph, center_level=1)

def test_P8():
    graph = StandardizedGraph()

    i1 = graph.add_vert(pos_x=5, pos_y=5, level=0, label="I")
    i2 = graph.add_vert(pos_x=-5, pos_y=5, level=0, label="I")
    i3 = graph.add_vert(pos_x=-5, pos_y=-5, level=0, label="I")
    i4 = graph.add_vert(pos_x=5, pos_y=-5, level=0, label="I")

    e1 = graph.add_vert(pos_x=-10, pos_y=0, level=0, label="E")
    e2 = graph.add_vert(pos_x=10, pos_y=0, level=0, label="E")
    e3 = graph.add_vert(pos_x=0, pos_y=0, level=0, label="E")

    # e4 = graph.add_vert(pos_x=-10, pos_y=0, level=0, label="E")
    e5 = graph.add_vert(pos_x=10, pos_y=0, level=0, label="E")
    e6 = graph.add_vert(pos_x=0, pos_y=0, level=0, label="E")

    graph.add_edges([
        (e1, e3), (e3, e2),
        (e1, e6), (e6, e5),
        (e1, i2), (e3, i2), (e3, i1), (e2, i1),
        (e1, i3), (e6, i3), (e6, i4), (e5, i4)
    ])

    vis.visualise_graph(graph, center_level=1)

    graph = P8(graph, e1, e3, e2)

    vis.visualise_graph(graph, center_level=1)


if __name__ == "__main__":
    test_P7()
    test_P8()

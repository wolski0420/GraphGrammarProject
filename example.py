import networkx as nx
import utils.vis as vis
from productions.P7 import P7, match_P7
from productions.P8 import P8, match_P8
from utils.StandardizedGraph import StandardizedGraph
from productions.P1 import P1, match_P1
from productions.P2 import match_P2
from productions.P3 import match_P3, P3
from productions.P4 import match_P4, P4
import matplotlib.pyplot as plt
from networkx.algorithms.isomorphism import is_isomorphic
from itertools import combinations
from productions.P5 import match_P5, P5
from productions.P6 import match_P6, P6

def test_P7():
    # graph = StandardizedGraph()
    #
    # i1 = graph.add_vert(pos_x=5, pos_y=5, level=0, label="I")
    # i2 = graph.add_vert(pos_x=-5, pos_y=5, level=0, label="I")
    # i3 = graph.add_vert(pos_x=-5, pos_y=-5, level=0, label="I")
    # i4 = graph.add_vert(pos_x=5, pos_y=-5, level=0, label="I")
    #
    # e1 = graph.add_vert(pos_x=-10, pos_y=0, level=0, label="E")
    # e2 = graph.add_vert(pos_x=10, pos_y=0, level=0, label="E")
    # e3 = graph.add_vert(pos_x=0, pos_y=0, level=0, label="E")
    #
    # e4 = graph.add_vert(pos_x=-10, pos_y=0, level=0, label="E")
    # e5 = graph.add_vert(pos_x=10, pos_y=0, level=0, label="E")
    # e6 = graph.add_vert(pos_x=0, pos_y=0, level=0, label="E")
    #
    # graph.add_edges([
    #     (e1, e3), (e3, e2),
    #     (e4, e6), (e6, e5),
    #     (e1, i2), (e3, i2), (e3, i1), (e2, i1),
    #     (e4, i3), (e6, i3), (e6, i4), (e5, i4)
    # ])
    #
    # vis.visualise_graph(graph, center_level=1)
    # graph = P7(graph, [e1,e3,e2], [e4,e6,e5])
    #
    # vis.visualise_graph(graph, center_level=1)

    level = 0
    pevel_prev = level - 1
    base_graph = StandardizedGraph()
    i1 = base_graph.add_vert(pos_x=-4, pos_y=0, level=pevel_prev, label="i")
    i2 = base_graph.add_vert(pos_x=4, pos_y=0, level=pevel_prev, label="i")
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
    e7 = base_graph.add_vert(pos_x=0, pos_y=0, level=pevel_prev, label="E")
    base_graph.add_edges([(i1, I1), (i1, I2), (i2, I3), (i2, I4)])
    base_graph.add_edges([(I1, e4), (I1, e5), (I2, e6), (I2, e5), (I3, e1), (I3, e2), (I4, e2), (I4, e3)])
    base_graph.add_edges([(e4, e5), (e6, e5), (e1, e2), (e2, e3)])
    base_graph.add_edges([(e7, i1), (e7,i2)])

    # for debugging
    vis.visualise_graph(base_graph, level)

    i_match0, i_match1 = match_P7(base_graph, level)[0]
    new_graph = P7(base_graph, i_match0, i_match1)

    vis.visualise_graph(new_graph, level)
    

def test_P8():
    # graph = StandardizedGraph()
    #
    # i1 = graph.add_vert(pos_x=5, pos_y=5, level=0, label="I")
    # i2 = graph.add_vert(pos_x=-5, pos_y=5, level=0, label="I")
    # i3 = graph.add_vert(pos_x=-5, pos_y=-5, level=0, label="I")
    # i4 = graph.add_vert(pos_x=5, pos_y=-5, level=0, label="I")
    #
    # e1 = graph.add_vert(pos_x=-10, pos_y=0, level=0, label="E")
    # e2 = graph.add_vert(pos_x=10, pos_y=0, level=0, label="E")
    # e3 = graph.add_vert(pos_x=0, pos_y=0, level=0, label="E")
    #
    # # e4 = graph.add_vert(pos_x=-10, pos_y=0, level=0, label="E")
    # e5 = graph.add_vert(pos_x=10, pos_y=0, level=0, label="E")
    # e6 = graph.add_vert(pos_x=0, pos_y=0, level=0, label="E")
    #
    # graph.add_edges([
    #     (e1, e3), (e3, e2),
    #     (e1, e6), (e6, e5),
    #     (e1, i2), (e3, i2), (e3, i1), (e2, i1),
    #     (e1, i3), (e6, i3), (e6, i4), (e5, i4)
    # ])
    #
    # vis.visualise_graph(graph, center_level=1)
    #
    # graph = P8(graph, [e1, e3, e2], [e1, e6,e5])
    #
    # vis.visualise_graph(graph, center_level=1)

    level = 1
    prev_level = level - 1
    base_graph = StandardizedGraph()
    i1 = base_graph.add_vert(pos_x=-4, pos_y=0, level=prev_level, label="i")
    i2 = base_graph.add_vert(pos_x=4, pos_y=0, level=prev_level, label="i")
    I1 = base_graph.add_vert(pos_x=-2, pos_y=2, level=level, label="I")
    I2 = base_graph.add_vert(pos_x=-2, pos_y=-2, level=level, label="I")
    I3 = base_graph.add_vert(pos_x=2, pos_y=2, level=level, label="I")
    I4 = base_graph.add_vert(pos_x=2, pos_y=-2, level=level, label="I")
    e1 = base_graph.add_vert(pos_x=0, pos_y=4, level=level, label="E")
    e2 = base_graph.add_vert(pos_x=0, pos_y=0, level=level, label="E")
    e3 = base_graph.add_vert(pos_x=0, pos_y=-4, level=level, label="E")
    e5 = base_graph.add_vert(pos_x=0, pos_y=0, level=level, label="E")
    e6 = base_graph.add_vert(pos_x=0, pos_y=-4, level=level, label="E")
    base_graph.add_edges([(i1, I1), (i1, I2), (i2, I3), (i2, I4)])
    base_graph.add_edges([(I1, e1), (I1, e5), (I2, e6), (I2, e5), (I3, e1), (I3, e2), (I4, e2), (I4, e3)])
    base_graph.add_edges([(e1, e5), (e6, e5), (e1, e2), (e2, e3)])
    e13 = base_graph.add_vert(pos_x=0, pos_y=1, level=prev_level, label="E")
    base_graph.add_edges([(e13, i1), (e13, i2)])
    # for debugging
    vis.visualise_graph(base_graph, level)

    i_match0, i_match1 = match_P8(base_graph, level)[0]
    for v in i_match0:
        print(v.level(), v.underlying, v.pos_x(), v.pos_y())
    for v in i_match1:
        print(v.level(), v.underlying, v.pos_x(), v.pos_y())
    print(i_match1,i_match0)

    n = base_graph.get_neighbours(i_match0[1],level,'E')
    print(n)

    new_graph = P8(base_graph, i_match0, i_match1)
    vis.visualise_graph(new_graph, level)


if __name__ == "__main__":
    # test_P7()
    test_P8()

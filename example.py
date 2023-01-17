import networkx as nx
import utils.vis as vis
from productions.P7 import P7, match_P7
from productions.P8 import P8, match_P8
from utils.StandardizedGraph import StandardizedGraph
from productions.P1 import P1
from productions.P2 import match_P2
from productions.P3 import match_P3, P3
from productions.P4 import match_P4, P4
import matplotlib.pyplot as plt
from networkx.algorithms.isomorphism import is_isomorphic
from itertools import combinations

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

if __name__ == "__main__":
    graph = StandardizedGraph()
    # v1 = graph.add_vert(pos_x = 0, pos_y = 0, level = 0, label = "El")
    # v2 = graph.add_vert(pos_x = 5, pos_y = 5, level = 0, label = "El")
    # v2 = graph.add_vert(pos_x = 5, pos_y = 0, level = 0, label = "El")
    # v3 = graph.add_vert(pos_x = 5, pos_y = -5, level = 0, label = "El")
    # graph.add_edges([(v1, v2), (v2, v3)])
    # vis.visualise_graph(graph)
    # graph = P1(graph, v1)
    # graph = P1(graph, v2)


    i = graph.add_vert(pos_x = 0, pos_y = 0, level = 0, label="I")
    e1 = graph.add_vert(pos_x = -10, pos_y = 10, level = 0, label="E")
    e2 = graph.add_vert(pos_x = 10, pos_y = 10, level = 0, label="E")
    e3 = graph.add_vert(pos_x = 10, pos_y = -10, level = 0, label="E")
    e4 = graph.add_vert(pos_x = -10, pos_y = -10, level = 0, label="E")

    e5 = graph.add_vert(pos_x = 0, pos_y = -10, level = 0, label="E")
    e6 = graph.add_vert(pos_x = 10, pos_y = 0, level = 0, label="E")

    graph.add_edges([
        (i, e1), (i, e2), (i, e3), (i, e4),
        (e1, e2),
        (e2, e6), (e3, e6),
        (e3, e5), (e4, e5), 
        (e1, e4)
    ])

    i_2 = graph.add_vert(pos_x = 30, pos_y = 30, level = 0, label="I")
    e1_2 = graph.add_vert(pos_x = 20, pos_y = 40, level = 0, label="E")
    e2_2 = graph.add_vert(pos_x = 40, pos_y = 40, level = 0, label="E")
    e3_2 = graph.add_vert(pos_x = 40, pos_y = 20, level = 0, label="E")
    e4_2 = graph.add_vert(pos_x = 20, pos_y = 20, level = 0, label="E")
    e5_2 = graph.add_vert(pos_x = 20, pos_y = 30, level = 0, label="E")


    graph.add_edges([
        (i_2, e1_2), (i_2, e2_2), (i_2, e3_2), (i_2, e4_2),
        (e1_2, e2_2), (e2_2, e3_2), (e3_2, e4_2), (e1_2, e5_2), 
        (e4_2, e5_2)
    ])

    subgraph = graph.underlying

    similar = match_P4(graph, 0)
    for x in similar:
        graph = P4(graph, x)
    # graph = P4(graph, similar[1])


    # print(nx.is_isomorphic(subgraph, similar))
    vis.visualise_graph(graph, center_level=1)


def p4_1():
    graph = StandardizedGraph()
    i = graph.add_vert(pos_x = 0, pos_y = 0, level = 0, label="I")
    e1 = graph.add_vert(pos_x = -10, pos_y = 10, level = 0, label="E")
    e2 = graph.add_vert(pos_x = 10, pos_y = 10, level = 0, label="E")
    e3 = graph.add_vert(pos_x = 10, pos_y = -10, level = 0, label="E")
    e4 = graph.add_vert(pos_x = -10, pos_y = -10, level = 0, label="E")

    e5 = graph.add_vert(pos_x = -10, pos_y = 0, level = 0, label="E")
    e6 = graph.add_vert(pos_x = 0, pos_y = 10, level = 0, label="E")

    graph.add_edges([
        (i, e1), (i, e2), (i, e3), (i, e4),
        (e1, e6), (e2, e6),
        (e2, e3), 
        (e3, e4), 
        (e1, e5), (e4, e5)
    ])

    i_2 = graph.add_vert(pos_x = 30, pos_y = 30, level = 0, label="I")
    e1_2 = graph.add_vert(pos_x = 20, pos_y = 40, level = 0, label="E")
    e2_2 = graph.add_vert(pos_x = 40, pos_y = 40, level = 0, label="E")
    e3_2 = graph.add_vert(pos_x = 40, pos_y = 20, level = 0, label="E")
    e4_2 = graph.add_vert(pos_x = 20, pos_y = 20, level = 0, label="E")
    e5_2 = graph.add_vert(pos_x = 20, pos_y = 30, level = 0, label="E")


    graph.add_edges([
        (i_2, e1_2), (i_2, e2_2), (i_2, e3_2), (i_2, e4_2),
        (e1_2, e2_2), (e2_2, e3_2), (e3_2, e4_2), (e1_2, e5_2), 
        (e4_2, e5_2)
    ])

    subgraph = graph.underlying

    similar = match_P4(graph, 0)
    print(similar)
    graph = P4(graph, similar[0])
    vis.visualise_graph(graph, center_level=1)



#### TO NIE POWINNO DZIALAC DLA P4:
    # graph.add_edges([
    #     (i, e1), (i, e2), (i, e3), (i, e4),
    #     (e1, e2),
    #     (e2, e6), (e6, e3) ,
    #     (e3, e4), 
    #     (e1, e5), (e4, e5)
    # ])



#### TO powinno dzialac dla P4:
    # graph.add_edges([
    #     (i, e1), (i, e2), (i, e3), (i, e4),
    #     (e1, e2),
    #     (e2, e6), (e3, e6),
    #     (e3, e5), (e4, e5), 
    #     (e1, e4)
    # ])
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
    #
    # e3 = graph.add_vert(pos_x=0, pos_y=0, level=0, label="E")
    # # e4 = graph.add_vert(pos_x=-10, pos_y=0, level=0, label="E")
    # e5 = graph.add_vert(pos_x=10, pos_y=0, level=0, label="E")
    # e6 = graph.add_vert(pos_x=0, pos_y=0, level=0, label="E")
    #
    # graph.add_edges([
    #     (e1, e3), (e3, e2),
    #     (e1, i2), (e3, i2), (e3, i1), (e2, i1),
    #     (e1, e6), (e6, e5),
    #     (e1, i3), (e6, i3), (e6, i4), (e5, i4)
    # ])
    #
    # vis.visualise_graph(graph, center_level=1)
    #
    # graph = P8(graph, [e1, e3, e2], [e1, e6,e5])
    # vis.visualise_graph(graph, center_level=1)
    #

    level = 1
    prev_level = level - 1
    base_graph = StandardizedGraph()
    i1 = base_graph.add_vert(pos_x=-4, pos_y=0, level=prev_level, label="i")
    i2 = base_graph.add_vert(pos_x=4, pos_y=0, level=prev_level, label="i")
    I1 = base_graph.add_vert(pos_x=-2, pos_y=2, level=level, label="I")
    I2 = base_graph.add_vert(pos_x=-2, pos_y=-2, level=level, label="I")
    I4 = base_graph.add_vert(pos_x=2, pos_y=-2, level=level, label="I")
    I3 = base_graph.add_vert(pos_x=2, pos_y=2, level=level, label="I")
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
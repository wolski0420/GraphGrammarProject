import networkx as nx
from productions.P12 import P12, match_P12
from productions.P11 import P11, match_P11
from productions.P10 import P10, match_P10
import utils.vis as vis
from productions.P13 import match_P13, P13
from productions.P14 import match_P14, P14
from productions.P15 import match_P15, P15
from productions.P7 import P7, match_P7
from productions.P8 import P8, match_P8
from utils.StandardizedGraph import StandardizedGraph, Vert
from productions.P1 import P1, match_P1
from productions.P2 import P2, match_P2
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
    e7 = base_graph.add_vert(pos_x=0, pos_y=4, level=pevel_prev, label="E")
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

def test_P11():
    level = 0
    pevel_prev = level - 1
    base_graph = StandardizedGraph()
    i1 = base_graph.add_vert(pos_x=-4, pos_y=0, level=pevel_prev, label="i")
    i2 = base_graph.add_vert(pos_x=4, pos_y=0, level=pevel_prev, label="i")
    I1 = base_graph.add_vert(pos_x=-2, pos_y=2, level=level, label="I")
    I2 = base_graph.add_vert(pos_x=-2, pos_y=-2, level=level, label="I")
    I3 = base_graph.add_vert(pos_x=4, pos_y=0, level=level, label="I")
    e1 = base_graph.add_vert(pos_x=0, pos_y=4, level=level, label="E")
    e2 = base_graph.add_vert(pos_x=0, pos_y=0, level=level, label="E")
    e3 = base_graph.add_vert(pos_x=0, pos_y=-4, level=level, label="E")
    e4 = base_graph.add_vert(pos_x=0, pos_y=4, level=level, label="E")
    e6 = base_graph.add_vert(pos_x=0, pos_y=-4, level=level, label="E")
    e7 = base_graph.add_vert(pos_x=0, pos_y=4, level=pevel_prev, label="E")
    base_graph.add_edges([(i1, I1), (i1, I2), (i2, I3)])
    base_graph.add_edges([(I1, e1), (I1, e2), (I2, e2), (I2, e3), (I3, e4), (I3, e6)])
    base_graph.add_edges([(e1, e2), (e2, e3), (e4, e6)])
    base_graph.add_edges([(e7, i1), (e7,i2)])

    # for debugging
    vis.visualise_graph(base_graph, level)

    i_match0, i_match1 = match_P11(base_graph, level)[0]
    new_graph = P11(base_graph, i_match0, i_match1)

    vis.visualise_graph(new_graph, level)

def test_P12():
    level = 0
    pevel_prev = level - 1
    base_graph = StandardizedGraph()
    i1 = base_graph.add_vert(pos_x=-4, pos_y=0, level=pevel_prev, label="i")
    i2 = base_graph.add_vert(pos_x=4, pos_y=0, level=pevel_prev, label="i")
    I1 = base_graph.add_vert(pos_x=-2, pos_y=2, level=level, label="I")
    I2 = base_graph.add_vert(pos_x=-2, pos_y=-2, level=level, label="I")
    I3 = base_graph.add_vert(pos_x=4, pos_y=0, level=level, label="I")
    e1 = base_graph.add_vert(pos_x=0, pos_y=4, level=level, label="E")
    e2 = base_graph.add_vert(pos_x=0, pos_y=0, level=level, label="E")
    e3 = base_graph.add_vert(pos_x=0, pos_y=-4, level=level, label="E")
    e6 = base_graph.add_vert(pos_x=0, pos_y=-4, level=level, label="E")
    e7 = base_graph.add_vert(pos_x=0, pos_y=4, level=pevel_prev, label="E")
    base_graph.add_edges([(i1, I1), (i1, I2), (i2, I3)])
    base_graph.add_edges([(I1, e1), (I1, e2), (I2, e2), (I2, e3), (I3, e1), (I3, e6)])
    base_graph.add_edges([(e1, e2), (e2, e3), (e1, e6)])
    base_graph.add_edges([(e7, i1), (e7,i2)])

    # for debugging
    vis.visualise_graph(base_graph, level)

    matched = match_P12(base_graph, level)[0]
    new_graph = P12(base_graph, matched)

    vis.visualise_graph(new_graph, level)

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

def ex_B():
    graph = StandardizedGraph()
    level = 0
    i = graph.add_vert(pos_x = 0, pos_y = 0, level = level, label="El")
    verts = match_P1(graph)
    graph = P1(graph, verts[0])
    level += 1
    # vis.visualise_graph(graph)

    graphs = match_P2(graph, level)
    graph = P2(graph, graphs[0])
    level += 1
    # vis.visualise_graph(graph)

    graphs = match_P2(graph, level)
    graphs_P10 = match_P10(graph, level)
    graph = P2(graph, graphs[0])
    graph = P2(graph, graphs[1])
    graph = P10(graph, graphs_P10[2])
    graph = P2(graph, graphs[3])
    level += 1
    # vis.visualise_graph(graph)

    groups_P11 = match_P11(graph, level)
    groups_P7 = match_P7(graph, level)

    graph = P11(graph, groups_P11[0][0], groups_P11[0][1])
    graph = P7(graph, groups_P7[0][0], groups_P7[0][1])
    level += 1
    vis.visualise_graph(graph)

def ex_C():
    graph = StandardizedGraph()
    level = 0
    i = graph.add_vert(pos_x = 0, pos_y = 0, level = level, label="El")
    verts = match_P1(graph)
    graph = P1(graph, verts[0])
    level += 1
    # vis.visualise_graph(graph)

    # 2
    graphs = match_P2(graph, level)
    graph = P2(graph, graphs[0])
    level += 1
    # vis.visualise_graph(graph)

    # 3
    graphs = match_P2(graph, level)
    graphs_P10 = match_P10(graph, level)
    graph = P2(graph, graphs[1])
    graph = P2(graph, graphs[3])
    graph = P10(graph, graphs_P10[0])
    graph = P10(graph, graphs_P10[2])
    level += 1
    # vis.visualise_graph(graph)
    p_10_0_id = graph.get_neighbours(Vert(graph, graphs_P10[0].underlying), graphs_P10[0].level()+1, "I" )[0]
    p_10_1_id = graph.get_neighbours(Vert(graph, graphs_P10[2].underlying), graphs_P10[0].level()+1, "I" )[0]

    # 3.5 concat 3 layer

    groups_P7 = match_P7(graph, level)
    for idx, verts in enumerate(groups_P7):
        graph = P7(graph, verts[0], verts[1])

    vis.visualise_graph(graph, move_equal=True)

    # 4 create 4 layer
    graphs_P10 = match_P10(graph, level)
    # print(graphs_P10)
    graphs_P2 = match_P2(graph, level)

    x_groups = {}
    for v in graphs_P10:
        x = v.pos_x()
        x_groups[x] = x_groups[x] + [v] if x in x_groups else [v]

    x_groups_sorted = sorted(x_groups.items())
    # print(x_groups_sorted)
    for ivert in x_groups_sorted[1][1]:
        graph = P10(graph, ivert)
    x_P2 = x_groups_sorted[2][0]

    verts_p2 = list(filter(lambda v: v.pos_x()==x_P2 ,graphs_P2))
    for ivert in verts_p2:
        graph = P2(graph, ivert)

    for ivert in x_groups_sorted[0][1]:
        graph = P10(graph, ivert)

    vis.visualise_graph(graph, hist=[4], move_equal=True)

    # # #
    # groups_P11 = match_P11(graph, level-1)
    # for idx, verts in enumerate(groups_P11):
    #     graph = P11(graph, verts[0], verts[1])
    #
    # vis.visualise_graph(graph, hist=[3], move_equal=True)
    #
    # #
    # groups_P13 = match_P13(graph, level-1)
    # for idx, verts in enumerate(groups_P13):
    #     graph = P13(graph, verts[0], verts[1])
    #
    # vis.visualise_graph(graph, hist=[3], move_equal=True)


    # # concat subgraphs
    # 4.5
    level += 1
    groups_P7 = match_P7(graph, level)
    # print(groups_P7)
    for idx, verts in enumerate(groups_P7):
        graph = P7(graph, verts[0], verts[1] )
    vis.visualise_graph(graph, hist=[4], move_equal=True)

    # 4.7
    vis.visualise_graph(graph, hist=[3,4], move_equal=True)
    groups_P11 = match_P11(graph, level)
    # print(groups_P11)

    for idx, verts in enumerate(groups_P11):
        graph = P11(graph, verts[0], verts[1])

    vis.visualise_graph(graph, hist=[2,3,4], move_equal=True)

    # 4.8
    groups_P13 = match_P13(graph, level)
    # print(groups_P13)

    for idx, verts in enumerate(groups_P13):
        graph = P13(graph, verts[0], verts[1])

    vis.visualise_graph(graph, hist=[3,4], move_equal=True)

    # # 4.85
    groups_P14 = match_P14(graph, level, True)
    # print(groups_P14)

    for idx, verts in enumerate(groups_P14):
        graph = P14(graph, verts[0], verts[1])

    vis.visualise_graph(graph, hist=[3,4], move_equal=True)

    # 4.9
    groups_P15 = match_P15(graph, level-1)
    for idx, verts in enumerate(groups_P15):
        graph = P15(graph, verts[0], verts[1])
    vis.visualise_graph(graph, hist=[3, 4], move_equal=True)

    # 5
    groups_P13 = match_P13(graph, level)
    print(groups_P13)
    for idx, verts in enumerate(groups_P13):
        graph = P13(graph, verts[0], verts[1])
    vis.visualise_graph(graph, hist=[3, 4], move_equal=True)
    vis.visualise_graph(graph, hist=[4], move_equal=True)
    vis.visualise_graph(graph,move_equal=True)

if __name__ == "__main__":

    # test_P12()
    ex_C()
    # ex_B()

import networkx as nx
import utils.vis as vis
from productions.P7 import P7
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


if __name__ == "__main__":
    graph = StandardizedGraph()

    i1 = graph.add_vert(pos_x = 5, pos_y = 5, level = 0, label="I")
    i2 = graph.add_vert(pos_x=-5, pos_y=5, level=0, label="I")
    i3 = graph.add_vert(pos_x=-5, pos_y=-5, level=0, label="I")
    i4 = graph.add_vert(pos_x=5, pos_y=-5, level=0, label="I")

    e1 = graph.add_vert(pos_x = -10, pos_y = 0, level = 0, label="E")
    e2 = graph.add_vert(pos_x = 10, pos_y = 0, level = 0, label="E")
    e3 = graph.add_vert(pos_x = 0, pos_y = 0, level = 0, label="E")

    e4 = graph.add_vert(pos_x = -10, pos_y = 0, level = 0, label="E")
    e5 = graph.add_vert(pos_x = 10, pos_y = 0, level = 0, label="E")
    e6 = graph.add_vert(pos_x = 0, pos_y = 0, level = 0, label="E")


    graph.add_edges([
        (e1, e3), (e3, e2),
        (e4,e6), (e6,e5),
        (e1, i2), (e3, i2), (e3,i1), (e2,i1),
        (e4,i3), (e6,i3), (e6,i4), (e5,i4)
    ])



    vis.visualise_graph(graph, center_level=1)

    graph = P7(graph, e1,e3,e2)

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
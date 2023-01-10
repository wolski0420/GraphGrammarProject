import networkx as nx
import utils.vis as vis
from productions.P7 import P7, match_P7
from productions.P8 import P8
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
    graph = P7(graph, [e1,e3,e2], [e4,e6,e5])

    vis.visualise_graph(graph, center_level=1)
    
    # level = 0
    # base_graph = StandardizedGraph()
    # e1 = base_graph.add_vert(pos_x=-4, pos_y=4, level=level, label="E")
    # e2 = base_graph.add_vert(pos_x=4, pos_y=4, level=level, label="E")
    # e3 = base_graph.add_vert(pos_x=4, pos_y=-4, level=level, label="E")
    # e4 = base_graph.add_vert(pos_x=-4, pos_y=-4, level=level, label="E")
    # e5 = base_graph.add_vert(pos_x=-4, pos_y=0, level=level, label="E")
    # i1 = base_graph.add_vert(pos_x=0, pos_y=0, level=level, label="I")
    # base_graph.add_edges([(e1, e2), (e2, e3), (e3, e4), (e4, e5), (e5, e1)])
    # base_graph.add_edges([(i1, e1), (i1, e2), (i1, e3), (i1, e4)])


    # i_match = match_P3(base_graph, level)[0]
    # # vis.visualise_graph(base_graph, center_level=0)
    
    # base_graph = P3(base_graph, i_match)
    # vis.visualise_graph(base_graph, center_level=1)
    
    
    # i_match = match_P1(base_graph, level+1)
    # print(i_match)
    # base_graph = P1(base_graph, i_match[0])
    # base_graph = P3(base_graph, i_match[1])
    # graph = match_P7(graph, )
    

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

    graph = P8(graph, [e1, e3, e2], [e1, e6,e5])        
    
    vis.visualise_graph(graph, center_level=1)


if __name__ == "__main__":
    # test_P7()
    test_P8()

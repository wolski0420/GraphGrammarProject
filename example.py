import networkx as nx
import utils.vis as vis
from utils.StandardizedGraph import StandardizedGraph
from productions.P1 import P1


graph = StandardizedGraph()
v1 = graph.add_vert(pos_x = 0, pos_y = 0, level = 0, label = "El")
# v2 = graph.add_vert(pos_x = 5, pos_y = 0, level = 0, label = "El")
# v3 = graph.add_vert(pos_x = 5, pos_y = -5, level = 0, label = "El")
# graph.add_edges([(v1, v2), (v2, v3)])
vis.visualise_graph(graph)
graph = P1(graph)
vis.visualise_graph(graph, center_level=1)
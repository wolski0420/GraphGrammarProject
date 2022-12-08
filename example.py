import networkx as nx
import utils.vis as vis
from utils.StandardizedGraph import StandardizedGraph
from productions.P1 import P1


graph = StandardizedGraph()
startNode = graph.add_vert(pos_x = 0, pos_y = 0, level = 0, label = "i")
vis.visualise_graph(graph)
graph = P1(graph)
vis.visualise_graph(graph, center_level=1)
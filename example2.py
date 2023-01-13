import utils.vis as vis
from utils.StandardizedGraph import StandardizedGraph
from productions.P1 import P1
from productions.P2 import match_P2, P2


graph = StandardizedGraph()
v1 = graph.add_vert(pos_x=0, pos_y=0, level=0, label="El")

graph = P1(graph, v1)

matched = match_P2(graph, 1)
print([v.underlying for v in matched])

graph = P2(graph, matched[0])
vis.visualise_graph(graph, center_level=2)
vis.visualise_graph(graph, center_level=2, hist=[2])

matched = match_P2(graph, 2)
graph = P2(graph, matched[0])
vis.visualise_graph(graph, center_level=3)
vis.visualise_graph(graph, center_level=3, hist=[3])

matched = match_P2(graph, 2)
graph = P2(graph, matched[0])
vis.visualise_graph(graph, center_level=3)
vis.visualise_graph(graph, center_level=3, hist=[3])

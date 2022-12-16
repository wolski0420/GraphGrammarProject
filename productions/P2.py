from utils.StandardizedGraph import StandardizedGraph, Vert
import networkx as nx
from networkx.algorithms.isomorphism import is_isomorphic

def P2(graph: StandardizedGraph, v: Vert):
    pass

def match_P2(graph: StandardizedGraph, level: int):
    verts = []
    for i in graph.find_by_label("I"):
        if (i.level() != level):
            continue
        G = graph.underlying
        neighbors = G.neighbors(i.underlying)
        is_valid = True
        valid_neighbors = [i for i in neighbors if nx.get_node_attributes(graph, "level") == level and nx.get_node_attributes(graph, "label") == "E"]
        subgraph = graph.subgraph_from_nodes(valid_neighbors + [i.underlying])
        
        expected_subgraph = Graph()
        expected_subgraph.add_nodes_from([ # labels are not compared
            (0, {"label": "I"}),
            (1, {"label": "E"}),
            (2, {"label": "E"}),
            (3, {"label": "E"}),
            (4, {"label": "E"})
        ])
        expected_subgraph.add_edges_from([
            (0, 1), (0, 2), (0, 3), (0, 4), (1, 2), (2, 3), (3, 4), (4, 1)
        ])
        
        if is_isomorphic(subgraph, expected_subgraph):
            verts.append(i)
    return verts
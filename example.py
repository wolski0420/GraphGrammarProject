import networkx as nx
import utils.vis as vis

# Right side of P1
baseX = 0
baseY = 0
G = nx.Graph()
G.add_node(-1, **{'pos_x': 0, 'pos_y': 0, 'level': 0, 'label': "i"})
G.add_node(0, **{'pos_x': 0, 'pos_y': 0, 'level': 1, 'label': "i"})
G.add_node(1, **{'pos_x': -10, 'pos_y': 10, 'level': 1, 'label': "E"})
G.add_node(2, **{'pos_x': 10, 'pos_y': 10, 'level': 1, 'label': "E"})
G.add_node(3, **{'pos_x': 10, 'pos_y': -10, 'level': 1, 'label': "E"})
G.add_node(4, **{'pos_x': -10, 'pos_y': -10, 'level': 1, 'label': "E"})
G.add_edges_from([(0,1), (0,2), (0,3), (0,4), (1,2), (2,3), (3,4), (4,1)])
G.add_edge(-1, 0)

# visualise_graph(G, hist=[1])
vis.visualise_graph(G)
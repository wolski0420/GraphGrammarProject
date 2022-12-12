from utils.StandardizedGraph import StandardizedGraph, Vert
import networkx as nx
from networkx.algorithms.isomorphism import is_isomorphic
from itertools import combinations, chain
import utils.vis as vis


class SurroundingMatcher:

    def __init__(self, broken_edges: int):
        self.broken_edges = broken_edges

    def match(self, graph: StandardizedGraph, level: int):
        i_vertices = list(filter(
            lambda i: i.level() == level,
            graph.find_by_label("I")
        ))
        return list(filter(
            lambda i_vert: self.get_valid_subgraph(graph, i_vert, level) is not None,
            i_vertices
        ))

    def subgraph_matches(self, subgraph):
        graph_template = self.get_graph_template()
        return is_isomorphic(subgraph, graph_template)

    def get_graph_template(self):

        base_verts = [
            (0, {"label": "I"}),
            (1, {"label": "E"}),
            (2, {"label": "E"}),
            (3, {"label": "E"}),
            (4, {"label": "E"})
        ]
        breaking_verts = [(5 + n, {"label": "E"}) for n in range(self.broken_edges)]
        base_edges = [(0, 1), (0, 2), (0, 3), (0, 4)]
        n_outer_verts = 4 + self.broken_edges
        outer_edges = [(n, (n + 1)) for n in range(1, n_outer_verts)] + [(n_outer_verts, 1)]
        expected_subgraph = nx.Graph()
        expected_subgraph.add_nodes_from(base_verts + breaking_verts)
        expected_subgraph.add_edges_from(base_edges + outer_edges)
        return expected_subgraph

    def get_valid_subgraph(self, graph, i_vertex, level: int):
        e_neighbours = self.get_neighbours(graph, i_vertex, level, "E")

        for surrounding_e_vertices in combinations(e_neighbours, 4):
            subgraph = self.valid_subgraph(graph.underlying, i_vertex.underlying, surrounding_e_vertices)
            if subgraph:
                return subgraph
        return None

    def get_neighbours(self, graph, vertex, level: int, label: str):
        return list(filter(
            lambda neigh: nx.get_node_attributes(graph.underlying, "level")[neigh] == level \
                          and nx.get_node_attributes(graph.underlying, "label")[neigh] == label,
            graph.underlying.neighbors(vertex.underlying)
        ))

    def valid_subgraph(self, graph, i_vertex, surrounding_e_vertices):
        broken_edges = self.find_broken_edges(graph, surrounding_e_vertices)
        # print(broken_edges)
        if len(broken_edges) != self.broken_edges:
            return None
        breaking_points = list(broken_edges.values())
        subgraph = graph.subgraph([i_vertex] + list(surrounding_e_vertices) + breaking_points)
        return subgraph if self.subgraph_matches(subgraph) else None

    def find_broken_edges(self, graph, surrounding_e_vertices):
        possible_e_edges = list(combinations(surrounding_e_vertices, 2))
        broken_edges = dict()
        for edge in possible_e_edges:
            breaking_point = self.get_breaking_point(graph, edge[0], edge[1])
            if breaking_point:
                broken_edges[edge] = breaking_point
        # print(broken_edges)
        return broken_edges

    def get_breaking_point(self, graph, e1, e2):
        if self.directly_connected(graph, e1, e2):
            return None
        e1_neighbours = set(graph.neighbors(e1))
        e2_neighbours = set(graph.neighbors(e2))
        connected_to_both = e1_neighbours.intersection(e2_neighbours)
        breaking_points = list(filter(
            lambda vertex: self.is_breaking_point(graph, e1, e2, vertex),
            connected_to_both
        ))
        return breaking_points[0] if len(breaking_points) > 0 else None

    def directly_connected(self, graph, e1, e2):
        return e2 in graph.neighbors(e1)

    def is_breaking_point(self, graph, e1, e2, breaking_point):
        return nx.get_node_attributes(graph, "label")[breaking_point] == "E" \
            and (nx.get_node_attributes(graph, "pos_x")[e1] + nx.get_node_attributes(graph, "pos_x")[e2]) / 2 == \
            nx.get_node_attributes(graph, "pos_x")[breaking_point] \
            and (nx.get_node_attributes(graph, "pos_y")[e1] + nx.get_node_attributes(graph, "pos_y")[e2]) / 2 == \
            nx.get_node_attributes(graph, "pos_y")[breaking_point]

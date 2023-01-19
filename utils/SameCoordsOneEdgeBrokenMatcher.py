from itertools import combinations
from utils.StandardizedGraph import StandardizedGraph, Vert
import networkx as nx
from networkx.algorithms.isomorphism import is_isomorphic

from utils.vis import visualise_graph


class SameCoordsMatcherOneEdgeBroken:
    def __init__(self, vertices_to_merge) -> None:

        self.vertices_to_merge = vertices_to_merge
    
    def match(self, graph: StandardizedGraph, level:int):
        self.level = level
        matching_vertices = self.find_all_matching_vertices(graph, level)
        # print("matching coords: ", matching_vertices)
     
        return self.find_matching_groups(graph, matching_vertices)
        
    def find_matching_groups(self, graph, matching_vertices):
        merge_parts = []
        
        for matching_vertices_combination in combinations(matching_vertices, 2):
            merge_parts.extend(self.find_matching_groups_for_combination(graph, matching_vertices_combination))
        
        return merge_parts # change to return i_verts
    
    def find_matching_groups_for_combination(self, graph, matching_vertices_combination):
        first_group = matching_vertices_combination[0]
        second_group = matching_vertices_combination[1]
        for i in range(len(first_group)):
            vert1 = first_group[i]
            for j in range(len(second_group)):
                vert2 = second_group[j]
                vert1_neighs = set(graph.get_neighbours(vert1, vert1.level(), "E"))
                vert2_neighs = set(graph.get_neighbours(vert2, vert2.level(), "E"))

                # print("vert1_neighs: ", vert1_neighs)

                if len(vert1_neighs.intersection(vert2_neighs)) > 0:
                    # print("vert1_neighs.intersection(vert2_neighs): ", vert1_neighs.intersection(vert2_neighs))
                    for vert in vert1_neighs.intersection(vert2_neighs):
                        if (vert1.pos_x() + vert2.pos_x()) / 2 == \
                                nx.get_node_attributes(graph.underlying, "pos_x")[vert] and \
                            (vert1.pos_y() + vert2.pos_y()) / 2 == \
                                nx.get_node_attributes(graph.underlying, "pos_y")[vert] and \
                            self.directly_connected(graph.underlying, vert1.underlying, vert) and \
                            self.directly_connected(graph.underlying, vert2.underlying, vert):
                                for k in range(len(first_group)):
                                    if k != i:
                                        vert3 = first_group[k]
                                        for l in range(len(second_group)):
                                            if l != j:
                                                vert4 = second_group[l]
                                                if self.check_production_predicats(graph, vert1, vert2, vert3, vert4, vert):
                                                    return [([vert1, vert3], [vert2, vert4])]

        return []
                        
    def directly_connected(self, graph, e1, e2):
        return e2 in graph.neighbors(e1)
        
    
    def check_production_predicats(self, graph, vert1, vert2, vert3, vert4, between_vert):
        if not self.directly_connected(graph.underlying, vert3.underlying, vert4.underlying) or \
                self.directly_connected(graph.underlying, vert1.underlying, vert3.underlying) or \
                    self.directly_connected(graph.underlying, vert2.underlying, vert4.underlying) or \
                        self.directly_connected(graph.underlying, vert1.underlying, vert4.underlying) or \
                            self.directly_connected(graph.underlying, vert2.underlying, vert3.underlying) or \
                                self.directly_connected(graph.underlying, vert3.underlying, between_vert) or \
                                    self.directly_connected(graph.underlying, vert4.underlying, between_vert):
                                        return False

        i_0_list = graph.get_i_neighbours(Vert(graph.underlying, between_vert), vert1.level())
        i_1_list = graph.get_i_neighbours(vert3, vert1.level())

        if len(i_0_list) != len(i_1_list) != 1:
            return False

        i_0 = i_0_list[0]
        i_1 = i_1_list[0]

        i_0_neigh = set(graph.get_neighbours(Vert(graph.underlying, i_0), self.level-1, 'E'))
        i_1_neigh = set(graph.get_neighbours(Vert(graph.underlying, i_1), self.level-1, 'E'))
        if len(i_0_neigh.intersection(i_1_neigh))==0:
            return False

        subgraph_nodes = [i_0, i_1] + [list(i_0_neigh.intersection(i_1_neigh))[0]] + [vert1.underlying, vert2.underlying, vert3.underlying, vert4.underlying, between_vert]

        i_0_neigh = set(graph.get_neighbours(Vert(graph.underlying, i_0), Vert(graph.underlying, i_0).level()+1, 'I'))
        e1_0_neigh = set(graph.get_neighbours(vert1, vert1.level(), 'I'))
        e2_0_neigh = set(graph.get_neighbours(Vert(graph.underlying, between_vert), vert1.level(), 'I'))
        e3_0_neigh = set(graph.get_neighbours(vert2, vert2.level(), 'I'))
        subgraph_nodes += list(e1_0_neigh.intersection(e2_0_neigh).intersection(i_0_neigh)) + list(e2_0_neigh.intersection(e3_0_neigh).intersection(i_0_neigh))
        i_1_neigh = set(graph.get_neighbours(Vert(graph.underlying, i_1), Vert(graph.underlying, i_1).level()+1, 'I'))
        e1_1_neigh = set(graph.get_neighbours(vert3, vert3.level(), 'I'))
        e2_1_neigh = set(graph.get_neighbours(vert4, vert4.level(), 'I'))
        subgraph_nodes += list(e1_1_neigh.intersection(e2_1_neigh).intersection(i_1_neigh))

        # visualise_graph(graph.underlying.subgraph(subgraph_nodes), self.level)
        template = self.get_template()
        if not is_isomorphic(graph.underlying.subgraph(subgraph_nodes), template):
            return False
        
        return True
    
    def get_template(self):
        base_verts = [
            (0, {"label": "i"}),
            (1, {"label": "i"}),
            (2, {"label": "I"}),
            (3, {"label": "I"}),
            (4, {"label": "I"}),
            (5, {"label": "E"}),
            (6, {"label": "E"}),
            (7, {"label": "E"}),
            (8, {"label": "E"}),
            (9, {"label": "E"}),
        ]
        
        if self.vertices_to_merge > 1:
            base_verts += [(10, {"label": "E"})]
            
        inner_edges = [
            (0, 9), (1, 9),
            (0, 2), (0, 3), (1, 4),
            (2, 5), (3, 6), (3, 5), (4, 8),
            (5, 6)
        ]
        
        if self.vertices_to_merge == 1:
            inner_edges += [
                # TODO
            ]
        else:
            inner_edges += [
                (8, 7), (4, 7),
                (2, 10), (10, 5)
            ]
            
        
        expected_subgraph = nx.Graph()
        expected_subgraph.add_nodes_from(base_verts)
        expected_subgraph.add_edges_from(inner_edges)
        
        return expected_subgraph 
    
    def find_all_matching_vertices(self, graph: StandardizedGraph, level:int): 
        ordered_everts = {}
        
        for vert in graph.find_by_label("E"):
            if vert.level() == level:
                key = (vert.pos_x(), vert.pos_y())
                ordered_everts[key] = [vert] if key not in ordered_everts else ordered_everts[key] + [vert]
        
        matching_verts = []
        for key, value in ordered_everts.items():
            if len(value) > 1:
                matching_verts.append(value)
                
        return matching_verts
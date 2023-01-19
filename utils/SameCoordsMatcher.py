from utils.StandardizedGraph import StandardizedGraph, Vert
import networkx as nx
from networkx.algorithms.isomorphism import is_isomorphic

from utils.vis import visualise_graph


class SameCoordsMatcher:
    def __init__(self, vertices_to_merge) -> None:

        self.vertices_to_merge = vertices_to_merge
    
    def match(self, graph: StandardizedGraph, level:int):
        matching_vertices = self.find_all_matching_vertices(graph, level)
        # print(matching_vertices)

        return self.find_matching_groups(graph, matching_vertices)

    def find_matching_groups(self, graph, matching_vertices):
        merge_parts = []

        for idx, match_verts in enumerate(matching_vertices):
            master_vert = match_verts[0]
            x_neigh, x_i = self.find_coord_neighs(graph, master_vert, 'x', matching_vertices)
            y_neigh, y_i = self.find_coord_neighs(graph, master_vert, 'y', matching_vertices)

            if len(x_neigh)>=self.vertices_to_merge:
                oposite_neigh, opos_i = self.find_opposite_vert_group(graph, x_neigh, 'x', match_verts[1:], matching_vertices)
                if oposite_neigh is not None:
                    group_0 = self.sort_verts(x_neigh, 'y')
                    group_1 = self.sort_verts(oposite_neigh, 'y')
                    group_00, group_11 = self.add_vert_if_needed(group_0, group_1, 'y', graph)
                    for idxg in range(len(group_00)+1-3):
                        group_0 = group_00[idxg:idxg+3]
                        group_1 = group_11[idxg:idxg + 3]

                        is_good = self.check_production_predicats(group_0, group_1, x_i, opos_i, 'y', graph)

                        merge_parts.append((group_0, group_1)) if is_good \
                                                                  and (group_0, group_1) not in merge_parts \
                                                                  and (group_1, group_0) not in merge_parts else None

            if len(y_neigh)>=self.vertices_to_merge:
                oposite_neigh, opos_i = self.find_opposite_vert_group(graph, y_neigh, 'y', match_verts[1:], matching_vertices)
                if oposite_neigh is not None:
                    group_0 = self.sort_verts(y_neigh, 'x')
                    group_1 = self.sort_verts(oposite_neigh, 'x')
                    group_00, group_11 = self.add_vert_if_needed(group_0, group_1, 'x', graph)
                    for idxg in range(len(group_00) + 1 - 3):
                        group_0 = group_00[idxg:idxg + 3]
                        group_1 = group_11[idxg:idxg + 3]

                        is_good = self.check_production_predicats(group_0, group_1, x_i, opos_i, 'x', graph)

                        merge_parts.append((group_0, group_1)) if is_good \
                                                                  and (group_0, group_1) not in merge_parts \
                                                                   and (group_1, group_0) not in merge_parts else None

        return merge_parts # change to return i_verts

    def add_vert_if_needed(self, group_0, group_1, coord_name, graph):
        group_0 = self.sort_verts(group_0, coord_name)
        group_1 = self.sort_verts(group_1, coord_name)

        if self.vertices_to_merge==2:
            common_vert = self.find_common_vert(group_0, group_1, graph, coord_name)
            group_0 += [common_vert] if common_vert is not None else []
            group_1 += [common_vert] if common_vert is not None else []

            group_0 = self.sort_verts(group_0, coord_name)
            group_1 = self.sort_verts(group_1, coord_name)

        return group_0, group_1


    def check_production_predicats(self, group_0, group_1,  i_0, i_1, coord_name, graph):
        group_0 = self.sort_verts(group_0, coord_name)
        group_1 = self.sort_verts(group_1, coord_name)
        i_0 = list(i_0)[0]
        i_1 = list(i_1)[0]

        # check coords values
        for i in range(len(group_0)):
            if group_0[i].pos_x() != group_1[i].pos_x() or group_0[i].pos_y() != group_1[i].pos_y():
                return False

        if (group_0[0].pos_x()+group_0[2].pos_x())/2 != (group_1[0].pos_x()+group_1[2].pos_x())/2 :
            return False
        if (group_0[0].pos_y() + group_0[2].pos_y())/2 != (group_1[0].pos_y() + group_1[2].pos_y())/2: ###
            return False

        if (group_0[0].pos_x()+group_0[2].pos_x())/2 != (group_0[1].pos_x()) :
            return False
        # print(group_1[0].pos_y(), group_1[1].pos_y(), group_1[2].pos_y())
        if (group_1[0].pos_y() + group_1[2].pos_y())/2 != (group_1[1].pos_y()):
            return False

        # check if 'i' vertices are connected by 'E'
        v = Vert(graph.underlying, i_0)
        i_0_neigh = set(graph.get_neighbours(v, v.level(), 'E'))
        i_1_neigh = set(graph.get_neighbours(Vert(graph.underlying, i_1), v.level(), 'E'))
        if len(i_0_neigh.intersection(i_1_neigh))==0:
            return False

        subgraph_nodes = [i_0, i_1] + list(i_0_neigh.intersection(i_1_neigh)) + list(set([g.underlying for g in group_0+group_1]))

        i_0_neigh = set(graph.get_neighbours(Vert(graph.underlying, i_0), Vert(graph.underlying, i_0).level()+1, 'I'))
        e1_0_neigh = set(graph.get_neighbours(group_0[0], group_0[0].level(), 'I'))
        e2_0_neigh = set(graph.get_neighbours(group_0[1], group_0[1].level(), 'I'))
        e3_0_neigh = set(graph.get_neighbours(group_0[2], group_0[2].level(), 'I'))
        subgraph_nodes += list(e1_0_neigh.intersection(e2_0_neigh).intersection(i_0_neigh)) + list(e2_0_neigh.intersection(e3_0_neigh).intersection(i_0_neigh))
        i_1_neigh = set(graph.get_neighbours(Vert(graph.underlying, i_1), Vert(graph.underlying, i_1).level()+1, 'I'))
        e1_1_neigh = set(graph.get_neighbours(group_1[0], group_1[0].level(), 'I'))
        e2_1_neigh = set(graph.get_neighbours(group_1[1], group_1[1].level(), 'I'))
        e3_1_neigh = set(graph.get_neighbours(group_1[2], group_1[2].level(), 'I'))
        subgraph_nodes += list(e1_1_neigh.intersection(e2_1_neigh).intersection(i_1_neigh))
        subgraph_nodes += list(e2_1_neigh.intersection(e3_1_neigh).intersection(i_1_neigh))

        template = self.get_template()
        # visualise_graph(template, self.level)
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
            (5, {"label": "I"}),
            (6, {"label": "E"}),
            (7, {"label": "E"}),
            (8, {"label": "E"}),
            (9, {"label": "E"}),
            (10, {"label": "E"}),
            (11, {"label": "E"}),
        ]

        if self.vertices_to_merge > 2:
            base_verts += [(12, {"label": "E"})]

        inner_edges = [
            (0, 11), (1, 11),
            (0, 2), (0,3), (1,4), (1,5),
            (2, 9), (3,10), (3,9), (4,7), (5,8), (5,7),
            (10,9), (8,7)
        ]

        if self.vertices_to_merge == 2:
            inner_edges += [
                (2, 6), (4,6),
                (6,9), (6,7)
            ]
        else:
            inner_edges += [
                (2, 6), (4,12),
                (6,9), (12,7)
            ]


        expected_subgraph = nx.Graph()
        expected_subgraph.add_nodes_from(base_verts)
        expected_subgraph.add_edges_from(inner_edges)

        return expected_subgraph



    def find_common_vert(self, group_0, group_1, graph, coord_name):
        for iter in range(len(group_0)):
            neighs_0 = set(graph.get_neighbours(group_0[iter], group_0[iter].level(), 'E'))
            neighs_1 = set(graph.get_neighbours(group_1[iter], group_0[iter].level(), 'E'))
            common = neighs_0.intersection(neighs_1)
            
            if len(common) > 0:
                idx = list(common)[0]
                common = Vert(graph.underlying, idx)
                is_good = True if (coord_name =='y' and common.pos_x() == group_0[0].pos_x() ) or \
                                (coord_name =='x' and common.pos_y() == group_0[0].pos_y() ) else False
                    
                if is_good: return common
                
        
    
    def sort_verts(self, group, coord_name):
        group.sort(key=lambda v: v.pos_x() if coord_name=='x' else v.pos_y())
        return group 

    def find_opposite_vert_group(self, graph, vert_group, coord_name, vertices_to_search, matching_vertices):
        for vert in vertices_to_search:
            potential_group, pot_i = self.find_coord_neighs(graph, vert, coord_name, matching_vertices)
            if self.compare_vert_groups(vert_group, potential_group):
                return potential_group, pot_i

        return None, None
                
            
    def compare_vert_groups(self, group_0, group_1):
        if len(group_0) != len(group_1):
            return False
        
        get_pos = lambda v: (v.pos_x(), v.pos_y())
        group_0_coords = map(get_pos, group_0)
        group_1_coords = map(get_pos, group_1)
        
        for el in group_0_coords:
            if el not in group_1_coords:
                return False
            
        return True
        
    
    def find_coord_neighs(self, graph, master_vert:Vert, coord_name: str, vertices_to_search: list):
        """
        find vert neighbours, (even far ones) which has the same coord 'coord_name' value and 
        has the same 'i' vert as far neighbour (and also has sibling with the same coords)
        """
        
        neighs = [master_vert]
        master_i = set(graph.get_i_neighbours(master_vert, master_vert.level()))
        for vs in vertices_to_search:
            match = self.check_coord((vs[0].pos_x(), vs[0].pos_y()), (master_vert.pos_x(), master_vert.pos_y()), coord_name)
            if match:
                for v in vs:
                    if v.underlying != master_vert.underlying:
                        v_i = graph.get_i_neighbours(v, v.level())
                        common_i = master_i.intersection(v_i)

                        neighs = neighs + [v] if len(common_i)>0 else neighs

        return neighs, master_i

                    
                    
    def check_coord(self, coords_0, coords_1, coord_name):
        return coords_0[0] == coords_1[0] if coord_name=='x' else coords_0[1] == coords_1[1]
        
    
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
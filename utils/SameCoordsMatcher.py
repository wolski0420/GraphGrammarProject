from utils.StandardizedGraph import StandardizedGraph, Vert
import networkx as nx
from networkx.algorithms.isomorphism import is_isomorphic

class SameCoordsMatcher:
    def __init__(self, vertices_to_merge) -> None:
        self.vertices_to_merge = vertices_to_merge
    
    def match(self, graph: StandardizedGraph, level:int):
        matching_vertices = self.find_all_matching_vertices(graph, level)
        print(matching_vertices)
     
        return self.find_matching_groups(graph, matching_vertices)
        
    
    
    def find_matching_groups(self, graph, matching_vertices):
        merge_parts = []
        
        for idx, match_verts in enumerate(matching_vertices):
            master_vert = match_verts[0]
            x_neigh = self.find_coord_neighs(graph, master_vert, 'x', matching_vertices[idx:])
            y_neigh = self.find_coord_neighs(graph, master_vert, 'y', matching_vertices[idx:])
            
            if len(x_neigh)==self.vertices_to_merge:
                oposite_neigh = self.find_opposite_vert_group(graph, x_neigh, 'x', match_verts[1:], matching_vertices[idx:])
                is_good = self.check_production_predicats(oposite_neigh, x_neigh, 'y')

                # check isomorphic?
                merge_parts.append((x_neigh, oposite_neigh)) if oposite_neigh is not None and is_good else None
            
            if len(y_neigh)==self.vertices_to_merge:
                oposite_neigh = self.find_opposite_vert_group(graph, y_neigh, 'y', match_verts[1:], matching_vertices[idx:])
                is_good = self.check_production_predicats(oposite_neigh, y_neigh, 'x')
                # check isomorphic?
                merge_parts.append((y_neigh, oposite_neigh)) if oposite_neigh is not None and is_good else None
        
        return merge_parts # change to return i_verts
    
    def check_production_predicats(self, group_0, group_1, coord_name):
        group_0 = self.sort_verts(group_0, coord_name)
        group_1 = self.sort_verts(group_1, coord_name)
        
        for i in range(len(group_0)):
            if group_0[i].pos_x != group_1[i].pos_x or group_0[i].pos_y != group_1[i].pos_y:
                return False
            
        if (group_0[0].pos_x+group_0[2].pos_x)/2 != (group_1[0].pos_x+group_1[2].pos_x)/2 :
            return False
        if (group_0[0].pos_y+group_0[2].pos_y)/2 != (group_1[0].pos_y+group_1[2].pos_y)/2 :
            return False
        
        return True
    
    def sort_verts(self, group, coord_name):
        group.sort(key=lambda v: v.pos_x if coord_name=='x' else v.pos_y)
        return group 

    def find_opposite_vert_group(self, graph, vert_group, coord_name, vertices_to_search, matching_vertices):
        
        for vert in vertices_to_search:
            potential_group = self.find_coord_neighs(graph, vert, coord_name, matching_vertices)
            if self.compare_vert_groups(vert_group, potential_group):
                return potential_group
                
            
    def compare_vert_groups(self, group_0, group_1):
        if len(group_0) != len(group_1):
            return False
        
        get_pos = lambda v: (v.pos_x, v.pos_y)
        group_0_coords = map(get_pos, group_0)
        group_1_coords = map(get_pos, group_1)
        
        for el in group_0_coords:
            if el not in group_1_coords:
                return False
            
        return True
        
    
    def find_coord_neighs(self, graph, master_vert:Vert, coord_name: str, vertices_to_search: list):
        """
        find vert neighbours, (even far ones) which has the same coord 'coord_name' value and 
        has the same 'i' vert as far neighbour
        """
        
        neighs = [master_vert]
        for vs in vertices_to_search:
            match = self.check_coord((vs[0].pos_x, vs[0].pos_y), (master_vert.pos_x, master_vert.pos_y), coord_name)
            if match:
                master_i = set(graph.get_i_neighbour(master_vert, master_vert.level))
                for v in vs:
                    v_i = graph.get_i_neighbour(v, v_i.level)
                    common_i = master_i.intersection(v_i)
                    
                    neighs = neighs + [v] if len(common_i)>0 else neighs
                    
        return neighs

                    
                    
    def check_coord(self, coords_0, coords_1, coord_name):
        return coords_0[0] == coords_1[0] if coord_name=='x' else coords_0[1] == coords_1[1]
        
    
    def find_all_matching_vertices(self, graph: StandardizedGraph, level:int): 
        ordered_everts = {}
        
        for vert in graph.find_by_label("E"):
            if vert.level == level:
                key = (vert.pos_x, vert.pos_y)
                ordered_everts[key] = [vert] if ordered_everts[key]==None else ordered_everts[key] + [vert]
        
        matching_verts = []
        for key, value in ordered_everts.items():
            if len(value) == self.vertices_to_merge:
                matching_verts.append(value)
                
        return matching_verts
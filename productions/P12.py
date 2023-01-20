import networkx as nx
from utils.StandardizedGraph import StandardizedGraph, Vert
from itertools import permutations, combinations
from collections import defaultdict

def P12(graph: StandardizedGraph, prod_left_side):
    graph.underlying.remove_edge(prod_left_side.e_top, prod_left_side.e_right)
    for e_right_neigh in list(graph.underlying.neighbors(prod_left_side.e_right)):
        graph.underlying.remove_edge(prod_left_side.e_right, e_right_neigh)
        graph.underlying.add_edge(prod_left_side.e_left_down, e_right_neigh)
    graph.underlying.remove_node(prod_left_side.e_right)
    return graph

def match_P12(graph: StandardizedGraph, level: int):
    e_yellow_vertices = list(filter(
        lambda v: v.level() == level,
        graph.find_by_label("E")
    ))
    candidate_es = []
    for e in e_yellow_vertices:
        candidate_es += get_valid_es(graph, e)
    
    return list(filter(
        lambda candidates: candidates.is_valid(),
        candidate_es
    ))


class P12_E_Verts():

    def __init__(self, graph, e_top, e_left_middle, e_left_down, e_right):
        self.graph = graph
        self.e_top = e_top
        self.e_left_middle = e_left_middle
        self.e_left_down = e_left_down
        self.e_right = e_right

    def is_valid(self):
        #TODO (na kazdym etapie szukania jak jest None to ma zwrocic false)
        i_left_top = self.get_common_neigh(self.e_top, self.e_left_middle, "I")
        i_left_down = self.get_common_neigh(self.e_left_middle, self.e_left_down, "I")
        i_right = self.get_common_neigh(self.e_right, self.e_top, "I")

        i_orange_left = self.get_common_neigh(i_left_top, i_left_down, "i")
        i_orange_right = self.get_neigh(i_right, "i")[0]
        
        e_top = self.get_common_neigh(i_orange_right, i_orange_left, "E")
        return e_top is not None

    def get_common_neigh(self, v1, v2, label: str):
        for i_vert in self.graph.find_by_label(label):
            i_neighbors = self.graph.underlying.neighbors(i_vert.underlying) 
            if v1 in i_neighbors and v2 in i_neighbors:
                return i_vert.underlying
        return None
    
    def get_neigh(self, v1, label: str):
        return list(filter(
            lambda n: nx.get_node_attributes(self.graph.underlying, "label")[n] == label,
            self.graph.underlying.neighbors(v1)
        ))

    def __str__(self):
        return f"E_TOP: {self.coords(self.e_top)}  E_LEFT_MIDDLE: {self.coords(self.e_left_middle)} E_LEFT_DOWN: {self.coords(self.e_left_down)} E_RIGHT: {self.coords(self.e_right)}"

    def __repr__(self):
        return self.__str__()

    def coords(self, vert):
        return (pos_x(self.graph.underlying, vert), pos_y(self.graph.underlying, vert))

def get_valid_es(graph: StandardizedGraph, e_top):
    valid_es = []
    for e_neigh_pair in combinations(graph.underlying.neighbors(e_top.underlying), 2):
        for e_left_middle, e_right in permutations(e_neigh_pair):
            if not is_vertex_between(graph.underlying, e_top.underlying, e_right, e_left_middle):
                continue
            for e_left_down in graph.underlying.neighbors(e_left_middle):
                if is_vertex_between(graph.underlying, e_top.underlying, e_left_down, e_left_middle):
                    valid_es.append(P12_E_Verts(graph, e_top.underlying, e_left_middle, e_left_down, e_right))

    return valid_es


def is_vertex_between(graph, v1, v2, middle_v):
    return ((pos_x(graph, v1) + pos_x(graph, v2)) / 2) == pos_x(graph, middle_v) and ((pos_y(graph, v1) + pos_y(graph, v2)) / 2) == pos_y(graph, middle_v)

def pos_x(graph, vert):
    return nx.get_node_attributes(graph, "pos_x")[vert]

def pos_y(graph, vert):
    return nx.get_node_attributes(graph, "pos_y")[vert]
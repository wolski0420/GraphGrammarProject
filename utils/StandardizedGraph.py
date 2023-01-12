import networkx as nx
from networkx.algorithms.isomorphism import is_isomorphic
from matplotlib import pyplot as plt


class Vert:
    def __init__(self, graph: nx.Graph, vertex):
        self.graph = graph
        self.underlying = vertex

    def level(self):
        return nx.get_node_attributes(self.graph, "level")[self.underlying]

    def label(self):
        return nx.get_node_attributes(self.graph, "label")[self.underlying]

    def pos_x(self):
        return nx.get_node_attributes(self.graph, "pos_x")[self.underlying]

    def pos_y(self):
        return nx.get_node_attributes(self.graph, "pos_y")[self.underlying]

    def __eq__(self, other):
        return isinstance(other, Vert) \
            and self.level() == other.level() \
            and self.label() == other.label() \
            and self.pos_x() == other.pos_x() \
            and self.pos_y() == other.pos_y()

    def __ne__(self, other):
        return not self.__eq__(other)


class StandardizedGraph:
    """
    Standardized form of a networkx graph, where the vertex IDs do not have to be manually managed.

    The underlying networkX graph can be found in .underlying, but direct modification of that is undesirable.
    Consider adding methods to this class instead.

    Internal vertices and the graph in general are all mutable.
    """

    def __init__(self):
        self.underlying = nx.Graph()
        self.max_node_id = 0

    def add_vert(self, pos_x: float, pos_y: float, label: str, level: int) -> Vert:
        self.underlying.add_node(self.max_node_id, pos_x=pos_x, pos_y=pos_y, label=label, level=level)
        node = self.max_node_id
        self.max_node_id += 1
        return Vert(self.underlying, node)

    def add_edge(self, v1: Vert, v2: Vert):
        self.underlying.add_edge(v1.underlying, v2.underlying)

    def add_edges(self, vert_pair_list):
        for (v1, v2) in vert_pair_list:
            self.add_edge(v1, v2)

    def modify_label(self, v: Vert, new_label: str):
        nx.set_node_attributes(self.underlying, {v.underlying: new_label}, name="label")
        return v

    def find_by_label(self, label: str):
        return [Vert(self.underlying, v) for (v, l) in nx.get_node_attributes(self.underlying, "label").items() if
                l == label]

    # add your methods here

    def get_neighbours(self, v: Vert, level: int, label: str):
        """
        get list of neighbours of v on selected level
        """
        return list(filter(
            lambda neigh: nx.get_node_attributes(self.underlying, "level")[neigh] == level and
                          nx.get_node_attributes(self.underlying, "label")[neigh] == label,
            self.underlying.neighbors(v.underlying)
        ))

    def __eq__(self, other):
        return isinstance(other, StandardizedGraph) \
            and is_isomorphic(self.underlying, other.underlying)

    def __ne__(self, other):
        return not self.__eq__(other)

    def find_by_pos(self, pos_x: float, pos_y:float):

        return [Vert(self.underlying, v) for v in list(filter(
            lambda node: nx.get_node_attributes(self.underlying, "pos_x")[node] == pos_x and
                          nx.get_node_attributes(self.underlying, "pos_y")[node] == pos_y,
            self.underlying.nodes
        ))]

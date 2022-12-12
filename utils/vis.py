import networkx as nx
from matplotlib import pyplot as plt

from utils import StandardizedGraph


def _get_color_by_level(level: int):
    match level:
        case 0: return "blue"
        case 1: return "violet"
        case 2: return "red"
        case 3: return "orange"
        case 4: return "yellow"
        case _: return "black"

def _recenter_by_hist(vertex_level, center_level, offset_dist=25):
    level_offset = center_level - vertex_level
    return level_offset * offset_dist

def _get_node_text(G, vertex, show_labels, show_position):
    text = nx.get_node_attributes(G, "label")[vertex] if show_labels else ""
    text += " " if show_labels and show_position else ""
    text += "(" + str(nx.get_node_attributes(G, "pos_x")[vertex]) + "," if show_labels else ""
    text +=  str(nx.get_node_attributes(G, "pos_y")[vertex]) + ")" if show_labels else ""
    return text

def visualise_graph(
        graph: StandardizedGraph, center_level=0, hist=[], show_labels=True,
        show_position=True, width=8, height=6, dpi=80
    ) -> None:
    '''
    Visualizes the graph with its history. 
    
    What part of the history will be drawn and where can be manipulated with optional parameters.

    Drawing positions are based on the "level", "pos_x" and "pos_y" parameters of the nodes.
    This means that nodes with the same position and level may overlap (be careful!).
    
    Optional keyword arguments:
    * center_level:   integer that decides which level od the graph will have real positions on the plot
    * hist:           list of "level" integers deciding the level that will be shown (entire history by default)
    * show_labels:    boolean deciding whether to show letter labels (based on the "label" param)
    * show_positions: boolean deciding whether to show positions (based on the "pos_x" and "pos_y" params)
    * width, height, dpi: matplotlib args
    '''
    G = graph.underlying
    plt.figure(figsize=(width, height), dpi=dpi)
    for (v1, v2) in G.edges():
        l1 = nx.get_node_attributes(G, "level")[v1]
        l2 = nx.get_node_attributes(G, "level")[v2]
        if hist and (l1 not in hist or l2 not in hist):
            continue
        x1 = nx.get_node_attributes(G, "pos_x")[v1]
        y1 = nx.get_node_attributes(G, "pos_y")[v1] + _recenter_by_hist(l1, center_level)
        x2 = nx.get_node_attributes(G, "pos_x")[v2]
        y2 = nx.get_node_attributes(G, "pos_y")[v2] + _recenter_by_hist(l2, center_level)
        plt.plot([x1, x2], [y1, y2], color="black")
    for vertex in G:
        l = nx.get_node_attributes(G, "level")[vertex]
        if hist and l not in hist:
            continue
        x = nx.get_node_attributes(G, "pos_x")[vertex]
        y = nx.get_node_attributes(G, "pos_y")[vertex] + _recenter_by_hist(l, center_level)
        plt.plot(x, y, marker='o', color=_get_color_by_level(l), markersize=8)
        if show_labels or show_position:
            plt.text(x + 0.5, y + 1, _get_node_text(G, vertex, show_labels, show_position))
    plt.show()
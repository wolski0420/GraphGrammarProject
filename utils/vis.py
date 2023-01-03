import networkx as nx
from matplotlib import pyplot as plt
from collections import defaultdict
from functools import reduce

from utils import StandardizedGraph


def _get_color_by_level(level: int):
    match level:
        case 0:
            return "blue"
        case 1:
            return "violet"
        case 2:
            return "red"
        case 3:
            return "orange"
        case 4:
            return "yellow"
        case _:
            return "black"


def _recenter_by_hist(vertex_level, center_level, offset_dist=25):
    level_offset = center_level - vertex_level
    return level_offset * offset_dist


def _get_node_text(G, vertex, show_labels, show_position):
    text = nx.get_node_attributes(G, "label")[vertex] if show_labels else ""
    text += " " if show_labels and show_position else ""
    text += (
        "(" + str(nx.get_node_attributes(G, "pos_x")[vertex]) + ","
        if show_labels
        else ""
    )
    text += str(nx.get_node_attributes(G, "pos_y")[vertex]) + ")" if show_labels else ""
    return text


def _sgn(i):
    if i < 0:
        return -1
    elif i > 0:
        return 1
    else:
        return 0


def _clamp(i):
    return max(-1, min(i, 1))


def visualise_graph(
    graph: StandardizedGraph,
    center_level=0,
    hist=[],
    show_labels=True,
    show_position=True,
    move_equal=True,
    width=8,
    height=6,
    dpi=80,
) -> None:
    """
    Visualizes the graph with its history.

    What part of the history will be drawn and where can be manipulated with optional parameters.

    Drawing positions are based on the "level", "pos_x" and "pos_y" parameters of the nodes.
    This means that nodes with the same position and level may overlap (be careful!).

    Optional keyword arguments:
    * center_level:   integer that decides which level od the graph will have real positions on the plot
    * hist:           list of "level" integers deciding the level that will be shown (entire history by default)
    * show_labels:    boolean deciding whether to show letter labels (based on the "label" param)
    * show_positions: boolean deciding whether to show positions (based on the "pos_x" and "pos_y" params)
    * move_equal:     boolean deciding whether to offset vertices with equal position parameters
    * width, height, dpi: matplotlib args
    """
    G = graph.underlying
    pos_x_attr = nx.get_node_attributes(G, "pos_x")
    pos_y_attr = nx.get_node_attributes(G, "pos_y")
    level_attr = nx.get_node_attributes(G, "level")
    offset_dict = defaultdict(lambda: (0, 0))
    if move_equal:
        equals = [
            [
                v2
                for v2 in G
                if abs(pos_x_attr[v1] - pos_x_attr[v2]) < 0.1
                and abs(pos_y_attr[v1] - pos_y_attr[v2]) < 0.1
                and level_attr[v1] == level_attr[v2]
            ]
            for v1 in G
        ]
        equals = [i for i in equals if len(i) > 1]
        for eq_list in equals:
            for v in eq_list:
                X = pos_x_attr[v]
                Y = pos_y_attr[v]
                v_neighbours = [i for i in G.neighbors(v) if level_attr[i]]
                v_diff = [
                    (_sgn(pos_x_attr[i] - X), _sgn(pos_y_attr[i] - Y))
                    for i in v_neighbours
                ]
                summed = reduce(lambda a, b: (a[0] + b[0], a[1] + b[1]), v_diff)
                offset = (_clamp(summed[0]), _clamp(summed[1]))
                offset_dict[v] = offset

    plt.figure(figsize=(width, height), dpi=dpi)
    for (v1, v2) in G.edges():
        l1 = level_attr[v1]
        l2 = level_attr[v2]
        if hist and (l1 not in hist or l2 not in hist):
            continue
        x1 = pos_x_attr[v1]
        y1 = pos_y_attr[v1] + _recenter_by_hist(l1, center_level)
        x2 = pos_x_attr[v2]
        y2 = pos_y_attr[v2] + _recenter_by_hist(l2, center_level)
        plt.plot(
            [x1 + offset_dict[v1][0], x2 + offset_dict[v2][0]],
            [y1 + offset_dict[v1][1], y2 + offset_dict[v2][1]],
            color="black",
        )
    for vertex in G:
        l = nx.get_node_attributes(G, "level")[vertex]
        if hist and l not in hist:
            continue
        x = pos_x_attr[vertex]
        y = pos_y_attr[vertex] + _recenter_by_hist(l, center_level)
        plt.plot(
            x + offset_dict[vertex][0],
            y + offset_dict[vertex][1],
            marker="o",
            color=_get_color_by_level(l),
            markersize=8,
        )
        if show_labels or show_position:
            plt.text(
                x + offset_dict[vertex][0] + 0.5,
                y + offset_dict[vertex][1] + 1,
                _get_node_text(G, vertex, show_labels, show_position),
            )
            # plt.text(x + 0.5, y + 1, vertex)
    plt.show()

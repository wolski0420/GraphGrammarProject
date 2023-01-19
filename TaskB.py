from utils.StandardizedGraph import StandardizedGraph
from utils.vis import visualise_graph
from productions.P1 import match_P1, P1
from productions.P2 import match_P2, P2
from productions.P7 import match_P7, P7
from productions.P10 import match_P10, P10


# TODO: implement P11 and P12
# from productions.P11 import match_P11, P11
# from productions.P12 import match_P12, P12

def step1(graph: StandardizedGraph) -> StandardizedGraph:
    matched = match_P1(graph)
    return P1(graph, matched[0])


def step2(graph: StandardizedGraph) -> StandardizedGraph:
    matched = match_P2(graph, level=1)
    return P2(graph, matched[0])


def step3(graph: StandardizedGraph) -> StandardizedGraph:
    matched_P2 = match_P2(graph, level=2)
    matched_P10 = match_P10(graph, level=2)
    matched_P2 = list(filter(lambda vert: vert.pos_x() > 0 or vert.pos_y() > 0, matched_P2))
    matched_P10 = list(filter(lambda vert: vert.pos_x() < 0 and vert.pos_y() < 0, matched_P10))
    for v in matched_P2:
        graph = P2(graph, v)
    return P10(graph, matched_P10[0])


# TODO: finish when P11 is available
def step4(graph: StandardizedGraph) -> StandardizedGraph:
    matched_P7 = match_P7(graph, level=3)
    # matched_P11 = match_P11(graph, level=3)
    matched_P7 = list(filter(
        lambda verts: all(vert.pos_y() == 0 for vert in verts[0]) and all(vert.pos_y() == 0 for vert in verts[1]),
        matched_P7)
    )
    matched_P7_0, matched_P7_1 = matched_P7[0]
    return P7(graph, matched_P7_0, matched_P7_1)


def step5(graph: StandardizedGraph) -> StandardizedGraph:
    matched_P7 = match_P7(graph, level=3)
    matched_P7_0, matched_P7_1 = matched_P7[0]
    return P7(graph, matched_P7_0, matched_P7_1)


# TODO: implement when P11 is available
def step6(graph: StandardizedGraph) -> StandardizedGraph:
    # matched_P11 = match_P11(graph, level=3)
    # matched_P11_0, matched_P11_1 = matched_P11[0]
    # return P7(graph, matched_P11_0, matched_P11_1)
    return graph


def task_B():
    level = 0
    graph = StandardizedGraph()
    graph.add_vert(0, 0, "El", level)

    visualise_graph(graph, center_level=0, hist=[0])

    steps = [step1, step2, step3, step4, step5, step6]

    for i, step in enumerate(steps):
        level = min(i, 3)
        graph = step(graph)
        visualise_graph(
            graph,
            height=max(6, 6 + 4 * (level - 1)),
            width=max(8, 8 + 2 * (level - 1)),
            dpi=max(80, 80 + 20 * (level - 1))
        )


if __name__ == "__main__":
    task_B()

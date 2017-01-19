""" Helper functions for project"""


EX_GRAPH0 = {0: set([1, 2]),
             1: set([]),
             2: set([])}

EX_GRAPH1 = {0: set([1, 4, 5]),
             1: set([2, 6]),
             2: set([3]),
             3: set([0]),
             4: set([1]),
             5: set([2]),
             6: set([])}

EX_GRAPH2 = {0: set([1, 4, 5]),
             1: set([2, 6]),
             2: set([3, 7]),
             3: set([7]),
             4: set([1]),
             5: set([2]),
             6: set([]),
             7: set([3]),
             8: set([1, 2]),
             9: set([0, 3, 4, 5, 6, 7])}

GRAPH1 = {0: set([]),
          1: set([0]),
          2: set([0]),
          3: set([0]),
          4: set([0])}


def make_complete_graph(num_nodes):
    """
    Takes a number of nodes, and return
    a graph (dictionary) with all possible
    edges
    """
    dictionary = {}
    for idx in range(num_nodes):
        edges = set([])
        for idx2 in range(num_nodes):
            if idx != idx2:
                edges.add(idx2)
        dictionary[idx] = edges
    return dictionary


def compute_out_degrees(digraph):
    """
    Takes a graph, and returns a dictionary
    with sme keys, but number of out-edges
    as value
    """
    dictionary = {}
    for key in digraph:
        dictionary[key] = len(digraph[key])
    return dictionary


def compute_in_degrees(digraph):
    """
    Takes a graph, and returns a dictionary
    with same keys, but number in-edges of node
    as value
    """
    dictionary = {}
    for key in digraph:
        dictionary[key] = 0
    for key in digraph:
        for edge in digraph[key]:
            dictionary[edge] += 1
    return dictionary


def in_degree_distribution(digraph):
    """
    Takes a digraph, and returns a dictionary
    whick keys are the in-degree, and
    the value is the number of nodes with that
    in-degree
    """
    in_degree_values = compute_in_degrees(digraph)
    dictionary = {}
    for node in in_degree_values:
        if in_degree_values[node] not in dictionary:
            dictionary[in_degree_values[node]] = 0
        dictionary[in_degree_values[node]] += 1
    return dictionary

"""
Some creation and computation
on graphs
"""
import random
import alg_dpa_trial as dpa

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

counter = 0


def compute_in_degrees(digraph):
    """
    Takes a graph, and returns a dictionary
    with same keys, but number in-edges of node
    as value
    """
    global counter
    dictionary = {}
    # for key in digraph:
    #     dictionary[key] = []
    #     counter += 1
    # for key in dictionary:
    #     in_edges = 0
    #     for node in digraph:
    #         if node != key:
    #             for elem in digraph[node]:
    #                 if elem == key:
    #                     in_edges += 1
    #                 counter += 1
    #     dictionary[key] = in_edges
    # dictionary = {}
    for key in digraph:
        dictionary[key] = 0
        # counter += 1
    for key in digraph:
        for edge in digraph[key]:
            dictionary[edge] += 1
            # print counter
            # counter += 1
    # print "Counter for compute:", counter
    # counter = 0
    return dictionary


def in_degree_distribution(digraph):
    """
    Takes a digraph, and returns a dictionary
    whick keys are the in-degree, and
    the value is the number of nodes with that
    in-degree
    """
    global counter
    in_degree_values = compute_in_degrees(digraph)
    dictionary = {}
    for node in in_degree_values:
        if in_degree_values[node] not in dictionary:
            dictionary[in_degree_values[node]] = 0
        dictionary[in_degree_values[node]] += 1
    return dictionary


def normalize_in_degree_graph(in_graph, total_nodes):
    normalized_graph = {}
    normalization = 0
    for degree in in_graph:
        normalized_graph[degree] = in_graph[degree] / float(total_nodes)
        normalization += normalized_graph[degree]
    # assert normalization == 1.0, "Not normalized"
    return normalized_graph


def modified_ER(length, probability):
    graph = {}
    for node in range(length):
        graph[node] = set([])
    for first_node in range(length):
        print first_node
        available_nodes = [idx for idx in range(length)]
        number_of_neighbors = int(random.gauss(length / 2, 30))
        neighbors = set([])
        for idx in range(number_of_neighbors):
            new_neighbor = random.choice(available_nodes)
            neighbors.add(new_neighbor)
            available_nodes.remove(new_neighbor)
        graph[first_node] = neighbors
        # print first_node
        # for second_node in range(length):
        #     if first_node != second_node:
        #         edge_proba = random.uniform(0, 1)
        #         if edge_proba < probability:
        #             graph[first_node].add(second_node)
    return graph


def DPA(length, num_neighbors):
    assert length >= num_neighbors and num_neighbors > 0
    # Init graph with num_neighbors nodes
    graph = {}
    for node in range(num_neighbors):
        graph[node] = set([])
    # Make the graph complete
    for first_node in graph:
        for second_node in graph:
            if first_node != second_node:
                graph[first_node].add(second_node)
    print "LENGTH", len(graph)
    # Create the rest
    a_dpa = dpa.DPATrial(num_neighbors)
    for idx in range(length - num_neighbors):
        graph[idx + num_neighbors] = a_dpa.run_trial(num_neighbors)
    return graph

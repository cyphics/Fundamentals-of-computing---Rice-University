"""
Helper function for second assignment.
"""

import random
from collections import deque
import alg_application2_provided as provided
import alg_upa_trial as upa


def bfs_visited(ugraph, start_node):
    """
    Take an undirected graph and a start node,
    and returns the connected graph that includes
    the start node
    """
    queue = deque()
    visited = set([start_node])
    queue.append(start_node)
    while len(queue) > 0:
        node = queue.pop()
        for neighbor in ugraph[node]:
            if neighbor not in visited:
                visited.add(neighbor)
                queue.append(neighbor)
    return visited


def cc_visited(ugraph):
    """
    Take an undirected graph and returns
    a set of all connected components
    """
    remaining_nodes = [node for node in ugraph]
    connected_components = []
    while len(remaining_nodes) > 0:
        node = remaining_nodes[0]
        # Compute connected component
        component = bfs_visited(ugraph, node)
        # Add result to set
        connected_components.append(component)
        # Remove visited nodes from remaining
        for elem in component:
            remaining_nodes.remove(elem)
    return connected_components


def largest_cc_size(ugraph):
    """
    Tak an undirected graph, and returns
    the size (int) and its largest connected
    component
    """
    size = 0
    all_components = cc_visited(ugraph)
    for component in all_components:
        if len(component) > size:
            size = len(component)
    return size


def compute_resilience(ugraph, attack_order):
    """
    Take a graph and a list of nodes, remove
    the nodes in order, and returns a list
    of the size of remaining largest component
    after each attack.
    """
    list_of_sizes = [largest_cc_size(ugraph)]
    for attacked_node in attack_order:
        provided.delete_node(ugraph, attacked_node)
        list_of_sizes.append(largest_cc_size(ugraph))
    return list_of_sizes


def ER_graph(length, probability):
    graph = {}
    for node in range(length):
        graph[node] = set([])
    for first_node in range(length):
        for second_node in range(first_node, length):
            if first_node != second_node:
                edge_proba = random.uniform(0, 1)
                if edge_proba < probability:
                    graph[first_node].add(second_node)
                    graph[second_node].add(first_node)
    return graph


def number_edges(ugraph):
    evaluated_nodes = []
    number_of_edges = 0
    for node in ugraph:
        for neighbor in ugraph[node]:
            if neighbor not in evaluated_nodes:
                number_of_edges += 1
                evaluated_nodes.append(node)
    return number_of_edges


def make_complete_graph(length):
    graph = {}
    for node in range(length):
        graph[node] = set([])

    # Make the graph complete
    for first_node in range(length):
        for second_node in range(first_node + 1, length):
            graph[first_node].add(second_node)
            graph[second_node].add(first_node)
    return graph


def UPA_graph(length, num_neighbors):
    assert length >= num_neighbors and num_neighbors > 0
    # Make the graph complete
    graph = make_complete_graph(num_neighbors)
    # Create the rest
    a_upa = upa.UPATrial(num_neighbors)
    for idx in range(length - num_neighbors):
        new_neighbors = a_upa.run_trial(num_neighbors)
        graph[idx + num_neighbors] = new_neighbors
        for neighbor in new_neighbors:
            graph[neighbor].add(idx + num_neighbors)

    return graph


def random_order(ugraph):
    list_nodes = [node for node in ugraph]
    random.shuffle(list_nodes)
    return list_nodes


def fast_targeted_order(ugraph):
    """
    Take a graph, and return a list of nodes in
    descending degree order.
    """
    DegreeSets = {}
    for degree in range(len(ugraph)):
        DegreeSets[degree] = set([])
    for node in range(len(ugraph)):
        degree = len(ugraph[node])
        DegreeSets[degree].add(node)
    ordered_nodes = []
    i = 0
    for degree in range(len(ugraph) - 1, -1, -1):
        while DegreeSets[degree]:
            current_node = DegreeSets[degree].pop()
            for neighbor in ugraph[current_node]:
                neighbor_degree = len(ugraph[neighbor])
                DegreeSets[neighbor_degree].remove(neighbor)
                DegreeSets[neighbor_degree - 1].add(neighbor)
            ordered_nodes.append(current_node)
            i += 1
            provided.delete_node(ugraph, current_node)
    return ordered_nodes


def build_plot(degree_distribution):
    """
    Build plot of the number of increments in mystery function
    """
    plot = [[], []]
    for degree in degree_distribution:
        # counter += 1
        plot[0].append(degree)
        plot[1].append(degree_distribution[degree])
    return plot

"""
Helper function for second assignment.
"""

from collections import deque


def delete_node(ugraph, node):
    """
    Delete a node from an undirected graph
    """
    neighbors = ugraph[node]
    ugraph.pop(node)
    for neighbor in neighbors:
        ugraph[neighbor].remove(node)


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
        delete_node(ugraph, attacked_node)
        list_of_sizes.append(largest_cc_size(ugraph))
    return list_of_sizes

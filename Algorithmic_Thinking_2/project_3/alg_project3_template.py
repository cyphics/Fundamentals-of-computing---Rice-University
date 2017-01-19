"""
Student template code for Project 3
Student will implement five functions:

slow_closest_pair(cluster_list)
fast_closest_pair(cluster_list)
closest_pair_strip(cluster_list, horiz_center, half_width)
hierarchical_clustering(cluster_list, num_clusters)
kmeans_clustering(cluster_list, num_clusters, num_iterations)

where cluster_list is a 2D list of clusters in the plane
"""

import math
import alg_cluster




######################################################
# Code for closest pairs of clusters

def pair_distance(cluster_list, idx1, idx2):
    """
    Helper function that computes Euclidean distance between two clusters in a list

    Input: cluster_list is list of clusters, idx1 and idx2 are integer indices for two clusters

    Output: tuple (dist, idx1, idx2) where dist is distance between
    cluster_list[idx1] and cluster_list[idx2]
    """
    return (cluster_list[idx1].distance(cluster_list[idx2]), min(idx1, idx2), max(idx1, idx2))


def slow_closest_pair(cluster_list):
    """
    Compute the distance between the closest pair of clusters in a list (slow)

    Input: cluster_list is the list of clusters

    Output: tuple of the form (dist, idx1, idx2) where the centers of the clusters
    cluster_list[idx1] and cluster_list[idx2] have minimum distance dist.
    """
    distance = (float('inf'), 0, 0)
    for first_idx in range(len(cluster_list)):
        for second_idx in range(len(cluster_list)):
            if first_idx != second_idx:
                distance = min(distance, pair_distance(cluster_list, first_idx, second_idx))
            # if pair_distance(cluster_list, first_cluster, second_cluster)[0] < distance:
            #     distance = pair_distance(cluster_list, first_cluster, second_cluster)
    return distance



def fast_closest_pair(cluster_list):
    """
    Compute the distance between the closest pair of clusters in a list (fast)

    Input: cluster_list is list of clusters SORTED such that horizontal positions of their
    centers are in ascending order

    Output: tuple of the form (dist, idx1, idx2) where the centers of the clusters
    cluster_list[idx1] and cluster_list[idx2] have minimum distance dist.
    """

    assert len(cluster_list) > 1, "List too short"

    distance = (float('inf'), 0, 0)
    list_length = len(cluster_list)

    # Base case
    if list_length <= 3:
        return slow_closest_pair(cluster_list)

    half_length = list_length / 2
    part_one = cluster_list[:half_length]
    part_two = cluster_list[half_length:]

    distance_one = fast_closest_pair(part_one)
    distance_two = fast_closest_pair(part_two)

    distance = min(distance_one, (distance_two[0], distance_two[1] + half_length, distance_two[2] + half_length))
    middle = (cluster_list[half_length - 1].horiz_center() + cluster_list[half_length].horiz_center()) / 2
    distance = min(distance, closest_pair_strip(cluster_list, middle, distance[0]))


    return distance


def closest_pair_strip(cluster_list, horiz_center, half_width):
    """
    Helper function to compute the closest pair of clusters in a vertical strip

    Input: cluster_list is a list of clusters produced by fast_closest_pair
    horiz_center is the horizontal position of the strip's vertical center line
    half_width is half the width of the strip (i.e; the maximum horizontal distance
    that a cluster can lie from the center line)

    Output: tuple of the form (dist, idx1, idx2) where the centers of the clusters
    cluster_list[idx1] and cluster_list[idx2] lie in the strip and have minimum distance dist.
    """

    # Create list in strip
    indices_list = []
    for idx in range(len(cluster_list)):
        if abs(cluster_list[idx].horiz_center() - horiz_center) < half_width:
            indices_list.append(idx)

    distance = (float('inf'), -1, -1)

    if len(indices_list) == 0:
        return distance
    # Sort in vertical order
    sort_indices_vertically(cluster_list, indices_list)
    length = len(indices_list)

    for first_idx in range(length - 1):
        for second_idx in range(first_idx + 1, min(first_idx + 3, length - 1) + 1):
            distance = min(distance, (cluster_list[indices_list[first_idx]].distance(cluster_list[indices_list[second_idx]]), indices_list[first_idx], indices_list[second_idx]))

    if distance[1] > distance[2]:
        old = tuple(distance)
        distance = (old[0], old[2], old[1])

    return distance


def sort_indices_vertically(cluster_list, indices_list):
    """
    Take a list of cluster, an incice list, and return the indice list
    by vertical ascending order
    """
    # Base case
    if len(indices_list) == 1:
        return indices_list

    # Recursive case
    middle = len(indices_list) / 2
    part_one = sort_indices_vertically(cluster_list, indices_list[:middle])
    part_two = sort_indices_vertically(cluster_list, indices_list[middle:])

    idx_1 = 0
    idx_2 = 0
    idx_3 = 0

    while idx_1 < len(part_one) and idx_2 < len(part_two):
        if cluster_list[part_one[idx_1]].vert_center() <= cluster_list[part_two[idx_2]].vert_center():
            indices_list[idx_3] = part_one[idx_1]
            idx_1 += 1
        else:
            indices_list[idx_3] = part_two[idx_2]
            idx_2 += 1
        idx_3 += 1

    if idx_1 == len(part_one):
        while idx_2 < len(part_two):
            indices_list[idx_3] = part_two[idx_2]
            idx_2 += 1
            idx_3 += 1
    else:
        while idx_1< len(part_one):
            indices_list[idx_3] = part_one[idx_1]
            idx_1 += 1
            idx_3 += 1


    return indices_list


######################################################################
# Code for hierarchical clustering


def hierarchical_clustering(cluster_list, num_clusters):
    """
    Compute a hierarchical clustering of a set of clusters
    Note: the function may mutate cluster_list

    Input: List of clusters, integer number of clusters
    Output: List of clusters whose length is num_clusters
    """

    while len(cluster_list) > num_clusters:
        # Sort clusters vertically
        cluster_list.sort(key = lambda cluster: cluster.horiz_center())
        # Find two closest clusters
        closest_clusters = fast_closest_pair(cluster_list)
        # Merge second into first
        cluster_list[closest_clusters[1]].merge_clusters(cluster_list[closest_clusters[2]])
        # Remove the second one
        del cluster_list[closest_clusters[2]]
        # Resort cluster list


    assert len(cluster_list) == num_clusters, "ERROR, wrong output size"

    return cluster_list


######################################################################
# Code for k-means clustering


def kmeans_clustering(cluster_list, num_clusters, num_iterations):
    """
    Compute the k-means clustering of a set of clusters
    Note: the function may not mutate cluster_list

    Input: List of clusters, integers number of clusters and number of iterations
    Output: List of clusters whose number_of_clusters is num_clusters
    """

    # Initialize centers
    # Find num_clusters biggest counties
    biggest_counties = []# set([])
    # Sort cluster_list by population size
    cluster_list_copy = []
    for cluster in cluster_list:
        cluster_list_copy.append(cluster)

    cluster_list_copy.sort(key = lambda cluster: cluster.total_population())
    for idx in range(num_clusters):
        biggest_county = cluster_list_copy[len(cluster_list) - idx - 1]
        biggest_counties.append(biggest_county)

    centers_list = []
    for county in biggest_counties:
        centers_list.append(alg_cluster.Cluster(set([]), county.horiz_center(), county.vert_center(), 0, 0))

    # For number of iterations
    for _ in range(num_iterations):
        # Init empty clusters
        list_of_clusters = []
        for center in centers_list:
            list_of_clusters.append(center.copy())

        # For each county, find closest center
        for county in cluster_list:
            distance = (float('inf'), -1)
            # Eval each center
            for idx in range(len(centers_list)):
                distance = min(distance, (centers_list[idx].distance(county), idx))
            # Add point to cluster
            list_of_clusters[distance[1]].merge_clusters(county)

        # Update each center position
        for idx in range(len(centers_list)):
            centers_list[idx] = alg_cluster.Cluster(set([]), list_of_clusters[idx].horiz_center(), list_of_clusters[idx].vert_center(), 0, 0)

    # position initial clusters at the location of clusters with largest populations
    assert len(list_of_clusters) == num_clusters, "ERROR, number of clusters incorrect"
    return list_of_clusters

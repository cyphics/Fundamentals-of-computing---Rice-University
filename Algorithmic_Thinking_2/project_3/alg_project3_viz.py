"""
Example code for creating and visualizing
cluster of county-based cancer risk data

Note that you must download the file
http://www.codeskulptor.org/#alg_clusters_matplotlib.py
to use the matplotlib version of this code
"""

# Flavor of Python - desktop or CodeSkulptor
DESKTOP = True

import math
import random
import urllib2
import alg_cluster
import matplotlib.pyplot as plt

# conditional imports
if DESKTOP:
    import alg_project3_template      # desktop project solution
    import alg_clusters_matplotlib
else:
    #import userXX_XXXXXXXX as alg_project3_solution   # CodeSkulptor project solution
    import alg_clusters_simplegui
    import codeskulptor
    codeskulptor.set_timeout(30)


###################################################
# Code to load data tables

# URLs for cancer risk data tables of various sizes
# Numbers indicate number of counties in data table

DIRECTORY = "http://commondatastorage.googleapis.com/codeskulptor-assets/"
DIRECTORY = "/home/cyphix/programmation/fundamentals/algorithmics/project_3/"

DATA_3108_URL = DIRECTORY + "data_clustering/unifiedCancerData_3108.csv"
DATA_896_URL = DIRECTORY + "data_clustering/unifiedCancerData_896.csv"
DATA_290_URL = DIRECTORY + "data_clustering/unifiedCancerData_290.csv"
DATA_111_URL = DIRECTORY + "data_clustering/unifiedCancerData_111.csv"


def load_data_table(data_url):
    """
    Import a table of county-based cancer risk data
    from a csv format file
    """
    # data_file = urllib2.urlopen(data_url)
    data_file = open(data_url, "r")

    data = data_file.read()
    data_lines = data.split('\n')
    print "Loaded", len(data_lines), "data points"
    data_tokens = [line.split(',') for line in data_lines]
    return [[tokens[0], float(tokens[1]), float(tokens[2]), int(tokens[3]), float(tokens[4])]
            for tokens in data_tokens]


############################################################
# Code to create sequential clustering
# Create alphabetical clusters for county data

def sequential_clustering(singleton_list, num_clusters):
    """
    Take a data table and create a list of clusters
    by partitioning the table into clusters based on its ordering

    Note that method may return num_clusters or num_clusters + 1 final clusters
    """

    cluster_list = []
    cluster_idx = 0
    total_clusters = len(singleton_list)
    cluster_size = float(total_clusters)  / num_clusters

    for cluster_idx in range(len(singleton_list)):
        new_cluster = singleton_list[cluster_idx]
        if math.floor(cluster_idx / cluster_size) != \
           math.floor((cluster_idx - 1) / cluster_size):
            cluster_list.append(new_cluster)
        else:
            cluster_list[-1] = cluster_list[-1].merge_clusters(new_cluster)

    return cluster_list


#####################################################################
# Code to load cancer data, compute a clustering and
# visualize the results


def run_example():
    """
    Load a data table, compute a list of clusters and
    plot a list of clusters

    Set DESKTOP = True/False to use either matplotlib or simplegui
    """
    data_table = load_data_table(DATA_111_URL)

    singleton_list = []
    for line in data_table:
        singleton_list.append(alg_cluster.Cluster(set([line[0]]), line[1], line[2], line[3], line[4]))


    # cluster_list = sequential_clustering(singleton_list, 15)
    # print "Displaying", len(cluster_list), "sequential clusters"

    cluster_list = alg_project3_template.hierarchical_clustering(singleton_list, 11)
    print "Displaying", len(cluster_list), "hierarchical clusters"

    #cluster_list = alg_project3_template.kmeans_clustering(singleton_list, 9, 5)
    #print "Displaying", len(cluster_list), "k-means clusters"

    print compute_distortion(cluster_list, data_table)


    # draw the clusters using matplotlib or simplegui
    if DESKTOP:

        alg_clusters_matplotlib.plot_clusters(data_table, cluster_list, False)
        # alg_clusters_matplotlib.plot_clusters(data_table, cluster_list, True)  #add cluster centers
    else:
        alg_clusters_simplegui.PlotClusters(data_table, cluster_list)   # use toggle in GUI to add cluster centers

# run_example()

def compute_distortion(cluster_list, data_table):
    distortion = 0
    for cluster in cluster_list:
        distortion += cluster.cluster_error(data_table)
    return distortion

def quality_comparison():
    data_table = load_data_table(DATA_290_URL)

    singleton_list = []
    for line in data_table:
        singleton_list.append(alg_cluster.Cluster(set([line[0]]), line[1], line[2], line[3], line[4]))

    hierarchical_distortion = []
    kmeans_distortion = []

    for idx in range(20, 5, -1):
        hierarchical_ouptut = alg_project3_template.hierarchical_clustering(singleton_list, idx)
        hierarchical_distortion.append(compute_distortion(hierarchical_ouptut, data_table))

    singleton_list = []
    for line in data_table:
        singleton_list.append(alg_cluster.Cluster(set([line[0]]), line[1], line[2], line[3], line[4]))

    for idx in range(20, 5, -1):
        kmeans_ouptut = alg_project3_template.kmeans_clustering(singleton_list, idx, 5)
        kmeans_distortion.append(compute_distortion(kmeans_ouptut, data_table))

    hierarchical_distortion.reverse()
    kmeans_distortion.reverse()


    abcissa = range(6, 21)
    plt.plot(abcissa, hierarchical_distortion, 'b', label="hierarchical distortion")
    plt.plot(abcissa, kmeans_distortion, 'r', label="k-means distortion")

    plt.xlabel("Number of clusters")
    plt.ylabel("Distortion ( x 10^11)")
    plt.title("Distortion comparison between hierarchical and k-means algo for 290 data table")
    # plt.xscale('log')
    # plt.yscale('log')
    plt.legend(bbox_to_anchor=(0.05, 1), loc=2, borderaxespad=0.)
    plt.show()
quality_comparison()

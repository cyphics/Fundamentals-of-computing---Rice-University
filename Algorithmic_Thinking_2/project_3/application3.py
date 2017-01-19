import matplotlib.pyplot as plt
import time
import random
import alg_cluster as cluster
import alg_project3_template as clustering
import alg_project3_viz as viz
import alg_clusters_matplotlib


def time_it(f, *args):
    start = time.clock()
    f(*args)
    return (time.clock() - start) * 1000


def gen_random_clusters(num_clusters):
    list_of_clusters = []

    # Generate num_clusters clusters
    for _ in range(num_clusters):

        cluster_center = (random.uniform(-1, 1), random.uniform(-1, 1))
        list_of_clusters.append(cluster.Cluster(set([]), cluster_center[0], cluster_center[1], 0, 0))
    return list_of_clusters


def viz_map(data, clustering_mode):
    """
    Load a data table, compute a list of clusters and
    plot a list of clusters

    Set DESKTOP = True/False to use either matplotlib or simplegui
    """
    if data == 1:
        data_table = viz.load_data_table(viz.DATA_111_URL)
    elif data == 2:
        data_table = viz.load_data_table(viz.DATA_290_URL)
    elif data == 3:
        data_table = viz.load_data_table(viz.DATA_896_URL)
    else:
        data_table = viz.load_data_table(data)

    singleton_list = []
    for line in data_table:
        singleton_list.append(cluster.Cluster(set([line[0]]), line[1], line[2], line[3], line[4]))

    if clustering_mode == "hierarchical":
        cluster_list = clustering.hierarchical_clustering(singleton_list, 9)
        print "Displaying", len(cluster_list), "hierarchical clusters"
    else:
        cluster_list = clustering.kmeans_clustering(singleton_list, 9, 5)
        print "Displaying", len(cluster_list), "k-means clusters"

    # print viz.compute_distortion(cluster_list, data_table)

    # draw the clusters using matplotlib or simplegui
    alg_clusters_matplotlib.plot_clusters(data_table, cluster_list, False)


def question1():
    times_slow = []
    times_fast = []

    NUM_OF_TRIALS = 200
    for idx in range(2, NUM_OF_TRIALS + 1):
        random_list = gen_random_clusters(idx)
        times_slow.append(time_it(clustering.slow_closest_pair, random_list))
        times_fast.append(time_it(clustering.fast_closest_pair, random_list))

    abcissa = range(2, NUM_OF_TRIALS + 1)

    plt.plot(abcissa, times_slow, 'b', label="slow_closest_pair")
    plt.plot(abcissa, times_fast, 'r', label="fast_closest_pair")
    plt.xlabel("Number of random clusters")
    plt.ylabel("Running time (milliseconds)")
    plt.title("Efficiency comparison between slow and fast pairing algorithm")
    plt.legend(bbox_to_anchor=(0.05, 1), loc=2, borderaxespad=0.)
    plt.show()


def question2():
    print "QUESTION 2"
    print "warning, takes a long time to compute"
    DIRECTORY = "/home/cyphix/programmation/fundamentals/algorithmics/project_3/"
    DATA_3108_URL = DIRECTORY + "data_clustering/unifiedCancerData_3108.csv"
    data_table = viz.load_data_table(DATA_3108_URL)

    singleton_list = []
    for line in data_table:
        singleton_list.append(cluster.Cluster(set([line[0]]), line[1], line[2], line[3], line[4]))

    cluster_list = clustering.hierarchical_clustering(singleton_list, 15)
    print "Displaying", len(cluster_list), "hierarchical clusters"

    # draw the clusters using matplotlib or simplegui
    alg_clusters_matplotlib.plot_clusters(data_table, cluster_list, False)


def question3():
    print "QUESTION 3"
    DIRECTORY = "/home/cyphix/programmation/fundamentals/algorithmics/project_3/"
    DATA_3108_URL = DIRECTORY + "data_clustering/unifiedCancerData_3108.csv"
    data_table = viz.load_data_table(DATA_3108_URL)

    singleton_list = []
    for line in data_table:
        singleton_list.append(cluster.Cluster(set([line[0]]), line[1], line[2], line[3], line[4]))

    cluster_list = clustering.kmeans_clustering(singleton_list, 15, 5)
    print "Displaying", len(cluster_list), "kmeans clusters"

    # draw the clusters using matplotlib or simplegui
    alg_clusters_matplotlib.plot_clusters(data_table, cluster_list, False)



def question5():
    print "QUESTON 5"
    viz_map(1, "hierarchical")


def question6():
    print"QUESTION 6"
    viz_map(1, "kmean")


def question7():
    print "QUESTION 7"
    data_table = viz.load_data_table(viz.DATA_111_URL)

    singleton_list = []
    for line in data_table:
        singleton_list.append(cluster.Cluster(set([line[0]]), line[1], line[2], line[3], line[4]))

    cluster_list_hierarchical = clustering.hierarchical_clustering(singleton_list, 9)

    singleton_list = []
    for line in data_table:
        singleton_list.append(cluster.Cluster(set([line[0]]), line[1], line[2], line[3], line[4]))

    cluster_list_kmeans = clustering.kmeans_clustering(singleton_list, 9, 5)

    print "Hierarcical distortion:", viz.compute_distortion(cluster_list_hierarchical, data_table)
    print "Kmeans distortion:", viz.compute_distortion(cluster_list_kmeans, data_table)


def question10(var):
    if var == 1:
        data_table = viz.load_data_table(viz.DATA_111_URL)
    elif var == 2:
        data_table = viz.load_data_table(viz.DATA_290_URL)
    else:
        data_table = viz.load_data_table(viz.DATA_896_URL)
    singleton_list = []
    for line in data_table:
        singleton_list.append(cluster.Cluster(set([line[0]]), line[1], line[2], line[3], line[4]))

    hierarchical_distortion = []
    kmeans_distortion = []

    for idx in range(20, 5, -1):
        hierarchical_ouptut = clustering.hierarchical_clustering(singleton_list, idx)
        hierarchical_distortion.append(viz.compute_distortion(hierarchical_ouptut, data_table))

    singleton_list = []
    for line in data_table:
        singleton_list.append(cluster.Cluster(set([line[0]]), line[1], line[2], line[3], line[4]))

    for idx in range(20, 5, -1):
        kmeans_ouptut = clustering.kmeans_clustering(singleton_list, idx, 5)
        kmeans_distortion.append(viz.compute_distortion(kmeans_ouptut, data_table))

    hierarchical_distortion.reverse()
    kmeans_distortion.reverse()

    abcissa = range(6, 21)
    plt.plot(abcissa, hierarchical_distortion, 'b', label="hierarchical distortion")
    plt.plot(abcissa, kmeans_distortion, 'r', label="k-means distortion")

    plt.xlabel("Number of clusters")
    plt.ylabel("Distortion ( x 10^11)")
    plt.title("Distortion comparison between hierarchical and k-means algo for 290 data table")
    plt.legend(bbox_to_anchor=(0.05, 1), loc=2, borderaxespad=0.)
    plt.show()


# question1()
# question2()
# question3()
# question5()
# question6()
# question7()
# question10(1)
# question10(2)
# question10(3)

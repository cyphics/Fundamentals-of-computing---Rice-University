import matplotlib.pyplot as plt
import time
import random
import alg_cluster as cluster
import alg_project3_template as clustering

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
# plt.xscale('log')
# plt.yscale('log')
plt.legend(bbox_to_anchor=(0.05, 1), loc=2, borderaxespad=0.)
plt.show()


### ANSWERS

# Question 7:
# for hierarchical_clustering: 1.7516 e+11
# for kmeans_clustering: 2.7125 e+11

# Question 8

# Since kmean algorithm initiates its search with the biggest existing counties, if two big counties are close to eachother, the algorithm will necessarily to put them in different clusters at the end, even though it would be wiser to put them in the same one. It is precisely what happens in the west part of the map, which explains the higher distortion of the kmean algorithm here.

# Question 9

# K-mean requires more supervision since the choice of initial clusters might lead to high distortion. Hierarchical algorithm does not require such a close look.

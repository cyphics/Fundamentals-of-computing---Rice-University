import unittest
import alg_project3_template as template
import alg_cluster as cluster
import urllib2

DIRECTORY = "http://commondatastorage.googleapis.com/codeskulptor-assets/"
DATA_24_URL = DIRECTORY + "data_clustering/unifiedCancerData_24.csv"

class testComputeDegree(unittest.TestCase):


    def test_slow_closest_pair_1(self):
        cluster_a = cluster.Cluster(set([1, 2, 3]), 100, 100, 1000, 1)
        cluster_b = cluster.Cluster(set([7]), 200, 400, 3000000, 6.1e-05)
        cluster_c = cluster.Cluster(set([8]), 202, 400, 3000000, 3.1e-05)
        cluster_list = [cluster_a, cluster_b, cluster_c]

        self.assertEqual(template.slow_closest_pair(cluster_list), (2.0, 1, 2))

    # def test_sort_clusters_vertically_1(self):
    #     cluster_a = cluster.Cluster(set([1, 2, 3]), 1, 100, 1, 1)
    #     cluster_b = cluster.Cluster(set([7]), 200, 4, 1, 6)
    #     cluster_c = cluster.Cluster(set([8]), 202, 400, 3, 3)
    #     cluster_list = [cluster_a, cluster_b, cluster_c]

    #     self.assertEqual(template.sort_clusters_vertically(cluster_list), [cluster_b, cluster_a, cluster_c])

    # def test_sort_clusters_vertically_2(self):
    #     cluster_a = cluster.Cluster(set([1]), 1, 10, 1, 1)
    #     cluster_b = cluster.Cluster(set([7]), 2, 11, 1, 6)
    #     cluster_c = cluster.Cluster(set([8]), 3, 40, 3, 3)
    #     cluster_list = [cluster_a, cluster_b, cluster_c]

    #     self.assertEqual(template.sort_clusters_vertically(cluster_list), [cluster_a, cluster_b, cluster_c])

    # def test_sort_clusters_vertically_3(self):
    #     cluster_a = cluster.Cluster(set([1]), 1, 10000, 1, 1)
    #     cluster_b = cluster.Cluster(set([7]), 2, 9939, 1, 6)
    #     cluster_c = cluster.Cluster(set([8]), 3, 40, 3, 3)
    #     cluster_list = [cluster_a, cluster_b, cluster_c]

    #     self.assertEqual(template.sort_clusters_vertically(cluster_list), [cluster_c, cluster_b, cluster_a])

    # def test_sort_indices_vertically_1(self):
    #     cluster_a = cluster.Cluster(set([1]), 1, 10000, 1, 1)
    #     cluster_b = cluster.Cluster(set([7]), 1, 9939, 1, 1)
    #     cluster_c = cluster.Cluster(set([8]), 1, 40, 1, 1)
    #     cluster_list = [cluster_a, cluster_b, cluster_c]

    #     self.assertEqual(template.sort_indices_vertically(cluster_list, [0, 1, 2]), [2, 1, 0])

    # def test_sort_indices_vertically_1(self):
    #     cluster_a = cluster.Cluster(set([1]), 1, 1, 1, 1)
    #     cluster_b = cluster.Cluster(set([7]), 1, 9, 1, 1)
    #     cluster_c = cluster.Cluster(set([8]), 1, 4, 1, 1)
    #     cluster_d = cluster.Cluster(set([8]), 1, 3, 1, 1)
    #     cluster_list = [cluster_a, cluster_b, cluster_c, cluster_d]

    #     self.assertEqual(template.sort_indices_vertically(cluster_list, [0, 1, 2, 3]), [0, 3, 2, 1])

    # def test_sort_indices_vertically_2(self):
    #     cluster_a = cluster.Cluster(set([]), 0, 0, 1, 0)
    #     cluster_b = cluster.Cluster(set([]), 1, 0, 1, 0)
    #     cluster_c = cluster.Cluster(set([]), 2, 0, 1, 0)
    #     cluster_d = cluster.Cluster(set([]), 3, 0, 1, 0)
    #     cluster_list = [cluster_a, cluster_b, cluster_c, cluster_d]

    #     self.assertEqual(template.sort_indices_vertically(cluster_list, [0, 1, 2, 3]), [0, 1, 2, 3])

    # def test_sort_indices_vertically_3(self):
    #     cluster_a = cluster.Cluster(set([]), 1.0, 1.0, 1, 0)
    #     cluster_b = cluster.Cluster(set([]), 1.0, 5.0, 1, 0)
    #     cluster_c = cluster.Cluster(set([]), 1.0, 4.0, 1, 0)
    #     cluster_d = cluster.Cluster(set([]), 1.0, 7.0, 1, 0)
    #     cluster_list = [cluster_a, cluster_b, cluster_c, cluster_d]

    #     self.assertEqual(template.sort_indices_vertically(cluster_list, [0, 1, 2, 3]), [0, 2, 1, 3])

    def test_closest_pair_strip_1(self):
        cluster_a = cluster.Cluster(set([1]), 1, 1, 1, 1)
        cluster_b = cluster.Cluster(set([2]), 1, 2, 1, 1)
        cluster_c = cluster.Cluster(set([3]), 1, 4, 1, 1)
        cluster_list = [cluster_a, cluster_b, cluster_c]

        self.assertEqual(template.closest_pair_strip(cluster_list, 2, 4), (1.0, 0, 1))

    def test_closest_pair_strip_2(self):
        cluster_a = cluster.Cluster(set([1]), 1, 100, 1, 1)
        cluster_b = cluster.Cluster(set([2]), 1, 200, 1, 1)
        cluster_c = cluster.Cluster(set([3]), 1, 400, 1, 1)
        cluster_d = cluster.Cluster(set([3]), 1, 110, 1, 1)
        cluster_e = cluster.Cluster(set([3]), 1, 240, 1, 1)
        cluster_list = [cluster_a, cluster_b, cluster_c, cluster_d, cluster_e]

        self.assertEqual(template.closest_pair_strip(cluster_list, 200, 400), (10, 0, 3))

    def test_closest_pair_strip_3(self):
        cluster_a = cluster.Cluster(set([1]), 1, 100, 1, 1)
        cluster_b = cluster.Cluster(set([2]), 4, 200, 1, 1)
        cluster_c = cluster.Cluster(set([3]), 1, 400, 1, 1)
        cluster_d = cluster.Cluster(set([3]), 1, 110, 1, 1)
        cluster_e = cluster.Cluster(set([3]), 5, 240, 1, 1)
        cluster_list = [cluster_a, cluster_b, cluster_c, cluster_d, cluster_e]

        self.assertEqual(template.closest_pair_strip(cluster_list, 4, 2), (40.01249804748511, 1, 4))


    def test_closest_pair_strip_4(self):
        cluster_a = cluster.Cluster(set([]), 0, 0, 1, 0)
        cluster_b = cluster.Cluster(set([]), 1, 0, 1, 0)
        cluster_c = cluster.Cluster(set([]), 2, 0, 1, 0)
        cluster_d = cluster.Cluster(set([]), 3, 0, 1, 0)
        cluster_list = [cluster_a, cluster_b, cluster_c, cluster_d]

        self.assertEqual(template.closest_pair_strip(cluster_list, 1.5, 1.0), (1.0, 1, 2))

    def test_closest_pair_strip_5(self):

        cluster_a = cluster.Cluster(set([]), 1.0, 1.0, 1, 0)
        cluster_b = cluster.Cluster(set([]), 1.0, 5.0, 1, 0)
        cluster_c = cluster.Cluster(set([]), 1.0, 4.0, 1, 0)
        cluster_d = cluster.Cluster(set([]), 1.0, 7.0, 1, 0)
        cluster_list = [cluster_a, cluster_b, cluster_c, cluster_d]

        self.assertEqual(template.closest_pair_strip(cluster_list, 1.5, 1.0), (1.0, 1, 2))

    def test_closest_pair_strip_6(self):
        self.assertEqual(template.closest_pair_strip([cluster.Cluster(set([]), 0.32, 0.16, 1, 0), cluster.Cluster(set([]), 0.39, 0.4, 1, 0), cluster.Cluster(set([]), 0.54, 0.8, 1, 0), cluster.Cluster(set([]), 0.61, 0.8, 1, 0), cluster.Cluster(set([]), 0.76, 0.94, 1, 0)], 0.46500000000000002, 0.070000000000000007), (float('inf'), -1, -1))

    def test_closest_pair_strip_7(self):
        self.assertEqual(template.closest_pair_strip([cluster.Cluster(set([]), 0, 0, 1, 0), cluster.Cluster(set([]), 0, 1, 1, 0), cluster.Cluster(set([]), 1, 0, 1, 0), cluster.Cluster(set([]), 1, 1, 1, 0)], 0.5, 1.0), (1.0, 0, 1))

    def test_slow_closest_pair_1(self):
        cluster_a = cluster.Cluster(set([1, 2, 3]), 100, 100, 1000, 1)
        cluster_b = cluster.Cluster(set([7]), 200, 400, 3000000, 6.1e-05)
        cluster_c = cluster.Cluster(set([8]), 202, 400, 3000000, 3.1e-05)
        cluster_list = [cluster_a, cluster_b, cluster_c]

        self.assertEqual(template.fast_closest_pair(cluster_list), (2.0, 1, 2))

    def test_fast_closest_pair_1(self):
        self.assertEqual(template.fast_closest_pair([cluster.Cluster(set([]), 0, 0, 1, 0), cluster.Cluster(set([]), 1, 0, 1, 0), cluster.Cluster(set([]), 2, 0, 1, 0), cluster.Cluster(set([]), 3, 0, 1, 0)]), (1.0, 0, 1))

    def test_fast_closest_pair_2(self):
        cluster_a = cluster.Cluster(set([1]), 2, 0, 1, 1)
        cluster_b = cluster.Cluster(set([2]), 0, 0, 2, 2)
        cluster_c = cluster.Cluster(set([3]), 5, 0, 1, 3)
        cluster_d = cluster.Cluster(set([4]), 3, 0, 1, 4)
        cluster_list = [cluster_a, cluster_b, cluster_c, cluster_d]

        self.assertEqual(template.fast_closest_pair(cluster_list), (1.0, 0, 3))

    def test_fast_closest_pair_2(self):
        cluster_b = cluster.Cluster(set([2]), 0, 0, 2, 2)
        cluster_a = cluster.Cluster(set([1]), 20, 0, 1, 1)
        cluster_c = cluster.Cluster(set([3]), 23, 0, 1, 3)
        cluster_d = cluster.Cluster(set([4]), 69, 0, 1, 4)
        cluster_e = cluster.Cluster(set([5]), 82, 0, 1, 4)
        cluster_list = [cluster_a, cluster_b, cluster_c, cluster_d, cluster_e]

        self.assertEqual(template.fast_closest_pair(cluster_list), (3.0, 0, 2))

    def test_hierarchical_clustering_1(self):
        cluster_a = cluster.Cluster(set([]), 0, 0, 1, 1)
        cluster_b = cluster.Cluster(set([]), 1, 0, 2, 2)
        cluster_c = cluster.Cluster(set([]), 2, 0, 1, 3)
        cluster_d = cluster.Cluster(set([]), 3, 0, 1, 4)
        cluster_list = [cluster_a, cluster_b, cluster_c, cluster_d]
        new_clusters = template.hierarchical_clustering(cluster_list, 3)

        self.assertEqual(new_clusters, [cluster_a, cluster_c, cluster_d])

    def test_hierarchical_clustering_2(self):
        cluster_a = cluster.Cluster(set([]), 0, 0, 1, 1)
        cluster_b = cluster.Cluster(set([]), 2, 0, 2, 2)
        cluster_c = cluster.Cluster(set([]), 3, 0, 1, 3)
        cluster_d = cluster.Cluster(set([]), 5, 0, 1, 4)
        cluster_list = [cluster_a, cluster_b, cluster_c, cluster_d]
        new_clusters = template.hierarchical_clustering(cluster_list, 3)

        self.assertEqual(new_clusters, [cluster_a, cluster_b, cluster_d])

    def test_hierarchical_clustering_2(self):
        cluster_a = cluster.Cluster(set([1]), 0, 0, 1, 1)
        cluster_b = cluster.Cluster(set([2]), 2, 0, 2, 2)
        cluster_c = cluster.Cluster(set([3]), 3, 0, 1, 3)
        cluster_d = cluster.Cluster(set([4]), 5, 0, 1, 4)
        cluster_list = [cluster_a, cluster_b, cluster_c, cluster_d]
        new_clusters = template.hierarchical_clustering(cluster_list, 2)

        self.assertEqual(new_clusters, [cluster_a, cluster_d])

    def test_hierarchical_clustering_3(self):
        cluster_a = cluster.Cluster(set([]), 2, 0, 1, 1)
        cluster_b = cluster.Cluster(set([]), 0, 0, 2, 2)
        cluster_c = cluster.Cluster(set([]), 3, 0, 1, 3)
        cluster_d = cluster.Cluster(set([]), 5, 0, 1, 4)
        cluster_list = [cluster_a, cluster_b, cluster_c, cluster_d]
        new_clusters = template.hierarchical_clustering(cluster_list, 3)

        self.assertEqual(new_clusters, [cluster_b, cluster_a, cluster_d])

    def test_kmeans_clustering_1(self):
        cluster_a = cluster.Cluster(set([1]), 0, 0, 1, 1)
        cluster_b = cluster.Cluster(set([2]), 1, 1, 2, 2)
        cluster_c = cluster.Cluster(set([3]), 2, 2, 1, 3)
        cluster_d = cluster.Cluster(set([4]), 3, 3, 1, 4)
        cluster_list = [cluster_a, cluster_b, cluster_c, cluster_d]
        new_clusters = template.kmeans_clustering(cluster_list, 4, 1)
        new_clusters.sort(key = lambda cluster: cluster.vert_center())

        answer = [cluster.Cluster(set([2]), 1.0, 1.0, 2, 2.0), cluster.Cluster(set([4]), 3.0, 3.0, 1, 4.0), cluster.Cluster(set([3]), 2.0, 2.0, 1, 3.0), cluster.Cluster(set([1]), 0.0, 0.0, 1, 1.0)]

        answer.sort(key = lambda cluster: cluster.vert_center())

        self.assertEqual(str(new_clusters), str(answer))

    def test_kmeans_clustering_2(self):
        cluster_a = cluster.Cluster(set([1]), 0, 0, 1, 1)
        cluster_b = cluster.Cluster(set([2]), 0.1, 0.1, 1, 1)
        cluster_c = cluster.Cluster(set([3]), 0.2, 0.2, 1, 4)
        cluster_d = cluster.Cluster(set([4]), 1, 1, 1, 4)
        cluster_e = cluster.Cluster(set([5]), 1.1, 1.1, 1, 2)
        cluster_list = [cluster_a, cluster_b, cluster_c, cluster_d, cluster_e]
        new_clusters = template.kmeans_clustering(cluster_list, 2, 2)
        new_clusters.sort(key = lambda cluster: cluster.vert_center())

        answer = [cluster.Cluster(set([4, 5]), 1.05, 1.05, 2, 3.0), cluster.Cluster(set([1, 2, 3]), 0.1, 0.1, 3, 2.0)]
        answer.sort(key = lambda cluster: cluster.vert_center())

        self.assertEqual(str(new_clusters), str(answer))


    def test_kmeans_clustering_3(self):
        cluster_a = cluster.Cluster(set([1]), 0, 0, 1, 1)
        cluster_b = cluster.Cluster(set([2]), 0.5, 0.5, 3, 1)
        cluster_c = cluster.Cluster(set([3]), 1.3, 1.3, 3, 3)
        cluster_d = cluster.Cluster(set([4]), 1.5, 1.5, 1, 4)
        cluster_list = [cluster_a, cluster_b, cluster_c, cluster_d]
        new_clusters = template.kmeans_clustering(cluster_list, 2, 4)
        new_clusters.sort(key = lambda cluster: cluster.vert_center())
        solution = set_of_county_tuples(new_clusters)

        answer = [cluster.Cluster(set([1, 2]), 0.25, 0.25, 2, 1.0), cluster.Cluster(set([3, 4]), 1.3, 1.3, 2, 3.5)]
        answer.sort(key = lambda cluster: cluster.vert_center())
        tuple_answer = set_of_county_tuples(answer)
        self.assertEqual(str(solution), str(tuple_answer))

    def test_kmeans_clustering_4(self):
        cluster_a = cluster.Cluster(set([1]), 0, 0, 1, 1)
        cluster_b = cluster.Cluster(set([2]), 1, 0, 2, 2)
        cluster_c = cluster.Cluster(set([3]), 1, 1, 1, 3)
        cluster_d = cluster.Cluster(set([4]), 3, 5, 1, 4)
        cluster_e = cluster.Cluster(set([5]), 3, 6, 1, 4)
        cluster_list = [cluster_a, cluster_b, cluster_c, cluster_d, cluster_e]
        new_clusters = template.kmeans_clustering(cluster_list, 2, 2)
        new_clusters.sort(key = lambda cluster: cluster.vert_center())

        answer = [cluster.Cluster(set([1, 2, 3]), 0.75, 0.25, 4, 2.0), cluster.Cluster(set([4, 5]), 3.0, 5.5, 2, 4.0)]
        answer.sort(key = lambda cluster: cluster.vert_center())

        self.assertEqual(str(new_clusters), str(answer))

    def test_kmeans_clustering_5(self):
        cluster_1 = cluster.Cluster(set([1]), 0, 0, 1, 1)
        cluster_2 = cluster.Cluster(set([2]), 10, 7, 1, 2)
        cluster_3 = cluster.Cluster(set([3]), 3, 7, 1, 3)
        cluster_4 = cluster.Cluster(set([4]), 1.2, 5, 1, 4)
        cluster_5 = cluster.Cluster(set([5]), 3.3, 6, 1, 4)
        cluster_6 = cluster.Cluster(set([6]), 0.3, 0.6, 1, 4)
        cluster_7 = cluster.Cluster(set([7]), 2.9, 6.4, 1, 4)
        cluster_8 = cluster.Cluster(set([8]), 139, 69, 1, 4)

        cluster_list = [cluster_1, cluster_2, cluster_3, cluster_4, cluster_5, cluster_6, cluster_7, cluster_8]
        new_clusters = template.kmeans_clustering(cluster_list, 4, 2)
        new_clusters.sort(key = lambda cluster: cluster.vert_center())
        result = set_of_county_tuples(new_clusters)

        answer = [cluster.Cluster(set([1, 6]), 0.15, 0.3, 2, 2.5), cluster.Cluster(set([3, 4, 5, 7]), 2.6, 6.1, 4, 3.75), cluster.Cluster(set([2]), 10.0, 7.0, 1, 2.0), cluster.Cluster(set([8]), 139.0, 69.0, 1, 4.0)]
        # answer.sort(key = lambda cluster: cluster.vert_center())

        expected_answer = set_of_county_tuples(answer)

        # self.assertEqual(str(new_clusters), str(answer))
        self.assertEqual(result, expected_answer)

    def test_kmeans_clustering_6(self):
        print
        print "Testing hierarchical_clustering on 24 county set"
        data_24_table = load_data_table(DATA_24_URL)
        cluster_list = []
        for idx in range(len(data_24_table)):
            line = data_24_table[idx]
            cluster_list.append(cluster.Cluster(set([line[0]]), line[1], line[2], line[3], line[4]))

        # alg_cluster.Cluster(set(['34017']), 909.08042421, 207.462937763, 608975, 9.1e-05)
        # alg_cluster.Cluster(set(['36061']), 911.072622034, 205.783086757, 1537195, 0.00015)

        # alg_cluster.Cluster(set(['34039']), 905.587082153, 210.045085725, 522541, 7.3e-05)
        # alg_cluster.Cluster(set(['34013']), 906.236730753, 206.977429459, 793633, 7.1e-05)
        new_clusters = template.kmeans_clustering(cluster_list, 15, 1)
        new_clusters.sort(key = lambda cluster: cluster.vert_center())

        result = set_of_county_tuples(new_clusters)
        solution = set([('34017', '36061'), ('06037',), ('06059',), ('36047',), ('36081',), ('06071', '08031'), ('36059',), ('36005',), ('55079',), ('34013', '34039'), ('06075',), ('01073',), ('06029',), ('41051', '41067'), ('11001', '24510', '51013', '51760', '51840', '54009')])

        for elem in result:
            if elem not in solution:
                print elem
                print "False"



    def test_kmeans_clustering_7(self):
        cluster_1 = cluster.Cluster(set(['1']), 909.08042421, 207.462937763, 608975, 9.1e-05) # 34017
        cluster_2 = cluster.Cluster(set(['2']), 911.072622034, 205.783086757, 1537195, 0.00015) # 36061

        cluster_3 = cluster.Cluster(set(['3']), 905.587082153, 210.045085725, 522541, 7.3e-05) # 34039
        cluster_4 = cluster.Cluster(set(['4']), 906.236730753, 206.977429459, 793633, 7.1e-05) # 34013

        # print "1"
        # print cluster_1.distance(cluster_2)
        # print cluster_1.distance(cluster_4)
        # print "2"
        # print cluster_2.distance(cluster_1)
        # print cluster_2.distance(cluster_3)
        # print cluster_2.distance(cluster_4)
        # print "3"
        # print cluster_3.distance(cluster_4)

        cluster_list = [cluster_1, cluster_2, cluster_3, cluster_4]

        result = template.kmeans_clustering(cluster_list, 2, 1)
        # print result


def set_of_county_tuples(cluster_list):
    """
    Input: A list of Cluster objects
    Output: Set of sorted tuple of counties corresponds to counties in each cluster
    """
    set_of_clusters = set([])
    for cluster in cluster_list:
        counties_in_cluster = cluster.fips_codes()

        # convert to immutable representation before adding to set
        county_tuple = tuple(sorted(list(counties_in_cluster)))
        set_of_clusters.add(county_tuple)
    return set_of_clusters

def load_data_table(data_url):
    """
    Import a table of county-based cancer risk data
    from a csv format file
    """
    data_file = urllib2.urlopen(data_url)
    data = data_file.read()
    data_lines = data.split('\n')
    print "Loaded", len(data_lines), "data points"
    data_tokens = [line.split(',') for line in data_lines]
    return [[tokens[0], float(tokens[1]), float(tokens[2]), int(tokens[3]), float(tokens[4])]
            for tokens in data_tokens]





def main():
    unittest.main()

if __name__ == '__main__':
    main()

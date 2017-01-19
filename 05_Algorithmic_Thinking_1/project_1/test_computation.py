import unittest
import graphs_to_test as graphs
import compute_functions as compute


class testComputeDegree(unittest.TestCase):

    def test_compute_in_degree(self):
        graph = graphs.GRAPH0
        self.assertEqual(compute.compute_in_degrees(graph), {0: 1, 1: 1, 2: 1, 3: 1})

    def test_compute_in_degree_2(self):
        graph = graphs.GRAPH1
        self.assertEqual(compute.compute_in_degrees(graph), {0: 4, 1: 0, 2: 0, 3: 0, 4: 0})

    def test_compute_in_degree_3(self):
        graph = graphs.GRAPH2
        self.assertEqual(compute.compute_in_degrees(graph), {0: 0, 1: 1, 2: 1, 3: 1, 4: 1})

    def test_compute_in_degree_4(self):
        graph = graphs.GRAPH3
        self.assertEqual(compute.compute_in_degrees(graph), {0: 4, 1: 4, 2: 4, 3: 4, 4: 4})

    def test_compute_in_degree_5(self):
        graph = graphs.GRAPH4
        self.assertEqual(compute.compute_in_degrees(graph), {'banana': 1, 'cat': 1, 'dog': 1, 'monkey': 0})

    def test_compute_in_degree_6(self):
        graph = graphs.GRAPH5
        self.assertEqual(compute.compute_in_degrees(graph), {1: 1, 2: 1, 3: 2, 4: 2, 5: 3, 6: 3, 7: 4, 8: 4})

    def test_compute_in_degree_7(self):
        graph = graphs.GRAPH6
        self.assertEqual(compute.compute_in_degrees(graph), {1: 2, 2: 2, 3: 1, 4: 3, 5: 2, 6: 2, 7: 2, 9: 2})

    def test_compute_in_degree_8(self):
        graph = graphs.GRAPH7
        self.assertEqual(compute.compute_in_degrees(graph), {0: 10, 1: 9, 2: 11, 3: 9, 4: 12, 5: 0, 6: 0, 7: 2, 8: 0, 9: 0, 10: 1, 11: 0, 12: 0, 13: 1, 14: 0})

    def test_compute_in_degree_9(self):
        graph = graphs.GRAPH8
        self.assertEqual(compute.compute_in_degrees(graph), {0: 16, 1: 11, 2: 5, 3: 3, 4: 2, 5: 1, 6: 1, 7: 2, 8: 2, 9: 0, 10: 0, 11: 0, 12: 0, 13: 0, 14: 1, 15: 0, 16: 0, 17: 1, 18: 0, 19: 0})


class testInDegreeDistribution(unittest.TestCase):

    def test_in_degree_distribution_1(self):
        graph = graphs.GRAPH0
        self.assertEqual(compute.in_degree_distribution(graph), {1: 4})

    def test_in_degree_distribution_2(self):
        graph = graphs.GRAPH1
        self.assertEqual(compute.in_degree_distribution(graph), {0: 4, 4: 1})

    def test_in_degree_distribution_3(self):
        graph = graphs.GRAPH2
        self.assertEqual(compute.in_degree_distribution(graph), {0: 1, 1: 4})

    def test_in_degree_distribution_4(self):
        graph = graphs.GRAPH3
        self.assertEqual(compute.in_degree_distribution(graph), {4: 5})

    def test_in_degree_distribution_5(self):
        graph = graphs.GRAPH4
        self.assertEqual(compute.in_degree_distribution(graph), {0: 1, 1: 3})

    def test_in_degree_distribution_6(self):
        graph = graphs.GRAPH5
        self.assertEqual(compute.in_degree_distribution(graph), {1: 2, 2: 2, 3: 2, 4: 2})

    def test_in_degree_distribution_7(self):
        graph = graphs.GRAPH6
        self.assertEqual(compute.in_degree_distribution(graph), {1: 1, 2: 6, 3: 1})

    def test_in_degree_distribution_8(self):
        graph = graphs.GRAPH7
        self.assertEqual(compute.in_degree_distribution(graph), {0: 7, 1: 2, 2: 1, 9: 2, 10: 1, 11: 1, 12: 1})

    def test_in_degree_distribution_9(self):
        graph = graphs.GRAPH8
        self.assertEqual(compute.in_degree_distribution(graph), {0: 9, 1: 4, 2: 3, 3: 1, 5: 1, 11: 1, 16: 1})


def main():
    unittest.main()

if __name__ == '__main__':
    main()

import unittest

import poc_distance as distance


class DistanceTests(unittest.TestCase):

    def testManhatanDistance1(self):
        p1 = (1, 1)
        p2 = (2, 3)
        self.assertEqual(distance.manhattan_distance(p1[0], p1[1], p2[0], p2[1]), 3)

    def testManhatanDistance2(self):
        p1 = (2, 3)
        p2 = (1, 1)
        self.assertEqual(distance.manhattan_distance(p1[0], p1[1], p2[0], p2[1]), 3)

    def testManhatanDistance3(self):
        p1 = (4, 8)
        p2 = (0, 0)
        self.assertEqual(distance.manhattan_distance(p1[0], p1[1], p2[0], p2[1]), 12)








def main():
    unittest.main()

if __name__ == '__main__':
    main()

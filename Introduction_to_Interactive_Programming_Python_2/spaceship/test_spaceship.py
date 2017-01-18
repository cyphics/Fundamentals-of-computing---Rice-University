import unittest
import math
import helper_functions as helper


class Tests(unittest.TestCase):

    def test_points_vector_1(self):
        self.assertEqual(helper.points_to_vector((0, 0), (1, 1)), (1, 1))

    def test_points_vector_2(self):
        self.assertEqual(helper.points_to_vector((1, 1), (0, 0)), (-1, -1))

    def test_fix_angle_1(self):
        self.assertEqual(helper.fix_angle(0), 0)

    def test_fix_angle_2(self):
        self.assertEqual(helper.fix_angle(math.pi), math.pi)

    def test_fix_angle_3(self):
        self.assertEqual(helper.fix_angle(2 * math.pi), 0)

    def test_fix_angle_4(self):
        self.assertEqual(helper.fix_angle(2), 2)

    def test_fix_angle_5(self):
        self.assertEqual(helper.fix_angle(5 * math.pi), math.pi)

    def test_fix_angle_6(self):
        self.assertEqual(helper.fix_angle(6 * math.pi), 0)

    def test_fix_angle_7(self):
        self.assertEqual(helper.fix_angle(-1), 5.283185307179586)

    def test_fix_angle_8(self):
        self.assertEqual(helper.fix_angle(-(math.pi / 2)), 3 * (math.pi / 2))

    def test_angle_to_vector_1(self):
        self.assertEqual(helper.angle_to_vector(0), (1, 0))

    def test_angle_to_vector_2(self):
        self.assertEqual(helper.angle_to_vector(math.pi), (-1, 1.2246467991473532e-16))

    def test_angle_to_vector_3(self):
        self.assertEqual(helper.angle_to_vector(2 * math.pi), (1, -2.4492935982947064e-16))

    def test_angle_to_vector_4(self):
        self.assertEqual(helper.angle_to_vector(math.pi / 2), (6.123233995736766e-17, 1))

    def test_angle_to_vector_5(self):
        self.assertEqual(helper.angle_to_vector(3 * math.pi / 2), (-1.8369701987210297e-16, -1))

    def test_vector_to_angle_1(self):
        self.assertEqual(helper.vector_to_angle((1, 0)), 0)

    def test_vector_to_angle_2(self):
        self.assertEqual(helper.vector_to_angle((1, 1)), math.pi / 4)

    def test_vector_to_angle_3(self):
        self.assertEqual(helper.vector_to_angle((2, 2)), math.pi / 4)

    def test_vector_to_angle_4(self):
        self.assertEqual(helper.vector_to_angle((0, 1)), math.pi / 2)

    def test_vector_to_angle_5(self):
        self.assertEqual(helper.vector_to_angle((0, 10)), math.pi / 2)

    def test_vector_to_angle_6(self):
        self.assertEqual(helper.vector_to_angle((0, -1)), 3 * math.pi / 2)


def main():
    unittest.main()

if __name__ == '__main__':
    main()

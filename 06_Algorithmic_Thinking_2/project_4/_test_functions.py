import unittest
import global_alignment
from matrix import ScoreMatrix


class testComputeGlobalAlignment(unittest.TestCase):


    def test_global_align_1(self):
        ALPHABET = "ACTG"
        sequence_a = "AC"
        sequence_b = "TAG"
        scoring_matrix = ScoreMatrix(ALPHABET)
        scoring_matrix.set_scoring(5, 2, -2, -4)
        result = global_alignment.ComputeGlobalAlignmentScores(sequence_a, sequence_b, scoring_matrix)
        printable = str(result)

        self.assertEqual(printable, "\n[0, -4, -8, -12]\n[-2, 2, 1, -3]\n[-4, 0, 4, 3]\n")

    def test_ComputeAlignment_1(self):
        ALPHABET = "ACTG"
        sequence_a = "AC"
        sequence_b = "TAG"

        scoring_matrix = ScoreMatrix(ALPHABET)
        scoring_matrix.set_scoring(5, 2, -2, -4)

        table = global_alignment.ComputeGlobalAlignmentScores(sequence_a, sequence_b, scoring_matrix)
        self.assertEqual(global_alignment.ComputeAlignment(sequence_a, sequence_b, scoring_matrix, table), ('-AC', 'TAG'))


def main():
    unittest.main()

if __name__ == '__main__':
    main()

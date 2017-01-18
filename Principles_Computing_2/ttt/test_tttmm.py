import unittest
#import poc_tttmm as ttt
import ttt_optimized as ttt
import poc_ttt_provided as provided

class Tests(unittest.TestCase):

    # def testOne(self):
    #     board = provided.TTTBoard(3, False, [[3, 2, 3], [2, 1, 3], [1, 1, 2]])
    #     print(board)
    #     print(ttt.mm_move(board, provided.PLAYERX))


    # def testTwo(self):
    #     print
    #     board = provided.TTTBoard(3, False, [[3, 1, 2], [3, 1, 1], [1, 1, 2]])
    #     print(board)
    #     print(ttt.mm_move(board, provided.PLAYERX))

    # def testThree(self):
    #     print
    #     board = provided.TTTBoard(3, False, [[3, 2, 2], [3, 1, 1], [1, 3, 1]])
    #     print(board)
    #     print(ttt.mm_move(board, provided.PLAYERX))

    # def testFour(self):
    #     print
    #     board = provided.TTTBoard(3, False, [[3, 2, 2], [3, 1, 2], [1, 3, 3]])
    #     print(board)
    #     print(ttt.mm_move(board, provided.PLAYERX))

    def test5(self):
        print
        board = provided.TTTBoard(3, False, [[3, 2, 1], [1, 1, 1], [1, 3, 1]])
        # print(board)
        # print(ttt.mm_move(board, provided.PLAYERX))
        self.assertEqual(ttt.mm_move(board, provided.PLAYERX), (0, (2, 0)))

    def test6(self):
        board = provided.TTTBoard(3, False, [[3, 2, 2], [2, 3, 3], [1, 3, 1]])
        print(board)
        self.assertEqual(ttt.mm_move(board, provided.PLAYERX), (0, (2, 2)))

    def test7(self):
        board = provided.TTTBoard(3, False, [[2, 3, 3], [3, 1, 2], [2, 1, 1]])
        # print(board)
        # print ttt.mm_move(board, provided.PLAYERX)  # , (0, (2, 2))
        self.assertEqual(ttt.mm_move(board, provided.PLAYERX), (1, (2, 2)))

    def test8(self):
        board = provided.TTTBoard(3, False, [[3, 2, 2], [2, 1, 1], [3, 1, 1]])
        # print(board)
        # print ttt.mm_move(board, provided.PLAYERO)
        self.assertEqual(ttt.mm_move(board, provided.PLAYERO), (-1, (2, 2)))

    def test9(self):
        board = provided.TTTBoard(2, False, [[provided.EMPTY, provided.EMPTY], [provided.EMPTY, provided.EMPTY]])
        # print(board)
        # print(ttt.mm_move(board, provided.PLAYERO))
        self.assertEqual(ttt.mm_move(board, provided.PLAYERO), (-1, (0, 0)))

    def test10(self):
        board = provided.TTTBoard(3, False, [[2, 1, 1], [1, 2, 3], [1, 1, 3]])
        # print board
        # print ttt.mm_move(board, provided.PLAYERO)
        self.assertEqual(ttt.mm_move(board, provided.PLAYERO), (-1, (0, 2)))

    def test11(self):
        board = provided.TTTBoard(3, False, [[2, 1, 1], [3, 3, 1], [1, 2, 1]])
        # print board
        # print ttt.mm_move(board, 2)
        self.assertEqual(ttt.mm_move(board, provided.PLAYERO), (-1, (1, 2)))



def main():
    unittest.main()

if __name__ == '__main__':
    main()

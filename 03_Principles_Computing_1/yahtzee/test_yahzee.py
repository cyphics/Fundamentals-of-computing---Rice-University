import unittest
import poc_yahtzee


class testYahtzee(unittest.TestCase):
    def test_expected_value_1(self):
        num_die_sides = 6
        held_dice = (3, 2, 2, 4, 1)
        num_free_dice = 5 - len(held_dice)
        self.assertEqual(poc_yahtzee.expected_value(held_dice, num_die_sides, num_free_dice), 4)

    def test_expected_value_2(self):
        num_die_sides = 6
        held_dice = (6, 6, 6, 6)
        num_free_dice = 5 - len(held_dice)
        self.assertEqual(poc_yahtzee.expected_value(held_dice, num_die_sides, num_free_dice), 25.0)

    def test_expected_value_3(self):
        num_die_sides = 6
        held_dice = (1, 1, 1, 1)
        num_free_dice = 5 - len(held_dice)
        self.assertEqual(poc_yahtzee.expected_value(held_dice, num_die_sides, num_free_dice), 4.666666666666667)

    def test_expected_value_4(self):
        num_die_sides = 6
        held_dice = ()
        num_free_dice = 5 - len(held_dice)
        self.assertEqual(poc_yahtzee.expected_value(held_dice, num_die_sides, num_free_dice), 8.753858024691358)

    def test_score_1(self):
        hand = tuple([])
        self.assertEqual(poc_yahtzee.score(hand), 0)

    def test_score_2(self):
        hand = tuple([2, 4])
        self.assertEqual(poc_yahtzee.score(hand), 4)

    def test_score_3(self):
        hand = tuple((3, 3, 3))
        self.assertEqual(poc_yahtzee.score(hand), 9)

    def test_score_4n(self):
        hand = tuple((1, 2, 2))
        self.assertEqual(poc_yahtzee.score(hand), 4)

    def test_score_5(self):
        hand = tuple([2, 3, 6])
        self.assertEqual(poc_yahtzee.score(hand), 6)

    def test_score_6(self):
        hand = tuple([6, 6, 5, 5, 5])
        self.assertEqual(poc_yahtzee.score(hand), 15)

    def test_gen_all_holds_1(self):
        hand = tuple([])
        self.assertEqual(poc_yahtzee.gen_all_holds(hand), set([()]), "Test #1:")

    def test_gen_all_holds_2(self):
        hand = tuple([2, 4])
        self.assertEqual(poc_yahtzee.gen_all_holds(hand), set([(), (2,), (4,), (2, 4)]), "Test #2:")

    def test_gen_all_holds_3(self):
        hand = tuple((3, 3, 3))
        self.assertEqual(poc_yahtzee.gen_all_holds(hand), set([(), (3,), (3, 3), (3, 3, 3)]), "Test #4:")

    def test_gen_all_holds_4(self):
        hand = tuple((1, 2, 2))
        self.assertEqual(poc_yahtzee.gen_all_holds(hand), set([(), (1,), (2,), (1, 2), (2, 2), (1, 2, 2)]), "Test #3:")

    def test_gen_all_holds_5(self):
        hand = tuple([2, 3, 6])
        self.assertEqual(poc_yahtzee.gen_all_holds(hand), set([(), (2,), (3,), (6,), (2, 3), (2, 6), (3, 6), (2, 3, 6)]), "Test #5:")



def main():
    unittest.main()

if __name__ == '__main__':
    main()

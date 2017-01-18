"""
Test suite for expected_velue in "Yahtzee"
"""

import poc_simpletest


def run_suite(expected_value):
    """
    Some informal testing code for expected_value
    """
    print("expected_value test suite:")

    # create a TestSuite object
    suite = poc_simpletest.TestSuite()

    num_die_sides = 6

    # test gen_all_holds on various inputs
    held_dice = (3, 2, 2, 4, 1)
    num_free_dice = 5 - len(held_dice)
    suite.run_test(expected_value(held_dice, num_die_sides, num_free_dice), 4, "Expected_Value #1:")

    held_dice = (6, 6, 6, 6)
    num_free_dice = 5 - len(held_dice)
    suite.run_test(expected_value(held_dice, num_die_sides, num_free_dice), 25.0, "Expected_Value #1:")

    held_dice = (1, 1, 1, 1)
    num_free_dice = 5 - len(held_dice)
    suite.run_test(expected_value(held_dice, num_die_sides, num_free_dice), 4.666666666666667, "Expected_Value #1:")

    held_dice = ()
    num_free_dice = 5 - len(held_dice)
    suite.run_test(expected_value(held_dice, num_die_sides, num_free_dice), 8.753858024691358, "Expected_Value #1:")


    suite.report_results()

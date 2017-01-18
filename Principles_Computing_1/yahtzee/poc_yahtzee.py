"""
Planner for Yahtzee
Simplifications:  only allow discard and roll, only score against upper level
"""

# Used to increase the timeout, if necessary
# import codeskulptor
# codeskulptor.set_timeout(20)


import poc_yahtzee_expected_value_testsuite
import poc_yahtzee_gen_all_holds_testsuite
import poc_yahtzee_score_testsuite
import poc_yahtzee_testsuite

def gen_all_sequences(outcomes, length):
    """
    Iterative function that enumerates the set of all sequences of
    outcomes of given length.
    """

    answer_set = set([()])
    for dummy_idx in range(length):
        temp_set = set()
        for partial_sequence in answer_set:
            for item in outcomes:
                new_sequence = list(partial_sequence)
                new_sequence.append(item)
                temp_set.add(tuple(new_sequence))
        answer_set = temp_set
    return answer_set


def gen_permutations(outcomes, length):
    """
    Iterative function that enumerates the set of all permutations of
    outcomes of given length
    """

    # Initialize set
    ans = set([()])
    # Iterate in length
    for dummy_idx in range(length):
        temp = set()
        # Take existing sequences
        for seq in ans:
            # Add outcome
            for item in outcomes:
                # If set does not contain item already
                if not set([item]).issubset(seq):
                    new_seq = list(seq)
                    new_seq.append(item)
                    temp.add(tuple(new_seq))
        ans = temp
    return ans


def gen_combinations(outcomes, lenght):
    """
    Function that returns all combinations
    from gen_permutations
    """
    permutations = gen_permutations(outcomes, lenght)
    commutations = [tuple(sorted(permutation)) for permutation in permutations]
    return set(commutations)


def gen_sorted_sequences(outcomes, length):
    """
    Function that creates all sorted sequences via gen_all_sequences
    """
    all_sequences = gen_all_sequences(outcomes, length)
    sorted_sequences = [tuple(sorted(sequence)) for sequence in all_sequences]
    return set(sorted_sequences)


def score(hand):
    """
    Takes a hand (tuple) and compute the maximal score for a Yahtzee
    hand according to the upper section of the Yahtzee score card.

    hand: full yahtzee hand

    Returns an integer score
    """
    # Sort hand because order does not count
    current_hand = sorted(list(hand))
    hand_score = 0
    for dice in current_hand:
        occurences = hand.count(dice)
        if dice * occurences > hand_score:
                hand_score = dice * occurences
#    return max([d_point * hand.count(d_point) for d_point in set(sorted(hand))])
    return hand_score


def expected_value(held_dice, num_die_sides, num_free_dice):
    """
    Compute the expected value based on held_dice given that there
    are num_free_dice to be rolled, each with num_die_sides.

    held_dice: dice that you will hold
    num_die_sides: number of sides on each die
    num_free_dice: number of dice to be rolled

    Returns a floating point expected value
    """
    current_expected_value = 0
    # Generate possible sequences from free dice
    possible_sequences = gen_all_sequences(list(range(1, num_die_sides + 1)), num_free_dice)
    # Score every sequence with current hold dice
    for sequence in possible_sequences:
        full_hand = list(held_dice + sequence)
        hand_score = score(full_hand)
        current_expected_value += hand_score
    return current_expected_value / float(len(possible_sequences))


def gen_all_holds(hand):
    """
    Generate all possible choices of dice from hand to hold.

    hand: full yahtzee hand

    Returns a set of tuples, where each tuple is dice to hold
    """
    all_holds = set([()])
    for dummy_idx in range(len(hand)):
        temp_set = set()
        for partial_sequence in all_holds:
            new_sequence = list(partial_sequence)
            new_sequence.append(hand[dummy_idx])
            temp_set.add(tuple(new_sequence))
        all_holds = all_holds.union(temp_set)
    return all_holds


def strategy(hand, num_die_sides):
    """
    Compute the hold that maximizes the expected value when the
    discarded dice are rolled.

    hand: full yahtzee hand
    num_die_sides: number of sides on each die

    Returns a tuple where the first element is the expected score and
    the second element is a tuple of the dice to hold
    """
    all_holds = gen_all_holds(hand)
    best_held_dice = ()
    best_value = 0
    for held_dice in all_holds:
        expected_value_for_hold = expected_value(held_dice, num_die_sides, len(hand) - len(held_dice))
        if expected_value_for_hold > best_value:
            best_value = expected_value_for_hold
            best_held_dice = held_dice

    return (best_value, best_held_dice)


def run_example():
    """
    Compute the dice to hold and expected score for an example hand
    """
    num_die_sides = 6
    hand = (1, 1, 1, 5, 6)
    hand_score, hold = strategy(hand, num_die_sides)
    print("Best strategy for hand", hand, "is to hold", hold, "with expected score", hand_score)


# run_example()

strategy((3, 3, 1, 2, 6), 6)
# poc_holds_testsuite.run_suite(gen_all_holds)
# import poc_yahtzee_score_testsuite
# import poc_yahtzee_expected_value_testsuite

# poc_yahtzee_score_testsuite.run_suite(score)
poc_yahtzee_expected_value_testsuite.run_suite(expected_value)
# poc_holds_testsuite.run_suite(gen_all_holds)

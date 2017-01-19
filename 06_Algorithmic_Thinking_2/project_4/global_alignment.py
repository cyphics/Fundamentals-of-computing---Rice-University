import helper_functions as helper
import project_4
from matrix import Matrix, ScoreMatrix

def ComputeGlobalAlignmentScores(seq_a, seq_b, scoring_matrix):
    global_matrix = Matrix(len(seq_b) + 1, len(seq_a) + 1)
    # Set first row
    for idx in range(len(seq_a)):
        previous = global_matrix.get_val(idx, 0)
        global_matrix.set_value(idx + 1, 0, previous + scoring_matrix.get_score_pair(seq_a[idx], "-"))

    for idx in range(len(seq_b)):
        previous = global_matrix.get_val(0, idx)
        global_matrix.set_value(0, idx + 1, previous + scoring_matrix.get_score_pair("-", seq_b[idx]))

    for idx1 in range(1, len(seq_a) + 1):
        for idx2 in range(1, len(seq_b) + 1):
            first = global_matrix.get_val(idx1 - 1, idx2 - 1) + scoring_matrix.get_score_pair(seq_a[idx1 - 1], seq_b[idx2 - 1])
            second = global_matrix.get_val(idx1 - 1, idx2) + scoring_matrix.get_score_pair(seq_a[idx1 - 1], "-")
            third = global_matrix.get_val(idx1, idx2 - 1) + scoring_matrix.get_score_pair("-", seq_b[idx2 - 1])
            max_value = max(first, second, third)


            global_matrix.set_value(idx1, idx2, max_value)
    return global_matrix

def ComputeLocalAlignmentScores(seq_a, seq_b, scoring_matrix):
    global_matrix = Matrix(len(seq_b) + 1, len(seq_a) + 1)
    # Set first row
    for idx in range(len(seq_a)):
        global_matrix.set_value(idx + 1, 0, 0)

    for idx in range(len(seq_b)):
        global_matrix.set_value(0, idx + 1, 0)

    for idx1 in range(1, len(seq_a) + 1):
        for idx2 in range(1, len(seq_b) + 1):
            first = global_matrix.get_val(idx1 - 1, idx2 - 1) + scoring_matrix.get_score_pair(seq_a[idx1 - 1], seq_b[idx2 - 1])
            second = global_matrix.get_val(idx1 - 1, idx2) + scoring_matrix.get_score_pair(seq_a[idx1 - 1], "-")
            third = global_matrix.get_val(idx1, idx2 - 1) + scoring_matrix.get_score_pair("-", seq_b[idx2 - 1])
            max_value = max(first, second, third)
            if max_value < 0:
                max_value = 0

            global_matrix.set_value(idx1, idx2, max_value)

    return global_matrix


def ComputeAlignment(seq_a, seq_b, score_matrix, table):
    length_a = len(seq_a)
    length_b = len(seq_b)

    a_prime = ""
    b_prime = ""

    while length_a > 0 and length_b > 0:
        if table.get_val(length_a, length_b) == table.get_val(length_a - 1, length_b - 1) + score_matrix.get_score_pair(seq_a[length_a - 1], seq_b[length_b - 1]):
            a_prime = seq_a[length_a - 1] + a_prime
            b_prime = seq_b[length_b - 1] + b_prime
            length_a -= 1
            length_b -= 1
        else:
            if table.get_val(length_a, length_b) == table.get_val(length_a - 1, length_b) + score_matrix.get_score_pair(seq_a[length_a - 1], "-"):
                a_prime = seq_a[length_a - 1] + a_prime
                b_prime = "-" + b_prime
                length_a -= 1
            else:
                b_prime = seq_b[length_b - 1] + b_prime
                a_prime = "-" + a_prime
                length_b -= 1

    while length_a > 0:
        a_prime = seq_a[length_a - 1] + a_prime
        b_prime = "-" + b_prime
        length_a -= 1

    while length_b > 0:
        b_prime = seq_b[length_b - 1] + b_prime
        a_prime = "-" + a_prime
        length_b -= 1

    return a_prime, b_prime


def ComputeLocalAlignment(seq_a, seq_b, score_matrix, table):
    a_prime = ""
    b_prime = ""

    # Find biggest value in table:
    starting_point = [float('-inf'), -1, -1]
    for idx1 in range(len(seq_a) + 1):
        for idx2 in range(len(seq_b) + 1):
            starting_point = max(starting_point, [table.get_val(idx1, idx2), idx1, idx2])

    length_a = starting_point[1]
    length_b = starting_point[2]

    while length_a > 0 and length_b > 0:
        if table.get_val(length_a, length_b) == table.get_val(length_a - 1, length_b - 1) + score_matrix.get_score_pair(seq_a[length_a - 1], seq_b[length_b - 1]):
            a_prime = seq_a[length_a - 1] + a_prime
            b_prime = seq_b[length_b - 1] + b_prime
            length_a -= 1
            length_b -= 1
        else:
            if table.get_val(length_a, length_b) == table.get_val(length_a - 1, length_b) + score_matrix.get_score_pair(seq_a[length_a - 1], "-"):
                a_prime = seq_a[length_a - 1] + a_prime
                b_prime = "-" + b_prime
                length_a -= 1
            else:
                b_prime = seq_b[length_b - 1] + b_prime
                a_prime = "-" + a_prime
                length_b -= 1
        if table.get_val(length_a, length_b) == 0:
            return a_prime, b_prime

    while length_a > 0:
        a_prime = seq_a[length_a - 1] + a_prime
        b_prime = "-" + b_prime
        length_a -= 1

    while length_b > 0:
        b_prime = seq_b[length_b - 1] + b_prime
        a_prime = "-" + a_prime
        length_b -= 1

    return a_prime, b_prime


def generateGlobalAlignment(first, second):
    string_a = first
    string_b = second
    all_a_dash = set([string_a])
    all_b_dash = set([string_b])
    final_set = set([])

    for _ in range(len(string_b)):
        temp_set = set([])
        for word in all_a_dash:
            for idx in range(len(string_a) + 1):
                new_string = word[:idx] + "_" + word[idx:]
                temp_set.add(new_string)
        all_a_dash = all_a_dash.union(temp_set)

    for _ in range(len(string_a)):
        temp_set = set([])
        for word in all_b_dash:
            for idx in range(len(string_b) + 1):
                new_string = word[:idx] + "_" + word[idx:]
                temp_set.add(new_string)
        all_b_dash = all_b_dash.union(temp_set)

    # Compare
    store = True
    for a_word in all_a_dash:
        for b_word in all_b_dash:
            if len(a_word) == len(b_word):
                store = True
                for idx in range(len(a_word)):
                    if a_word[idx] == "_" and b_word[idx] == "_":
                        store = False
                if store:
                    final_set.add((a_word, b_word))
    return final_set

""" Project 4"""

def build_scoring_matrix(alpha, diag_score, off_diag_score, dash_score):
    """ Take an alphabet, the separated scores, and return
    the scoring matrix"""
    a_alphabet = set(alpha)
    a_alphabet.add("-")
    a_matrix = {}
    for letter in a_alphabet:
        a_matrix[letter] = 0
    for key in a_matrix:
        intern_dict = {}
        for letter in a_alphabet:
            if letter == key:
                intern_dict[letter] = diag_score
            else:
                intern_dict[letter] = off_diag_score
            if letter == "-":
                intern_dict[letter] = dash_score
            elif key == "-":
                intern_dict[letter] = dash_score
        a_matrix[key] = intern_dict
    # a_matrix["-"]["-"] = float('inf')
    return a_matrix


def compute_alignment_matrix(seq_x, seq_y, score_matrix, global_flag):
    """ Take two sequences and a score matrix and a flag
    Returns the global/local alignment table """
    alignment_matrix = [[0 for _ in range(len(seq_y) + 1)] for _ in range(len(seq_x) + 1) ]
    # Set first row
    for idx in range(len(seq_x)):
        previous = alignment_matrix[idx][0]
        if global_flag:
            alignment_matrix[idx + 1][0] = previous + score_matrix[seq_x[idx]]["-"]
        else:
            alignment_matrix[idx + 1][0] = 0
    for idx in range(len(seq_y)):
        previous = alignment_matrix[0][idx]
        if global_flag:
            alignment_matrix[0][idx + 1] = previous + score_matrix["-"][seq_y[idx]]
        else:
            alignment_matrix[0][idx + 1] = 0
    for idx1 in range(1, len(seq_x) + 1):
        for idx2 in range(1, len(seq_y) + 1):
            first = alignment_matrix[idx1 - 1][idx2 - 1] + score_matrix[seq_x[idx1 - 1]][seq_y[idx2 - 1]]
            second = alignment_matrix[idx1 - 1][idx2] + score_matrix[seq_x[idx1 - 1]]["-"]
            third = alignment_matrix[idx1][idx2 - 1] + score_matrix["-"][seq_y[idx2 - 1]]
            max_value = max(first, second, third)

            if not global_flag:
                if max_value < 0:
                    max_value = 0

            alignment_matrix[idx1][idx2] = max_value

    # for idx in range(len(seq_x)):
    #     for idx2 in range(len(seq_y)):
    #         pass
    return alignment_matrix


def compute_global_alignment(seq_x, seq_y, score_matrix, table):
    """ Take two sequences, a score matrix and an alignment table
    and returns the best global alignment"""
    length_a = len(seq_x)
    length_b = len(seq_y)

    a_prime = ""
    b_prime = ""

    while length_a > 0 and length_b > 0:
        if table[length_a][length_b] == table[length_a - 1][length_b - 1] + score_matrix[seq_x[length_a - 1]][seq_y[length_b - 1]]:
            a_prime = seq_x[length_a - 1] + a_prime
            b_prime = seq_y[length_b - 1] + b_prime
            length_a -= 1
            length_b -= 1
        else:
            if table[length_a][length_b] == table[length_a - 1][length_b] + score_matrix[seq_x[length_a - 1]]["-"]:
                a_prime = seq_x[length_a - 1] + a_prime
                b_prime = "-" + b_prime
                length_a -= 1
            else:
                b_prime = seq_y[length_b - 1] + b_prime
                a_prime = "-" + a_prime
                length_b -= 1

    while length_a > 0:
        a_prime = seq_x[length_a - 1] + a_prime
        b_prime = "-" + b_prime
        length_a -= 1

    while length_b > 0:
        b_prime = seq_y[length_b - 1] + b_prime
        a_prime = "-" + a_prime
        length_b -= 1

    return table[-1][-1], a_prime, b_prime


def compute_local_alignment(seq_x, seq_y, score_matrix, table):
    """ Take two sequences, a score matrix and an alignment table
    and returs the score of the best alignment, with the two corresponding
    sequences"""

    a_prime = ""
    b_prime = ""

    # Find biggest value in table:
    starting_point = [float('-inf'), -1, -1]
    for idx1 in range(len(seq_x) + 1):
        for idx2 in range(len(seq_y) + 1):
            starting_point = max(starting_point, [table[idx1][idx2], idx1, idx2])
    length_a = starting_point[1]
    length_b = starting_point[2]

    while length_a > 0 and length_b > 0:
        if table[length_a][length_b] == table[length_a - 1][length_b - 1] + score_matrix[seq_x[length_a - 1]][seq_y[length_b - 1]]:
            a_prime = seq_x[length_a - 1] + a_prime
            b_prime = seq_y[length_b - 1] + b_prime
            length_a -= 1
            length_b -= 1
        else:
            if table[length_a][length_b] == table[length_a - 1][length_b] + score_matrix[seq_x[length_a - 1]]["-"]:
                a_prime = seq_x[length_a - 1] + a_prime
                b_prime = "-" + b_prime
                length_a -= 1
            else:
                b_prime = seq_y[length_b - 1] + b_prime
                a_prime = "-" + a_prime
                length_b -= 1
        if table[length_a][length_b] == 0:
            return starting_point[0], a_prime, b_prime

    while length_a > 0:
        a_prime = seq_x[length_a - 1] + a_prime
        b_prime = "-" + b_prime
        length_a -= 1
        if table[length_a][length_b] == 0:
            return starting_point[0], a_prime, b_prime

    while length_b > 0:
        b_prime = seq_y[length_b - 1] + b_prime
        a_prime = "-" + a_prime
        length_b -= 1
        if table[length_a][length_b] == 0:
            return starting_point[0], a_prime, b_prime

    return starting_point[0], a_prime, b_prime




# if __name__ == "__main__":
#     alphabet = "abcd"
#     seq_a = "abd"
#     seq_b = "ab"
#     scoring_matrix = build_scoring_matrix(alphabet, 5, 2, -2)
#     for entry in scoring_matrix:
#         print entry, scoring_matrix[entry]

#     align_matrix = compute_alignment_matrix(seq_a, seq_b, scoring_matrix, False)

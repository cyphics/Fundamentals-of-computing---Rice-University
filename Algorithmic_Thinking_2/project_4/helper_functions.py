from matrix import Matrix

def genScoringMatrix(size, equal_score, align_score, x_dash, y_dash):
    matrix_size = size
    equality_score = equal_score
    alignment_score = align_score
    x_dash_score = x_dash
    y_dash_score = y_dash

    a_matrix = Matrix(matrix_size, matrix_size)

    for idx in range(matrix_size):
        for idx_2 in range(matrix_size):
            if idx != idx_2:
                a_matrix.set_value(idx, idx_2, alignment_score)
    for idx in range(matrix_size):
        a_matrix.set_value(idx, matrix_size - 1, x_dash_score)
        a_matrix.set_value(matrix_size - 1, idx, y_dash_score)

        a_matrix.set_value(idx, idx, 5)
    a_matrix.set_value(-1, -1, float('inf'))
    return a_matrix


if __name__ == "__main__":
    a_matrix = genScoringMatrix(5, 5, 2, -2, -4)
    print a_matrix

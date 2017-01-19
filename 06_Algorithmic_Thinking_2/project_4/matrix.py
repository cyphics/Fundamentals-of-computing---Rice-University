class Matrix:
    def __init__(self, width, height):
        self._matrix = [[0 for idx in range(width)] for idx2 in range(height)]

    def __str__(self):
        result = "\n"
        for line in self._matrix:
            result +=  str(line) + "\n"
        return result

    def set_value(self, x, y, value):
        self._matrix[x][y] = value

    def get_val(self, x, y):
        return self._matrix[x][y]


class ScoreMatrix(Matrix):
    def __init__(self, alphabet):
        self._alphabet = alphabet
        self._alphabet += "-"
        self._size = len(self._alphabet)
        Matrix.__init__(self, self._size + 1, self._size + 1)
        for idx in range(1, self._size + 1):
            self._matrix[idx][0] = self._alphabet[idx - 1]
            self._matrix[0][idx] = self._alphabet[idx - 1]

    def set_scoring(self, iden, overlap, x_dash, y_dash):
        self._equal_score = iden
        self._align_score = overlap
        self._x_dash_score = x_dash
        self._y_dash_score = y_dash
        self.set_value(0, 0, "+")
        for idx in range(1, self._size + 1):
            for idx_2 in range(1, self._size + 1):
                if idx != idx_2:
                    self.set_value(idx, idx_2, self._align_score)
        for idx in range(1, self._size + 1):
            self.set_value(idx, self._size , self._x_dash_score)
            self.set_value(self._size, idx, self._y_dash_score)

            self.set_value(idx, idx, self._equal_score)
        self.set_value(-1, -1, float('inf'))


    def get_score_pair(self, first, second):
        for idx1 in range(self._size + 1):
            if self.get_val(idx1, 0) == first:
                for idx2 in range(self._size + 1):
                    if self.get_val(0, idx2) == second:
                        return self.get_val(idx1, idx2)
        print "ERROR, bad score search"





if __name__ == "__main__":
    # a_matrix = Matrix(4, 5)
    # a_matrix.set_value(1, 1, 3)
    # print a_matrix
    # print a_matrix.get_val(1, 1)
    # print a_matrix.get_val(0, 0)

    alphabet = "ABCD"
    a_score_matrix = ScoreMatrix(alphabet)
    a_score_matrix.set_scoring(5, 2, -2, -4)
    print a_score_matrix

    print a_score_matrix.get_score_pair("D", "D")

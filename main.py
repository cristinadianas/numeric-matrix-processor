ADD_MATRICES = 1
SCALE_MATRIX = 2
MULTIPLY_MATRICES = 3
TRANSPOSE_MATRIX = 4
CALCULATE_DETERMINANT = 5
INVERSE_MATRIX = 6

MAIN_DIAGONAL = 1
SIDE_DIAGONAL = 2
VERTICAL_LINE = 3
HORIZONTAL_LINE = 4

operations = """1. Add matrices
2. Multiply matrix by a constant
3. Multiply matrices
4. Transpose matrix
5. Calculate a determinant
6. Inverse matrix
0. Exit"""
transpositions = """1. Main diagonal
2. Side diagonal
3. Vertical line
4. Horizontal line"""


def get_user_choice(options):
    print(options)
    return int(input("Your choice: "))


def get_matrix_info(ordinal_number_word=""):
    rows, cols = [int(n) for n in input(f"Enter size of {ordinal_number_word}matrix: ").split()]

    print(f"Enter {ordinal_number_word}matrix:")
    values = []
    for row in range(rows):
        values.append([])
        for num in input().split():
            values[row].append(float(num) if "." in num else int(num))

    return rows, cols, values


class Matrix:
    def __init__(self, y_max, x_max, values=None):
        self.y_max = y_max
        self.x_max = x_max
        if values:
            self.values = values
        else:
            self.values = [[0 for _ in range(x_max)] for _ in range(y_max)]

    def print_matrix(self):
        if self.values:
            print("The result is: ")
            for y in range(self.y_max):
                print(*self.values[y])
        else:
            print("This operation cannot be performed.")

    def is_square(self):
        return self.y_max == self.x_max

    def add_matrices(self, matrix2):
        if self.y_max == matrix2.y_max and self.x_max == matrix2.x_max:
            result = Matrix(self.y_max, self.x_max)

            for y in range(result.y_max):
                for x in range(result.x_max):
                    result.values[y][x] = self.values[y][x] + matrix2.values[y][x]

            return result

    def scale_matrix(self, scalar):
        result = Matrix(self.y_max, self.x_max)

        for y in range(result.y_max):
            for x in range(result.x_max):
                result.values[y][x] = scalar * self.values[y][x]

        return result

    def multiply_matrices(self, matrix2):
        if self.x_max == matrix2.y_max:
            result = Matrix(self.y_max, matrix2.x_max)

            for y in range(result.y_max):
                for x in range(result.x_max):
                    for idx in range(self.x_max):
                        result.values[y][x] += self.values[y][idx] * matrix2.values[idx][x]

            return result

    def transpose_matrix(self, transp_type=MAIN_DIAGONAL):
        if transp_type == MAIN_DIAGONAL:
            result = Matrix(self.x_max, self.y_max)
            for y in range(result.y_max):
                for x in range(result.x_max):
                    result.values[y][x] = self.values[x][y]
            return result

        elif transp_type == SIDE_DIAGONAL:
            result = Matrix(self.x_max, self.y_max)
            for y in range(result.y_max):
                for x in range(result.x_max):
                    result.values[y][x] = self.values[self.x_max - x - 1][self.y_max - y - 1]
            return result

        elif transp_type == VERTICAL_LINE:
            result = Matrix(self.y_max, self.x_max)
            for y in range(result.y_max):
                for x in range(result.x_max):
                    result.values[y][x] = self.values[y][result.x_max - x - 1]
            return result

        elif transp_type == HORIZONTAL_LINE:
            result = Matrix(self.y_max, self.x_max)
            for y in range(result.y_max):
                for x in range(result.x_max):
                    result.values[y][x] = self.values[result.y_max - y - 1][x]
            return result

    def minor_matrix(self, del_row, del_col):
        if del_row < self.x_max and del_col < self.y_max:
            result = []

            for row in self.values:
                result.append(row[:del_col] + row[del_col + 1:])

            result = result[:del_row] + result[del_row + 1:]

            return Matrix(self.y_max - 1, self.x_max - 1, result)

        else:
            print("An error has occured.")

    def determinant(self):
        if not self.is_square():
            return "This operation cannot be performed."

        if self.y_max == 1:
            return self.values[0][0]

        determinant = 0
        for y, row in enumerate(self.values):
            minor = self.minor_matrix(y, 0)
            cofactor = (-1) ** y * minor.determinant()
            determinant += row[0] * cofactor
        return determinant

    def adjoint_matrix(self):
        if self.is_square():
            result = Matrix(self.y_max, self.x_max)

            for y, row in enumerate(self.values):
                for x, col in enumerate(self.values[y]):
                    result.values[y][x] = (-1) ** (y + x) * self.minor_matrix(y, x).determinant()

            return result.transpose_matrix()

    def inverse_matrix(self):
        determinant = self.determinant()
        if self.is_square() and determinant != 0:
            return self.adjoint_matrix().scale_matrix(1 / determinant)


operation = get_user_choice(operations)

while operation:
    if operation == ADD_MATRICES:
        matrix_1 = Matrix(*get_matrix_info("first "))
        matrix_2 = Matrix(*get_matrix_info("second "))
        Matrix.add_matrices(matrix_1, matrix_2).print_matrix()

    elif operation == SCALE_MATRIX:
        matrix = Matrix(*get_matrix_info())
        constant = int(input("Enter constant: "))
        matrix.scale_matrix(constant).print_matrix()

    elif operation == MULTIPLY_MATRICES:
        matrix_1 = Matrix(*get_matrix_info("first "))
        matrix_2 = Matrix(*get_matrix_info("second "))
        Matrix.multiply_matrices(matrix_1, matrix_2).print_matrix()

    elif operation == TRANSPOSE_MATRIX:
        transposition_type = get_user_choice(transpositions)
        matrix = Matrix(*get_matrix_info())
        matrix.transpose_matrix(transposition_type).print_matrix()

    elif operation == CALCULATE_DETERMINANT:
        matrix = Matrix(*get_matrix_info())
        print(matrix.determinant())

    elif operation == INVERSE_MATRIX:
        matrix = Matrix(*get_matrix_info())
        matrix.inverse_matrix().print_matrix()

    print()
    operation = get_user_choice(operations)

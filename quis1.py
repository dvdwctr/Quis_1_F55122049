class MatrixOperations:
    def __init__(self, matrix):
        self.matrix = matrix

    def find_min_max(self):
        min_val = min(min(row) for row in self.matrix)
        max_val = max(max(row) for row in self.matrix)
        return min_val, max_val

    def transpose(self):
        transpose_matrix = [[self.matrix[j][i] for j in range(len(self.matrix))] for i in range(len(self.matrix[0]))]
        return transpose_matrix

    def multiply(self, other_matrix):
        if len(self.matrix[0]) != len(other_matrix):
            raise ValueError("Ukuran matrix tidak sesuai untuk perkalian")

        result = [[0 for _ in range(len(other_matrix[0]))] for _ in range(len(self.matrix))]

        for i in range(len(self.matrix)):
            for j in range(len(other_matrix[0])):
                for k in range(len(other_matrix)):
                    result[i][j] += self.matrix[i][k] * other_matrix[k][j]

        return result

    def add(self, other_matrix):
        if len(self.matrix) != len(other_matrix) or len(self.matrix[0]) != len(other_matrix[0]):
            raise ValueError("Ukuran matrix tidak sesuai untuk penjumlahan")

        result = [[0 for _ in range(len(self.matrix[0]))] for _ in range(len(self.matrix))]

        for i in range(len(self.matrix)):
            for j in range(len(self.matrix[0])):
                result[i][j] = self.matrix[i][j] + other_matrix[i][j]

        return result


if __name__ == "__main__":
    matrix_A = [
        [34, 100, 12],
        [72, 24, 55],
        [61, 20, 19]
    ]

    matrix_operations = MatrixOperations(matrix_A)

    # Menghitung elemen terbesar dan terkecil
    min_val, max_val = matrix_operations.find_min_max()
    print("Elemen terbesar:", max_val)
    print("Elemen terkecil:", min_val)

    # Transpose matrix
    transpose_matrix = matrix_operations.transpose()
    print("Transpose matrix:")
    for row in transpose_matrix:
        print(row)

    # Menghitung perkalian matrix dengan transpose matrix
    matrix_B = transpose_matrix
    product_matrix = matrix_operations.multiply(matrix_B)
    print("Hasil perkalian matrix:")
    for row in product_matrix:
        print(row)

    # Menghitung penjumlahan matrix dengan transpose matrix
    sum_matrix = matrix_operations.add(matrix_B)
    print("Hasil penjumlahan matrix:")
    for row in sum_matrix:
        print(row)
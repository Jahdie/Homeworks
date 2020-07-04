# Реализовать класс Matrix (матрица). Обеспечить перегрузку конструктора класса (метод __init__()), который должен
# принимать данные (список списков) для формирования матрицы.
# Следующий шаг — реализовать перегрузку метода __str__() для вывода матрицы в привычном виде.
# Далее реализовать перегрузку метода __add__() для реализации операции сложения двух объектов класса Matrix
# (двух матриц). Результатом сложения должна быть новая матрица.
class Matrix:
    def __init__(self, matrix_list):
        self.matrix_list = matrix_list

    def __str__(self):
        format_list = self.matrix_list
        for index_1 in range(len(self.matrix_list)):
            for index_2 in range(len(self.matrix_list[index_1])):
                format_list[index_1][index_2] = str(self.matrix_list[index_1][index_2])
        matrix_string = ''
        for element in format_list:
            string = " ".join(element) + "\n"
            matrix_string = matrix_string + string
        return f"{matrix_string}"

    def __add__(self, other):
        matrix_sum = self.matrix_list
        for index_1 in range(len(self.matrix_list)):
            for index_2 in range(len(self.matrix_list[index_1])):
                sum_elements_matrix = int(other.matrix_list[index_1][index_2]) + int(self.matrix_list[index_1][index_2])
                matrix_sum[index_1][index_2] = sum_elements_matrix

        return Matrix(matrix_sum)


my_matrix_1 = Matrix([[1, 2, 3, 4], [5, 6, 7, 8], [1, 2, 3, 4]])
my_matrix_2 = Matrix([[9, 10, 11, 12], [13, 14, 15, 16], [3, 4, 5, 6]])

print(f"{my_matrix_1}+\n{my_matrix_2}=\n{my_matrix_1 + my_matrix_2}")

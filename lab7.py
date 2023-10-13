# Дана квадратная матрица. Сформировать все возможные варианты данной матрицы путем
# перестановки строк и столбцов, в которых диагональный элемент равен нулю.
# + сумма элементов сторки с диагональным элементом равным нулю не должна быть больше размера матрицы уноженного на 5
# + переставляем только четные столбцы и строки


import random
import copy


class Matrix:
    def __init__(self, n):
        self.count = [0]
        self.number_check(n)
        if n == 1:
            self.matrix = [[1, 0, 1, 0, 1],
                      [1, 0, 1, 0, 1],
                      [1, 0, 0, 0, 1],
                      [1, 0, 1, 0, 1],
                      [1, 0, 1, 0, 1]]
            self.n = 5
        else:
            while True:
                matrix = [[random.randint(0, 10) for _ in range(n)] for _ in range(n)]
                for i in range(n):
                    if matrix[i][i] == 0 or matrix[i][n - 1 - i] == 0:
                        break

    def number_check(self, n):
        while True:
            try:
                k = int(n)
                if k > 0:
                    break
                else:
                    print('Введенное число отрицательное.')

            except ValueError:
                print('Введенное значение не является числом.')

    def print_matrix(self):
        print()
        for row in self.matrix:
            for elem in row:
                print('{:4}'.format(elem), end=' ')
            print()
        print()

    def check_2(self, matrix, row):
        if sum(matrix[row]) > len(matrix) * 5:
            return False
        else:
            return True


    def F_rec(self, row=0, column=0, exist=[[], []]):
        if row == len(self.matrix):
            return
        self.F_rec(row + 1, column + 1)
        if self.check_2(self.matrix, row):
            if self.matrix[row][row] == 0 and row % 2 != 0 and row not in exist[0] :
                exist[0].append(row)
                new_matrix = copy.deepcopy(self.matrix)
                for i in range(len(self.matrix)):
                    new_matrix[row][i], new_matrix[i][column] = new_matrix[i][column], new_matrix[row][i]
                self.print_matrix()
                self.count[0] += 1
            if self.matrix[row][self.n - 1 - row] == 0 and row % 2 != 0 and row != len(self.matrix) // 2 and row not in exist[1]:
                exist[1].append(row)
                new_matrix = copy.deepcopy(self.matrix)
                for i in range(len(self.matrix)):
                    new_matrix[row][i], new_matrix[self.n - 1 - i][self.n - 1 - column] = new_matrix[self.n - 1 - i][self.n - 1 - column],  new_matrix[row][i]
                self.print_matrix()
                self.count[0] += 1
            self.F_rec(row + 1, column + 1, exist)
        else:
            self.F_rec(row + 1, column + 1, exist)


    def F_iter(self):
        count = 0
        exist = [[], []]
        stack = [(copy.deepcopy(self.matrix), 0, 0)]
        k = self.n - 1
        while stack:
            matrix, row, column = stack.pop()
            if row == len(matrix):
                count += 1
                continue
            stack.append((matrix, row + 1, column + 1))
            if self.check_2(matrix, row):
                if matrix[row][row] == 0 and row % 2 != 0 and row not in exist[0]:
                    exist[0].append(row)
                    new_matrix = copy.deepcopy(matrix)
                    for i in range(len(matrix)):
                        new_matrix[row][i], new_matrix[i][column] = new_matrix[i][column], new_matrix[row][i]
                    self.print_matrix()
                    stack.append((matrix, row + 1, column + 1))
                if matrix[row][k - row] == 0 and row % 2 != 0 and row != len(matrix) // 2 and row not in exist[1]:
                    exist[1].append(row)
                    new_matrix = copy.deepcopy(matrix)
                    for i in range(len(matrix)):
                        new_matrix[row][i], new_matrix[k - i][k - column] = new_matrix[k - i][k - column],  new_matrix[row][i]
                    self.print_matrix()
                    stack.append((matrix, row + 1, column + 1))
            else:
                if matrix[row][row] == 0 and row not in exist[0]:
                    print('сумма элементов строки ' + str(row) + ' оказалась больше размера матрицы * 5')
                if matrix[row][k - row] == 0 and row != len(matrix) // 2 and row not in exist[1]:
                    print('сумма элементов строки ' + str(row) + ' оказалась больше размера матрицы * 5')
        print('Общее количество вариантов: ', count - 1)




if input('Напишите 1 для запуска тестовой матрицы или ничего для случайной: ') == '1':
    mat = Matrix(1)
else:
    mat = Matrix(int(input('Размер матрицы: ')))
print('Начальная матрица:')
mat.print_matrix()

print('Рекурсивный перебор возможных вариантов.')
mat.F_rec()
print('Общее количество вариантов: ', mat.count[0])

print('Итеративный перебор возможных вариантов.')
mat.F_iter()


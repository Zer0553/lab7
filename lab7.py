# Дана квадратная матрица. Сформировать все возможные варианты данной матрицы путем
# перестановки строк и столбцов, в которых диагональный элемент равен нулю.
# + сумма элементов сторки с диагональным элементом равным нулю не должна быть больше размера матрицы уноженного на 5
# + переставляем только четные столбцы и строки


import random
import copy


class Program:
    def __init__(self):
        self.row_column = number_check('Введите ширину и высоту массива: ')
        while(True):
            handler_name = input('Введите желаемый тип перебора массива (rec, iter): ')
            if handler_name == 'rec':
                self.handler = RecursiveHandler()
                break
            elif handler_name == 'iter':
                self.handler = IterativeHandler()
                break
            else:
                print('Введено неправильное имя обработчика.')

    def start(self):
        matrix = check_1(self.row_column)
        n = self.row_column
        print('Начальная матрица:')
        print_array(matrix)
        count = self.handler.start(matrix, n)
        print('Общее количество вариантов: ', count)
        if count == 0:
            print('Проверяемый массив не подошел под условия.')


class Handler:
    def check_2(self, matrix, row):
        if sum(matrix[row]) > len(matrix) * 5:
            return False
        else:
            return True


class RecursiveHandler(Handler):
        def start(self, matrix, n):
            count = [0]
            self.F_rec(matrix, 0, 0, count, n - 1)
            return count[0]

        def F_rec(self, matrix, row, column, count, n, exist=[[], []]):
            if row == len(matrix):
                return
            self.F_rec(matrix, row + 1, column + 1, count, n)
            if self.check_2(matrix, row):
                if matrix[row][row] == 0 and row % 2 != 0 and row not in exist[0]:
                    exist[0].append(row)
                    new_matrix = copy.deepcopy(matrix)
                    for i in range(len(matrix)):
                        new_matrix[row][i], new_matrix[i][column] = new_matrix[i][column], new_matrix[row][i]
                    print_array(new_matrix)
                    count[0] += 1
                if matrix[row][n - row] == 0 and row % 2 != 0 and row != len(matrix) // 2 and row not in exist[1]:
                    exist[1].append(row)
                    new_matrix = copy.deepcopy(matrix)
                    for i in range(len(matrix)):
                        new_matrix[row][i], new_matrix[n - i][n - column] = new_matrix[n - i][n - column], \
                                                                            new_matrix[row][i]
                    print_array(new_matrix)
                    count[0] += 1
                self.F_rec(matrix, row + 1, column + 1, count, n, exist)
            else:
                self.F_rec(matrix, row + 1, column + 1, count, n, exist)


class IterativeHandler(Handler):
    def start(self, matrix, n):
        count = 0
        exist = [[], []]
        stack = [(copy.deepcopy(matrix), 0, 0)]
        k = n - 1
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
                    print_array(new_matrix)
                    stack.append((matrix, row + 1, column + 1))
                if matrix[row][k - row] == 0 and row % 2 != 0 and row != len(matrix) // 2 and row not in exist[1]:
                    exist[1].append(row)
                    new_matrix = copy.deepcopy(matrix)
                    for i in range(len(matrix)):
                        new_matrix[row][i], new_matrix[k - i][k - column] = new_matrix[k - i][k - column], new_matrix[row][
                            i]
                    print_array(new_matrix)
                    stack.append((matrix, row + 1, column + 1))
            else:
                if matrix[row][row] == 0 and row not in exist[0]:
                    pass
                if matrix[row][k - row] == 0 and row != len(matrix) // 2 and row not in exist[1]:
                    pass
        return count - 1


def number_check(n):
    while True:
        try:
            k = int(input(n))
            if k > 0:
                return k
            else:
                print('Введенное число отрицательное.')

        except ValueError:
            print('Введенное значение не является числом.')


def check_1(n):
    while True:
        matrix = [[random.randint(0, 10) for i in range(n)] for j in range(n)]
        for i in range(n):
            if matrix[i][i] == 0 or matrix[i][n - 1 - i] == 0:
                return matrix


def print_array(array):
    for row in array:
        for elem in row:
            print('{:4}'.format(elem), end=' ')
        print()
    print()

program = Program()
program.start()


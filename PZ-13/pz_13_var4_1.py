
try:
    matrix_shape = input('Введите количество строк  матрицы:\t')
    matrix_shape = int(matrix_shape)
except:
    raise BaseException(f'Количество строк матрицы должно быть целым числов, вы ввели {matrix_shape}')


matrix = []


for i in range(matrix_shape):
    row_matrix = list(map(float, input(f'Введите {i + 1} строку матрицы:\t').split()))
    if len(row_matrix) == matrix_shape:
        matrix.append(row_matrix)
    else: 
        raise BaseException(f'Матрица не квадратная. Ожидался размер строки {matrix_shape}, вы ввели {len(row_matrix)}')
    
matrix_result = [[matrix[i][j] * 2 if i!=j else matrix[i][j] for j in range(matrix_shape)] for i in range(matrix_shape)]
    

for i in range(matrix_shape):
    print(matrix_result[i])


# Введите количество строк квадратной матрицы:    4
# Введите 1 строку матрицы:       1 2 3 4
# Введите 2 строку матрицы:       5 6 7 8
# Введите 3 строку матрицы:       9 1 2 3
# Введите 4 строку матрицы:       4 5 6 7
# [1.0, 4.0, 6.0, 8.0]
# [10.0, 6.0, 14.0, 16.0]
# [18.0, 2.0, 2.0, 6.0]
# [8.0, 10.0, 12.0, 7.0]

# Введите количество строк квадратной матрицы:    2
# Введите 1 строку матрицы:       1 2
# Введите 2 строку матрицы:       3 4
# [1.0, 4.0]
# [6.0, 4.0]


# Введите количество строк квадратной матрицы:    3
# Введите 1 строку матрицы:       1 2 3 4
# BaseException: Матрица не квадратная. Ожидался размер строки 3, вы ввели 4

# Введите количество строк квадратной матрицы:    koshka
# BaseException: Количество строк матрицы должно быть целым числов, вы ввели koshka
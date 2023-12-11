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
    
flag_all_negative = True

for row in matrix:
    for elem in row:
        flag_all_negative *= elem < 0
        
print(not flag_all_negative)


# Введите количество строк  матрицы:      2
# Введите 1 строку матрицы:       -1 -5
# Введите 2 строку матрицы:       -4 -3
# False

# Введите количество строк  матрицы:      2
# Введите 1 строку матрицы:       3 -5
# Введите 2 строку матрицы:       -4 8
# True


# Введите количество строк  матрицы:      2
# Введите 1 строку матрицы:       6 5
# Введите 2 строку матрицы:       4 5
# True

# Введите количество строк  матрицы:      2
# Введите 1 строку матрицы:       -1 -2
# Введите 2 строку матрицы:       -3 65465413165
# True
matrix_shape = int(input('Введите количество строк  матрицы:\t'))

matrix = []



for i in range(matrix_shape):
    row_matrix = list(map(float, input(f'Введите {i + 1} строку матрицы:\t').split()))
    if len(row_matrix) == matrix_shape:
        matrix.append(row_matrix)
    else: 
        raise BaseException(f'Матрица не квадратная. Ожидался размер строки {matrix_shape}, вы ввели {len(row_matrix)}')


matrix_result = []    
for i in range(matrix_shape):
    matrix_result.append([])
    for j in range(matrix_shape):
        if i!=j:
            matrix_result[i].append(matrix[i][j] * 2)
        else:
            matrix_result[i].append(matrix[i][j])


for i in range(matrix_shape):
    print(matrix_result[i])
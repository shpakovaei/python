# Напишите функцию для транспонирования матрицы Пример: [[1, 2, 3], [4, 5, 6]] -> [[1,4], [2,5], [3, 6]]

def transportation_matrix(matrix):
    transportation_matrix = [[matrix[j][i] for j in range(len(matrix))]
                         for i in range(len(matrix[0]))]
    return transportation_matrix

matrix = [[1, 2, 3], [4, 5, 6]]
result = transportation_matrix(matrix)
print(result)
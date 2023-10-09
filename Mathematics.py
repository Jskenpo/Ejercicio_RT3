from math import isclose, sqrt


def add_matrices(matrix1, matrix2):
    if len(matrix1) != len(matrix2) or len(matrix1[0]) != len(matrix2[0]):
        raise ValueError("Error en matrices, dimensiones distintas :(")
    result = [[matrix1[i][j] + matrix2[i][j] for j in range(len(matrix1[0]))] for i in range(len(matrix1))]
    return result


def subtract_matrices(matrix1, matrix2):
    if len(matrix1) != len(matrix2) or len(matrix1[0]) != len(matrix2[0]):
        raise ValueError("Error en matrices, dimensiones distintas :(")
    result = [[matrix1[i][j] - matrix2[i][j] for j in range(len(matrix1[0]))] for i in range(len(matrix1))]
    return result


def multiply_matrices(matrix1, matrix2):
    if len(matrix1[0]) != len(matrix2):
        raise ValueError(
            "El número de columnas de la matriz 1 debe coincidir con el número de filas de la matriz 2.")
    result = [[sum(matrix1[i][k] * matrix2[k][j] for k in range(len(matrix2))) for j in range(len(matrix2[0]))] for i in
              range(len(matrix1))]
    return result


def multiply_matrix_by_scalar(matrix, scalar):
    result = [[cell * scalar for cell in row] for row in matrix]
    return result


def multiply_matrix_by_vector(matrix, vector):
    if len(vector) != len(matrix[0]):
        raise ValueError(
            "La longitud del vector incorrecta, no coincide con el número de columnas de la matriz.")
    result = [sum(matrix[i][j] * vector[j] for j in range(len(vector))) for i in range(len(matrix))]
    return result


def matrix_transpose(matrix):
    result = [[matrix[j][i] for j in range(len(matrix))] for i in range(len(matrix[0]))]
    return result


def bc_coords(A, B, C, P):
    BCP = abs((P[0] * C[1] + C[0] * B[1] + B[0] * P[1]) - (P[1] * C[0] + C[1] * B[0] + B[1] * P[0]))
    CAP = abs((A[0] * C[1] + C[0] * P[1] + P[0] * A[1]) - (A[1] * C[0] + C[1] * P[0] + P[1] * A[0]))
    ABP = abs((A[0] * B[1] + B[0] * P[1] + P[0] * A[1]) - (A[1] * B[0] + B[1] * P[0] + P[1] * A[0]))

    ABC = abs((A[0] * B[1] + B[0] * C[1] + C[0] * A[1]) - (A[1] * B[0] + B[1] * C[0] + C[1] * A[0]))

    if ABC == 0:
        return None

    u = BCP / ABC
    v = CAP / ABC
    w = ABP / ABC

    if (0 <= u <= 1) and (0 <= v <= 1) and (0 <= w <= 1) and isclose(u + v + w, 1.0):
        return u, v, w
    else:
        return None


def subtract_vectors(vector1, vector2):
    if len(vector1) != len(vector2):
        raise ValueError("Los vectores no tienen la misma longitud.")
    result = tuple(a - b for a, b in zip(vector1, vector2))
    return result


def add_vectors(vector1, vector2):
    if len(vector1) != len(vector2):
        raise ValueError("Los vectores no tienen la misma longitud.")
    result = tuple(a + b for a, b in zip(vector1, vector2))
    return result


def euclidean_norm(x):
    squared_sum = sum(v ** 2 for v in x)
    norm = sqrt(squared_sum)
    return norm


def divide_tuple_by_scalar(t, d):
    if d != 0:
        divided_tuple = tuple(value / d for value in t)
        return divided_tuple
    else:
        return t


def cross_product(vector1, vector2):
    if len(vector1) != 3 or len(vector2) != 3:
        raise ValueError("Los vectores no tienen la longitud correcta para el producto cruz.")
    cross_product = [
        vector1[1] * vector2[2] - vector1[2] * vector2[1],
        vector1[2] * vector2[0] - vector1[0] * vector2[2],
        vector1[0] * vector2[1] - vector1[1] * vector2[0]
    ]
    return cross_product


def invert_matrix(matrix):
    if len(matrix) != len(matrix[0]):
        raise ValueError("La matriz no es cuadrada.")
    n = len(matrix)
    augmented_matrix = [row + [1 if i == j else 0 for j in range(n)] for i, row in enumerate(matrix)]

    for i in range(n):
        pivot_row = augmented_matrix[i]
        pivot_element = pivot_row[i]

        if pivot_element == 0:
            raise ValueError("La matriz es singular, no tiene inversa.")

        pivot_row_normalized = [elem / pivot_element for elem in pivot_row]
        augmented_matrix[i] = pivot_row_normalized

        for k in range(n):
            if k != i:
                factor = augmented_matrix[k][i]
                row_to_subtract = [elem * factor for elem in pivot_row_normalized]
                augmented_matrix[k] = [x - y for x, y in zip(augmented_matrix[k], row_to_subtract)]

    inverse_matrix = [row[n:] for row in augmented_matrix]
    return inverse_matrix


def dot_product(array1, array2):
    if len(array1) != len(array2):
        raise ValueError("Los arrays no tienen la misma longitud.")
    dot_product = sum(a * b for a, b in zip(array1, array2))
    return dot_product


def scalar_multiply(scalar, arr):
    return [scalar * x for x in arr]


def subtract_arrays(arr1, arr2):
    if len(arr1) != len(arr2):
        raise ValueError("Los arrays no tienen la misma longitud.")
    return [a - b for a, b in zip(arr1, arr2)]

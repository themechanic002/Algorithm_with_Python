# 10830 행렬 제곱

temp = list(map(int, input().split()))
n = temp[0]
b = temp[1]

orig_matrix = []
for i in range(n):
    orig_matrix.append(list(map(int, input().split())))


def multiply(n, matrixA, matrixB):
    new_matrix = [[0 for i in range(n)] for j in range(n)]
    for i in range(n):
        for j in range(n):
            sum = 0
            for k in range(n):
                sum += matrixA[i][k] * matrixB[k][j]
            new_matrix[i][j] = sum % 1000
    return new_matrix


def divide(matrix, n, b):
    if b > 2:
        if b % 2 == 0:
            return multiply(n, divide(matrix, n, b // 2), divide(matrix, n, b // 2))
        else:
            return multiply(n, multiply(n, divide(matrix, n, b // 2), divide(matrix, n, b // 2)), matrix)

    elif b == 2:
        return multiply(n, matrix, matrix)
    elif b == 1:
        return matrix


result = divide(orig_matrix, n, b)
for i in range(n):
    for j in range(n):
        print(result[i][j], end=' ')
    print("")

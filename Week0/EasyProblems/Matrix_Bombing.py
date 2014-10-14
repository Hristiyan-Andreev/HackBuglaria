def bomb_matrix(matrix):
    width = len(matrix[0])
    depth = len(matrix)
    results = {}
    suma = 0
    for row in range(0, depth - 1):
        for column in range(0, width - 1):
            suma = 0
            if column > 0:
                suma += matrix[column - 1][row] - matrix[column][row]
                if row < depth:
                    suma += matrix[column - 1][row + 1] - matrix[column][row]
                if row > 0:
                    suma += matrix[column - 1][row - 1] - matrix[column][row]
            if column < width - 1:
                suma += matrix[column + 1][row] - matrix[column][row]
                if row < depth:
                    suma += matrix[column + 1][row + 1] - matrix[column][row]
                if row > 0:
                    suma += matrix[column + 1][row - 1] - matrix[column][row]
            if row > 0:
                suma += matrix[column][row + 1] - matrix[column][row]
            if row < depth - 1:
                suma += matrix[column][row - 1] - matrix[column][row]
            coord = row, column
            results[coord] = suma
    return results


def main():
    m = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
    print(bomb_matrix(m))
    m = [[]]
if __name__ == '__main__':
    main()

def sum_matrix(m):
    sum = 0
    for i in range(0, len(m)):
        for number in m[i]:
            sum += number
    return sum


def main():
    m = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
    print(sum_matrix(m))
    m = [[0, 0, 0], [0, 0, 0], [0, 0, 0]]
    print(sum_matrix(m))
    m = [[1, 2], [3, 4], [5, 6], [7, 8], [9, 10]]
    print(sum_matrix(m))


if __name__ == '__main__':
    main()

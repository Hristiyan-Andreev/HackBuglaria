def sevens_in_row(arr, n):
    sum = 0
    for number in arr:
        if number == 7:
            for i in range(number, number + n+1):
                if i == 7:
                    sum += 1
                    if sum == n:
                        return True
    return False


def main():
    print(sevens_in_row([1, 7, 7, 3, 4], 2))
    print(sevens_in_row([1, 7, 7, 3, 4], 3))
    print(sevens_in_row([10, 8, 7, 6, 7, 7, 7, 20, -7], 3))
    print(sevens_in_row([1, 7, 1, 7, 7], 4))

if __name__ == '__main__':
    main()

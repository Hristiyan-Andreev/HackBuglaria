def contain_digits(number, digits):
    array = list(map(int, str(number)))
    flag = False
    for digit in digits:
        for num in array:
            flag = False
            if num == digit:
                flag = True
                break
        if flag is False:
            return False
    return True


def main():
    print(contain_digits(402123, [0, 3, 4]))
    print(contain_digits(666, [6, 4]))

if __name__ == '__main__':
    main()

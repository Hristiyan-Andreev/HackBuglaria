def contains_digit(number, digit):
    array = list(map(int, str(number)))

    for num in array:
        if num == digit:
            return True
    return False


def main():
    print(contains_digit(123, 4))
    print(contains_digit(42, 2))


if __name__ == '__main__':
    main()

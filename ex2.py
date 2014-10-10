def sum_of_digits(number):
    sumdigits = 0
    while number:
        sumdigits += abs(number) % 10
        number //= 10

    return sumdigits


def main():

    print(sum_of_digits(123))
    print(sum_of_digits(1234))
    print(sum_of_digits(10))

if __name__ == '__main__':
    main()

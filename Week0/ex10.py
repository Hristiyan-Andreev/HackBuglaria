def is_number_balanced(number):
    array = list(map(int, str(number)))
    sum_left = 0
    sum_right = 0
    for i in range(0, len(array) // 2):
        sum_left += array[i]

    if len(array) % 2 == 0:
        for i in range((len(array) // 2), len(array)):
            sum_right += array[i]
    else:
        for i in range((len(array) // 2) + 1, len(array)):
            sum_right += array[i]

    if sum_left == sum_right:
        return True
    else:
        return False


def main():
    print(is_number_balanced(3443))
    print(is_number_balanced(34543))
    print(is_number_balanced(13459))
    print(is_number_balanced(2345))

if __name__ == '__main__':
    main()

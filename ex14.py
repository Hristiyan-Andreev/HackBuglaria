def biggest_difference(array):
    max = min = array[0]
    for number in array:
        if number > max:
            max = number
        elif number < min:
            min = number
    return min - max


def main():
    print(biggest_difference([1, 2, 3, 4, 5]))
    print(biggest_difference([-10, -9, -1]))

if __name__ == '__main__':
    main()

def array_to_number(array):
    s = int(''.join(map(str, array)))
    return s


def main():
    print(array_to_number([1, 2, 3, 4]))
if __name__ == '__main__':
    main()

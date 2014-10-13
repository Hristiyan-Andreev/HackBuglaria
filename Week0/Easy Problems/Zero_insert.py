def zero_insert(number):
    array = list(map(int, str(number)))
    i = 0
    while i <= len(array) - 2:
        if (array[i] == array[i+1] or ((array[i] + array[i+1]) % 10 == 0)):
            array.insert(i+1, 0)
            i += 2
        else:
            i += 1
    return int(''.join(map(str, array)))


def main():
    print(zero_insert(116457))
    print(zero_insert(6446))
    print(zero_insert(55555555))

if __name__ == '__main__':
    main()

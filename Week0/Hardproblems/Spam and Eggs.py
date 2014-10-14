def prepare_meal(number):

    if number % 3 == 0:
        n = 2
        string = 'spam'
        while 3**n <= number:
            if number % 3**n == 0:
                string = string + ' spam'
            n += 1
    else:
        string = ''

    if number % 5 == 0:
        string = string + ' and eggs'
    return string


def main():
    print(prepare_meal(15))
    print(prepare_meal(45))

if __name__ == '__main__':
    main()

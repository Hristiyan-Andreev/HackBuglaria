def is_int_palindrome(n):
    array = list(map(int, str(n)))
    rev_array = array[::-1]
    if array == rev_array:
        print (array)
        print (rev_array)
        return True
    else:
        print (array)
        print (rev_array)
        return False


def main():
    print(is_int_palindrome(93435))
    print(is_int_palindrome(10001))


if __name__ == '__main__':
    main()

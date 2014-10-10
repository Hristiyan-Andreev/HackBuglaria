def is_prime(n):
    for i in range(1, abs(n+1)):
        if n % i == 0:
            if n == 1:
                return False
            if not (i == abs(n) or i == 1):
                return False
    return True


def main():
    print("7 " + str(is_prime(7)))
    print("1 " + str(is_prime(1)))
    print("2 " + str(is_prime(2)))
    print("8 " + str(is_prime(8)))
    print("11 " + str(is_prime(11)))
    print("-10 " + str(is_prime(-10)))

if __name__ == '__main__':
    main()

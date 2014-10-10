def is_prime(n):
    for i in range(1, abs(n+1)):
        if n % i == 0:
            if n == 1:
                return False
            if not (i == abs(n) or i == 1):
                return False
    return True


def prime_number_of_divisors(n):
    divisors = 0
    for i in range(1, n+1):
        if n % i == 0:
            divisors += 1
    print("{} ".format(str(n)) + str(is_prime(divisors)))


def main():
    prime_number_of_divisors(7)
    prime_number_of_divisors(8)
    prime_number_of_divisors(9)
    prime_number_of_divisors(20)


if __name__ == '__main__':
    main()

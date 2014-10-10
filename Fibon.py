def nth_fibonacci(n):
    if n == 0:
        return 1
    elif n == 1:
        return 1
    elif n == 2:
        return 2
    else:
        return (n-1) + (n-2)


def main():
    print(nth_fibonacci(0))
    print(nth_fibonacci(1))
    print(nth_fibonacci(2))
    print(nth_fibonacci(3))
if __name__ == '__main__':
    main()

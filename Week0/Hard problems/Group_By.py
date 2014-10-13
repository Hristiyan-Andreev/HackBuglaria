def groupby(func, seq):
    results = {}
    for i in range(0, len(seq)):
        result = func(seq[i])
        if result not in results:
            results[result] = [seq[i]]
        else:
            results[result].append(seq[i])

    return results


def main():
    print(groupby(lambda x: x % 2, [0, 1, 2, 3, 4, 5, 6, 7]))
    print(groupby(lambda x: 'odd' if x % 2 else 'even', [1, 2, 3, 5, 8, 9, 10, 12]))
    print(groupby(lambda x: x % 3, [0, 1, 2, 3, 4, 5, 6, 7]))

if __name__ == '__main__':
    main()

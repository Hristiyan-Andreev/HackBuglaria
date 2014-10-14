def count_words(array):
    words = {}
    for word in array:
        if (word in words) is False:
            words[word] = 1
        else:
            words[word] = words[word] + 1
    return words


def main():
    print(count_words(["apple", "banana", "apple", "pie"]))
    print(count_words(["python", "python", "python", "ruby"]))


if __name__ == '__main__':
    main()

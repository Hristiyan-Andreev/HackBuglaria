def count_substrings(haystack, needle, count):
    index = haystack.find(needle)
    if index == -1:
        return count
    count += 1

    return count_substrings(haystack[index + len(needle):], needle, count)


def main():
    print(count_substrings("PaticaPatica", "ica", 0))
    print(count_substrings("PaticanaGostivisaisa", "isa", 0))

if __name__ == '__main__':
    main()

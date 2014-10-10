def count_vowels(string, count, Vowels):
    count = 0
    for Vowel in Vowels:
        for letter in string:
            if letter == Vowel:
                count += 1
    return count


def main():
    print(count_vowels("Python", 0, "AaEeIiOoUuYy"))
    print(count_vowels("Theistareykjarbunga", 0, "AaEeIiOoUuYy"))

if __name__ == '__main__':
    main()

 


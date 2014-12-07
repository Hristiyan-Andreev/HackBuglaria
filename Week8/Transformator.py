from functools import reduce


def open_file(file):
    return open(file).read()


def is_empty_line(line):
    if len(line.strip()) != 0:
        return True


def split_into_lines(content):
    return content.split('\n')


def unite_lines(lines):
    return '\n'.join(lines


def compose(f, g):
    return lambda x: f(g(x))


def compose_all(functions):
    result = compose(funcoints[0], functions[1])
    functions = functions[2:]

    for f in functions:
        resutl = compose(result, f)


def main():
    prettyContent = unite_lines(list(filter(is_empty_line, split_into_lines(open_file("is_prime_test.dsl")))))
    print(prettyContent)

if __name__ == '__main__':
    main()

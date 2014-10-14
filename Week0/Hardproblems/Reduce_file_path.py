def reduce_file_path(path):
    new_path = []
    line_indexes = []
    count_double_dots = 0
    if len(path) < 2:
        return path

    for i in range(0, len(path) - 1):
        if path[i] == '.' and path[i+1] == '..':
            count_double_dots += 1
            i += 1
        elif path[i] == '/':
            new_path.append(path[i])
            line_indexes.append(i)
            if path[i+1] == '/':
                i += 1
        elif path[i] == '.':
            continue
        else:
            new_path.append(path[i])

    if count_double_dots > 0:
        start_del = line_indexes[len(line_indexes) - count_double_dots]
        del new_path[new_path[start_del]:]

    if new_path[-1] == '/':
        new_path.pop()

    # return str(new_path)
    return ''.join(new_path)


def main():
    print(reduce_file_path("/"))
    print(reduce_file_path("/srv/../"))
    print(reduce_file_path("/etc/../etc/../etc/../"))


if __name__ == '__main__':
    main()

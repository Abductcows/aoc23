import re


def is_special(c):
    if c == '.':
        return False
    return ord(c) > ord('9') or ord(c) < ord('0')


def get_all_neighbors(row, start_col, length, m, n):
    res = []

    if start_col - 1 >= 0:
        res.append([row, start_col - 1])
    if start_col + length < n:
        res.append([row, start_col + length])

    if row - 1 >= 0:
        res.extend([
            [row - 1, start_col + j] for j in range(length)
        ])
        if start_col - 1 >= 0:
            res.append([row - 1, start_col - 1])
        if start_col + length < n:
            res.append([row - 1, start_col + length])
    if row + 1 < m:
        res.extend([
            [row + 1, start_col + j] for j in range(length)
        ])
        if start_col - 1 >= 0:
            res.append([row + 1, start_col - 1])
        if start_col + length < n:
            res.append([row + 1, start_col + length])
    return res


def run(filename):
    with open(filename) as file:
        lines = file.readlines()

    m, n = len(lines), len(lines[0]) - 1
    result = 0

    gears = dict()

    for i, line in enumerate(lines):
        content = re.split(r'([&/\n.\-=+$%@*#])', line.strip())
        content = [token for token in content if token]

        j = 0
        content_index = 0
        while content_index < len(content):
            token = content[content_index]
            if token.isdigit():
                for neighbor in get_all_neighbors(i, j, len(token), m, n):
                    if lines[neighbor[0]][neighbor[1]] == '*':
                        if tuple(neighbor) in gears:
                            result += gears[tuple(neighbor)] * int(token)
                            del gears[tuple(neighbor)]
                        else:
                            gears[tuple(neighbor)] = int(token)
            j += len(token)
            content_index += 1

    print(result)


if __name__ == '__main__':
    # run('example.txt')
    run('input.txt')

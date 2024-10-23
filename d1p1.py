def first_digit_value(s):
    for c in s:
        if ord('0') <= ord(c) <= ord('9'):
            return ord(c) - ord('0')


def run(filename):
    with open(filename) as file:
        data = file.readlines()

    result = sum([10 * first_digit_value(line) + first_digit_value(line[::-1]) for line in data])
    print(result)


if __name__ == '__main__':
    # run('example.txt')
    run('input.txt')

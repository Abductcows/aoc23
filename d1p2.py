def first_digit_or_spelled_value(s, start, stop, step):
    digit_words = ['one', 'two', 'three', 'four', 'five', 'six', 'seven', 'eight', 'nine']

    for i in range(start, stop, step):
        if ord('0') <= ord(s[i]) <= ord('9'):
            return ord(s[i]) - ord('0')

        for j, digit_word in enumerate(digit_words):
            if s[i:].find(digit_word) == 0:
                return j + 1


def run(filename):
    with open(filename) as file:
        data = file.readlines()

    result = sum(
        [10 * first_digit_or_spelled_value(line, 0, len(line), 1)
         + first_digit_or_spelled_value(line, len(line) - 1, -1, -1)
         for line in data]
    )

    print(result)


if __name__ == '__main__':
    # run('example.txt')
    run('input.txt')

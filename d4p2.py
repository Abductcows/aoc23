def run(filename):
    with open(filename) as file:
        lines = file.readlines()

    extras = [0] * (2 * len(lines))
    for i, line in enumerate(lines):
        winning = line.split('|')[0].split(':')[1].strip()
        winning = [int(num) for num in winning.split(' ') if num]
        own_numbers = line.split('|')[1].strip()
        own_numbers = [int(num) for num in own_numbers.split(' ') if num]

        matched = 0
        for num in own_numbers:
            if num in winning:
                matched += 1

        for j in range(matched):
            extras[i + j + 1] += extras[i] + 1


    result = len(lines) + sum(extras)
    print(result)


if __name__ == '__main__':
    # run('example.txt')
    run('input.txt')

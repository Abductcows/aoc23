def run(filename):
    with open(filename) as file:
        lines = file.readlines()

    result = 0
    for line in lines:
        winning = line.split('|')[0].split(':')[1].strip()
        winning = [int(num) for num in winning.split(' ') if num]
        own_numbers = line.split('|')[1].strip()
        own_numbers = [int(num) for num in own_numbers.split(' ') if num]

        score = 0
        for num in own_numbers:
            if num in winning:
                if score == 0:
                    score = 1
                else:
                    score *= 2

        result += score

    print(result)

if __name__ == '__main__':
    # run('example.txt')
    run('input.txt')

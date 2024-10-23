from functools import reduce

def get_max_cubes_in_entire_game(rounds: list[str]):
    maxima = {'red': 0, 'green': 0, 'blue': 0}

    for round in rounds:
        colors = round.strip().split(',')
        for color in colors:
            count, color_name = color.strip().split(' ')
            maxima[color_name] = max(maxima[color_name], int(count))

    return maxima


def run(filename):
    with open(filename) as file:
        data = file.readlines()


    ans = 0
    for game in data:
        rounds = game.split(':')[1].strip().split(';')

        max_cubes = get_max_cubes_in_entire_game(rounds)

        power = reduce(lambda acc, v: acc * v, max_cubes.values(), 1)
        ans += power

    print(ans)

if __name__ == '__main__':
    # run('example.txt')
    run('input.txt')

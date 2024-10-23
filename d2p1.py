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

    availables = {'red': 12, 'green': 13, 'blue': 14}

    ans = 0
    for game in data:
        game_id = int(game.split(':')[0].split(' ')[1])
        rounds = game.split(':')[1].strip().split(';')

        max_cubes = get_max_cubes_in_entire_game(rounds)

        for cube_color in max_cubes:
            if max_cubes[cube_color] > availables[cube_color]:
                break
        else:
            ans += game_id

    print(ans)

if __name__ == '__main__':
    # run('example.txt')
    run('input.txt')

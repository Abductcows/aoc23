def get_index(direction):
    if direction == 'L':
        return 0
    if direction == 'R':
        return 1
    raise ValueError(f'what the hell is a {direction}?')


def run(filename):
    with open(filename) as file:
        lines = file.readlines()

    instructions = lines[0].strip()
    transitions = dict()
    for line in lines[2:]:
        key = line.split('=')[0].strip()
        vals = [val.strip() for val in line.split('=')[1].strip().strip('(').strip(')').split(',')]
        transitions[key] = vals

    result = 0
    start_nodes = [key for key in transitions if key[-1] == 'A']
    print(start_nodes)


    min_steps, max_steps = 1, 1
    while True:
        for start_node in start_nodes:
            found_in = dive(start_node, instructions, transitions, min_steps, max_steps)
            if found_in < 0:
                max_steps = max(max_steps + 1, min_steps)
                break
            if result == 0:
                result = found_in
            if found_in > result:
                result = found_in
                min_steps = found_in
                break
            max_steps = max(max_steps + 1, min_steps)
        else:
            break

    print(result)


def dive(start, instructions, transitions, min_steps, max_steps):
    steps = 0
    current = start
    while True:
        if steps > max_steps:
            return -1
        if steps >= min_steps and current[-1] == 'Z':
            return steps
        direction = instructions[steps % len(instructions)]
        current = transitions[current][get_index(direction)]
        steps += 1


if __name__ == '__main__':
    # run('example.txt')
    run('input.txt')

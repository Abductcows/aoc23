import math
from functools import reduce


def get_index(direction):
    if direction == 'L':
        return 0
    if direction == 'R':
        return 1
    raise ValueError(f'what the hell is a {direction}?')


def lcm(a, b):
    return abs(a * b) // math.gcd(a, b)


def lcm_of_iterable(numbers):
    return reduce(lcm, numbers)


def run(filename):
    with open(filename) as file:
        lines = file.readlines()

    instructions = lines[0].strip()
    transitions = dict()
    for line in lines[2:]:
        key = line.split('=')[0].strip()
        vals = [val.strip() for val in line.split('=')[1].strip().strip('(').strip(')').split(',')]
        transitions[key] = vals

    start_nodes = [key for key in transitions if key[-1] == 'A']
    print(start_nodes)

    result = []
    min_steps = 1

    for start_node in start_nodes:
        found_in = dive(start_node, instructions, transitions, min_steps)
        result.append(found_in)

    print(lcm_of_iterable(result))


def dive(start, instructions, transitions, min_steps):
    steps = 0
    current = start
    while True:
        if current[-1] == 'Z':
            return steps
        direction = instructions[steps % len(instructions)]
        current = transitions[current][get_index(direction)]
        steps += 1


if __name__ == '__main__':
    # run('example.txt')
    run('input.txt')

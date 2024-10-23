def run(filename):
    with open(filename) as file:
        lines = file.readlines()


if __name__ == '__main__':
    run('example.txt')
    # run('input.txt')

def find_directional_intersection(x1, y1, dx1, dy1, x2, y2, dx2, dy2):
    det = dx1 * dy2 - dy1 * dx2

    if det == 0:
        return None

    t = ((x2 - x1) * dy2 - (y2 - y1) * dx2) / det
    u = ((x2 - x1) * dy1 - (y2 - y1) * dx1) / det

    if t >= 0 and u >= 0:
        intersection_x = x1 + t * dx1
        intersection_y = y1 + t * dy1
        return intersection_x, intersection_y
    else:
        return None


def run(filename, test_min, test_max):
    with open(filename) as file:
        lines = file.readlines()

    coords = []
    speeds = []
    for line in lines:
        line_coords = line.split('@')[0].split(',')
        coords.append([int(coord.strip()) for coord in line_coords[:2]])
        line_speeds = line.split('@')[1].split(',')
        speeds.append([int(speed.strip()) for speed in line_speeds[:2]])

    res = 0
    n = len(coords)
    for i in range(n):
        for j in range(i, n):
            intersection = find_directional_intersection(
                coords[i][0], coords[i][1], speeds[i][0], speeds[i][1],
                coords[j][0], coords[j][1], speeds[j][0], speeds[j][1]
            )
            if intersection and intersection[0] >= test_min and intersection[1] >= test_min \
                    and intersection[0] <= test_max and intersection[1] <= test_max:
                res += 1
    print(res)


if __name__ == '__main__':
    run('example.txt', 7, 27)
    run('input.txt', 200_000_000_000_000, 400_000_000_000_000)

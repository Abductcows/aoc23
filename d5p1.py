class SpecialDict:
    def __init__(self):
        self.bounds = []

    def put(self, dest, source, length):
        self.bounds.append(
            [source, source + length, source - dest]
        )

    def get(self, item):
        for bound in self.bounds:
            if bound[0] <= item < bound[1]:
                return item - bound[2]
        return item


seed_to_soil, soil_to_fert, fert_to_water, water_to_light, light_to_temp, temp_to_hum, hum_to_loc, \
    = SpecialDict(), SpecialDict(), SpecialDict(), SpecialDict(), SpecialDict(), SpecialDict(), SpecialDict()

maps = [seed_to_soil, soil_to_fert, fert_to_water, water_to_light, light_to_temp, temp_to_hum, hum_to_loc]


def get_seed_location(seed):
    return hum_to_loc.get(temp_to_hum.get(
        light_to_temp.get(water_to_light.get(
            fert_to_water.get(soil_to_fert.get(
                seed_to_soil.get(seed)))))))


def run(filename):
    with open(filename) as file:
        lines = file.readlines()

    cur_map = -1
    for line in lines[1:]:
        if ':' in line:
            cur_map += 1
            continue
        if not line.strip():
            continue

        map = maps[cur_map]
        numbers = [int(num) for num in line.strip().split(' ') if num]
        map.put(numbers[0], numbers[1], numbers[2])

    seeds = [int(num) for num in lines[0].split(':')[1].strip().split(' ') if num]
    seed_locations = [get_seed_location(seed) for seed in seeds]
    result = min(seed_locations)
    print(result)


if __name__ == '__main__':
    # run('example.txt')
    run('input.txt')

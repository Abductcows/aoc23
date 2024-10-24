def run(filename):
    with open(filename) as file:
        lines = file.readlines()

    times_total = lines[0].split(':')[1].strip()
    times_total = [time.strip() for time in times_total.split(' ') if time.strip()]
    times_total = [int(''.join(times_total))]

    distance_records = lines[1].split(':')[1].strip()
    distance_records = [distance.strip() for distance in distance_records.split(' ') if distance.strip()]
    distance_records = [int(''.join(distance_records))]

    speed_gained = 1
    result = 1
    for race_id in range(len(times_total)):
        total_viable_configurations = 0
        for i in range(1, times_total[race_id] - 1):
            score = i * speed_gained * (times_total[race_id] - i)
            if score > distance_records[race_id]:
                total_viable_configurations += 1
        result *= total_viable_configurations

    print(result)


if __name__ == '__main__':
    # run('example.txt')
    run('input.txt')

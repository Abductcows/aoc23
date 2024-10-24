from functools import cmp_to_key


def my_ord(c):
    custom_map = {'A': 14, 'K': 13, 'Q': 12, 'J': 11, 'T': 10, **{str(num): num for num in range(9, 1, -1)}}
    if c in custom_map:
        return custom_map[c]
    raise ValueError('What did u feed me')


def hand_str_cmp(s1, s2):
    for i in range(len(s1)):
        diff = my_ord(s1[i]) - my_ord(s2[i])
        if diff != 0:
            return diff // abs(diff)
    return 0


def rate(hand):
    counts = {c: hand.count(c) for c in set(hand)}
    by_size = sorted([[v, k] for k, v in counts.items()], key=lambda pair: pair[0], reverse=True)
    n = len(by_size)
    flags = {'five kind': 64, 'four kind': 32, 'full house': 16, 'three kind': 8, 'two pair': 4, 'one pair': 2,
             'high card': 1}
    cur_flags = 0
    if by_size[0][0] == 5:
        cur_flags |= flags['five kind']
    elif by_size[0][0] == 4:
        cur_flags |= flags['four kind']
    elif by_size[0][0] == 3:
        if n > 1 and by_size[1][0] == 2:
            cur_flags |= flags['full house']
        else:
            cur_flags |= flags['three kind']
    elif by_size[0][0] == 2:
        if n > 1 and by_size[1][0] == 2:
            cur_flags |= flags['two pair']
        else:
            cur_flags |= flags['one pair']
    elif by_size[0][0] == 1:
        cur_flags |= flags['high card']
    return cur_flags


def compare_hands(h1, h2):
    rating1, rating2 = rate(h1), rate(h2)

    if rating1 < rating2:
        return -1
    if rating1 > rating2:
        return 1
    return hand_str_cmp(h1, h2)


def run(filename):
    with open(filename) as file:
        lines = file.readlines()

    hands = []
    bids = []
    for line in lines:
        hands.append(line.split(' ')[0].strip())
        bids.append(int(line.split(' ')[1].strip()))

    s = sorted(zip(hands, bids), key=lambda pair: cmp_to_key(compare_hands)(pair[0]))

    result = 0
    for i in range(len(s)):
        result += s[i][1] * (i + 1)

    print(result)


if __name__ == '__main__':
    # run('example.txt')
    run('input.txt')

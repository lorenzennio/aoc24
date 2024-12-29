import argparse

def min_dist(i, data, field):
    start = 0+0j
    end  = field+field*1j
    coords = set([x + y*1j for x in range(field+1) for y in range(field+1)]) - set(data[:i])

    seen = set()
    queue = [(0, start)]

    for dist, pos in queue:
        if pos == end: return dist

        for st in [1, -1, 1j, -1j]:
            p = pos + st
            if p not in seen and p in coords:
                queue.append((dist+1, p))
                seen.add(p)

    return 1e9

def solution1(data, field):
    best = min_dist(1024, data, field)
    return best

def solution2(data, field):
    for i in range(len(data)):
        best = min_dist(1024, data, field)
        if best == 1e9: return data[i-1]

if __name__=='__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument('-t', default=False, action=argparse.BooleanOptionalAction)
    args = parser.parse_args()

    file = 'test.txt' if args.t else 'input.txt'
    field = 6 if args.t else 70

    with open(file, 'r') as f:
        input = [
            complex(int(line.split(',')[0]), int(line.split(',')[1]))
            for line in f.read().strip().split('\n')
            ]

    print(solution1(input, field))
    print(solution2(input, field))

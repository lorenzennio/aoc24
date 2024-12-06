import numpy as np
import argparse
import time

def ongrid(grid, position):
    if np.any(position<0) or np.any(position>=len(grid)):
        return False
    return True

directions = {
        (-1, 0) : ( 0, 1),
        ( 0, 1) : ( 1, 0),
        ( 1, 0) : ( 0,-1),
        ( 0,-1) : (-1, 0)
        }

def solution1(data):
    obstacles = np.argwhere(data=='#').tolist()
    positions = data=='^'
    guard = np.argwhere(positions)[0]
    step = (-1,0)

    while ongrid(data, guard):
        positions[*guard] = True
        if (guard+step).tolist() in obstacles:
            step = directions[step]
        else:
            guard += step

    return positions


def solution2(data, all_positions):
    obstacles = np.argwhere(data=='#').tolist()
    all_positions = np.argwhere(all_positions).tolist()
    count=0
    for obstruction in all_positions:
        new_obstacles = obstacles + [obstruction]
        guard = np.argwhere(data=='^')[0]
        step = (-1,0)
        hit_from = []
        while ongrid(data, guard):
            if (guard+step).tolist() in new_obstacles:
                hf = [guard.tolist(), (guard+step).tolist()]
                if hf in hit_from:
                    count += 1
                    break
                hit_from.append(hf)
                step = directions[step]
            else:
                guard += step
    return count

if __name__=='__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument('-t', default=False, action=argparse.BooleanOptionalAction)
    args = parser.parse_args()

    file = 'test.txt' if args.t else 'input.txt'

    with open(file, 'r') as f:
        input = f.read().strip().split('\n')
        input = np.array([[c for c in line] for line in input])

    start = time.time()
    sol1 = solution1(input)
    end1 = time.time()
    print(np.sum(sol1), end1-start)
    sol2 = solution2(input, sol1)
    end2 = time.time()
    print(solution2(input, sol1), end2-end1)


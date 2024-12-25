import numpy as np
import argparse
from collections import defaultdict
from heapq import heappop, heappush

def neighbours(p, d, coords):
    n = []
    for s in [1,-1,1j,-1j]:
        if p+s in coords:
            n.append((p+s, ))
    return n

class Complex(complex):
    __lt__=lambda s,o: abs(s) < abs(o)
    __add__=lambda s,o: Complex(complex(s)+o)
    __radd__=lambda s,o: Complex(complex(s)+o)
    __mul__=lambda s,o: Complex(complex(s)*o)
    __rmul__=lambda s,o: Complex(complex(s)*o)

steps = [
    (Complex(  1),    1),
    (Complex( 1j), 1001),
    (Complex(-1j), 1001),
]

def find_paths(start, end, coords):
    paths = []
    best = 1e9
    visited = defaultdict(lambda: 1e10)
    queue = [(0, start, 1, [start])]

    while queue:
        score, pos, dir, path = heappop(queue)

        if score > visited[pos, dir]: continue
        else: visited[pos, dir] = score

        if pos == end and score <= best:
            best = score
            paths += [path]

        for st, sc in steps:
            s = score + sc
            d = dir * st
            p = pos + d
            if p not in coords: continue
            heappush(queue, (s, p, d, path+[p]))

    return best, paths

def solution(data):
    start,  = (k for k,v in data.items() if v=='S')
    end,  = (k for k,v in data.items() if v=='E')
    coords = set([k for k,v in data.items() if v=='.']+[start, end])
    best, paths = find_paths(start, end, coords)
    return best, len(set.union(*map(set, paths)))

if __name__=='__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument('-t', default=False, action=argparse.BooleanOptionalAction)
    args = parser.parse_args()

    file = 'test.txt' if args.t else 'input.txt'

    with open(file, 'r') as f:
        input = {
            col+row*1j:c for row, line in enumerate(f)
            for col, c in enumerate(line.strip())
        }

    print(*solution(input))

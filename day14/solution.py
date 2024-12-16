import re
import argparse
import copy
from collections import Counter
from functools import reduce
import numpy as np

def wrap(p):
    return (((p.real % lx) + lx) % lx +
            (((p.imag % ly) + ly) % ly)*1j)

def step(p):
    return [wrap(p[0]+p[1]), p[1]]

def quadrant(p):
    if   p[0].real < (lx-1)/2 and p[0].imag < (ly-1)/2: return 0
    elif p[0].real > (lx-1)/2 and p[0].imag < (ly-1)/2: return 1
    elif p[0].real < (lx-1)/2 and p[0].imag > (ly-1)/2: return 2
    elif p[0].real > (lx-1)/2 and p[0].imag > (ly-1)/2: return 3

def visualize(pts):
    for y in range(ly):
        line = ['.' for _ in range(lx)]
        for p in pts:
            if p[0].imag == y:
                line[int(p[0].real)] = 'x'
        print(''.join(line))
    print()

def variance(pts):
    x=[p[0].real for p in pts]
    y=[p[0].imag for p in pts]
    return np.std(x), np.std(y)

def solution1(data):
    pts = copy.copy(data)
    var = []
    steps = 100
    for _ in range(steps):
        pts = list(map(step, pts))
        var.append(variance(pts))
    qs = list(map(quadrant, pts))
    count = Counter(qs)
    sf = reduce(lambda x,y: x*y, [v for k, v in count.items() if k != None])
    return sf

def solution2(data):
    pts = copy.copy(data)
    var = []
    p = [pts]
    steps = 10000
    for _ in range(steps):
        pts = list(map(step, pts))
        p.append(pts)
        var.append(variance(pts))
    var = np.array(var)
    for i, v in enumerate(var):
        if v[0]==min(var[:,0]) and v[1]==min(var[:,1]):
            visualize(p[i+1])
            return i+1
    return 0

if __name__=='__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument('-t', default=False, action=argparse.BooleanOptionalAction)
    args = parser.parse_args()

    file = 'test.txt' if args.t else 'input.txt'
    lx = 11 if args.t else 101
    ly =  7 if args.t else 103

    with open(file, 'r') as f:
        input = f.read().strip().split('\n')
        input = map(lambda x: re.findall(r'-?\d+\.?\d*', x), input)
        input = [list(map(int, i)) for i in input]
        input = [[i[0]+i[1]*1j, i[2]+i[3]*1j] for i in input]

    print(solution1(input))
    print(solution2(input))

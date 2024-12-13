import numpy as np
import argparse
import re

def solution1(data):
    tokens = 0
    for d in data:
        da = d[0]
        db = d[1]
        p = d[2]
        det = da[0]*db[1]-da[1]*db[0]
        n = [(p[0]*db[1]-p[1]*db[0])/det, (-p[0]*da[1]+p[1]*da[0])/det]
        if list(map(int, n)) == n:
            tokens+=n[0]*3+n[1]
    return int(tokens)

def solution2(data):
    tokens = 0
    for d in data:
        da = d[0]
        db = d[1]
        p = [x+10000000000000 for x in d[2]]
        det = da[0]*db[1]-da[1]*db[0]
        n = [(p[0]*db[1]-p[1]*db[0])/det, (-p[0]*da[1]+p[1]*da[0])/det]
        if list(map(int, n)) == n:
            tokens+=n[0]*3+n[1]
    return int(tokens)

if __name__=='__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument('-t', default=False, action=argparse.BooleanOptionalAction)
    args = parser.parse_args()

    file = 'test.txt' if args.t else 'input.txt'

    with open(file, 'r') as f:
        input = f.read().strip().split('\n\n')
        input = [i.split('\n')for i in input]
        input = [[list(map(int,re.findall(r'-?\d+', s))) for s in i] for i in input]

    print(solution1(input))
    print(solution2(input))

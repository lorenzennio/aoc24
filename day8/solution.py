import numpy as np
import argparse
from collections import defaultdict
from copy import deepcopy

def coord_pairs(d):
    value_dict = defaultdict(list)

    for key, value in d.items():
        value_dict[value].append(key)

    pairs = []
    for keys in value_dict.values():
        if len(keys) > 1:
            for i in range(len(keys)):
                for j in range(i + 1, len(keys)):
                    pairs.append((keys[i], keys[j]))

    return pairs

def calc_nodes(pair, n):
    delta = pair[1] - pair[0]
    return [pair[0]-i*delta for i in range(1,n)]+[pair[1]+i*delta for i in range(1,n)]

def solution1(data):
    pois = {k:v for k,v in data.items() if v!='.'}
    pairs = coord_pairs(pois)
    for p in pairs:
        nodes = calc_nodes(p, 2)
        for node in nodes:
                if node in data:
                    data[node] = '#'
    return sum(1 for v in data.values() if v == '#')

def solution2(data):
    pois = {k:v for k,v in data.items() if v!='.'}
    pairs = coord_pairs(pois)
    for p in pairs:
        nodes = calc_nodes(p, 100)
        for node in nodes:
                if node in data:
                    data[node] = '#'

    return sum(1 for v in data.values() if v != '.')

if __name__=='__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument('-t', default=False, action=argparse.BooleanOptionalAction)
    args = parser.parse_args()

    file = 'test.txt' if args.t else 'input.txt'

    with open(file, 'r') as f:
        input = {
            row+ col*1j: char for row, line in enumerate(f)
            for col, char in enumerate(line.strip())
            }

    print(solution1(deepcopy(input)))
    print(solution2(deepcopy(input)))

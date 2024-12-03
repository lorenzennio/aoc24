import numpy as np
import argparse
import re

def solution1(data):
    mul = re.findall(r"mul\(\d{1,3},\d{1,3}\)", data)
    pairs = np.array([re.findall(r"\d{1,3}", m) for m in mul]).astype(int)
    sum = np.sum(pairs[:,0]*pairs[:,1])
    return sum

def solution2(data):
    rmul    = r"mul\(\d{1,3},\d{1,3}\)"
    rdo     = r"do\(\)"
    rdont   = r"don't\(\)"
    instructions = re.findall(f"({rmul}|{rdo}|{rdont})", data)
    sum = 0
    on = True
    for i in instructions:
        if re.match(rmul, i) and on:
            nrs = list(map(int, re.findall(r"\d{1,3}", i)))
            sum += nrs[0]*nrs[1]
        elif re.match(rdo, i):
            on = True
        elif re.match(rdont, i):
            on=False
    return sum
    pass

if __name__=='__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument('-t', default=False, action=argparse.BooleanOptionalAction)
    args = parser.parse_args()

    file = 'test.txt' if args.t else 'input.txt'

    with open(file, 'r') as f:
        input = f.read()

    print(solution1(input))
    print(solution2(input))

import numpy as np
import argparse

def solution1(data):
    data = data.T
    data.sort()
    differences = np.abs(np.diff(data, axis=0))
    sum = np.sum(differences)
    return int(sum)

def solution2(data):
    left = data.T[0].tolist()
    right = data.T[1].tolist()
    score = 0
    for nr in left:
        occurance = right.count(nr)
        score += nr*occurance
    return int(score)

if __name__=='__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument('-t', default=False, action=argparse.BooleanOptionalAction)
    args = parser.parse_args()

    file = 'test.txt' if args.t else 'input.txt'

    with open(file, 'r') as f:
        input = np.loadtxt(f)

    print(solution1(input))
    print(solution2(input))

import numpy as np
import argparse

def solution1(data):
    pass

def solution2(data):
    pass

if __name__=='__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument('-t', default=False, action=argparse.BooleanOptionalAction)
    args = parser.parse_args()

    file = 'test.txt' if args.t else 'input.txt'

    with open(file, 'r') as f:
        input = np.loadtxt(f)

    print(solution1(input))
    print(solution2(input))

import numpy as np
import argparse
import awkward as ak

def solution1(data):
    sorted = np.sort(data, axis=1)

    safe_mask = ak.all(data==sorted, axis=1)
    data_masked = data[safe_mask]
    diff = np.abs(data_masked[:,1:] - data_masked[:,:-1])
    safe = ak.sum(ak.all((diff > 0) & (diff < 4), axis=1))

    safe_mask = ak.all(data==sorted[:,::-1], axis=1)
    data_masked = data[safe_mask]
    diff = np.abs(data_masked[:,1:] - data_masked[:,:-1])
    safe += ak.sum(ak.all((diff > 0) & (diff < 4), axis=1))

    return safe

def reduced_reports(report):
    reduced = [report]
    reduced += [np.delete(report, i) for i in range(len(report))]
    return ak.Array(reduced)

def solution2(data):
    safe = 0
    for report in data:
        reports = reduced_reports(report)
        safe += 1 if solution1(reports)>0 else 0
    return safe

if __name__=='__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument('-t', default=False, action=argparse.BooleanOptionalAction)
    args = parser.parse_args()

    file = 'test.txt' if args.t else 'input.txt'

    with open(file, 'r') as f:
        input = f.read()
        input = [i.split(' ') for i in input.split('\n')]
        input = [list(map(int, i)) for i in input]
        input = ak.Array(input)

    print(solution1(input))
    print(solution2(input))

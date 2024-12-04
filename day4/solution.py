import numpy as np
import argparse
from scipy.ndimage import rotate

def solution1(data):
    directions = np.array([
        [ 1,  0],
        [ 1,  1],
        [ 0,  1],
        [-1,  1],
        [-1,  0],
        [-1, -1],
        [ 0, -1],
        [ 1, -1]
    ])
    x_max = len(data[0])-1
    y_max = len(data)-1

    coordX = np.array(np.where(data=='X')).T

    count = 0
    for coord in coordX:
        for direction in directions:
            word = ''
            path = np.array([coord + i*direction for i in range(4)])
            if np.any(path<0): continue
            if np.any(path[:,0]>x_max): continue
            if np.any(path[:,1]>y_max): continue
            for p in path:
                word += data[*p]
            if word=='XMAS': count +=1

    return count

def solution2(data):
    directions = np.array([
        [ 1,  1],
        [-1,  1],
        [-1, -1],
        [ 1, -1]
    ])
    x_max = len(data[0])-1
    y_max = len(data)-1

    coordM = np.array(np.where(data=='M')).T

    coordA =[]
    for coord in coordM:
        for direction in directions:
            word = ''
            path = np.array([coord + i*direction for i in range(3)])
            if np.any(path<0): continue
            if np.any(path[:,0]>x_max): continue
            if np.any(path[:,1]>y_max): continue
            for p in path:
                word += data[*p]
            if word=='MAS': coordA.append(path[1])
    _, counts = np.unique(np.array(coordA), axis=0, return_counts=True)
    pairs = sum(counts==2)
    return pairs

if __name__=='__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument('-t', default=False, action=argparse.BooleanOptionalAction)
    args = parser.parse_args()

    file = 'test.txt' if args.t else 'input.txt'

    with open(file, 'r') as f:
        input = np.loadtxt(f, dtype='U')
        input = np.array([[c for c in line] for line in input])

    print(solution1(input))
    print(solution2(input))

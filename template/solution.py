import numpy as np

def solution(data):
    pass

if __name__=='__main__':
    with open('test.txt', 'r') as f:
        input_test = np.loadtxt(f)

    with open('input.txt', 'r') as f:
        input = np.loadtxt(f)

    data = input if input else input_test

    result = solution(data)

    print(result)
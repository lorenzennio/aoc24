import numpy as np

def solution(data):
    pass

if __name__=='__main__':
    with open('input-test.txt', 'r') as f:
        input_test = f.read()

    with open('input.txt', 'r') as f:
        input = f.read()

    data = input if input else input_test

    result = solution(data)

    print(result)
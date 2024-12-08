import numpy as np
import argparse
import time
from itertools import product

def all_partitions(values):
    if not values:
        return [[]]

    first_element = values[0]
    rest_partitions = all_partitions(values[1:])

    result = []
    for partition in rest_partitions:
        # Create a new partition by adding the first element to an existing subset
        for i in range(len(partition)):
            new_partition = partition[:i] + [[first_element] + partition[i]] + partition[i+1:]
            result.append(new_partition)

        # Add a new subset containing the first element as a separate subset
        result.append([[first_element]] + partition)

    return result

def equation1(eq):
    result, values = eq
    s = np.sum(values)
    p = np.prod(values)
    if result<s and result>p:
        return 0
    elif result==s or result==p:
        return result
    operations = [p for p in product([True, False], repeat=len(values)-1)]
    for operation in operations:
        r = values[0]
        for o,v in zip(operation, values[1:]):
            if o: r += v
            else: r *= v
        if result == r:
            return result
    return 0

def solution1(data):
    results = list(map(equation1, data))
    return sum(results)

def equation2(eq):
    result, values = eq
    operations = [p for p in product([0,1,2], repeat=len(values)-1)]
    for operation in operations:
        r = values[0]
        for o,v in zip(operation, values[1:]):
            if o==0: r = int(str(r) + str(v))
            elif o==1: r += v
            elif o==2: r *= v
        if result == r:
            return result
    return 0

def solution2(data):
    results = list(map(equation2, data))
    return sum(results)

if __name__=='__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument('-t', default=False, action=argparse.BooleanOptionalAction)
    args = parser.parse_args()

    file = 'test.txt' if args.t else 'input.txt'

    with open(file, 'r') as f:
        input = f.read().strip().split('\n')
        input=[[k for k in i.split(': ')] for i in input]
        input = [[int(i[0]),list(map(int,i[1].split(' ')))] for i in input]

    start=time.time()
    sol1 = solution1(input)
    end1 = time.time()
    print(sol1, end1-start)
    sol2=solution2(input)
    end2=time.time()
    print(sol2, end2-end1)

import argparse
from functools import cache

@cache
def rules(stone, d=75):
    if d == 0: return 1

    if stone==0: return rules(1, d-1)

    ll = len(str(stone))

    if ll%2: return rules(stone*2024, d-1)

    return rules(stone // 10**(ll//2), d-1) + rules(stone % 10**(ll//2), d-1)

def solution1(data):
    return sum(map(lambda x: rules(x,25), data))

def solution2(data):
    return sum(map(lambda x: rules(x,75), data))

if __name__=='__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument('-t', default=False, action=argparse.BooleanOptionalAction)
    args = parser.parse_args()

    file = 'test.txt' if args.t else 'input.txt'

    with open(file, 'r') as f:
        input = list(map(int, f.read().split()))

    print(solution1(input))
    print(solution2(input))

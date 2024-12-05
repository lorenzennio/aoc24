import numpy as np
import argparse

def rules_for_manual(rules, manual):
    return np.array([rule for rule in rules if rule[0] in manual and rule[1] in manual])

def tails_of_manual(rules):
    left, right = rules.T
    start = set(left) - set(right)
    end = set(right) - set(left)
    return start.pop(), end.pop()

def is_correct(manual, rules):
    while manual.size>1:
        man_rules = rules_for_manual(rules, manual)
        start, end = tails_of_manual(man_rules)
        if manual[0] != start or manual[-1] != end:
            return False
        else:
            manual = np.delete(manual,[0,-1])
            man_rules = rules_for_manual(man_rules, manual)
            is_correct(manual, man_rules)
    return True

def sum_middle(manuals):
    sum = 0
    for manual in manuals:
        middle_id = int((len(manual)-1)/2)
        sum += manual[middle_id]
    return sum

def sort_manual(manual, rules):
    manual = np.array(manual)
    starts = []
    ends = []
    man_rules = rules_for_manual(rules, manual)
    while manual.size>1:
        start, end = tails_of_manual(man_rules)
        starts.append(start)
        ends.append(end)
        manual = manual[manual!=start]
        manual = manual[manual!=end]
        man_rules = rules_for_manual(man_rules, manual)
    sorted = starts + manual.tolist() + ends[::-1]
    return sorted

def solution1(data):
    rules, manuals = data
    correct_manuals = []
    for manual in manuals:
        manual = np.array(manual)
        if is_correct(manual, rules):
            correct_manuals.append(manual)
    return sum_middle(correct_manuals)

def solution2(data):
    rules, manuals = data
    incorrect_manuals = []
    for manual in manuals:
        manual = np.array(manual)
        if not is_correct(manual, rules):
            incorrect_manuals.append(manual)
    sorted_manuals = []
    for manual in incorrect_manuals:
        sorted_manuals.append(sort_manual(manual, rules))
    return sum_middle(sorted_manuals)

if __name__=='__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument('-t', default=False, action=argparse.BooleanOptionalAction)
    args = parser.parse_args()

    file = 'test.txt' if args.t else 'input.txt'

    with open(file, 'r') as f:
        input = f.read().split('\n\n')
        input = [i.split('\n') for i in input]
        input = [
            [list(map(int, i.split('|'))) for i in input[0]],
            [list(map(int, i.split(','))) for i in input[1]]
        ]

    print(solution1(input))
    print(solution2(input))

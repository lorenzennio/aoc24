import argparse
import re

regA = None
regB = None
regC = None
program = []
instruction = 0
output = []

def combo(operand):
    match operand:
        case 4: return regA
        case 5: return regB
        case 6: return regC
        case _: return operand

def opt(opcode, operand):
    global regA, regB, regC, instruction, output

    match opcode:
        case 0: regA = int(regA / 2**combo(operand))
        case 1: regB = regB ^ operand
        case 2: regB = combo(operand) % 8
        case 3: instruction = instruction if regA==0 else operand-2
        case 4: regB = regB ^ regC
        case 5: output += [ combo(operand) % 8 ]
        case 6: regB = int(regA / 2**combo(operand))
        case 7: regC = int(regA / 2**combo(operand))

def reset(data):
    global regA, regB, regC, program, instruction, output
    regA, regB, regC, program = data
    instruction = 0
    output = []

def run(data, a = None):
    global instruction, regA
    reset(data)
    if a: regA=int(a)
    while True:
        try:
            opcode = program[instruction]
            operand = program[instruction+1]
        except:
            break
        opt(opcode, operand)
        instruction += 2

def solution1(data):
    global instruction
    run(data)
    return ','.join(map(str,output))

regAs = []
def find(data, a, pow):
    global regAs
    if pow >=0:
        for n in range(8):
            run(data, a+n*8**pow)
            if output==program: regAs.append(a+n*8**pow)
            if output[pow:]==program[pow:]:
                find(data, a+n*8**pow, pow-1)

def solution2(data):
    maxpow = 0
    run(data, 8**maxpow)
    while len(output) != len(program):
        maxpow +=1
        run(data, 8**maxpow)
    find(data, 0, maxpow)
    return min(regAs)

if __name__=='__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument('-t', default=False, action=argparse.BooleanOptionalAction)
    args = parser.parse_args()

    file = 'test.txt' if args.t else 'input.txt'

    with open(file, 'r') as f:
        reg, pro = f.read().strip().split('\n\n')
        a, b, c = list(map(int, re.findall(r'\b\d+\b', reg)))
        p = list(map(int, re.findall(r'\b\d+\b', pro)))

    print(solution1((a, b, c, p)))
    print(solution2((a, b, c, p)))

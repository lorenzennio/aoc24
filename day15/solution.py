import argparse

step = {
    '^': -1j,
    'v':  1j,
    '<': -1,
    '>':  1,
}

def solution1(warehouse, instructions):
    border = [k for k,v in warehouse.items() if v=='#']
    boxes = [k for k,v in warehouse.items() if v=='O']
    robot = [k for k,v in warehouse.items() if v=='@'][0]
    for i in instructions:
        new_robot = robot+step[i]
        if new_robot in border:
            continue
        elif new_robot in boxes:
            tomove = [new_robot]
            while tomove[-1]+step[i] in boxes:
                tomove.append(tomove[-1]+step[i])
            if tomove[-1]+step[i] in border:
                continue
            boxes = [b+step[i] if b in tomove else b for b in boxes]
        robot=new_robot

    s = sum([b.real+b.imag*100 for b in boxes])
    return int(s)

def in_boxes(coords, boxes):
    return [b for b in boxes if any(c in coords for c in b)]

def to_check(boxes, step):
    c = []
    for box in boxes:
        if step==1:
            c.append(box[1]+1)
        elif step==-1:
            c.append(box[0]-1)
        else:
            c.append(box[0]+step)
            c.append(box[1]+step)
    return list(set(c))

def move_boxes(boxes, step):
    return [[b[0]+step, b[1]+step] for b in boxes]

def visualize(warehouse, boxes, border, robot):
    warehouse = {k:'.' for k,v in warehouse.items()}
    for k in border: warehouse[k]='#'
    for b in boxes:
        warehouse[b[0]]='['
        warehouse[b[1]]=']'
    warehouse[robot]='@'
    line_id=0
    line= ''
    for k,v in warehouse.items():
        if k.imag>line_id:
            print(line)
            line_id+=1
            line=''
        line += v
    print(line)

def solution2(warehouse, instructions):
    border = [k for k,v in warehouse.items() if v=='#']
    boxes = [[k,k+1] for k,v in warehouse.items() if v=='[']
    robot = [k for k,v in warehouse.items() if v=='@'][0]
    for i in instructions:
        new_robot = robot+step[i]
        if new_robot in border:
            continue
        elif len(in_boxes([new_robot], boxes)):
            run=True
            tomove = [[b for b in boxes if new_robot in b]]
            while len(tomove[-1])>0:
                check = to_check(tomove[-1], step[i])
                if any(c in border for c in check):
                    run=False
                    break
                tomove.append(in_boxes(check, boxes))
            if run:
                tomove = [b for bb in tomove for b in bb]
                boxes = [[b[0]+step[i], b[1]+step[i]] if b in tomove else b for b in boxes]
                robot=new_robot
        else:
            robot=new_robot
    visualize(warehouse, boxes, border, robot)
    s = sum([b[0].real+b[0].imag*100 for b in boxes])
    return int(s)

if __name__=='__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument('-t', default=False, action=argparse.BooleanOptionalAction)
    args = parser.parse_args()

    file = 'test.txt' if args.t else 'input.txt'

    with open(file, 'r') as f:
        warehouse, instructions = f.read().strip().split('\n\n')
        warehouse1 = {
            col+row*1j:c for row, line in enumerate(warehouse.split('\n'))
            for col, c in enumerate(line.strip())
        }
        warehouse2 = warehouse.replace('#', '##')
        warehouse2 = warehouse2.replace('O', '[]')
        warehouse2 = warehouse2.replace('.', '..')
        warehouse2 = warehouse2.replace('@', '@.')
        warehouse2 = {
            col+row*1j:c for row, line in enumerate(warehouse2.split('\n'))
            for col, c in enumerate(line.strip())
        }
        instructions = instructions.replace('\n', '')

    print(solution1(warehouse1, instructions))
    print(solution2(warehouse2, instructions))

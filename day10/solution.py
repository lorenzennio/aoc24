import argparse

visited=[]

def solution(data):
    global visited

    def walk(pos):
        global visited
        for step in [1, -1, 1j, -1j]:
            npos = pos + step
            if npos in data:
                if data[npos] == data[pos] + 1:
                    visited += [npos]
                    walk(npos)
            else:
                continue
        return

    starts = [k for k, v in data.items() if v == 0]

    score=0
    rating=0
    for s in starts:
        visited = [s]
        walk(s)
        points = [data[v] for v in list(set(visited))]
        score += sum([1 for p in points if p==9])
        points = [data[v] for v in visited]
        rating += sum([1 for p in points if p==9])
        visited = []

    return score, rating

if __name__=='__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument('-t', default=False, action=argparse.BooleanOptionalAction)
    args = parser.parse_args()

    file = 'test.txt' if args.t else 'input.txt'

    with open(file, 'r') as f:
        input = {
            row+col*1j: int(char) for row, line in enumerate(f)
            for col, char in enumerate(line.strip())
            }
    sol1, sol2 = solution(input)
    print(sol1)
    print(sol2)

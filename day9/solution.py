import numpy as np
import argparse

def solution1(data):
    d = [[f'{int(i/2)}']*int(v) if i%2==0 else ['.']*int(v) for i,v in enumerate(data)]
    d = [x for m in d for x in m]
    for i, v in enumerate(d):
        if i > len(d): break
        while d[-1]=='.': d = d[:-1]
        if v=='.':
            d[i] = d[-1]
            d = d[:-1]
    return sum([i*int(v) for i,v in enumerate(d)])

def solution2(data):
    d = [[f'{int(i/2)}']*int(v) if i%2==0 else '.'*int(v) for i,v in enumerate(data)]
    d = [e for e in d if e!='']
    df = [f for f in d if ('.' not in f) and f != ''][::-1]

    for f in df:
        #try to find a place for f
        lf = len(f)
        space = next((i for i,s in enumerate(d) if '.' in s and len(s) >= lf), None)
        if space is not None:
            ls = len(d[space])
            #if we find one, place f in that space
            d[space] = f
            # add correct space a the end of f
            if ls-lf>0: d.insert(space+1, '.'*(ls-lf))
            # find f in d, from back
            fi = len(d)-1-next((i for i,ff in enumerate(reversed(d)) if ff==f), None)
            # replace f with corresponding space
            d[fi] = '.'*len(f)
            # concatenate spaces
            cl = '.' in d[fi-1]
            try:
                cu = '.' in d[fi+1]
            except IndexError:
                cu = False
            if cl and cu:
                d[fi-1] += d[fi]+d[fi+1]
                del d[fi]
                del d[fi]
            elif cl and not cu:
                d[fi-1] += d[fi]
                del d[fi]
            elif not cl and cu:
                d[fi] += d[fi+1]
                del d[fi+1]
    d = [x for m in d for x in m]
    return sum([i*int(v) for i,v in enumerate(d) if v!='.'])

if __name__=='__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument('-t', default=False, action=argparse.BooleanOptionalAction)
    args = parser.parse_args()

    file = 'test.txt' if args.t else 'input.txt'

    with open(file, 'r') as f:
        input = f.read().strip()

    print(solution1(input))
    print(solution2(input))

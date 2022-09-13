import sys
from math import ceil
#input functions
readint = lambda: int(sys.stdin.readline())
readints = lambda: map(int,sys.stdin.readline().split())
readar = lambda: list(map(int,sys.stdin.readline().split()))
flush = lambda: sys.stdout.flush()

"""
0 2 1 0 0 3 1 0 0 1 4 0 0 2 1 0

"""

def solve(n):
    if n == 1:
        print("? 1 2",flush=True)
        return readint()
    candidates = list()
    for j in range(2**(n-2)):
        a = 4*j+1
        b = 4*j+4
        x = "? "+str(a)+" "+str(b)+"\n"
        sys.stdout.write(x)
        flush()
        res = readint()
        if res == 1:
            candidates.append(a)
            candidates.append(4*j+3)
        elif res == 2:
            candidates.append(4*j+2)
            candidates.append(b)
        else:
            candidates.append(4*j+2)
            candidates.append(4*j+3)
    while len(candidates) != 1:
        r = list()
        for k in range(len(candidates)//4):
            a = candidates[4*k]
            b = candidates[4*k+3]
            c = candidates[4*k+1]
            d = candidates[4*k+2]
            if a == -1 or c == -1:
                if a == -1: r.append(c)
                else: r.append(a)
                if b == -1: r.append(d)
                elif d == -1: r.append(b)
                else:
                    x = "? "+str(d)+" "+str(b)+"\n"
                    sys.stdout.write(x)
                    flush()
                    res = readint()
                    if res == 1:
                        r.append(d)
                    elif res == 2:
                        r.append(b)
                    else:
                        r.append(-1)
            elif d == -1 or b == -1:
                if b == -1: r.append(d)
                else: r.append(b)
                if a == -1: r.append(c)
                elif c == -1: r.append(a)
                else:
                    x = "? "+str(a)+" "+str(c)+"\n"
                    sys.stdout.write(x)
                    flush()
                    res = readint()
                    if res == 1:
                        r.append(a)
                    elif res == 2:
                        r.append(c)
                    else:
                        r.append(-1)

            else:
                x = "? "+str(a)+" "+str(b)+"\n"
                sys.stdout.write(x)
                flush()
                res = readint()
                if res == 1:
                    b = candidates[4*k+1]
                    x = "? "+str(a)+" "+str(b)+"\n"
                    sys.stdout.write(x)
                    flush()
                    res = readint()
                    if res == 1:
                        r.append(a)
                    elif res == 2:
                        r.append(b)
                    else:
                        r.append(-1)
                    r.append(candidates[4*k+2])
                elif res == 2:
                    r.append(candidates[4*k+1])
                    a = candidates[4*k+2]
                    x = "? "+str(a)+" "+str(b)+"\n"
                    sys.stdout.write(x)
                    flush()
                    res = readint()
                    if res == 1:
                        r.append(a)
                    elif res == 2:
                        r.append(b)
                    else:
                        r.append(-1)
                else:
                    r.append(candidates[4*k+1])
                    r.append(candidates[4*k+2])
        if len(candidates) % 4 == 1: r.append(candidates[-1])
        elif len(candidates) % 4 == 2:
            a = candidates[-2]
            b = candidates[-1]
            x = "? "+str(a)+" "+str(b)+"\n"
            sys.stdout.write(x)
            flush()
            res = readint()
            if res == 1:
                r.append(a)
            elif res == 2:
                r.append(b)
        elif len(candidates) % 4 == 3:
            r.append(candidates[-3])
            a = candidates[-2]
            b = candidates[-1]
            x = "? "+str(a)+" "+str(b)+"\n"
            sys.stdout.write(x)
            flush()
            res = readint()
            if res == 1:
                r.append(a)
            elif res == 2:
                r.append(b)
        candidates = r
    return candidates[0]
    
snth = readint()
for i in range(snth):
    n = readint()
    if n > 17 or n < 1: break
    print("!",str(solve(n)))
    if i + 1 != snth: flush()
    

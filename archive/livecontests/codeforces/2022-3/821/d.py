import sys

#input functions
readint = lambda: int(sys.stdin.readline())
readints = lambda: map(int,sys.stdin.readline().split())
readar = lambda: list(map(int,sys.stdin.readline().split()))
flush = lambda: sys.stdout.flush()

def solve(n,x,y,a,b):
    e = list()
    for j in range(n):
        if a[j] != b[j]: e.append(j)
    xx = len(e)
    if xx % 2 == 1: return -1
    ans = 0
    if n == 3:
        if e[0]+1 == e[1]: return x
        else: return y
    if n == 4 and e[0] == 1 and e[0] == 2: return x
    if xx == 2 and (e[0]+1) == e[1]: #special case
        return min(x,2*y)
    return (xx//2)*y
"""
    else:
        it = 0
        pairs = 0
        while it < xx-1:
            if e[it]+1 == e[it+1]:
                pairs += 1
                it += 1
            it += 1
        return x*pairs+y*((xx//2)-pairs)
"""
for i in range(readint()):
    n,x,y = readints()
    a = input()
    b = input()
    print(solve(n,x,y,a,b))

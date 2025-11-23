import sys

#input functions
readint = lambda: int(sys.stdin.readline())
readints = lambda: map(int,sys.stdin.readline().split())
readar = lambda: list(map(int,sys.stdin.readline().split()))
flush = lambda: sys.stdout.flush()
readin = lambda: sys.stdin.readline()[:-1]
readins = lambda: map(str,sys.stdin.readline().split())


def f(ar,s,x,k):
    v = k
    painting = False
    for i in range(len(ar)):
        if ar[i] > x:
            if s[i] == "B": # must paint
                if not painting:
                    painting = True
                    v -= 1
                    if v == -1: return False
            else:
                painting = False
    return True
    
for _ in range(readint()):
    n,k = readints()
    s = readin()
    ar = readar()
    low = 0
    high = 1000000000
    while high-low > 1:
        mid = (low+high)//2
        if f(ar,s,mid,k): high = mid
        else: low = mid
    if f(ar,s,low,k): print(low)
    else: print(high)

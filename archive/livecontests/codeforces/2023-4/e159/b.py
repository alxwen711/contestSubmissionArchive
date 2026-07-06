import sys

#input functions
readint = lambda: int(sys.stdin.readline())
readints = lambda: map(int,sys.stdin.readline().split())
readar = lambda: list(map(int,sys.stdin.readline().split()))
flush = lambda: sys.stdout.flush()

def f(x,n,p,l,t):
    taskcount = (n+6)//7
    score = (x*l)+(min(2*x,taskcount)*t)
    return score >= p

for _ in range(readint()):
    n,p,l,t = readints()
    low = 1
    high = n
    while high-low > 1:
        mid = (low+high)//2
        if f(mid,n,p,l,t): high = mid
        else: low = mid
    if f(low,n,p,l,t): print(n-low)
    else: print(n-high)

import sys

#input functions
readint = lambda: int(sys.stdin.readline())
readints = lambda: map(int,sys.stdin.readline().split())
readar = lambda: list(map(int,sys.stdin.readline().split()))
flush = lambda: sys.stdout.flush()
readin = lambda: sys.stdin.readline()[:-1]
readins = lambda: map(str,sys.stdin.readline().split())

def f(ar,n,x):
    ansa,ansb = 0,0
    for i in range(x-1,-1,-1):
        if ar[i] != ar[x]:
            ansa = i+1
            break
    for j in range(x+1,n):
        if ar[j] != ar[x]:
            ansb = n-j
            break
    return max(ansa,ansb)

for _ in range(readint()):
    n = readint()
    ar = readar()
    ar.sort()
    l = n//2
    r = (n+1)//2
    print(min(f(ar,n,l),f(ar,n,r)))

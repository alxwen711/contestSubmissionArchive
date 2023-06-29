import sys

#input functions
readint = lambda: int(sys.stdin.readline())
readints = lambda: map(int,sys.stdin.readline().split())
readar = lambda: list(map(int,sys.stdin.readline().split()))
flush = lambda: sys.stdout.flush()

def solve(a,b,c,k):
    x = 0
    cmin = 10**(c-1)
    cmax = 10**c-1
    bmin = 10**(b-1)
    bmax = 10**b-1
    for i in range(10**(a-1),10**a):
        l = max(cmin-i,bmin)
        h = min(cmax-i,bmax)
        f = max(0,h-l+1)
        if k > f: k -= f
        else:
            aa = i
            bb = l+k-1
            print(aa,"+",bb,"=",aa+bb)
            return
    print(-1)
    return

for i in range(readint()):
    a,b,c,k = readints()
    solve(a,b,c,k)

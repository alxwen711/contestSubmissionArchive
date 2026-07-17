import sys

#input functions
readint = lambda: int(sys.stdin.readline())
readints = lambda: map(int,sys.stdin.readline().split())
readar = lambda: list(map(int,sys.stdin.readline().split()))
flush = lambda: sys.stdout.flush()

def setar(x):
    br = list()
    for i in range(4):
        br.append(x % 2)
        x = x // 2
    return br

def solve(n,u,r,d,l):
    free = n-2
    if max(free,u,r,d,l) == free: return "YES" #no corners needed
    #try each corner setup?
    for i in range(16):
        ar = setar(i)
        a,b,c,e = u,r,d,l
        if ar[0] == 1:
            a -= 1
            e -= 1
        if ar[1] == 1:
            a -= 1
            b -= 1
        if ar[2] == 1:
            c -= 1
            e -= 1
        if ar[3] == 1:
            b -= 1
            c -= 1
        if max(free,a,b,c,e) == free and min(0,a,b,c,e) == 0: return "YES"
    return "NO"
            

for i in range(readint()):
    n,u,r,d,l = readints()
    print(solve(n,u,r,d,l))
    

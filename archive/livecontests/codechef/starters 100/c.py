import sys

#input functions
readint = lambda: int(sys.stdin.readline())
readints = lambda: map(int,sys.stdin.readline().split())
readar = lambda: list(map(int,sys.stdin.readline().split()))
flush = lambda: sys.stdout.flush()

def gen(n,ar):
    cr = list()
    inc = (n+1)//2
    for a in range(n//2):
        cr.append(ar[a])
        cr.append(ar[a+inc])
    if n % 2 == 1: cr.append(ar[inc-1])
    for r in range(n-2):
        x = cr[r]-cr[r+1]
        y = cr[r+1]-cr[r+2]
        if x*y >= 0: return -1
    return cr
    
for i in range(readint()):
    n = readint()
    ar = readar()
    ar.sort()
    br = gen(n,ar)
    if br != -1: print(*br)
    else:
        ar.reverse()
        br = gen(n,ar)
        if br != -1: print(*br)
        else: print(-1)

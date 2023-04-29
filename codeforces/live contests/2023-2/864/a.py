import sys

#input functions
readint = lambda: int(sys.stdin.readline())
readints = lambda: map(int,sys.stdin.readline().split())
readar = lambda: list(map(int,sys.stdin.readline().split()))
flush = lambda: sys.stdout.flush()

def edge(a,b,n,m):
    if a == 1 and b == 1: return 2
    if a == n and b == 1: return 2
    if a == 1 and b == m: return 2
    if a == n and b == m: return 2
    if a == 1: return 1
    if a == n: return 1
    if b == 1: return 1
    if b == m: return 1
    return 0

for i in range(readint()):
    n,m = readints()
    a,b,c,d = readints()
    x = edge(a,b,n,m)
    y = edge(c,d,n,m)
    print(4-max(x,y))

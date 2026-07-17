import sys

#input functions
readint = lambda: int(sys.stdin.readline())
readints = lambda: map(int,sys.stdin.readline().split())
readar = lambda: list(map(int,sys.stdin.readline().split()))
flush = lambda: sys.stdout.flush()
readin = lambda: sys.stdin.readline()[:-1]
readins = lambda: map(str,sys.stdin.readline().split())

"""
bitset method could work?
either all even or all odd, else impossible
80 40 20 10
40 0 20 30
20 20 0 10
10 10 10 0
5 5 5 5
0 0 0 0
take largest, divided by 2?
"""
def solve(n,ar):
    for i in range(n-1):
        if ar[i] % 2 != ar[i+1] % 2:
            print(-1)
            return
    ans = list()
    if ar[0] % 2 == 1:
        ans.append(1)
        for a in range(n):
            ar[a] = abs(ar[a]-1)
    v = max(ar)
    while v != 0:
        c = v//2
        if v == 1: c += 1
        ans.append(c)
        for b in range(n):
            ar[b] = abs(ar[b]-c)
        v = max(ar)
    print(len(ans))
    print(*ans)
    
for _ in range(readint()):
    n = readint()
    ar = readar()
    solve(n,ar)

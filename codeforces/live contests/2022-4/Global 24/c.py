import sys

#input functions
readint = lambda: int(sys.stdin.readline())
readints = lambda: map(int,sys.stdin.readline().split())
readar = lambda: list(map(int,sys.stdin.readline().split()))
flush = lambda: sys.stdout.flush()
"""
no cycle of 3
x - x is only case of connecting same
add edges when possible with each new node?
bidirectional graph
"""

def solve(n,ar):
    best = 0
    for j in range(n-1):
        if ar[j] != ar[j+1]:
            x = min(j+1,n-j-1)
            if x > best: best = x
            else: break
    if best == 0: return n//2
    return best*(n-best)

for i in range(readint()):
    n = readint()
    ar = readar()
    ar.sort()
    print(solve(n,ar))

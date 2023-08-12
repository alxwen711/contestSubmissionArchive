import sys

#input functions
readint = lambda: int(sys.stdin.readline())
readints = lambda: map(int,sys.stdin.readline().split())
readar = lambda: list(map(int,sys.stdin.readline().split()))
flush = lambda: sys.stdout.flush()

def solve(n,ar):
    if n == 1: return "NO"
    a = ar.count(1)
    s = sum(ar)
    mv = n+a
    if mv > s: return "NO"
    return "YES"

for i in range(readint()):
    n = readint()
    ar = readar()
    print(solve(n,ar))
    

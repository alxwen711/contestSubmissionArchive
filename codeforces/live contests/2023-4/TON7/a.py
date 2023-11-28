import sys

#input functions
readint = lambda: int(sys.stdin.readline())
readints = lambda: map(int,sys.stdin.readline().split())
readar = lambda: list(map(int,sys.stdin.readline().split()))
flush = lambda: sys.stdout.flush()

def solve(n,ar):
    if ar[0] != 1: return "NO"
    return "YES"

for _ in range(readint()):
    n = readint()
    ar = readar()
    print(solve(n,ar))

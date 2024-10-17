import sys

#input functions
readint = lambda: int(sys.stdin.readline())
readints = lambda: map(int,sys.stdin.readline().split())
readar = lambda: list(map(int,sys.stdin.readline().split()))
flush = lambda: sys.stdout.flush()
readin = lambda: sys.stdin.readline()[:-1]
readins = lambda: map(str,sys.stdin.readline().split())
"""
both players have cards going from 1 to n
m is greater than n
"""
def solve(n,m):
    t = n*n+n
    r = t % m
    if r > 0 and r <= n: return "Bob"
    return "Alice"
    
    
for _ in range(readint()):
    n,m = readints()
    print(solve(n,m))

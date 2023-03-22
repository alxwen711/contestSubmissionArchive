import sys

#input functions
readint = lambda: int(sys.stdin.readline())
readints = lambda: map(int,sys.stdin.readline().split())
readar = lambda: list(map(int,sys.stdin.readline().split()))
flush = lambda: sys.stdout.flush()

"""
is there value y from 1 to p such that
p(p+1)/2+x % n =
odd value can brute force until n
even value brute forces until 2n?
"""

def solve(n,x,p):
    limit = n
    if n % 2 == 0: limit*=2
    for i in range(1,min(limit,p)+1):
        x = (x+i) % n
        if x == 0: return "Yes"
    return "No"
    

for i in range(readint()):
    n,x,p = readints()
    print(solve(n,x,p))

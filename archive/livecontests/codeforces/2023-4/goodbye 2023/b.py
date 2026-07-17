import sys
from math import lcm

#input functions
readint = lambda: int(sys.stdin.readline())
readints = lambda: map(int,sys.stdin.readline().split())
readar = lambda: list(map(int,sys.stdin.readline().split()))
flush = lambda: sys.stdout.flush()

"""
x is not considered a divisor of x
"""

def solve(a,b):
    x = lcm(a,b)
    if x == b: x *= (b//a)
    return x

for _ in range(readint()):
    a,b = readints()
    print(solve(a,b))

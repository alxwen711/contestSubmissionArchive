import sys
from math import log
#input functions
readint = lambda: int(sys.stdin.readline())
readints = lambda: map(int,sys.stdin.readline().split())
readar = lambda: list(map(int,sys.stdin.readline().split()))
flush = lambda: sys.stdout.flush()

"""
A can only be from 2 to 6

1 roll of A -> covers up to A-1
2 rolls of A -> covers up to A*A-1

ABCDEF vals rolled covers up to product-1
on average you are multiplying by 3.5

2/3 1 roll -> 13.33333
1/6 roll+20 -> 6.6666666
1/6 loop back -> 12?

* by 6/5 to account for the 1 case
"""

def f(x): # how many dice rolls to multiply 1 to x
    if x == 1: return 0
    return log(x)/log(3.5)

n,a,x,y = readints()
b = 1
best = 9999999999999999999999999
bc = 0
while True:
    sc = f(n//b+1)
    best = min(best,bc+(sc*y))
    if sc == 0: break
    bc += x
    b *= a
print(best)

import sys

#input functions
readint = lambda: int(sys.stdin.readline())
readints = lambda: map(int,sys.stdin.readline().split())
readar = lambda: list(map(int,sys.stdin.readline().split()))
flush = lambda: sys.stdout.flush()
readin = lambda: sys.stdin.readline()[:-1]
readins = lambda: map(str,sys.stdin.readline().split())
"""
0,a,b
then next is last 2 summed - 3rd last
full seq is 0,a,b,a+b,2b,a+2b,3b,a+3b

set up sequence of b,2b,3b,4b...
figure out where the +a cases occur

a < b: 0,a,b,a+b,2b...
a < 2b: 0,b,a,2b,a+b...
a < 3b: 0,b,2b,a,3b,a+b...
"""

for _ in range(readint()):
    a,b,k = readints()
    k -= 1
    rounds = a//b
    if k <= rounds: print(b*k)
    else:
        x = k-rounds
        if x % 2 == 1: # a+b case
            print(a+b*(x//2))
        else:
            print(b*(rounds+x//2))

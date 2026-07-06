import sys

#input functions
readint = lambda: int(sys.stdin.readline())
readints = lambda: map(int,sys.stdin.readline().split())
readar = lambda: list(map(int,sys.stdin.readline().split()))
flush = lambda: sys.stdout.flush()
readin = lambda: sys.stdin.readline()[:-1]
readins = lambda: map(str,sys.stdin.readline().split())

"""
011010110 -> 001110110
6 swaps -> 4 swaps

3+ swaps -> -2
0101 -> 0011
101 -> 011

2 swaps is 10 or 010, both are -1

1 swap (01), no change

"""

for _ in range(readint()):
    n = readint()
    s = readin()
    swapcount = 0
    for i in s:
        if int(i) != swapcount % 2: swapcount += 1
    if swapcount == 0: print(n)
    else: print(n+max(1,swapcount-2))

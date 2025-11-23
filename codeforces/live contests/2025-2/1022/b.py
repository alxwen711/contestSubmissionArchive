import sys

#input functions
readint = lambda: int(sys.stdin.readline())
readints = lambda: map(int,sys.stdin.readline().split())
readar = lambda: list(map(int,sys.stdin.readline().split()))
flush = lambda: sys.stdout.flush()
readin = lambda: sys.stdin.readline()[:-1]
readins = lambda: map(str,sys.stdin.readline().split())

"""
possible cases:
under/equal bit count: same value
even diff: add diff (use 1's)
odd diff: diff+1 only if target is not 1
odd diff AND 1 target: wack
0 even diff: add diff
0 odd diff: bruh

2 1 -> 5
4 1 -> 7?
"""

for _ in range(readint()):
    n,x = readints()
    v = x
    bit = 0
    while v != 0:
        bit += v % 2
        v //= 2
    if bit == 0: # 0 case
        if n == 1: print(-1)
        elif n % 2 == 0: print(n)
        else: print(n+3)
    elif bit >= n: print(x)
    else:
        diff = n-bit
        if diff % 2 == 0: print(x+diff)
        elif x != 1: print(x+diff+1)
        else: print(x+diff+3)

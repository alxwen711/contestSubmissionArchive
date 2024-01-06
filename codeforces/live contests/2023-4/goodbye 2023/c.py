import sys

#input functions
readint = lambda: int(sys.stdin.readline())
readints = lambda: map(int,sys.stdin.readline().split())
readar = lambda: list(map(int,sys.stdin.readline().split()))
flush = lambda: sys.stdout.flush()

"""
each operation is to add/merge 2 values, if odd sum, -1
either way result must be even
masha strategy is to take pairs of odds
olya wants to take odd/even pairs to get -1 effect

0,-1,0,-1,-2,-1,-2,-3,-2,-3,-4,-3

"""

def f(odd):
    x = odd//3
    if odd % 3 == 1: x += 1
    return x

for _ in range(readint()):
    n = readint()
    ar = readar()
    odd = 0
    br = list()
    ans = 0
    for i in range(n):
        ans += ar[i]
        if ar[i] % 2 == 1: odd += 1
        br.append(ans-f(odd))
    br[0] = ar[0]
    print(*br)

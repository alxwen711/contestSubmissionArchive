import sys

#input functions
readint = lambda: int(sys.stdin.readline())
readints = lambda: map(int,sys.stdin.readline().split())
readar = lambda: list(map(int,sys.stdin.readline().split()))
flush = lambda: sys.stdout.flush()

"""
even with no luck, can you win inf coins?
Possible to use a martingale strategy?
"""

def solve(k,x,a):
    if x >= a: return "NO" #could lose all initial bets
    ans = 1
    for i in range(x):
        v = (ans+k-1)//(k-1)
        ans += v
    if ans > a: return "NO"
    return "YES"

for _ in range(readint()):
    k,x,a = readints()
    print(solve(k,x,a))

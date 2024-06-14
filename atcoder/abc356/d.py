import sys

#input functions
readint = lambda: int(sys.stdin.readline())
readints = lambda: map(int,sys.stdin.readline().split())
readar = lambda: list(map(int,sys.stdin.readline().split()))
flush = lambda: sys.stdout.flush()

"""
should be possible to get popcount more easily from
0 to 2**x-1, using this traverse bit by bit to get answer
if 1: possibly increment counter, add to 2**x-1 sum
if 0: skip bit

0,1,4,12,32


new method: just go full division troll
"""

n,m = readints()
ans = 0
v = 1
while v <= m:
    if v & m != 0: # count occurance of this bit
        rounds = (n+1)//v
        ans += (rounds//2)*v
        if rounds % 2 == 1: ans += n+1-(rounds*v)
    v *= 2
print(ans % 998244353)

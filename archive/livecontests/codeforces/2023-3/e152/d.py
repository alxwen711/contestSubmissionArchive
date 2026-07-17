import sys

#input functions
readint = lambda: int(sys.stdin.readline())
readints = lambda: map(int,sys.stdin.readline().split())
readar = lambda: list(map(int,sys.stdin.readline().split()))
flush = lambda: sys.stdout.flush()

"""
this might be dp?
0 1 0 0 1 0 2 example array
1 1 2 3 3 4 4
track if have +1 credit and if credit used to paint prev tile

0 0 2 0 0
1 2 2 2 3

0 2 0 1 0
"""

n = readint()
ar = readar()
dp = [1]*n
plus = False
prev = True

if ar[0] != 0:
    plus = True

for i in range(1,n):
    if ar[i] == 0: #0 case
        if plus:
            prev = False
            plus = False
            dp[i] = dp[i-1]
        else:
            prev = True
            dp[i] = dp[i-1]+1
    elif ar[i] == 1: #1 case
        if plus:
            plus = True
            prev = True
            dp[i] = dp[i-1]
        elif prev:
            prev = True
            dp[i] = dp[i-1]
        else: #prev is already covered but no extra
            plus = True
            prev = True
            dp[i] = dp[i-1]+1
    else: #2 case
        if plus:
            prev = False
            plus = True
            dp[i] = dp[i-1]
        elif prev:
            prev = True
            plus = True
            dp[i] = dp[i-1]
        else:
            prev = True
            plus = True
            dp[i] = dp[i-1]+1
print(dp[-1])

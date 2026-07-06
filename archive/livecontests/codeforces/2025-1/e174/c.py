import sys

#input functions
readint = lambda: int(sys.stdin.readline())
readints = lambda: map(int,sys.stdin.readline().split())
readar = lambda: list(map(int,sys.stdin.readline().split()))
flush = lambda: sys.stdout.flush()
readin = lambda: sys.stdin.readline()[:-1]
readins = lambda: map(str,sys.stdin.readline().split())

"""
all middle elements must be 2?
12222223
"""

mod = 998244353

for _ in range(readint()):
    n = readint()
    ar = readar()
    dp = [1,0,0,0]
    for i in ar:
        if i == 1:
            dp = [dp[0],(dp[1]+dp[0]) % mod,dp[2],dp[3]]
        elif i == 2:
            dp = [dp[0],dp[1],(2*dp[2]+dp[1]) % mod,dp[3]]
        elif i == 3:
            dp = [dp[0],dp[1],dp[2],(dp[3]+dp[2]) % mod]
    print(dp[3])

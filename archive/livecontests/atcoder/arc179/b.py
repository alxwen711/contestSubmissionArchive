import sys

#input functions
readint = lambda: int(sys.stdin.readline())
readints = lambda: map(int,sys.stdin.readline().split())
readar = lambda: list(map(int,sys.stdin.readline().split()))
flush = lambda: sys.stdout.flush()

"""
2**10 cases for valid values to use, likely involves a dp here
"""

m,n = readints()
ar = readar()
cases = 2**m
riv = [0]*m
for ii in range(m):
    riv[ar[ii]-1] += (2**ii)
dp = [0]*cases
dp[-1] = 1
mod = 998244353

for i in range(n):
    #print(dp)
    prev = dp
    dp = [0]*cases
    for a in range(cases):
        if prev[a] != 0:
            v = 1
            for b in range(m):
                if v & a != 0: # valid option
                    cv = (a - v) | riv[b]
                    dp[cv] = (dp[cv]+prev[a]) % mod
                v *= 2
#print(dp)
print(sum(dp) % mod)

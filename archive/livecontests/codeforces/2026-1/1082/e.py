import sys

#input functions
readint = lambda: int(sys.stdin.readline())
readints = lambda: map(int,sys.stdin.readline().split())
readar = lambda: list(map(int,sys.stdin.readline().split()))
flush = lambda: sys.stdout.flush()
readin = lambda: sys.stdin.readline()[:-1]
readins = lambda: map(str,sys.stdin.readline().split())

"""
push right, consider all subsequences for regular count
only positions with sum at least 1?

conditions that make a valid shift:
- anything containing no ( or no )
- if ( is the last char, then automatically yes
- else starting point must be a 2 or higher if receiving )?
- if there are several ) starting, the consecutive ( must all be score 2+

[empty,
only 2+ (,
only (,
only ),
ends in ( and contains 1-,
ends in ( and only 2+ (,
ends in ) and contains 1-,
ends in ) and only 2+ (,]

last testcase:
1012321210
()((())())
101 2 3 2 1210
()( ( ( ) )())
101 0 1 2 1210
()( ) ( ( )())

something is off with this case work
"""
from copy import deepcopy

m = 998244353
for _ in range(readint()):
    n = readint()
    s = readin()
    v = 0
    ar = list()
    for i in s:
        if i == "(": v += 1
        else: v -= 1
        ar.append(v)
    dp = [1,0,0,0,0,0,0,0]
    print(ar)
    for i in range(n):
        ndp = deepcopy(dp)
        if s[i] == ")":
            """
            [empty,
            only 2+ (,
            only ( contains 1-,
            only ),
            ends in ( and contains 1-,
            ends in ( and only 2+ (,
            ends in ) and contains 1-,
            ends in ) and only 2+ (,]
            """
            ndp[0] = (ndp[0]) % m
            ndp[1] = (ndp[1]) % m
            ndp[2] = (ndp[2]) % m            
            ndp[3] = (ndp[3]+dp[0]+dp[3]) % m
            ndp[4] = (ndp[4]) % m
            ndp[5] = (ndp[5]) % m
            ndp[6] = (ndp[6]+dp[2]+dp[4]+dp[6]) % m
            ndp[7] = (ndp[7]+dp[1]+dp[5]+dp[7]) % m
        elif ar[i] > 2:
            ndp[0] = (ndp[0]) % m
            ndp[1] = (ndp[1]+dp[0]+dp[1]) % m
            ndp[2] = (ndp[2]+dp[2]) % m            
            ndp[3] = (ndp[3]) % m
            ndp[4] = (ndp[4]+dp[4]+dp[6]) % m
            ndp[5] = (ndp[5]+dp[3]+dp[5]+dp[7]) % m
            ndp[6] = (ndp[6]) % m
            ndp[7] = (ndp[7]) % m
        else:
            ndp[0] = (ndp[0]) % m
            ndp[1] = (ndp[1]) % m
            ndp[2] = (ndp[2]+dp[0]+dp[1]+dp[2]) % m            
            ndp[3] = (ndp[3]) % m
            ndp[4] = (ndp[4]+dp[3]+dp[4]+dp[5]+dp[6]+dp[7]) % m
            ndp[5] = (ndp[5]) % m
            ndp[6] = (ndp[6]) % m
            ndp[7] = (ndp[7]) % m
        dp = ndp
        print(dp)
    print((sum(dp)-dp[0]-dp[6]) % m)
    




            

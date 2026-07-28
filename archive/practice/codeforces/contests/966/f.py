import sys
from copy import deepcopy
#input functions
readint = lambda: int(sys.stdin.readline())
readints = lambda: map(int,sys.stdin.readline().split())
readar = lambda: list(map(int,sys.stdin.readline().split()))
flush = lambda: sys.stdout.flush()
readin = lambda: sys.stdin.readline()[:-1]
readins = lambda: map(str,sys.stdin.readline().split())

"""
greedy?

the cost for scoring points only decreases with each one

last case is REALLY weird with this, might be a better idea
to try dp since k only goes to 100
"""

for _ in range(readint()):
    n,k = readints()
    dp = [999999999999999999]*(k+1)
    dp[0] = 0
    for _ in range(n):
        a,b = readints()
        cost = [0]
        while a != 1 or b != 1:
            if a > b:
                cost.append(cost[-1]+b)
                a -= 1
            else:
                cost.append(cost[-1]+a)
                b -= 1
        # 1 by 1 case
        cost.append(cost[-1]+1)
        cost.append(cost[-1]) 
        # compute new min dp costs
        ndp = deepcopy(dp)
        for j in range(1,len(cost)):
            for l in range(j,k+1):
                ndp[l] = min(ndp[l],dp[l-j]+cost[j])
        dp = ndp
    print(-1 if dp[-1] == 999999999999999999 else dp[-1])

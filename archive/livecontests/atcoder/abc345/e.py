import sys

#input functions
readint = lambda: int(sys.stdin.readline())
readints = lambda: map(int,sys.stdin.readline().split())
readar = lambda: list(map(int,sys.stdin.readline().split()))
flush = lambda: sys.stdout.flush()

"""
part 1: take each adj group where balls are same colour
get highest value in group, remove rest
if not enough removals then -1

part 2: dp sequence
track colour of last ball in sequence

dp[length][colour] = max(dp[length-1][x], x != [colour]) + value
dp[1][colour] = value (0 length assumes value 0)

n can be 200000, 1,2,1,21,2 colour seq is oof
"""

n,k = readints()
ar = list()
for _ in range(n):
    c,v = readints()
    ar.append((c,v))
pc = ar[0][0]
pb = ar[0][1]
br = list()

for i in range(n):
    if ar[i][0] == pc:
        pb = max(pb,ar[i][1])
    else:
        br.append((pc,pb))
        pc = ar[i][0]
        pb = ar[i][1]
br.append((pc,pb))
lr = n-k
if lr > len(br): print(-1)
else: # dp to get best for length lr
    # this part has a different dp approach
    # current method likely overflows memory?
    # needs to invert the memory situation
    # either take it or don't
    # [score,previous,length (with some min req)]
    dp = list()
    for _ in range(lr+1):
        tmp = [-999999999999999]*(n+1)
        dp.append(tmp)
    for j in range(len(br)):
        cc = br[j][0]
        vv = br[j][1]
        dp[1][cc] = max(dp[1][cc],vv)
        for k in range(2,min(j+2,lr+1)):
            b = -999999999999999
            for l in range(n+1):
                if l != cc: b = max(b,dp[k-1][l])
            dp[k][cc] = max(dp[k][cc],b+vv)
            if dp[k][cc] < 0: break
    ans = max(dp[lr])
    if ans < 0: ans = 0
    print(ans)
    print(dp)


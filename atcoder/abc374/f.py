import sys

#input functions
readint = lambda: int(sys.stdin.readline())
readints = lambda: map(int,sys.stdin.readline().split())
readar = lambda: list(map(int,sys.stdin.readline().split()))
flush = lambda: sys.stdout.flush()
readin = lambda: sys.stdin.readline()[:-1]
readins = lambda: map(str,sys.stdin.readline().split())

"""
at most k orders can be shipped together, possible wait dp?
limit the answer based on n (<= 100)

with each last shipping group and time it was shipped, compute
the lowest sum of times, subtract sum(ar) to get optimal
"""

n,k,x = readints()
ar = readar()
dp = list()
dp.append({})
dp[0][-1000000000000000000000] = 0 # [number of previous completed][last clear time] = min time sum
for i in range(n):
    tt = ar[i]
    ndp = {}
    for j in range(1,min(i+1,k)+1): # compute based on shipping 1/2/3/.../k
        for d in dp[i-j+1].keys():
            c = dp[i-j+1][d]
            t = max(d+x,tt)
            ndp[t] = min(c+(t*j),ndp.get(t,1000000000000000000000000000000))
    dp.append(ndp)
ans = 58947589345734957345449549
for ii in dp[-1].keys():
    ans = min(dp[-1][ii],ans)
print(ans-sum(ar))

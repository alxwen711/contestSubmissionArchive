import sys

#input functions
readint = lambda: int(sys.stdin.readline())
readints = lambda: map(int,sys.stdin.readline().split())
readar = lambda: list(map(int,sys.stdin.readline().split()))
flush = lambda: sys.stdout.flush()
readin = lambda: sys.stdin.readline()[:-1]
readins = lambda: map(str,sys.stdin.readline().split())

"""
the sum of strengths is at most 1500
the number of players is at most 100

IF a solution exists, does at least 1 team have to have the exact sum? (no)
highest possible is floor(2n/3), with 1 1 1, 11 11 11, 111 111 111

greedy idea of trying to fix largest problem first collapses on first example
"""

n = readint()
p = list()
s = 0
for _ in range(n):
    a,b = readints()
    a -= 1
    p.append((b,a))
    s += b
p.sort()
p.reverse()
if s % 3 != 0: print(-1)
else:
    t = s//3
    dp = {}
    dp[(t,t,t)] = 0
    for i in range(n):
        a,b = p[i][1],p[i][0]
        ndp = {}
        for k in dp.keys():
            v = dp[k]
            if (v*3)//2 <= n:
                if k[0] >= b:
                    e = (k[0]-b,k[1],k[2])
                    if 0 == a: ndp[e] = min(ndp.get(e,10000),v)
                    else: ndp[e] = min(ndp.get(e,10000),v+1)
                if k[1] >= b:
                    e = (k[0],k[1]-b,k[2])
                    if 1 == a: ndp[e] = min(ndp.get(e,10000),v)
                    else: ndp[e] = min(ndp.get(e,10000),v+1)
                if k[2] >= b:
                    e = (k[0],k[1],k[2]-b)
                    if 2 == a: ndp[e] = min(ndp.get(e,10000),v)
                    else: ndp[e] = min(ndp.get(e,10000),v+1)
        dp = ndp
    print(dp.get((0,0,0),-1))

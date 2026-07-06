import sys

#input functions
readint = lambda: int(sys.stdin.readline())
readints = lambda: map(int,sys.stdin.readline().split())
readar = lambda: list(map(int,sys.stdin.readline().split()))
flush = lambda: sys.stdout.flush()
readin = lambda: sys.stdin.readline()[:-1]
readins = lambda: map(str,sys.stdin.readline().split())

# [x][y] = solution to first x values given that the last match was y ago

# track min vals from the diagonals

"""
this is meant to track sums, not indiv values

"""

n,m,l = readints()
ar = readar()
x = 0
for i in range(l-1):
    x += ar[i]
ans = list()
ptr = 0
y = 0
for j in range(l-1,n):
    x += ar[j]
    req = -x % m
    while ptr != len(ans):
        if ans[ptr][0]+l-1 <= j-l: ptr += 1
        elif ans[ptr][1] < req:
            req -= ans[ptr][1]
            ptr += 1
        else:
            ans[ptr] = (ans[ptr][0],ans[ptr][1] - req)
            break
    if req != 0:
        ans.append((j-l+1,req))
        y += req
        x += req
    x -= ar[j-l]
print(y)
"""
dp = list()
dp.append([0]*l)
for _ in range(n):
    dp.append([999999999]*l)


ans = [999999999]*(n+1)
ans[0] = 0

for a in range(1,n+1):
    for b in range(min(a,l)):
        # complete [a][b]
        baseval = -ar[a-b-1] % m
        baseval += min(ans[max(0,a-b-l):a-b])
        dp[a][b] = baseval
        ans[a-b] = min(ans[a-b],baseval)
    for c in range(a,l):
        dp[a][c] = 0

print(min(dp[-1]))
"""

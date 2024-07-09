import sys

#input functions
readint = lambda: int(sys.stdin.readline())
readints = lambda: map(int,sys.stdin.readline().split())
readar = lambda: list(map(int,sys.stdin.readline().split()))
flush = lambda: sys.stdout.flush()

"""
we're pretty much treating each metal type as it's own problem
a situation is considered better by default assuming it
requires fewer starting ingots and burns through fewer ingots


[(5, 3), (6, 2), (9, 1)]
in the dp state, imagine having exactly 5, exactly 6, exactly 9
7 is basically 6 here, 8 is 6 + 1
[(1,5,3),(1,6,2),(3,9,1)]

wait why tf did i not just do basic dp here
the 10**9 limit is for the metal types only
"""

n,m = readints()
ar = readar()
br = readar()
cr = readar()
d = {}
# pseudo list
ingotstates = list()
for i in range(n):
    diff = ar[i]-br[i]
    #t = (ar[i],diff)
    ingotstates.append(ar[i])
    if d.get(ar[i]) == None: d[ar[i]] = diff
    else: d[ar[i]] = min(d[ar[i]],diff)
ingotstates.sort()

dr = [ingotstates[0]]
best = d[ingotstates[0]]
for j in range(1,n):
    if d[ingotstates[j]] < best:
        best = d[ingotstates[j]]
        dr.append(ingotstates[j])

dp = [0]*2000001
req = [0]*2000001
index = 0
#print(dr)
for i in range(dr[index],2000001):
    if index != len(dr)-1:
        if dr[index+1] <= i: index += 1
    req[i] = d[dr[index]]
    dp[i] = max(dp[i-1],1+dp[i-req[i]])


while True:
    if req[-1] == req[-2]:
        dp.pop()
        req.pop()
    else: break

# bin search the rest
ans = 0
lv = len(dp)
for c in cr:
    if c >= lv:
        ans += dp[-1]+((c-lv+1)//req[-1])
    else: ans += dp[c]
print(ans*2)

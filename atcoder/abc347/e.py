import sys

#input functions
readint = lambda: int(sys.stdin.readline())
readints = lambda: map(int,sys.stdin.readline().split())
readar = lambda: list(map(int,sys.stdin.readline().split()))
flush = lambda: sys.stdout.flush()
"""
initial sequence of n 0's
int sequence is off/on switch
after each iteration, every value in S
has its index in ar incremented
increment is num of values in s

track num of elements after each query,
then use prefix sum to get ranges
split queries by num type to get ranges
then can determine sum of each individual
"""
n,q = readints()
ar = readar()
ans = [0]*n
d = [0]*(n+1)
s = 0
sr = list()
for i in ar:
    if d[i] == 0:
        d[i] = 1
        s += 1
    else:
        d[i] = 0
        s -= 1
    sr.append(s)
br = list()
b = 0
br.append(b)
for j in range(q):
    b += sr[j]
    br.append(b)
#print(sr)
#print(br)
d = {}
for k in range(q):
    x = ar[k]
    if d.get(x) == None: d[x] = list()
    d[x].append(k)
#print(d)
for l in range(1,n+1):
    if d.get(l) != None:
        le = len(d[l])
        for m in range(le//2):
            ai,bi = d[l][2*m],d[l][2*m+1]
            ans[l-1] += br[bi]-br[ai]
        if le % 2 == 1: ans[l-1] += br[q]-br[d[l][-1]]
print(*ans)

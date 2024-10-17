import sys

#input functions
readint = lambda: int(sys.stdin.readline())
readints = lambda: map(int,sys.stdin.readline().split())
readar = lambda: list(map(int,sys.stdin.readline().split()))
flush = lambda: sys.stdout.flush()
readin = lambda: sys.stdin.readline()[:-1]
readins = lambda: map(str,sys.stdin.readline().split())

s = readin()
n = len(s)
d = {}
for i in range(n):
    if d.get(s[i]) == None: d[s[i]] = list()
    d[s[i]].append(i)
ans = 0
for j in d.keys():
    ar = d[j]
    t = sum(ar)
    m = len(ar)
    for k in range(m-1):
        t -= ar[k]
        ans += (t - (ar[k]+1)*(m-k-1))
print(ans)

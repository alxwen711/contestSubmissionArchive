import sys

#input functions
readint = lambda: int(sys.stdin.readline())
readints = lambda: map(int,sys.stdin.readline().split())
readar = lambda: list(map(int,sys.stdin.readline().split()))
flush = lambda: sys.stdout.flush()

n = readint()
d = {}
for _ in range(n):
    a,c = readints()
    if d.get(c) == None: d[c] = a
    else: d[c] = min(d[c],a)
ans = -1
for i in d.keys():
    ans = max(ans,d[i])
print(ans)

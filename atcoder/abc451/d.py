import sys
from copy import deepcopy
#input functions
readint = lambda: int(sys.stdin.readline())
readints = lambda: map(int,sys.stdin.readline().split())
readar = lambda: list(map(int,sys.stdin.readline().split()))
flush = lambda: sys.stdout.flush()
readin = lambda: sys.stdin.readline()[:-1]
readins = lambda: map(str,sys.stdin.readline().split())

n = readint()
p2 = [1]
for _ in range(29):
    p2.append(p2[-1]*2)

q = deepcopy(p2)
d = {}
for snth in q:
    d[snth] = 1
while len(q) != 0:
    x = q.pop()
    for i in p2:
        y = int(str(x)+str(i))
        if y > 1000000000:
            break
        if d.get(y) == None:
            q.append(y)
            d[y] = 1
v = list(d.keys())
v.sort()
print(v[n-1])

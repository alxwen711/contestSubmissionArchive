import sys

#input functions
readint = lambda: int(sys.stdin.readline())
readints = lambda: map(int,sys.stdin.readline().split())
readar = lambda: list(map(int,sys.stdin.readline().split()))
flush = lambda: sys.stdout.flush()
readin = lambda: sys.stdin.readline()[:-1]
readins = lambda: map(str,sys.stdin.readline().split())

n = readint()
ar = readar()
d = {}
for i in range(n):
    x = ar[i]
    if d.get(x) == None: d[x] = list()
    d[x].append(i)
ans = 0
for snth in range(n):
    ans += (snth+1)*(n-snth)
for j in d.keys():
    m = len(d[j])
    d[j].append(n)
    adder = 0
    base = 0
    for k in range(m):
        base += adder*(d[j][k+1]-d[j][k])
        adder += 1
    #print(d[j],base)
    prev = -1
    for l in range(m-1):
        ans -= base*(d[j][l]-prev)
        prev = d[j][l]
        base -= d[j][-1]-d[j][l+1]
print(ans)
#print(d)

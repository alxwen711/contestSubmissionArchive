import sys

#input functions
readint = lambda: int(sys.stdin.readline())
readints = lambda: map(int,sys.stdin.readline().split())
readar = lambda: list(map(int,sys.stdin.readline().split()))
flush = lambda: sys.stdout.flush()
readin = lambda: sys.stdin.readline()[:-1]
readins = lambda: map(str,sys.stdin.readline().split())

n,t = readints()
s = readin()
ar = readar()
l = list()
r = list()
for i in range(n):
    if s[i] == "1": r.append(ar[i])
    else: l.append(ar[i])

l.sort()
r.sort()

ans = 0
if len(l) != 0 and len(r) != 0:
    ln = len(l)
    rn = len(r)
    # compute r cases (l cases are not needed)
    li = 0
    ri = 0
    for a in r:
        # l vals must be inbetween a and a+2n inclusive
        while ri != ln:
            if l[ri] <= (2*t+a): ri += 1
            else: break
        while li != ln:
            if l[li] < a: li += 1
            else: break
        ans += (ri-li)
print(ans)

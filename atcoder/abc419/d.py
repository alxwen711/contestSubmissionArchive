import sys

#input functions
readint = lambda: int(sys.stdin.readline())
readints = lambda: map(int,sys.stdin.readline().split())
readar = lambda: list(map(int,sys.stdin.readline().split()))
flush = lambda: sys.stdout.flush()
readin = lambda: sys.stdin.readline()[:-1]
readins = lambda: map(str,sys.stdin.readline().split())

n,m = readints()
s = readin()
t = readin()
ar = [0]*n
br = [0]*n
for _ in range(m):
    l,r = readints()
    ar[l-1] += 1
    br[r-1] += 1
ans = list()
x = 0
for i in range(n):
    x += ar[i]
    if x % 2 == 0: ans.append(s[i])
    else: ans.append(t[i])
    x -= br[i]
print(*ans, sep="")

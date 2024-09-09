import sys

#input functions
readint = lambda: int(sys.stdin.readline())
readints = lambda: map(int,sys.stdin.readline().split())
readar = lambda: list(map(int,sys.stdin.readline().split()))
flush = lambda: sys.stdout.flush()
readin = lambda: sys.stdin.readline()[:-1]
readins = lambda: map(str,sys.stdin.readline().split())

ar = list()
m = 0
for _ in range(readint()):
    s = readin()
    ar.append((len(s),s))
    m = max(m,len(s))
n = len(ar)
ans = list()
for _ in range(m):
    tmp = ["*"]*n
    ans.append(tmp)
for i in range(n):
    for j in range(ar[-i-1][0]):
        ans[j][i] = ar[-i-1][1][j]
for k in range(m):
    while ans[k][-1] == "*":
        ans[k].pop()
    print(*ans[k],sep="")

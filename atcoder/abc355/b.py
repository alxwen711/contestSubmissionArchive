import sys

#input functions
readint = lambda: int(sys.stdin.readline())
readints = lambda: map(int,sys.stdin.readline().split())
readar = lambda: list(map(int,sys.stdin.readline().split()))
flush = lambda: sys.stdout.flush()

n,m = readints()
ar = readar()
br = readar()
cr = list()
for i in ar:
    cr.append((i,1))
for j in br:
    cr.append((j,2))
cr.sort()
ans = "No"
for k in range(n+m-1):
    if cr[k][1] == 1 and cr[k+1][1] == 1:
        ans = "Yes"
        break
print(ans)

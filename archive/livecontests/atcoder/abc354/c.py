import sys

#input functions
readint = lambda: int(sys.stdin.readline())
readints = lambda: map(int,sys.stdin.readline().split())
readar = lambda: list(map(int,sys.stdin.readline().split()))
flush = lambda: sys.stdout.flush()

n = readint()
ar = list()
cr = list()
for i in range(n):
    a,c = readints()
    ar.append((a,-c,(i+1)))
ar.sort()
ar.reverse()
cost = -99999999999999999999
for i in ar:
    if i[1] > cost:
        cost = i[1]
        cr.append((i[0],-i[1],i[2]))
ans = list()
for c in cr:
    ans.append(c[2])
ans.sort()
print(len(ans))
print(*ans)

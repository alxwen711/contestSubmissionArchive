import sys

#input functions
readint = lambda: int(sys.stdin.readline())
readints = lambda: map(int,sys.stdin.readline().split())
readar = lambda: list(map(int,sys.stdin.readline().split()))
flush = lambda: sys.stdout.flush()

n = readint()
ar = list()
for i in range(n):
    s = input()
    ar.append(s)
wc = [0]*n
for a in range(n-1):
    for b in range(a+1,n):
        if ar[a][b] == "x":
            wc[b] += 1
        else:
            wc[a] += 1
br = list()
for c in range(n):
    br.append((wc[c],-c-1))
br.sort()
br.reverse()
ans = list()
for d in range(n):
    ans.append(-br[d][1])
print(*ans)

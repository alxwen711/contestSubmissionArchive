import sys

#input functions
readint = lambda: int(sys.stdin.readline())
readints = lambda: map(int,sys.stdin.readline().split())
readar = lambda: list(map(int,sys.stdin.readline().split()))
flush = lambda: sys.stdout.flush()

def solve(ar,m):
    index = 0
    ans = list()
    for i in range(len(ar)):
        if ar[i][0] == index:
            ans.append(ar[i][1])
            index += 1
        elif ar[i][0] > index:
            print(-1)
            return
        if index == m: break
    print(*ans)
for i in range(readint()):
    m = readint()
    d = {}
    for j in range(m):
        n = readint()
        tmp = readar()
        for k in range(n):
            d[tmp[k]] = j
    ar = list()
    for l in d.keys():
        ar.append((d[l],l))
    ar.sort()
    solve(ar,m)

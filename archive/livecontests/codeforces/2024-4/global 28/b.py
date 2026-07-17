import sys

#input functions
readint = lambda: int(sys.stdin.readline())
readints = lambda: map(int,sys.stdin.readline().split())
readar = lambda: list(map(int,sys.stdin.readline().split()))
flush = lambda: sys.stdout.flush()
readin = lambda: sys.stdin.readline()[:-1]
readins = lambda: map(str,sys.stdin.readline().split())

for _ in range(readint()):
    n,k = readints()
    v = 1
    ans = [0]*n
    r = k
    if r != 1:
        for i in range(n//r):
            ans[min(n-1,r*i+k-1)] = v
            v += 1
    for j in range(n):
        if ans[j] == 0:
            ans[j] = v
            v += 1
    print(*ans)

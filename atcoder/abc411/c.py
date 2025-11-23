import sys

#input functions
readint = lambda: int(sys.stdin.readline())
readints = lambda: map(int,sys.stdin.readline().split())
readar = lambda: list(map(int,sys.stdin.readline().split()))
flush = lambda: sys.stdout.flush()
readin = lambda: sys.stdin.readline()[:-1]
readins = lambda: map(str,sys.stdin.readline().split())

n,q = readints()
ar = readar()
h = [0]*(n+5)
ans = 0
for i in ar:
    if h[i] == 0:
        ans += 1
        h[i] = 1
        ans -= (h[i-1]+h[i+1])
    else:
        ans -= 1
        h[i] = 0
        ans += (h[i-1]+h[i+1])
    print(ans)

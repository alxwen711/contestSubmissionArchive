import sys

#input functions
readint = lambda: int(sys.stdin.readline())
readints = lambda: map(int,sys.stdin.readline().split())
readar = lambda: list(map(int,sys.stdin.readline().split()))
flush = lambda: sys.stdout.flush()

for i in range(readint()):
    s = readint()
    il = readar()
    ans = 0
    for j in range(s):
        ar = readar()
        tl = sum(ar)-ar[0]
        tl -= (ar[0]-1)*il[j]
        ans += tl
    print(ans)

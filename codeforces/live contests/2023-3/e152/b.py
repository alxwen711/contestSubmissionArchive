import sys

#input functions
readint = lambda: int(sys.stdin.readline())
readints = lambda: map(int,sys.stdin.readline().split())
readar = lambda: list(map(int,sys.stdin.readline().split()))
flush = lambda: sys.stdout.flush()

for i in range(readint()):
    n,k = readints()
    ar = readar()
    br = list()
    for j in range(n):
        if ar[j] % k == 0: br.append((-k,j))
        br.append((-(ar[j] % k),j))
    br.sort()
    cr = list()
    for k in range(n):
        cr.append(br[k][1]+1)
    print(*cr)

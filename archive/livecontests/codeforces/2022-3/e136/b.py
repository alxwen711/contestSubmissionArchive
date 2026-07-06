import sys

#input functions
readint = lambda: int(sys.stdin.readline())
readints = lambda: map(int,sys.stdin.readline().split())
readar = lambda: list(map(int,sys.stdin.readline().split()))
flush = lambda: sys.stdout.flush()

def solve(n,ar):
    br = list()
    br.append(ar[0])
    for j in range(1,n):
        if ar[j] <= br[-1] and ar[j] != 0:
            print(-1)
            return
        br.append(br[-1]+ar[j])
    print(*br)

for i in range(readint()):
    n = readint()
    ar = readar()
    solve(n,ar)

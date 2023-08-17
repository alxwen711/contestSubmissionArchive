import sys

#input functions
readint = lambda: int(sys.stdin.readline())
readints = lambda: map(int,sys.stdin.readline().split())
readar = lambda: list(map(int,sys.stdin.readline().split()))
flush = lambda: sys.stdout.flush()

for i in range(readint()):
    n = readint()
    ar = readar()
    x = max(ar)
    br = list()
    cr = list()
    for j in ar:
        if j == x: cr.append(j)
        else: br.append(j)
    if len(cr) == n: print(-1)
    else:
        print(len(br),len(cr))
        print(*br)
        print(*cr)

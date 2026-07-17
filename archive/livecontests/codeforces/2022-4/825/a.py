import sys

#input functions
readint = lambda: int(sys.stdin.readline())
readints = lambda: map(int,sys.stdin.readline().split())
readar = lambda: list(map(int,sys.stdin.readline().split()))
flush = lambda: sys.stdout.flush()

for i in range(readint()):
    n = readint()
    ar = readar()
    br = readar()
    e = abs(sum(ar)-sum(br))
    er = 0
    for j in range(n):
        if ar[j] != br[j]: er += 1
    if er != e: e += 1
    print(e)

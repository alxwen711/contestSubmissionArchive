import sys

#input functions
readint = lambda: int(sys.stdin.readline())
readints = lambda: map(int,sys.stdin.readline().split())
readar = lambda: list(map(int,sys.stdin.readline().split()))
flush = lambda: sys.stdout.flush()

for i in range(readint()):
    n,m = readints()
    ar = readar()
    br = readar()
    for j in range(len(br)):
        ar[ar.index(min(ar))] = br[j]
    print(sum(ar))

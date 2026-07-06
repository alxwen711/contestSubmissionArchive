import sys

#input functions
readint = lambda: int(sys.stdin.readline())
readints = lambda: map(int,sys.stdin.readline().split())
readar = lambda: list(map(int,sys.stdin.readline().split()))
flush = lambda: sys.stdout.flush()
readin = lambda: sys.stdin.readline()[:-1]
readins = lambda: map(str,sys.stdin.readline().split())

for _ in range(readint()):
    n = readint()
    br = readar()
    ar = [0]*n
    for i in range(n-1):
        ar[i] |= br[i]
        ar[i+1] |= br[i]
    flag = True
    for j in range(n-1):
        if ar[j] & ar[j+1] != br[j]:
            flag = False
            break
    if flag: print(*ar)
    else: print(-1)

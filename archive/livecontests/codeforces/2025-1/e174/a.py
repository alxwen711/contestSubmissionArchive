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
    ar = readar()
    br = list()
    for i in range(n-2):
        if ar[i] == 1: br.append(i)
    ans = "YES"
    for j in range(len(br)-1):
        if br[j]+2 == br[j+1]: ans = "NO"
    print(ans)

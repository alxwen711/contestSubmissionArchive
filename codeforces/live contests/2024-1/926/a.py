import sys

#input functions
readint = lambda: int(sys.stdin.readline())
readints = lambda: map(int,sys.stdin.readline().split())
readar = lambda: list(map(int,sys.stdin.readline().split()))
flush = lambda: sys.stdout.flush()

for _ in range(readint()):
    n = readint()
    ar = readar()
    """
    ar.sort()
    br = list()
    for i in range(n//2):
        br.append(ar[i])
        br.append(ar[-i-1])
    if n % 2 == 1: br.append(ar[n//2])
    ans = 0
    for j in range(n-1):
        ans += abs(br[j]-br[j+1])
    print(ans)
        
    """
    print(max(ar)-min(ar))

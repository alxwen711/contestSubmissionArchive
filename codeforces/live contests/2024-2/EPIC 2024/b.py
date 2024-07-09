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
    prev = -1
    br = list()
    for i in ar:
        if prev <= i: prev = i
        else: br.append(prev-i)
    br.sort()
    ans = 0
    last = 0
    #print(br)
    m = len(br)
    for j in range(m):
        ans += (m-j+1)*(br[j]-last)
        last = br[j]
    print(ans)

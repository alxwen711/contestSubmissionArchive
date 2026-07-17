import sys

#input/output functions
readint = lambda: int(sys.stdin.readline())
readints = lambda: map(int,sys.stdin.readline().split())
readar = lambda: list(map(int,sys.stdin.readline().split()))
flush = lambda: sys.stdout.flush()

for i in range(readint()):
    n,r = readints()
    ar = readar()
    ar.sort()
    br = list()
    for j in range(r-1):
        br.append(ar[j+1]-ar[j]-1)
    if r == 1: br.append(n-1)
    else: br.append(n-ar[-1]+ar[0]-1)
    br.sort()
    br.reverse()
    clean = 0
    for k in range(r):
        x = br[k]-(4*k)
        if x < 1: break
        elif x == 1:
            clean += 1
            break
        else:
            clean += (x-1)
    print(n-clean)
    



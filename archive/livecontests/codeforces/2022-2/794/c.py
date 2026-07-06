import sys

def solve(br,n):
    #if n % 2 == 1: return 0
    for k in range(n-2):
        if not ((br[k] > br[k+1] and br[k+2] > br[k+1]) or (br[k] < br[k+1] and br[k+2] < br[k+1])):
            return 0
    #check front and back individually
    if not ((br[0] > br[1] and br[0] > br[-1]) or (br[0] < br[1] and br[0] < br[-1])): return 0
    if not ((br[-1] > br[-2] and br[-1] > br[0]) or (br[-1] < br[-2] and br[-1] < br[0])): return 0
    return 1
    

for i in range(int(sys.stdin.readline())):
    n = int(sys.stdin.readline())
    ar = list(map(int, sys.stdin.readline().split()))
    ar.sort()
    br = list()
    if n % 2 == 0:
        for j in range(n//2):
            br.append(ar[j])
            br.append(ar[j+n//2])
    else:
        for j in range(n//2):
            br.append(ar[j])
            br.append(ar[j+n//2+1])
        br.append(ar[n//2])

    if solve(br,n) == 1:
        print("YES")
        print(*br)
    else: print("NO")

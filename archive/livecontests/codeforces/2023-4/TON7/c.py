import sys

#input functions
readint = lambda: int(sys.stdin.readline())
readints = lambda: map(int,sys.stdin.readline().split())
readar = lambda: list(map(int,sys.stdin.readline().split()))
flush = lambda: sys.stdout.flush()

# x pairs where a beats b

def solve(br,cr,n,x):
    ans = [0]*n
    for i in range(x):
        ans[cr[i+n-x][1]] = br[i]
        if cr[i+n-x][0] <= br[i]: return False
        
    for j in range(n-x):
        ans[cr[j][1]] = br[j+x]
        if cr[j][0] > br[j+x]: return False

    print("YES")
    print(*ans)
    return True

    
for _ in range(readint()):
    n,x = readints()
    ar = readar()
    br = readar()
    cr = list() #ar tuples
    for i in range(n):
        cr.append((ar[i],i))
    cr.sort()
    br.sort()
    if solve(br,cr,n,x) == False: print("NO")

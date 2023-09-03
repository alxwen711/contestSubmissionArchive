import sys

#input functions
readint = lambda: int(sys.stdin.readline())
readints = lambda: map(int,sys.stdin.readline().split())
readar = lambda: list(map(int,sys.stdin.readline().split()))
flush = lambda: sys.stdout.flush()

for i in range(readint()):
    n = readint()
    ar = readar()
    fdp = [0,0]
    bdp = [0,0]
    fc = 0 #neg section
    bc = 0 #pos section
    for j in range(n-1):
        if ar[j] <= ar[j+1]: fc += 1
        if ar[-j-1] <= ar[-j-2]: bc += 1
        fdp.append(fc)
        bdp.append(bc)
    ans = bdp[n]
    for k in range(1,n+1):
        ans = min(ans,fdp[k]+bdp[n-k]+1)
    print(ans)
        

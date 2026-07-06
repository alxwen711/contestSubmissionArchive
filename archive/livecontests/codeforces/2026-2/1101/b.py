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
    ans = [0]*n
    excess = 0
    ans[0] = ar[0]
    for i in range(1,n):
        req = ans[i-1]
        if ar[i] >= req:
            ans[i] = req
            excess += (ar[i]-req)
        elif (ar[i]+excess) >= req:
            ans[i] = req
            excess -= (req-ar[i])
        else: # must go lower
            total = req*i+excess+ar[i] # amount of frosting up to here
            ans[i] = total//(i+1)
            excess = total % (i+1)
    print(*ans)

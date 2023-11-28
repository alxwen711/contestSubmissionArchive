import sys

#input functions
readint = lambda: int(sys.stdin.readline())
readints = lambda: map(int,sys.stdin.readline().split())
readar = lambda: list(map(int,sys.stdin.readline().split()))
flush = lambda: sys.stdout.flush()

"""
weight is the minimum required so that the entire thing could collapse
(different from minimum guarantee)
each case can take O(log n)

corner cases have only one way for weight to travel
"""

for i in range(readint()):
    n = readint()
    ar = readar()
    br = readar()
    lr = [0]*n
    rl = [0]*n
    lr[-1] = br[-1]-ar[-1]
    rl[0] = br[0]-ar[0]

    #rl
    for j in range(1,n):
        mr = br[j]-ar[j]
        prev = rl[j-1]
        rl[j] = max(mr,prev-ar[j])


    #lr
    for k in range(n-2,-1,-1):
        mr = br[k]-ar[k]
        prev = lr[k+1]
        lr[k] = max(mr,prev-ar[k])

    ans = [0]*n
    ans[0] = lr[0]
    ans[-1] = rl[-1]
    for a in range(1,n-1):
        ans[a] = max(br[a]-ar[a],rl[a-1]+lr[a+1]-ar[a])
    print(*ans)

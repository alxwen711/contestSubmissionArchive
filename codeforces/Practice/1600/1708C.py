import sys

def solve(x,n,q,ar):
    ans = [0]*n
    r = x
    left = n
    for j in range(n):
        if q == 0:
            return False,ans
        if r == 0: break
        if left == r: #must take
            ans[j] = 1
            r -= 1
            if ar[j] > q:
                q -= 1
        else: #optional
            if q >= ar[j]:
                ans[j] = 1
                r -= 1
        left -= 1
    return True,ans


def bs(n,q,ar):
    low = 0
    high = n
    while high-low > 1:
        mid = (low+high)//2
        x,pr = solve(mid,n,q,ar)
        if x: low = mid
        else: high = mid
    x,pr = solve(high,n,q,ar)
    if x:
        print(*pr,sep="")
        return
    x,pr = solve(low,n,q,ar)
    print(*pr,sep="")
    return


for i in range(int(sys.stdin.readline())):
    n,q = map(int,sys.stdin.readline().split())
    ar = list(map(int,sys.stdin.readline().split()))
    bs(n,q,ar)

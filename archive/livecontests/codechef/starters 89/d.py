import sys

#input functions
readint = lambda: int(sys.stdin.readline())
readints = lambda: map(int,sys.stdin.readline().split())
readar = lambda: list(map(int,sys.stdin.readline().split()))
flush = lambda: sys.stdout.flush()
"""
have to find a numerical solve,
case where A is all 1's and a 2 and B is all 1000000's
can be solved if k can be at least 2

operations are:
b += 1, m += 1
a += k, n += 1
"""
def solve(n,m,k,a,b):
    # a/n > b/m goal
    if k == 1 and a == n: return -1 # A avg 1 with only 1 addition
    if (a*m) > (b*n): return 0 # already done
    if a >= n*k: #special case where only B reduction is possible, bin search
        low = 1
        high = 2**420 #hopefully enough
        while high-low > 1:
            mid = (high+low)//2
            if (a*(m+mid)) > ((b+mid)*n): high = mid
            else: low = mid
        if (a*(m+low)) > ((b+low)*n): return low
        return high
    ans = 0
    if b >= m*k: # need to reduce B avg until below k
        low = 1
        high = 2**100
        while high-low > 1:
            mid = (high+low)//2
            if (b+mid) < (m+mid)*k: high = mid
            else: low = mid
        if (b+low) < (m+low)*k: ans = low
        else: ans = high
    b += ans
    m += ans
    best = 9999999999999999999999999999999999999999999999999999999999999999999999
    while True:
        # find A increment needed to exceed avg
        diff = (b*n)-(a*m)+1
        inc = k*m-b # must be positive
        r = max((diff+inc-1)//inc,0) #cannot subtract moves
        # if at least same? else exit
        if (r + ans) <= best: best = r+ans
        else: break
        # add a 1 to b
        ans += 1
        b += 1
        m += 1
    return best

for i in range(readint()):
    n,m,k = readints()
    ar = readar()
    br = readar()
    print(solve(n,m,k,sum(ar),sum(br)))

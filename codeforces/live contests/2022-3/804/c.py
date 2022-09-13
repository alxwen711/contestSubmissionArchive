import sys

def solve(n,ar):
    if n < 4: return 1
    h = [0]*n
    for j in range(n):
        h[ar[j]] = j
    ff = h[0]
    fff = h[1]
    low = min(ff,fff)
    high = max(ff,fff)
    r = high-low-1
    ans = 1
    f = 1
    for k in range(n-2):
        if low == 0 and high == n-1:
            f = r
            break
        x = k+2
        position = h[x]
        if low < position < high: #in range
            ans = (ans * r) % 1000000007
            r -= 1
        elif position < low: #set new low
            r += (low-position-1)
            low = position
        else: #set new high
            r += (position-high-1)
            high = position

            
    while f > 1:
        ans = (ans * f) % 1000000007
        f -= 1
    return ans

for i in range(int(sys.stdin.readline())):
    n = int(sys.stdin.readline())
    ar = list(map(int,sys.stdin.readline().split()))
    print(solve(n,ar))

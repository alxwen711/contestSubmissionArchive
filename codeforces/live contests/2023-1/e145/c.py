import sys

#input functions
readint = lambda: int(sys.stdin.readline())
readints = lambda: map(int,sys.stdin.readline().split())
readar = lambda: list(map(int,sys.stdin.readline().split()))
flush = lambda: sys.stdout.flush()



def b(k,h):
    low = 0
    high = 30
    while high-low > 1:
        mid = (low+high)//2
        if h[mid] > k: high = mid
        else: low = mid
    if h[high] <= k: return high
    else: return low


h = [0]*31
for snth in range(31):
    h[snth] = (snth*snth+snth)//2


for i in range(readint()):
    n,k = readints()
    x = b(k,h)
    ar = [2]*x
    r = k-h[x]
    if r != 0:
        ar.append(-2*(x-r)-1)
    l = len(ar)
    for j in range(n-l):
        ar.append(-1000)
    print(*ar)

import sys

#input functions
readint = lambda: int(sys.stdin.readline())
readints = lambda: map(int,sys.stdin.readline().split())
readar = lambda: list(map(int,sys.stdin.readline().split()))
flush = lambda: sys.stdout.flush()

def b(n,ar,x):
    low = 0
    high = n-1
    while high-low > 1:
        mid = (low+high)//2
        if ar[mid] >= x: high = mid
        else: low = mid
    if ar[low] >= x: return low
    elif ar[high] >= x: return high
    else: return high + 1

n = readint()
ar = readar()
ar.sort()
#print(ar)
br = [0]
for i in range(n):
    br.append(br[-1]+ar[i])
#print(ar)
#print(br)
ans = 0
for j in range(n-1):
    v = ar[j]*(n-j-1)+br[-1]-br[j+1]
    #print(v)
    #subtract 10 mil+ cases
    #print(min(n-b(n,ar,100000000-ar[j]),n-j-1))
    v -= 100000000*min(n-b(n,ar,100000000-ar[j]),n-j-1)
    ans += v
    #print(v)
print(ans)

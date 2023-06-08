import sys
"""
find largest subarray

"""
#input functions
readint = lambda: int(sys.stdin.readline())
readints = lambda: map(int,sys.stdin.readline().split())
readar = lambda: list(map(int,sys.stdin.readline().split()))
flush = lambda: sys.stdout.flush()

def nil(ar,a,b,h,n):
    x,y = ar[a],ar[b]
    h[x] = b
    h[y] = a
    low = h[1]
    high = h[1]
    for k in range(2,n):
        c = h[k]
        low = min(low,c)
        high = max(high,c)
        if high-low+1 == k:
            h[x] = a
            h[y] = b
            return False
    return True

for i in range(readint()):
    n = readint()
    ar = readar()
    h = [0]*(n+1)
    for j in range(n):
        h[ar[j]] = j
    a = h[1]
    b = h[2]
    if nil(ar,0,0,h,n): print(1,1)
    elif nil(ar,a,0,h,n): print(1,a+1)
    elif nil(ar,a,n-1,h,n): print(a+1,n)
    elif nil(ar,b,0,h,n): print(1,b+1)
    elif nil(ar,b,n-1,h,n): print(b+1,n)
    else: print(1,2)
    

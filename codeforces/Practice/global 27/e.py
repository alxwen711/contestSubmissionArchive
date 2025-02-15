import sys

#input functions
readint = lambda: int(sys.stdin.readline())
readints = lambda: map(int,sys.stdin.readline().split())
readar = lambda: list(map(int,sys.stdin.readline().split()))
flush = lambda: sys.stdout.flush()
readin = lambda: sys.stdin.readline()[:-1]
readins = lambda: map(str,sys.stdin.readline().split())

"""
always optimal to perform the top ups as early as needed
there's likely some sort of min/max range of optimal number
of power boosts

brute force first 1000 power boost calculations

then there are at most 100 direct after strikes needed
"""

def f(x,y,z,k,b):
    ans = b*x
    req = (b-1)//k
    ans += req*y
    dmg = (req*req+req)//2*k
    remaininghp = z-dmg
    reqstrikes = max((remaininghp+b-1)//b,0)
    ans += reqstrikes*y
    return ans

def g(x,y,z,k,c):
    req = (c-1)//k
    dmg = (req*req+req)//2*k
    remaininghp = z-dmg
    return max((remaininghp+c-1)//c,0)

def solve(x,y,z,k):
    ans = 376897324242496874986734896734634689347897689
    for i in range(1,10101):
        v = f(x,y,z,k,i)
        if v < ans:
            ans = v
    for j in range(10100,0,-1):
        low = 1
        high = z
        while high-low > 1:
            mid = (low+high)//2
            if g(x,y,z,k,mid) <= j: high = mid
            else: low = mid
        if g(x,y,z,k,high) >= j: ans = min(ans,f(x,y,z,k,high))
        else: ans = min(ans,f(x,y,z,k,low))
    return ans
        

for _ in range(readint()):
    x,y,z,k = readints()
    print(solve(x,y,z,k))
    

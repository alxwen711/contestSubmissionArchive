import sys

#input functions
readint = lambda: int(sys.stdin.readline())
readints = lambda: map(int,sys.stdin.readline().split())
readar = lambda: list(map(int,sys.stdin.readline().split()))
flush = lambda: sys.stdout.flush()
readin = lambda: sys.stdin.readline()[:-1]
readins = lambda: map(str,sys.stdin.readline().split())

"""
determine the maximum diagonal, *2 is the max increase per cut
try ternary search?

convex means you can cut at any 2 points and it will be in the shape
don't sqrt unless REALLY needed

problem feels potentially like a bait, ternary search seems to not be it
unless it's not on the vertices??

This does NOT appear to be ternary search, also 2pt would not work either
go to furthest point, try finding further from that point, and repeat? NO

div and conquer???? no??

so rain takes 14 attempts, this is some fucked shit isn't it

ternary search but we try smaller segments
"""

def distance(a,b):
    return abs(a[0]-b[0])**2+abs(a[1]-b[1])**2

def f(best,k,x):
    
    if x == 1: return 4*x*x*best >= k*k
    else: return 4*x*x*best > k*k

n,k = readints()
points = list()
for _ in range(n):
    x,y = readints()
    points.append((x,y))
best = 0

for i in range(n-1):
    for j in range(i+1,n):
        best = max(best,distance(points[i],points[j]))
low = 0
high = 100000000000000000000000000000 # this is enough right
while high - low > 1:
    mid = (low+high)//2
    if f(best,k,mid): high = mid
    else: low = mid
if f(best,k,low): print(low)
else: print(high)

        

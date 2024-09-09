import sys

#input functions
readint = lambda: int(sys.stdin.readline())
readints = lambda: map(int,sys.stdin.readline().split())
readar = lambda: list(map(int,sys.stdin.readline().split()))
flush = lambda: sys.stdout.flush()
readin = lambda: sys.stdin.readline()[:-1]
readins = lambda: map(str,sys.stdin.readline().split())

"""
sum of distances from pts <= d
overlap method has issues with cases where points are close together

also there could be up to 1000000000000 points practically

horizontal distances can be tracked with a running sum sort
vertical distances, track all possibilities -> bin search
"""

n,d = readints()
ar = list()
br = list()
for _ in range(n):
    a,b = readints()
    a += 1000000
    b += 1000000
    ar.append(a)
    br.append(b)
ar.sort()
br.sort()

# compute horizontal distances
hd = list()

sindex = 0
dist = sum(ar)-(ar[0]*n)
hd.append(dist)
for i in range(ar[0]+1,ar[-1]+1):
    while sindex != n:
        if i > ar[sindex]: sindex += 1
        else: break
    dist -= n
    dist += sindex*2
    hd.append(dist)
while hd[-1] < d:
    hd.append(hd[-1]+n)
for snth in range(hd[0]+n,d+1,n):
    hd.append(snth)

#print(hd)

# compute vertical distances
vd = list()

sindex = 0
dist = sum(br)-(br[0]*n)
vd.append(dist)
for i in range(br[0]+1,br[-1]+1):
    while sindex != n:
        if i > br[sindex]: sindex += 1
        else: break
    dist -= n
    dist += sindex*2
    vd.append(dist)
while vd[-1] < d:
    vd.append(vd[-1]+n)
for snth in range(vd[0]+n,d+1,n):
    vd.append(snth)

#print(vd)

hd.sort()
vd.sort()
nn = len(vd)
ans = 0
for a in hd:
    t = d-a
    low = 0
    high = nn-1
    while high-low > 1:
        mid = (low+high)//2
        if vd[mid] <= t: low = mid
        else: high = mid
    if vd[high] <= t: ans += high+1
    elif vd[low] <= t: ans += low+1
    else: ans += low
    #print(ans)
print(ans)

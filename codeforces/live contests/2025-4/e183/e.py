import sys

#input functions
readint = lambda: int(sys.stdin.readline())
readints = lambda: map(int,sys.stdin.readline().split())
readar = lambda: list(map(int,sys.stdin.readline().split()))
flush = lambda: sys.stdout.flush()
readin = lambda: sys.stdin.readline()[:-1]
readins = lambda: map(str,sys.stdin.readline().split())

a,b = readints()
n = readint()
ar = readar()
br = readar()

seg = list()
tmp = [0]*1000001
seg.append(tmp)
while len(seg[-1]) > 1:
    seg.append([0]*(len(seg[-1])//2))

for i in range(n):
    r = max(0,ar[i]-a)+max(0,br[i]-b)
    seg[0][r] += 1
    r //= 2
    for j in range(1,len(seg)):
        if len(seg[j]) == r: break
        seg[j][r] += 1
        r //= 2

def f(seg,x):
    index = x-1
    t = 0
    for i in range(len(seg)):
        if index == -1: return t >= x
        if index % 2 == 0:
            t += seg[i][index]
            index -= 1
        index //= 2
    return t >= x
for _ in range(readint()):
    i,na,nb = readints()
    i -= 1
    prev = max(0,ar[i]-a)+max(0,br[i]-b)
    ar[i] = na
    br[i] = nb
    nn = max(0,ar[i]-a)+max(0,br[i]-b)
    if prev != nn: # replacement
        r = prev
        seg[0][r] -= 1
        r //= 2
        for j in range(1,len(seg)):
            if len(seg[j]) == r: break
            seg[j][r] -= 1
            r //= 2
        r = nn
        seg[0][r] += 1
        r //= 2
        for j in range(1,len(seg)):
            if len(seg[j]) == r: break
            seg[j][r] += 1
            r //= 2
    low = 0
    high = n
    while high-low > 1:
        mid = (low+high)//2
        if f(seg,mid): low = mid
        else: high = mid
    if not f(seg,1): print(0)
    elif f(seg,high): print(high)
    else: print(low)
        
        

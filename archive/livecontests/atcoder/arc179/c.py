import sys
from random import randint
#input functions
readint = lambda: int(sys.stdin.readline())
readints = lambda: map(int,sys.stdin.readline().split())
readar = lambda: list(map(int,sys.stdin.readline().split()))
flush = lambda: sys.stdout.flush()

"""
middle adding actually can fail (-100 60 60 60 with 101 cap)
also has issues with values being equal
equal issue can be resolved with double comparison, but would use too many queries
merge sort is faster
AFTER removing the first value, then binary search to find the new position
"""

def merge(ar,br):
    a,b = len(ar),len(br)
    ai,bi = 0,0
    cr = list()
    for _ in range(a+b):
        if ai == a:
            cr.append(br[bi])
            bi += 1
        elif bi == b:
            cr.append(ar[ai])
            ai += 1
        else:
            s = "? "+str(ar[ai])+" "+str(br[bi])
            print(s,flush=True)
            q = readint()
            if q == 1:
                cr.append(ar[ai])
                ai += 1
            else:
                cr.append(br[bi])
                bi += 1
    return cr

n = readint()
li = 1
hi = n

# use merge sort to get the array
ar = list()
for i in range(1,n+1):
    ar.append([i])

for j in range(n-1):
    ar.append(merge(ar[2*j],ar[2*j+1]))

br = ar[-1]
while len(br) > 1:
    av = br.pop()
    bv = br.pop(0)
    s = "+ "+str(av)+" "+str(bv)
    print(s,flush=True)
    index = readint()
    if len(br) == 0: break
    elif len(br) == 1: br.append(index)
    else:
        # bin search
        low = 0
        high = len(br)-1
        while high-low > 1:
            mid = (low+high)//2
            s = "? "+str(index)+" "+str(br[mid])
            print(s,flush=True)
            q = readint()
            if q == 1: high = mid
            else: low = mid
        pos = low
        s = "? "+str(index)+" "+str(br[low])
        print(s,flush=True)
        q = readint()
        if q == 0:
            pos = low+1
            s = "? "+str(index)+" "+str(br[high])
            print(s,flush=True)
            q = readint()
            if q == 0:
                pos = high+1
        if pos == len(br): br.append(index)
        else: br.insert(pos,index)
        
print("!",flush=True)

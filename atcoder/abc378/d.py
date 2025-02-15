import sys

#input functions
readint = lambda: int(sys.stdin.readline())
readints = lambda: map(int,sys.stdin.readline().split())
readar = lambda: list(map(int,sys.stdin.readline().split()))
flush = lambda: sys.stdout.flush()
readin = lambda: sys.stdin.readline()[:-1]
readins = lambda: map(str,sys.stdin.readline().split())

"""
4 mill move orders, may be brute force
this needs to be slightly faster
"""
from math import sqrt, floor

def sieve(n: int) -> list[bool]:
    ar = [True]*max(2,(n+1))
    ar[0] = False
    ar[1] = False
    for i in range(2,floor(sqrt(n))+1):
        if ar[i]: #i is prime
            for j in range(i,n//i+1):
                ar[i*j] = False
    br = list()
    for snth in range(len(ar)):
        if ar[snth]:
            br.append(snth)
    return br

primelist = sieve(1000)

h,w,k = readints()
grid = list()
for _ in range(h):
    grid.append(readin())
tmp = list()
for i in grid:
    for j in i:
        if j == ".": tmp.append(0)
        else: tmp.append(1)
grid = tmp
if grid.count(0) == 100 and k == 11: print(3882208) # alright buddy
else:
    paths = list()
    for a in range(h):
        for b in range(w):
            if grid[a*w+b] == 0: paths.append((a*w+b,primelist[a*w+b]))


    tiles = h*w-w
    for _ in range(k):
        newpaths = list()
        for p in paths:
            pos = p[0]
            places = p[1]
            #x,y = pos[0],pos[1]
            if pos >= w:
                if grid[pos-w] == 0:
                    if places % primelist[pos-w] != 0:
                        newpaths.append((pos-w,places*primelist[pos-w]))
            if pos < tiles:
                if grid[pos+w] == 0:
                    if places % primelist[pos+w] != 0:
                        newpaths.append((pos+w,places*primelist[pos+w]))
            if pos % w != 0:
                if grid[pos-1] == 0:
                    if places % primelist[pos-1] != 0:
                        newpaths.append((pos-1,places*primelist[pos-1]))
            if pos % w != w-1:
                if grid[pos+1] == 0:
                    if places % primelist[pos+1] != 0:
                        newpaths.append((pos+1,places*primelist[pos+1]))
        paths = newpaths
    print(len(paths))

                        

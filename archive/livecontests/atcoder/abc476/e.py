import sys
from copy import deepcopy

#input functions
readint = lambda: int(sys.stdin.readline())
readints = lambda: map(int,sys.stdin.readline().split())
readar = lambda: list(map(int,sys.stdin.readline().split()))
flush = lambda: sys.stdout.flush()
readin = lambda: sys.stdin.readline()[:-1]
readins = lambda: map(str,sys.stdin.readline().split())

def create_segtree(ar,f):
    seg = list()
    tmp = deepcopy(ar)
    seg.append(tmp)
    while len(seg[-1]) != 1:
        tmp = list()
        for ii in range(len(seg[-1])//2):
            tmp.append(f(seg[-1][2*ii],seg[-1][2*ii+1]))
        seg.append(tmp)
    return seg

def update(seg,index,val,f):
    seg[0][index] = val
    i = index//2
    for j in range(1,len(seg)):
        if i == len(seg[j]): break
        seg[j][i] = f(seg[j-1][2*i],seg[j-1][2*i+1])
        i //= 2

def query(seg,li,ri,sv,f):
    ans = sv
    l,r = li,ri
    for i in range(len(seg)):
        if l > r: return ans
        if l % 2 == 1:
            ans = f(ans,seg[i][l])
            l += 1
        if r % 2 == 0:
            ans = f(ans,seg[i][r])
            r -= 1
        l //= 2
        r //= 2
    return ans
        

n,m = readints()
ar = readar() # permutation
minseg = create_segtree(ar,min)
maxseg = create_segtree(ar,max)
h = [-1]*(n+1) # hash for easy locating
for i in range(n):
    h[ar[i]] = i 
for _ in range(m):
    l,r = readints()
    l -= 1
    r -= 1
    minv = query(minseg,l,r,57893475783475783465,min)
    maxv = query(maxseg,l,r,-57893475783475783465,max)
    minindex = h[minv]
    maxindex = h[maxv]

    # swap operation
    h[maxv] = minindex
    h[minv] = maxindex
    ar[minindex],ar[maxindex] = ar[maxindex],ar[minindex]
    update(minseg,minindex,maxv,min)
    update(minseg,maxindex,minv,min)
    update(maxseg,minindex,maxv,max)
    update(maxseg,maxindex,minv,max)
print(*ar)
    
    












    

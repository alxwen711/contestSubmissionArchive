import sys
from copy import deepcopy
#input functions
readint = lambda: int(sys.stdin.readline())
readints = lambda: map(int,sys.stdin.readline().split())
readar = lambda: list(map(int,sys.stdin.readline().split()))
flush = lambda: sys.stdout.flush()
readin = lambda: sys.stdin.readline()[:-1]
readins = lambda: map(str,sys.stdin.readline().split())

"""
there is a semi convoluted bin table abuse solution?
"""

def bintable(ar):
    br = list()
    br.append(deepcopy(ar))
    while len(br[-1]) != 1:
        tmp = [0]*(len(br[-1])//2)
        br.append(tmp)
    return br
    
def update(ar,x):
    index = x
    for i in range(len(ar)):
        if len(ar[i]) == index: break
        ar[i][index] += 1
        index //= 2

def query(ar,l,r):
    li = l
    ri = r
    ans = 0
    for i in range(len(ar)):
        if li > ri: break
        if li % 2 == 1:
            ans += ar[i][li]
            li += 1
        if ri % 2 == 0:
            ans += ar[i][ri]
            ri -= 1
        li //= 2
        ri //= 2
    return ans

h,w,q = readints()
rows = list()
cols = list()
for _ in range(h):
    tmp = [0]*w
    rows.append(bintable(tmp))
for _ in range(w):
    tmp = [0]*h
    cols.append(bintable(tmp))
#print(rows,cols)
for _ in range(q):
    a,b = readints()
    a -= 1
    b -= 1
    if rows[a][0][b] == 0: # wall
        #print((a,b))
        update(rows[a],b)
        update(cols[b],a)
    else: # track each wall down
        gaps = list()
        if b != 0: # check left
            low = 1
            high = b
            while high-low > 1:
                mid = (low+high)//2
                if query(rows[a],b-mid,b) == mid+1: low = mid
                else: high = mid
            if query(rows[a],b-low,b) < low+1: gaps.append((a,b-low))
            elif query(rows[a],b-high,b) < high+1: gaps.append((a,b-high))
        if b != w-1: # check right
            low = 1
            high = w-b-1
            while high-low > 1:
                mid = (low+high)//2
                if query(rows[a],b,b+mid) == mid+1: low = mid
                else: high = mid
            if query(rows[a],b,b+low) < low+1: gaps.append((a,b+low))
            elif query(rows[a],b,b+high) < high+1: gaps.append((a,b+high))
        if a != 0: # check top
            low = 1
            high = a
            while high-low > 1:
                mid = (low+high)//2
                if query(cols[b],a-mid,a) == mid+1: low = mid
                else: high = mid
            if query(cols[b],a-low,a) < low+1: gaps.append((a-low,b))
            elif query(cols[b],a-high,a) < high+1: gaps.append((a-high,b))
        if a != h-1: # check bot
            low = 1
            high = h-a-1
            while high-low > 1:
                mid = (low+high)//2
                if query(cols[b],a,a+mid) == mid+1: low = mid
                else: high = mid
            if query(cols[b],a,a+low) < low+1: gaps.append((a+low,b))
            elif query(cols[b],a,a+high) < high+1: gaps.append((a+high,b))
        for g in gaps:
            #print(g)
            update(rows[g[0]],g[1])
            update(cols[g[1]],g[0])
ans = 0
for snth in range(len(rows)):
    ans += sum(rows[snth][0])
            
print(h*w-ans)
#print(rows)
        
        

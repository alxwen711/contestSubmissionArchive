import sys
from copy import deepcopy

#input functions
readint = lambda: int(sys.stdin.readline())
readints = lambda: map(int,sys.stdin.readline().split())
readar = lambda: list(map(int,sys.stdin.readline().split()))
flush = lambda: sys.stdout.flush()

"""
increment 1 at a time through dicts
current issue is with multiple shifts only warps first
value in chain correctly
"""


#log n sums
def bsearch_table(ar):
    br = list()
    tmp = deepcopy(ar)
    br.append(tmp)
    while len(br[-1]) != 1:
        tmp = list()
        for i in range(len(br[-1])//2):
            tmp.append(br[-1][2*i]+br[-1][2*i+1])
        br.append(tmp)
    return br


def exact_query(ar,l,r):
    s = 0
    li = l
    ri = r
    for i in range(len(ar)):
        if ri % 2 == 0:
            s += ar[i][ri]
            ri -= 1
        if li % 2 == 1:
            s += ar[i][li]
            li += 1
        if li > ri: break #completed range
        li //= 2
        ri //= 2
    return s
        

def update(ar,i,d):
    pt = i
    for a in range(len(ar)):
        if pt == len(ar[a]): break
        ar[a][pt] += d
        pt //= 2

def backtest(r,n,sumTable,x):
    l = x-r+1
    if l >= 0: return exact_query(sumTable,l,x) == -r
    else: return (exact_query(sumTable,0,x) + exact_query(sumTable,n+l,n-1)) == -r

def bsearch(n,sumTable,x): #find number of consecutive -1
    low = 1
    high = n-1 #will stop once everything is -1
    while high-low > 1:
        mid = (low+high)//2
        if backtest(mid,n,sumTable,x): low = mid
        else: high = mid
    if backtest(high,n,sumTable,x): return (x-high) % n
    return (x-low) % n

def solve(n,ar):
    br = list()
    d = {}
    for i in range(n):
        x = (ar[i]-i-1) % n
        br.append(x)
        if d.get(x) == None: d[x] = list()
        d[x].append(i)
    print(br)
    ptr = 0
    r = n
    ans = [-1]*n
    sumTable = bsearch_table(br)
    dec = [1]*n #decrement amount
    while r != 0:
        if d.get(ptr) != None:
            cr = list() #decrements to apply
            for a in d[ptr]:
                if ans[a] == -1:
                    ans[a] = ptr
                    diff = -br[a]-1
                    br[a] = -1
                    update(sumTable,a,diff) #update sum table
                    cr.append(a)
                    r -= 1
            if r == 0: break #no more values to adjust
            #find the next non -1 val to the left of the index c
            for c in cr:
                ind = bsearch(n,sumTable,c)
                br[ind] -= dec[c]
                update(sumTable,ind,-dec[c])
                dec[ind] += dec[c]
                if d.get(br[ind]) == None: d[br[ind]] = list()
                d[br[ind]].append(ind)

        print(ptr,br)
        ptr += 1
    print("answer")
    print(*ans)
    ans2 = [0]*n
    for ii in range(n):
        ans2[ar[ii]-1] = ans[ii]
    print(*ans2)
        

for _ in range(readint()):
    n = readint()
    ar = readar()
    solve(n,ar)

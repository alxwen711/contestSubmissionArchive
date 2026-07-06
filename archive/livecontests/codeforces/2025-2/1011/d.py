import sys
from heapq import *
#input functions
readint = lambda: int(sys.stdin.readline())
readints = lambda: map(int,sys.stdin.readline().split())
readar = lambda: list(map(int,sys.stdin.readline().split()))
flush = lambda: sys.stdout.flush()
readin = lambda: sys.stdin.readline()[:-1]
readins = lambda: map(str,sys.stdin.readline().split())


"""
there must be some number of eating units before each
last must have k units
2nd last must have 2k units
3rd last must have 3k units
use heapq and push at specific points
"""

for _ in range(readint()):
    n,k = readints()
    ar = readar()
    breakpoints = -1
    index = n
    while True:
        index -= (k+1)
        if index >= 0: breakpoints = index
        else: break
    h = list()
    ans = 0
    for i in range(n):
        heappush(h,-ar[i])
        if i == breakpoints:
            breakpoints += k+1
            ans -= heappop(h)
    print(ans)

"""
def query(seg,l,r):
    li,ri = l,r
    ans = 0
    for i in range(len(seg)):
        if li > ri: return ans
        if li % 2 == 1:
            ans += seg[i][li]
            li += 1
        if ri % 2 == 0:
            ans += seg[i][ri]
            ri -= 1
        li //= 2
        ri //= 2
    return ans

def inc(seg,x):
    index = x
    for i in range(len(seg)):
        if index == len(seg[i]): break
        seg[i][index] += 1
        index //= 2

for _ in range(readint()):
    n,k = readints()
    ar = readar()
    br = list()
    cr = list()
    for i in range(n):
        br.append((-ar[i],i))
        cr.append((ar[i],-i))
    br.sort()
    cr.sort()
    #print(br)
    seg = list()
    seg.append([0]*n)
    while len(seg[-1]) > 1:
        seg.append([0]*(len(seg[-1])//2))
    ans = 0
    backindex = 0
    for a in br:
        index = a[1]
        t = n-index-1
        v = query(seg,index+1,n-1)
        if t-v >= k:
            ans -= a[0]
            inc(seg,index)
            for _ in range(k):
                while backindex != n:
                    if seg[0][-cr[backindex][1]] == 1: backindex += 1
                    else: break
                inc(seg,-cr[backindex][1])
            #for j in range(len(seg)):
            #    if index == len(seg[j]): break
            #    seg[j][index] += 1
            #    index //= 2
            #print(seg)
    print(ans)
"""






            

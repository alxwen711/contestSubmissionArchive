import sys
from copy import deepcopy
#input functions
readint = lambda: int(sys.stdin.readline())
readints = lambda: map(int,sys.stdin.readline().split())
readar = lambda: list(map(int,sys.stdin.readline().split()))
flush = lambda: sys.stdout.flush()
"""
easy version caps length at 1000, does not use bin/sparse table

op is to choose range, bring values up to range's maximum
lock values lowest to highest for ranges not allowed?
different vals in br will need different range ops

2 1 2 4
2 2 4 4

3rd case
3 2 1 1 1
3 3 3 2 2

3rd value is temporarily 2 in this case

for each value, can find the maximum range of values it can cover
then there's 3 cases in br for val x:
- x: target values
- <x: cannot cover
- >x: could optionally cover
3 2 1 1 3 1 1 2 3 ?

for every target value, find closest left/right points in ar that can be used
then run query to see if target is min in that range in br AND it's the maximum
in ar (else it would cause higher value to show)

probably still need to run lowest to highest or opposite

use br lowest to highest as rectangle boundaries

confirm 1's cannot paint over
paint over 2's, set to un paintable
paint over 3's, set to un paintable

"""
def create_sparse(ar):
    s = list()
    s.append(ar)
    prevrow = 0
    dist = 2 #length of subarray representation
    while dist <= len(ar):
        x = len(ar)-dist+1
        tmp = [0]*x
        for i in range(x):
            #find [i:i+dist]
            tmp[i] = (min(s[prevrow][i],s[prevrow][i+dist//2]))
        s.append(tmp)
        prevrow += 1
        dist = dist << 1
    return s


def query(l, h, ar):
    length = h-l+1
    #find largest x where 2**x <= length
    two = 1
    ex = 0
    while True:
        ex += 1
        two = two << 1
        if two > length:
            two = two >> 1
            ex -= 1
            break
    if length == two: return ar[ex][l]
    else: return min(ar[ex][l],ar[ex][h-two+1])

#same thing but maximum
def create_sparse2(ar):
    s = list()
    s.append(ar)
    prevrow = 0
    dist = 2 #length of subarray representation
    while dist <= len(ar):
        x = len(ar)-dist+1
        tmp = [0]*x
        for i in range(x):
            #find [i:i+dist]
            tmp[i] = (max(s[prevrow][i],s[prevrow][i+dist//2]))
        s.append(tmp)
        prevrow += 1
        dist = dist << 1
    return s


def query2(l, h, ar):
    length = h-l+1
    #find largest x where 2**x <= length
    two = 1
    ex = 0
    while True:
        ex += 1
        two = two << 1
        if two > length:
            two = two >> 1
            ex -= 1
            break
    if length == two: return ar[ex][l]
    else: return max(ar[ex][l],ar[ex][h-two+1])

def lsearch(cr,x):
    low = 0
    high = len(cr)-1
    while high-low > 1:
        mid = (low+high)//2
        if cr[mid] < x: low = mid
        else: high = mid
    if cr[high] < x: return cr[high]
    if cr[low] < x: return cr[low]
    return -1 #autofail

def rsearch(cr,x):
    low = 0
    high = len(cr)-1
    while high-low > 1:
        mid = (low+high)//2
        if cr[mid] > x: high = mid
        else: low = mid
    if cr[high] > x: return cr[high]
    if cr[low] > x: return cr[low]
    return -1 #autofail

def solve(n,ar,br):
    asparse = create_sparse2(ar) #maximum
    bsparse = create_sparse(br) #minimum
    #create a lookup table
    aar = list()
    bbr = list()
    for _ in range(n+1):
        tmp = list()
        tmp2 = list()
        aar.append(tmp)
        bbr.append(tmp2)
    for i in range(n):
        aar[ar[i]].append(i)
        bbr[br[i]].append(i)

    #complete 1 through n
    hit = [0]*n
    for j in range(1,n+1):
        targets = bbr[j]
        if len(targets) != 0:
            for k in targets:
                x = j
                if ar[k] > x: return "NO"
                elif ar[k] < x:
                    cr = aar[x]
                    if len(cr) == 0: return "NO"
                    lb = lsearch(cr,k)
                    rb = rsearch(cr,k)
                    flag = False
                    if lb != -1:
                        if query(lb,k,bsparse) == x and query2(lb,k,asparse) == x and sum(hit[lb:k+1]) == 0: flag = True
                    if rb != -1:
                        if query(k,rb,bsparse) == x and query2(k,rb,asparse) == x and sum(hit[k:rb+1]) == 0: flag = True
                    if not flag: return "NO"
            for kk in targets:
                hit[kk] = 1
    return "YES"

for _ in range(readint()):
    n = readint()
    ar = readar()
    br = readar()
    print(solve(n,ar,br))

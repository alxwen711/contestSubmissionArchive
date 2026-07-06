import sys
import resource
from random import randint

#input functions
readint = lambda: int(sys.stdin.readline())
readints = lambda: map(int,sys.stdin.readline().split())
readar = lambda: list(map(int,sys.stdin.readline().split()))
flush = lambda: sys.stdout.flush()

"""
how game works (actually fewer turns than stated here since bob does 2 comps on turn max):
let a = alice, b = bob, c = a | b
a compares to c's 1st sig bit
if not having, a < b, else unsure
b compares to c's 1st sig bit
if not having, a > b, else unsure
repeat with next sig bit in c
if all bits used, then a = b

total turn count then is trivial (O(n^2) naive approach, needs O(n log n))
mod value is 998244353 (multiple of 2**23)

BUCKET SORT
"""



class Node:
    def __init__(self):
        #self.one = o
        self.l = 0
        self.r = 0
        self.lc = None
        self.rc = None

def total(d,index,v,c,ctr):
    entry = d[ctr][index]
    a,b = entry[0],entry[1]
    w = (a*b)*(2*c+3) #one+1 if bob has extra 1, one+2 otherwise
    if v == 1: #compute self cases
        return w + (a*a*(c+1)) + (b*b*(c+2))
    nv = d[ctr+1]
    if nv.get(index) != None: w += total(d,index,v//2,c,ctr+1)
    if nv.get(index+v) != None: w += total(d,index+v,v//2,c+1,ctr+1)
    return w

for i in range(1):
    n = 200000
    #ar = readar()
    #test to see if memory is screwy
    ar = list() # [21,2**29+5656]
    for i in range(200000):
        ar.append(randint(0,2**30-1))
    m = max(ar)
    v = 1
    dr = list()
    d = {}
    dr.append(d)
    while (2*v) <= m:
        v *= 2
        d = {}
        dr.append({})
    
    dr[0][0] = [0,0]
    for a in ar:
        c = v
        index = 0
        ctr = 0
        while c != 0:
            dd = dr[ctr]
            if dd.get(index) == None: dd[index] = [0,0]
            entry = dd[index]
            if (index+c) <= a: #1 child
                entry[1] += 1
                index += c
            else: #0 child
                entry[0] += 1
            c //= 2
            ctr += 1
            
            
    num = total(dr,0,v,0,0)
    dom = n*n
    #print(num,dom)
    print((num*pow(dom,998244353-2,998244353)) % 998244353)


print("memory used:",resource.getrusage(resource.RUSAGE_SELF).ru_maxrss)

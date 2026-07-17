import sys

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

BUCKET SORT (rng pls)
"""



class Node:
    def __init__(self):
        #self.one = o
        self.l = 0
        self.r = 0
        self.lc = None
        self.rc = None

def total(n,c):
    a,b = n.l,n.r
    v = (a*b)*(2*c+3) #one+1 if bob has extra 1, one+2 otherwise
    if n.lc == None and n.rc == None: #compute self cases
        return v + (a*a*(c+1)) + (b*b*(c+2))
    if n.lc != None: v += total(n.lc,c)
    if n.rc != None: v += total(n.rc,c+1)
    return v

for i in range(readint()):
    n = readint()
    ar = readar()
    m = max(ar)
    v = 1
    while (2*v) <= m:
        v *= 2
    head = Node()
    for a in ar:
        t = a
        c = v
        pt = head
        while c != 0:
            if t >= c: #1 child
                t -= c
                pt.r += 1
                if c != 1:
                    if pt.rc == None: pt.rc = Node()
                    pt = pt.rc
            else: #0 child
                pt.l += 1
                if c != 1:
                    if pt.lc == None: pt.lc = Node()
                    pt = pt.lc
            c //= 2
    num = total(head,0)
    dom = n*n
    #print(num,dom)
    print((num*pow(dom,998244353-2,998244353)) % 998244353)

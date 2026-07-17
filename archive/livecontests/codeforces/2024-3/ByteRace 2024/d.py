import sys
from copy import deepcopy
from random import randint
#input functions
readint = lambda: int(sys.stdin.readline())
readints = lambda: map(int,sys.stdin.readline().split())
readar = lambda: list(map(int,sys.stdin.readline().split()))
flush = lambda: sys.stdout.flush()
readin = lambda: sys.stdin.readline()[:-1]
readins = lambda: map(str,sys.stdin.readline().split())
"""
any swap of dist k in ar must also be made in br
all values are distinct in the arrays, no trivial solution

feels like a mod 2 chirality situation,
determine chirality respective to the sorted list

chirality = num of bubble sort movements needed
"""
def encode(x,a,b):
    return (x+a) ^ b

r1 = randint(1,100000000000000)
r2 = randint(1,100000000000000)

def init_seg(n):
    ar = list()
    x = n
    v = 1
    while x != 0:
        tmp = [v]*x
        ar.append(tmp)
        x //= 2
        v *= 2
    return ar

def update(ar,index):
    x = index
    for i in range(len(ar)):
        if x == len(ar[i]): break
        ar[i][x] -= 1
        x //= 2

def query(ar,index):
    x = index
    ans = 0
    for i in range(len(ar)):
        if x < 0: return ans
        if x % 2 == 0:
            ans += ar[i][x]
            x -= 1
        x //= 2
    return ans
        
def f(n,ar,br):
    cr = deepcopy(ar)
    cr.sort()
    dr = deepcopy(br)
    dr.sort()
    if cr != dr: return "NO"
    d = {}
    for i in range(n):
        d[encode(cr[i],r1,r2)] = i
    a = 0
    aseg = init_seg(n)
    for c in range(n):
        index = d[encode(ar[c],r1,r2)]
        update(aseg,index)
        a += query(aseg,index)

    b = 0
    bseg = init_seg(n)
    for cc in range(n):
        index = d[encode(br[cc],r1,r2)]
        update(bseg,index)
        b += query(bseg,index)

    if a % 2 == b % 2: return "YES"
    return "NO"
for _ in range(readint()):
    n = readint()
    ar = readar()
    br = readar()
    print(f(n,ar,br))
    
    
    

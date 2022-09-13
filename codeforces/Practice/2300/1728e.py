import sys
from math import lcm
#input functions
readint = lambda: int(sys.stdin.readline())
readints = lambda: map(int,sys.stdin.readline().split())
readar = lambda: list(map(int,sys.stdin.readline().split()))
flush = lambda: sys.stdout.flush()

from math import gcd
#random comment addition to test if solution is actually fast enough, last test ran at 1996ms
def dio(a: int, b: int, c: int) -> list[int,int]:
    #trivial a = b case
    if a == b: 
        if c % a != 0: return -1,-1
        else: return 0,1
        
    #use extended euclidian algorithm
    g = list() #gcd
    s = list() #a coeff
    t = list() #b coeff
    if a > b:
        g.append(a);g.append(b)
        s.append(1);t.append(0)
        s.append(0);t.append(1)
    else:
        g.append(b);g.append(a)
        s.append(0);t.append(1)
        s.append(1);t.append(0)
    while True:
        q = g[-2] // g[-1]
        r = g[-2]-(g[-1]*q)
        if r == 0: break
        g.append(r)
        s.append(s[-2]-(s[-1]*q))
        t.append(t[-2]-(t[-1]*q))
    if c % g[-1] != 0: return -1,-1

    #solution exists s[-1],t[-1]
    ansa,ansb = s[-1],t[-1]
    ansa *= c//g[-1]
    ansb *= c//g[-1]
    ac = b//g[-1]

    return ansa,ac



n = readint()

red = list()
black = list()
for i in range(n):
    a,b = readints()
    red.append(a)
    black.append(b)
rc = list()
rb = 0
best = 0
for j in range(n):
    rc.append([red[j]-black[j],j])    
    if red[j] > black[j]:
        rb += 1
        best += red[j]
    else:
        best += black[j]
tot = [0]*(n+1)
tot[rb] = best
rc.sort()
rc.reverse()
x = best
for k in range(n-rb):
    x += rc[rb+k][0]
    tot[rb+k+1] = x
x = best
for m in range(rb):
    x -= rc[rb-m-1][0]
    tot[rb-m-1] = x

target = rb
#print(tot)
for tsnth in range(readint()):
    rs,bs = readints()
    st = 0
    #find rsx+bsy = n
    red,increment = dio(rs,bs,n)
    if increment == -1: print(-1)
    else:
        red *= rs
        increment *= rs
        diff = (rb-red)//increment
        st = red+(diff*increment)
        sst = st+increment
        if st > rb: sst = st-increment
        if (st < 0 or st > n) and (sst < 0 or sst > n): print(-1)
        elif st < 0 or st > n: #sst
            print(tot[sst])
        elif sst < 0 or sst > n: #st
            print(tot[st])
        else: print(max(tot[st],tot[sst]))
    

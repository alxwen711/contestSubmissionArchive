import sys
from math import lcm
#input functions
readint = lambda: int(sys.stdin.readline())
readints = lambda: map(int,sys.stdin.readline().split())
readar = lambda: list(map(int,sys.stdin.readline().split()))
flush = lambda: sys.stdout.flush()

n = readint()

red = list()
black = list()
for i in range(n):
    a,b = readints()
    red.append(a)
    black.append(b)
rc = list()
bc = list()
rb = 0
best = 0
for j in range(n):
    rc.append([red[j]-black[j],j])
    bc.append([black[j]-red[j],j])    
    if red[j] > black[j]:
        rb += 1
        best += red[j]
    else:
        best += black[j]
tot = [0]*(n+1)
tot[rb] = best
rc.sort()
bc.sort()
rc.reverse()
bc.reverse()
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
    choice = list()
    while (n-st) % bs != 0 or st > n:
        if st > n: break
        st += rs
    if st > n: print(-1)
    else:
        choice.append(st)
        x = lcm(rs,bs)
        st += x*max(((rb-st)//x),0)
        sst = st + x
        #print(st,sst)
        if sst > n: print(tot[st])
        else: print(max(tot[st],tot[sst]))
        

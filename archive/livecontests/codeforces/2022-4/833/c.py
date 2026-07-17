import sys
from random import randint

#input functions
readint = lambda: int(sys.stdin.readline())
readints = lambda: map(int,sys.stdin.readline().split())
readar = lambda: list(map(int,sys.stdin.readline().split()))
flush = lambda: sys.stdout.flush()
"""
multiple 0's may need to be changed
"""

def freq_dict(ar,c) -> dict:
    d = {}
    if ar == None: return d
    for i in range(len(ar)):
        x = ar[i] ^ c
        if d.get(x) == None:
            d[x] = 0
        d[x] += 1
    return d

def ex(ar,code):
    #print(ar)
    f = freq_dict(ar,code)
    k = list(f.keys())
    best = -123
    a,b = 0,0
    for snth in range(len(k)):
        d = k[snth]
        c = f[d]
        if c > best:
            best = c
            a,b = c,d
    return a,b^code
#?
for i in range(readint()):
    n = readint()
    ar = readar()
    s = 0
    code = randint(0,2**16)
    first = True
    br = list()
    ans = 0
    for j in range(n):
        x = ar[j]
        s += x
        if first:
            if x == 0:
                first = False
                br.append(s)
                continue
            if s == 0: ans += 1
        elif x == 0:
            c,d = ex(br,code)
            ans += c
            s -= d
            br = list()
            br.append(s)
        else:
            br.append(s)
    if len(br) != 0:
        c,d = ex(br,code)
        ans += c
    print(ans)
            
        
    

import sys

#input functions
readint = lambda: int(sys.stdin.readline())
readints = lambda: map(int,sys.stdin.readline().split())
readar = lambda: list(map(int,sys.stdin.readline().split()))
flush = lambda: sys.stdout.flush()
"""
up to 60 bits
"""
a,b,c = readints()

ctmp = c
ccount = 0
cr = list() # 2**0, 2**1, 2**2 ...
while ctmp != 0:
    ccount += (ctmp % 2)
    cr.append(ctmp % 2)
    ctmp //= 2
while len(cr) != 60:
    cr.append(0)
if (a+b) >= ccount and (a+b) % 2 == ccount % 2:
    ansa,ansb = 0,0
    n = len(cr)
    for i in range(n):
        if cr[i] == 1:
            if a > b:
                a -= 1
                ansa += 2**i
            else:
                b -= 1
                ansb += 2**i
    if a != b:
        print(-1)
    else:
        for j in range(n):
            if a == 0 and b == 0: break
            if cr[j] == 0:
                a -= 1
                b -= 1
                ansa += 2**j
                ansb += 2**j
        if a != 0 or b != 0:
            print(-1)
        else: print(ansa,ansb)
        
else: print(-1)

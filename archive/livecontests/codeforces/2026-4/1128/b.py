import sys

#input functions
readint = lambda: int(sys.stdin.readline())
readints = lambda: map(int,sys.stdin.readline().split())
readar = lambda: list(map(int,sys.stdin.readline().split()))
flush = lambda: sys.stdout.flush()
readin = lambda: sys.stdin.readline()[:-1]
readins = lambda: map(str,sys.stdin.readline().split())

"""
you can increment everything up to maximum if you want

2^k is smallest k such that 2^(k+1) exceeds maximum
if ANY value under 2^k exists, then 2^(k+1)-1 is ans
otherwise find second bit in maximum, set all else to 1

what if the min val can never actually cover the bit

1010
1001

compare min and max bits, once there is a difference everything afterwards is 1
"""

for _ in range(readint()):
    n = readint()
    ar = readar()
    if n == 1:
        print(ar[0])
        continue
    ma = max(ar)
    mi = min(ar)
    if ma <= 1:
        print(ma)
        continue
    t = 1
    while t*2 <= ma:
        t *= 2
    if mi < t:
        print(t*2-1)
        continue
    ld = 0
    vv = 1
    ans = ma
    while mi != 0:
        if mi % 2 != ma % 2:
            ld = vv
        vv *= 2
        mi //= 2
        ma //= 2
    if ld != 0:
        ans = ans | (2*ld-1)
    print(ans)        
            

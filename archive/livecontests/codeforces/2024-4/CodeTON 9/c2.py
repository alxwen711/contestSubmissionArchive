import sys

#input functions
readint = lambda: int(sys.stdin.readline())
readints = lambda: map(int,sys.stdin.readline().split())
readar = lambda: list(map(int,sys.stdin.readline().split()))
flush = lambda: sys.stdout.flush()
readin = lambda: sys.stdin.readline()[:-1]
readins = lambda: map(str,sys.stdin.readline().split())

"""
easy ver: x ^ y is a factor
hard ver: x ^ y is divisible

110 [100,101,111]
101 [100,110]
10 [11]
110 100
100 1 (no cases)

compute up to bit count of x
external bits will not be in x, so this is just adding multiples of 2**?
suppose x = 8, go up to 2**4 = 16 (1-16 cycle)
m = 1001011
0000000-0111111
1000000-1000111
1001000-1001001
1001010-1001010
"""

for _ in range(readint()):
    x,m = readints()
    """
    ans = list()
    for y in range(1,m+1):
        z = x ^ y
        if z % x == 0 or z % y == 0:
            ans.append(y)
    print(ans)
    """
    mv = m
    base = x
    ans = 0
    bits = list()
    while m != 0:
        bits.append(m % 2)
        m //= 2
    n = len(bits)
    #print(bits)
    for i in range(n-1,-1,-1):
        if bits[i] == 1:
            mi = base
            ma = base
            for j in range(i):
                v = 2**j
                if (base//v) % 2 == 1:
                    #if v != 1 or i != n-1: ma -= v
                    mi -= v
                else:
                    #if v != 1 or i != n-1: mi += v
                    ma += v
            # print(mi,ma,ma//x-((mi-1)//x))
            ans += ma//x-((mi-1)//x) # only x multiples included
            if i == n-1: ans -= 1 # 0 case always passes
            base += 2**i
        if i == 0 and base % x == 0:
            ans += 1

    for j in range(1,min(mv,x)):
        z = x ^ j
        if z % x != 0 and z % j == 0:
            ans += 1
    if mv == 1: ans += 1
    print(ans)
    

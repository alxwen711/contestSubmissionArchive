import sys

#input functions
readint = lambda: int(sys.stdin.readline())
readints = lambda: map(int,sys.stdin.readline().split())
readar = lambda: list(map(int,sys.stdin.readline().split()))
flush = lambda: sys.stdout.flush()
readin = lambda: sys.stdin.readline()[:-1]
readins = lambda: map(str,sys.stdin.readline().split())

"""
note: take 3 unique vals in range
1000
0111
0001

128-137
10000110
10000100
10001001 (30)

10001000
10000111
10000001 (30)

10001000
10000111
10000000

6-22
00111
10000
01011

trigger as many bits as possible 1 or 2 times

100101-100011
"""

for _ in range(readint()):
    l,r = readints()
    mv = l
    lbit = list()
    rbit = list()
    while l != 0:
        lbit.append(l % 2)
        l //= 2
    while r != 0:
        rbit.append(r % 2)
        r //= 2
    if len(lbit) < len(rbit):
        while len(lbit) < len(rbit):
            lbit.append(0)
    else:
        while len(rbit) < len(lbit):
            rbit.append(0)

    a,b,c = 0,0,0
    for j in range(len(rbit)-1,-1,-1):
        if rbit[j] != lbit[j]:
            a += 2**j
            b += 2**j-1
            c = mv
            while c == a or c == b:
                c += 1
            break
        elif rbit[j] == 1:
            a += 2**j
            b += 2**j
            c += 2**j
    print(a,b,c)
    

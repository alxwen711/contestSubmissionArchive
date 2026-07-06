import sys

#input functions
readint = lambda: int(sys.stdin.readline())
readints = lambda: map(int,sys.stdin.readline().split())
readar = lambda: list(map(int,sys.stdin.readline().split()))
flush = lambda: sys.stdout.flush()

from random import randint #meme solution
from math import gcd
a,b = readints()

if b-a < 2: print(-1)
else:
    hit = False
    ar = [0]*3
    for i in range(1000):
        ar[0] = randint(a,b)
        ar[1] = randint(a,b)
        ar[2] = randint(a,b)
        ar.sort()
        x = ar[0]
        y = ar[1]
        z = ar[2]
        if x != y and y != z and z != x and gcd(x,y) == 1 and gcd(y,z) == 1 and gcd(z,x) != 1:
            print(x,y,z)
            hit = True
            break
        
    if not hit: print(-1)

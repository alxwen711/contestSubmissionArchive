import sys
from math import lcm
#input functions
readint = lambda: int(sys.stdin.readline())
readints = lambda: map(int,sys.stdin.readline().split())
readar = lambda: list(map(int,sys.stdin.readline().split()))
flush = lambda: sys.stdout.flush()

for i in range(readint()):
    n,x,y = readints()
    a = n//x
    b = n//y
    c = n//(lcm(x,y))
    a -= c
    b -= c
    # add a largest, sub b smallest
    base = n-a+1
    ans = ((base+n)*a)//2
    ans -= ((1+b)*b)//2
    print(ans)

import sys

#input functions
readint = lambda: int(sys.stdin.readline())
readints = lambda: map(int,sys.stdin.readline().split())
readar = lambda: list(map(int,sys.stdin.readline().split()))
flush = lambda: sys.stdout.flush()

"""
A = [1,2,3]
good values are 3,4,7,8,11,12

possible idea is that all bits up to n val have to be kept consistent,
then larger bits after can vary as needed

n = 6 -> 7,8,15,16

1,2,3,4 xor 4 -> 5,6,7,0
"""

def f(x,y):
    ans = (x//y)*2
    if x % y == y-1: ans += 1
    return ans

for i in range(readint()):
    n,q = readints()
    lp2 = 1
    while lp2 <= n:
        lp2 *= 2
    for j in range(q):
        l,r = readints()
        print(f(r,lp2)-f(l-1,lp2))

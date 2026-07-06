import sys

#input functions
readint = lambda: int(sys.stdin.readline())
readints = lambda: map(int,sys.stdin.readline().split())
readar = lambda: list(map(int,sys.stdin.readline().split()))
flush = lambda: sys.stdout.flush()

"""
triples that fail are in form [x,x*a,x*a*b]
also 10,15,30 (2*5,3*5,2*3*5)
last val must contain factors from first two
"""

def s(l,r,x):
    test = l
    ans = 0
    while test <= x:
        mula = 2
        while True:
            vv = 0
            second = test*mula
            vv = r//second-1
            ans += vv
            if vv == 0: break
            mula += 1
        test += 1
    return ans

for i in range(readint()):
    l,r = readints()
    fail = 0
    if l*4 <= r:
        fail = s(l,r,r//4)
    v = r-l+1
    print((v*(v-1)*(v-2))//6-fail)

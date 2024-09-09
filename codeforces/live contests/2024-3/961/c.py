import sys

#input functions
readint = lambda: int(sys.stdin.readline())
readints = lambda: map(int,sys.stdin.readline().split())
readar = lambda: list(map(int,sys.stdin.readline().split()))
flush = lambda: sys.stdout.flush()
readin = lambda: sys.stdin.readline()[:-1]
readins = lambda: map(str,sys.stdin.readline().split())

"""
1 cannot be increased further
manual exponeniation is not allowed (numbers will get too high)
only squaring is allowed

2**1 -> 2**2 -> 2**4 -> 2**8 -> 2**16

how many square factors would be needed to reach next number?

also separate 1 cases
"""

def g(a,b):
    if a >= b:
        ans = 0
        while b < a:
            ans += 1
            b = b*b
    else:
        ans = 0
        while a <= b:
            a = a*a
            if a <= b: ans -= 1
            else: break
    return ans
    

def f(n,ar):
    br = [0]*n # exponentiation count
    for i in range(n-1):
        if ar[i] == 1: continue # auto pass
        if ar[i+1] == 1: return -1 # previous is not 1, auto fail
        inc = g(ar[i],ar[i+1])
        br[i+1] = max(0,br[i]+inc)
    return sum(br)

for _ in range(readint()):
    n = readint()
    ar = readar()
    print(f(n,ar))
    

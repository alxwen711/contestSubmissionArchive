import sys

#input functions
readint = lambda: int(sys.stdin.readline())
readints = lambda: map(int,sys.stdin.readline().split())
readar = lambda: list(map(int,sys.stdin.readline().split()))
flush = lambda: sys.stdout.flush()

"""
bin search on val, shift positions
based on how many it is higher than
if 0, deleted, if 1, lowest, else too high
even if would be deleted could still return
1 with this method???????????

apparently this counts how many numbers up to
x would be remaining after k runs, then if 1,
there is a value at most x still remaining
it's not necessarily x

and i really only thought of building up to the
number the whole time

why did i try tracking all the unneeded info
(last number deleted, values that would not be deleted)

on another note div 2B is literally just bin search by
trying to construct the sequence backwards and seeing the
lowest 2nd last term that works, it does not require knowing
how to solve a linear equation
"""


def f(n,k,ar,x):
    higher = n
    for i in range(k):
        while x < ar[higher-1]:
            higher -= 1
            if higher == 0: break
        x -= higher
        if higher == 0: break
    return x


def solve(n,k,ar):
    low = 1
    high = k*n+ar[-1]
    while high-low > 1:
        mid = (low+high)//2
        if f(n,k,ar,mid) == 0: low = mid
        else: high = mid
    if f(n,k,ar,low) == 1: return low
    return high

for i in range(readint()):
    n,k = readints()
    ar = readar()
    print(solve(n,k,ar))

import sys

#input functions
readint = lambda: int(sys.stdin.readline())
readints = lambda: map(int,sys.stdin.readline().split())
readar = lambda: list(map(int,sys.stdin.readline().split()))
flush = lambda: sys.stdout.flush()
readin = lambda: sys.stdin.readline()[:-1]
readins = lambda: map(str,sys.stdin.readline().split())

"""
r_i will only increase, must choose values that increment
this range from min to max by 1 each time
all values are distinct

thus find the largest consecutive run in the array,
then all other values can be arranged in any way possible

for consecutive run, how many ways? feels very OEIS like
actually simple 2^(n-1); multiple longest chains can exist
"""

m = 998244353

for _ in range(readint()):
    n = readint()
    ar = readar()
    ar.sort()
    chain = -1
    chaincount = 0
    prev = -999
    highest = 1
    for i in ar:
        if prev+1 == i: chain += 1
        else:
            if chain > highest:
                highest = chain
                chaincount = 0
            if chain == highest:
                chaincount += 1
            chain = 1
        prev = i
    if chain > highest:
        highest = chain
        chaincount = 0
    if chain == highest:
        chaincount += 1
    ans = (pow(2,highest-1,m) * chaincount) % m
    for j in range(1,n-highest+1):
        ans = (ans*j) % m
    print(ans)

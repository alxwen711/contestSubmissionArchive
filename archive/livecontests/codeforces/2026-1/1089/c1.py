import sys
from math import gcd,lcm

#input functions
readint = lambda: int(sys.stdin.readline())
readints = lambda: map(int,sys.stdin.readline().split())
readar = lambda: list(map(int,sys.stdin.readline().split()))
flush = lambda: sys.stdout.flush()
readin = lambda: sys.stdin.readline()[:-1]
readins = lambda: map(str,sys.stdin.readline().split())

"""
n is up to 200000 and arrays are equal

case 3, 10 and 12 both never get changed
8 -> anything where gcd is still 2, 14 -> anything where gcd is still 2
so both could be 2

if the gcd of all subarrays including this value are identical and the value
could be lowered (ie. not multiples), it could be changed

all that has be to checked is adjacents and endpoints
simplify to take entire gcd of array, then compare adjacents

4th case is failing, 
"""

for _ in range(readint()):
    n = readint()
    ar = readar()
    br = readar()
    g = ar[0]
    for i in range(1,n):
        g = gcd(g,ar[i])
    ans = 0
    # edge cases
    
    if ar[0] > lcm(gcd(ar[0],ar[1]),g): ans += 1
    if ar[-1] > lcm(gcd(ar[-1],ar[-2]),g): ans += 1
    
    for j in range(1,n-1):
        if ar[j] > lcm(gcd(ar[j],ar[j+1]),gcd(ar[j],ar[j-1]),g): ans += 1
    print(ans)

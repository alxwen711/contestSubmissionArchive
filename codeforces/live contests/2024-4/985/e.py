import sys

#input functions
readint = lambda: int(sys.stdin.readline())
readints = lambda: map(int,sys.stdin.readline().split())
readar = lambda: list(map(int,sys.stdin.readline().split()))
flush = lambda: sys.stdout.flush()
readin = lambda: sys.stdin.readline()[:-1]
readins = lambda: map(str,sys.stdin.readline().split())

"""
the elements go up to 400000, is it possible to map out every edge?
would be about 5.2 million edges

can 2 generate EVERY non prime? yes

then if there are multiple primes, it cannot work
otherwise if exactly 1 prime exists, assuming everything else works, then yes

97->97*2->98*2 = 49*4->...89*89
"""

from math import sqrt, floor

def fsieve(n: int) -> list[int]: 
    ar = [1]*max(2,(n+1))
    ar[0] = 0
    for i in range(2,floor(sqrt(n))+1):
        if ar[i] == 1: #i is prime
            for j in range(i,n//i+1):
                if ar[i*j] == 1: ar[i*j] = i
    return ar


s = fsieve(400000)
#print(s[:30])

def minbase(x):
    a = s[x]
    b = x//a
    if a == 1: return -1
    if a % 2 == 1 and b % 2 == 1:
        b -= 1
        return a*(b//2)
    else:
        return x//2
    
for _ in range(readint()):
    n = readint()
    ar = readar()
    ar.sort()
    if s[ar[0]] == 1 and ar[0] != 2: # check multiples
        ans = ar[0]
        for i in range(1,n):
            if minbase(ar[i]) < ans or s[ar[i]] == 1:
                ans = -1
                break
        print(ans)
    else:
        ans = 2
        for i in range(1,n):
            if s[ar[i]] == 1:
                ans = -1
                break
        print(ans)
    

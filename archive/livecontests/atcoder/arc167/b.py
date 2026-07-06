import sys

#input functions
readint = lambda: int(sys.stdin.readline())
readints = lambda: map(int,sys.stdin.readline().split())
readar = lambda: list(map(int,sys.stdin.readline().split()))
flush = lambda: sys.stdout.flush()

#factorization problem
"""
for b = 1, count number of "pairs" to set
base , base2, base3, base4

subtract the square cases?

a = 2 [1]
1*1,1*3,1*6,1*10,1*15,1*21
1,3,6,10,15,21
1,2,6,8,15,18

a = 6 [1,1]
2*1,3*3,4*6,5*10,6*15,7*21
2,9,24,50,90,147
2,8,24,48,90,144

a = 4,9,25 [2]
1,5,10,18,27,39
n**2+n-1-(n-1)//2

a = 8 [3]
2,7,15,26,40,57
n*(3*n+1)/2

a = 16
2,9,19,34,52,75

a = 12 [2,1]
3*1,5*3,7*6,9*10,11*15,13*21,15*28
3,15,42,90,165,273,420

a = 24 [3,1]
4*1,7*3,10*6,13*10,16*15
4,21,60,130,240

a = 36
4,25,73,162,302

a = 40,385 [1,1,1]
4,27,96,250
2*2*1,3*3*3,4*4*6,5*5*10,6*6*15
same factorization pattern should result in same value

a = 360 [3,2,1]
12,105,420,1170,2640

a = 924 [2,1,1,1]
12,135,672,2250,5940
12,134,672,2248,5940
12,67,224,562,1188

taking product works for the 2nd value in sequence (b = 2)
"""

from math import sqrt, floor

def sieve(n: int) -> list[bool]:
    ar = [True]*max(2,(n+1))
    br = list()
    ar[0] = False
    ar[1] = False
    for i in range(2,floor(sqrt(n))+1):
        if ar[i]: #i is prime
            for j in range(i,n//i+1):
                ar[i*j] = False
    for s in range(n+1):
        if ar[s]:
            br.append(s)
    return br
ar = sieve(1000000)
f = list()
a,b = readints()
for i in ar:
    if i*i > a: break
    if a % i == 0:
        x = 0
        while a % i == 0:
            a //= i
            x += 1
        f.append(x)
if a != 1: f.append(1)
if b == 0: print(0)
else:
    #print(f)
    ans = 1
    odd = True
    m = 998244353
    for g in f:
        mult = g*b+1
        if mult % 2 == 0: odd = False
        ans *= mult
        ans = ans % m
    if odd: ans -= 1
    ans = (ans*499122177) % m
    ans = (ans*b) % m
    if odd: ans = (ans+(b//2)) % m  
    print(ans)

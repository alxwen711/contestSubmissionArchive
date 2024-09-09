import sys
from copy import deepcopy

#input functions
readint = lambda: int(sys.stdin.readline())
readints = lambda: map(int,sys.stdin.readline().split())
readar = lambda: list(map(int,sys.stdin.readline().split()))
flush = lambda: sys.stdout.flush()
readin = lambda: sys.stdin.readline()[:-1]
readins = lambda: map(str,sys.stdin.readline().split())

"""
is f hashable?

given a subsequence, find frequencies?

trivially the sequences must be of same length

in theory this is easily hackable, but atcoder does not have hacking

confirm product and sum match, BUT remap the arrays to primes??
"""

from math import sqrt, floor

def sieve(n: int) -> list[bool]:
    ar = [True]*max(2,(n+1))
    ar[0] = False
    ar[1] = False
    for i in range(2,floor(sqrt(n))+1):
        if ar[i]: #i is prime
            for j in range(i,n//i+1):
                ar[i*j] = False
    br = list()
    for j in range(len(ar)):
        if ar[j]: br.append(j)
    return br

ref = sieve(3000000)
ref.reverse()
index = 0

n,qc = readints()
tmp1 = readar()
tmp2 = readar()
h = [0]*(n+1)
ar = list()
br = list()
for i in range(n):
    if h[tmp1[i]] == 0:
        h[tmp1[i]] = ref[index]
        index += 1
    if h[tmp2[i]] == 0:
        h[tmp2[i]] = ref[index]
        index += 1
    ar.append(h[tmp1[i]])
    br.append(h[tmp2[i]])

def binTable(ar,op):
    m = 1991096119
    br = list()
    tmp = deepcopy(ar)
    br.append(tmp)
    while len(br[-1]) != 1:
        tmp = list()
        for i in range(len(br[-1])//2):
            if op: tmp.append((br[-1][2*i]*br[-1][2*i+1]) % m)
            else: tmp.append((br[-1][2*i]+br[-1][2*i+1]) % m)
        br.append(tmp)
    return br

def q(ar,l,r,op):
    m = 1991096119
    li = l
    ri = r
    ans = 1
    for snth in range(len(ar)):
        if li > ri: break
        if li % 2 == 1:
            if op: ans = (ans*ar[snth][li]) % m
            else: ans = (ans+ar[snth][li]) % m
            li += 1
        if ri % 2 == 0:
            if op: ans = (ans*ar[snth][ri]) % m
            else: ans = (ans+ar[snth][ri]) % m
            ri -= 1
        li //= 2
        ri //= 2
    return ans

cr = binTable(ar,True)
dr = binTable(br,True)
er = binTable(ar,False)
fr = binTable(br,False)

for _ in range(qc):
    a,b,c,d = readints()
    a -= 1
    b -= 1
    c -= 1
    d -= 1
    if b-a != d-c: print("No")
    elif q(cr,a,b,True) == q(dr,c,d,True) and q(er,a,b,False) == q(fr,c,d,False):
        print("Yes")
    else:
        print("No")
    

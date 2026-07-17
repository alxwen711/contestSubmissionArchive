import sys

#input functions
readint = lambda: int(sys.stdin.readline())
readints = lambda: map(int,sys.stdin.readline().split())
readar = lambda: list(map(int,sys.stdin.readline().split()))
flush = lambda: sys.stdout.flush()
readin = lambda: sys.stdin.readline()[:-1]
readins = lambda: map(str,sys.stdin.readline().split())

"""
15 non-1 factors of 120 are arranged into 7 layers similar to below:

2
3
5
4->6->10->15
8->12->20->30
24->40->60
120

2*3*2*2*5

number of factors + number of distinct factors?

2,3,4,5,6,8,10,12,15,20,24,30,40,60,120
"""

primes = [i for i in range(1000001)]
for ii in range(2,1002):
    if primes[ii] == ii: # prime
        for j in range(2*ii,1000001,ii):
            if primes[j] == j: primes[j] = ii

for _ in range(readint()):
    n = readint()
    pl = list()
    while n != 1:
        pl.append(primes[n])
        n //= primes[n]
    ans = len(pl)
    prev = pl[0]
    for p in pl:
        if prev != p:
            prev = p
            ans += 1
    print(ans)


    

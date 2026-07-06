import sys

#input functions
readint = lambda: int(sys.stdin.readline())
readints = lambda: map(int,sys.stdin.readline().split())
readar = lambda: list(map(int,sys.stdin.readline().split()))
flush = lambda: sys.stdout.flush()

"""
how to compute beauty of an array in linear time first?
t3 ends in 7,3,4
sum is 14
take from sum -> multiply
(7*7+3*11+4*10)//2 = 122//2=61
k can be 10^9, cannot use heap +1 strat
"""

def solve(n,k,ar):
    total = sum(ar)+k # for computing total later
    # first find how many of the lowest vals can be levelled
    index = 0
    for i in range(n-1):
        diff = ar[i+1]-ar[i]
        req = diff*(i+1)
        if req > k: break
        else:
            k -= req
            index += 1
    # update first vals to match
    for j in range(index):
        ar[j] = ar[index]

    # add last k
    index += 1
    inc = k//index #remaining increment
    p1 = k % index #p1 val

    for m in range(index):
        ar[m] += inc
        if p1 > m: ar[m] += 1

    ans = 0
    for u in range(n):
        ans = (ans+ar[u]*(total-ar[u])) % 1000000007
    #500000004 is mod inv of 2
    return (ans*500000004) % 1000000007

for i in range(readint()):
    n,k = readints()
    ar = readar()
    ar.sort()
    print(solve(n,k,ar))

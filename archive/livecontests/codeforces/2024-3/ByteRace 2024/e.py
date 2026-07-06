import sys

#input functions
readint = lambda: int(sys.stdin.readline())
readints = lambda: map(int,sys.stdin.readline().split())
readar = lambda: list(map(int,sys.stdin.readline().split()))
flush = lambda: sys.stdout.flush()
readin = lambda: sys.stdin.readline()[:-1]
readins = lambda: map(str,sys.stdin.readline().split())

"""
O(n log n)

first k balls are special

if k = 0, then assume chances equal to freque5
1 1
732507
2 2
5817860 5398510
5 1
2122894 4951549 2750585 7821535 3214167
8 4
1405323 5069867 6883092 6972029 328406 2478975 7628890 9973340
4 2
9662050 3566134 3996473 9872255
ncies of balls picked
so n = 5, sum(ar)/5*3 for alice's expected score

first case the special ball average is equal to non-special ball average

trivial case: if k = n, alice gets all bals, bob gets nothing
"""
m = 1000000007
for _ in range(readint()):
    n,k = readints()
    ar = readar()
    base = n-k
    ansa,ansb = 0,0
    inv = pow(base+1,m-2,m)
    a = (base+2)//2
    b = (base+1)//2
    for i in range(k):
        ansa = (ansa+(a*inv*ar[i])) % m
        ansb = (ansb+(b*inv*ar[i])) % m
    inv = pow(base,m-2,m)
    a = (base+1)//2
    b = (base)//2
    for j in range(k,n):
        ansa = (ansa+(a*inv*ar[j])) % m
        ansb = (ansb+(b*inv*ar[j])) % m
    print(ansa,ansb)

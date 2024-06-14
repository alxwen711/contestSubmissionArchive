import sys

#input functions
readint = lambda: int(sys.stdin.readline())
readints = lambda: map(int,sys.stdin.readline().split())
readar = lambda: list(map(int,sys.stdin.readline().split()))
flush = lambda: sys.stdout.flush()

# some sort of binary scaling is used here

m = 998244353
n = readint()
l = len(str(n))
ans = 0
v = n % m
c = n
boost = 0
ex = 1
while c != 0:
    if c % 2 == 1:
        ans = (ans+(v*pow(10,boost*l,m))) % m
        boost += ex
    c //= 2
    v = (v*pow(10,ex*l,m)+v) % m
    ex *= 2
print(ans)
    

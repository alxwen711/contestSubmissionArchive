import sys

#input functions
readint = lambda: int(sys.stdin.readline())
readints = lambda: map(int,sys.stdin.readline().split())
readar = lambda: list(map(int,sys.stdin.readline().split()))
flush = lambda: sys.stdout.flush()
readin = lambda: sys.stdin.readline()[:-1]
readins = lambda: map(str,sys.stdin.readline().split())


"""
some sort of weighted average iterative
n**2 choices for picking
2n-2 have the position in 1 spot, these are divided equally across remaining pos
1 has the position in both spots
everything else will not move the ball
"""
m = 998244353
n,k = readints()
ans = 1
base = (n*n+n)//2
inv = pow(n*n,m-2,m)
for _ in range(k):
    s = (base-ans)*2+(ans*(n*n-(2*n-2)))
    ans = (s*inv) % m
print(ans)

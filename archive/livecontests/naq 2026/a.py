import sys

#input functions
readint = lambda: int(sys.stdin.readline())
readints = lambda: map(int,sys.stdin.readline().split())
readar = lambda: list(map(int,sys.stdin.readline().split()))
flush = lambda: sys.stdout.flush()
readin = lambda: sys.stdin.readline()[:-1]
readins = lambda: map(str,sys.stdin.readline().split())

"""
1+3+6+10+15...

1,4,10,20,35,56

1,4,9,16

target sum of squares:
[1, 5, 14, 30, 55, 91, 140, 204, 285, 385]
[6, 30, 84, 180, 330, 546, 840, 1224, 1710, 2310]


v = 0
ar = list()
for i in range(1,11):
    v = (i*(i+1)*(2*i+1))//6
    ar.append(v)

print(ar)
"""
n = readint()
m = 998244353

squares = (n*(n+1)*(2*n+1))//6
lines = (n*(n+1))//2
ans = (squares + lines) // 2
print(ans % m)

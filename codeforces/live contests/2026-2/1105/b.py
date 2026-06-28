import sys

#input functions
readint = lambda: int(sys.stdin.readline())
readints = lambda: map(int,sys.stdin.readline().split())
readar = lambda: list(map(int,sys.stdin.readline().split()))
flush = lambda: sys.stdout.flush()
readin = lambda: sys.stdin.readline()[:-1]
readins = lambda: map(str,sys.stdin.readline().split())

"""
tc 7 is everything div 2
all exponents of 2

0
2
6
7
9
959
1000000000**2-1
0

tc6 answer is 2**959
"""
p = 998244353
for _ in range(readint()):
    n,m,r,c = readints()
    v = n*m-((n-r+1)*(m-c+1))
    print(pow(2,v,p))
"""
p = 998244353
x = 0
while True:
    x += 1
    if pow(2,x,p) == 543661425:
        print(x)
        break
"""

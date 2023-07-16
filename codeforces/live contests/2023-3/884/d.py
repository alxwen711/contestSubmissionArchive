import sys

#input functions
readint = lambda: int(sys.stdin.readline())
readints = lambda: map(int,sys.stdin.readline().split())
readar = lambda: list(map(int,sys.stdin.readline().split()))
flush = lambda: sys.stdout.flush()

"""
gap of a factor of n cannot have same
issue is something like 720720 has 240 factors
~250 million operations?
if you use factors I'll probably hack you
"""

for i in range(readint()):
    n = readint()
    factors = list()
    x = 1
    while x != n and n % x == 0:
        x += 1
    ans = list()
    for j in range(n):
        ans.append(chr(97+(j%x)))
    print(*ans,sep="")

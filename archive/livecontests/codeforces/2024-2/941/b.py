import sys

#input functions
readint = lambda: int(sys.stdin.readline())
readints = lambda: map(int,sys.stdin.readline().split())
readar = lambda: list(map(int,sys.stdin.readline().split()))
flush = lambda: sys.stdout.flush()

"""
no subset of a can add to k
there exists a subset that can add to anything from
1 to n (unless it is k)

there is always a solution

note only up to 25 values allowed and limit of n is 1 million

if k = 1, 2,3,4,8,16... will suffice
if k = 2, 1,3,4,5,8,16
if k = 3, 1,4,5,6,8,16
k = 4, 1,2,5,8,14,26,50
k = 5, 1,2,6,8

k = 2, 1,3,5

use powers of 2 up to k

10 7
1 2 3 8

1000 270
1 2 4 8 16 32 64 128 14 271 540 810 1080 ...  
"""

for _ in range(readint()):
    n,k = readints()
    ans = list()
    s = 0
    x = 1
    while (x+s) < k:
        ans.append(x)
        s += x
        x *= 2
    if s < k-1: ans.append(k-1-s)
    ans.append(k+1)
    ans.append(2*k)
    ans.append(3*k)
    ans.append(4*k)
    while len(ans) < 25:
        ans.append(ans[-1]*2)
    print(len(ans))
    print(*ans)

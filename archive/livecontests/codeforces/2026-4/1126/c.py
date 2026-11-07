import sys

#input functions
readint = lambda: int(sys.stdin.readline())
readints = lambda: map(int,sys.stdin.readline().split())
readar = lambda: list(map(int,sys.stdin.readline().split()))
flush = lambda: sys.stdout.flush()
readin = lambda: sys.stdin.readline()[:-1]
readins = lambda: map(str,sys.stdin.readline().split())

"""
number of values to output will be under 1000000
0 is useless

1
1 2 1 1 1 2 1
1 3 1
is length 7 possible on 4?
1 2 1 4 1 2 1
"""

for _ in range(readint()):
    n = readint()
    ans = [1]
    v = 1
    while v*2 <= n:
        v *= 2
        ans = ans + [v] + ans
    #if n == 1: ans = ans + [1] + ans
    #else:
    ans = ans + [0] + ans
    print(len(ans))
    print(*ans)

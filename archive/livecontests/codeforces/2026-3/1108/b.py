import sys
from math import lcm
#input functions
readint = lambda: int(sys.stdin.readline())
readints = lambda: map(int,sys.stdin.readline().split())
readar = lambda: list(map(int,sys.stdin.readline().split()))
flush = lambda: sys.stdout.flush()
readin = lambda: sys.stdin.readline()[:-1]
readins = lambda: map(str,sys.stdin.readline().split())


"""
1
-1 (2 case is impossible?)
1 2 3
1 2 3 6

"""

for _ in range(readint()):
    n = readint()
    if n == 2: print(-1)
    elif n == 1: print(1)
    else:
        ans = [1,2,3]
        for _ in range(n-3):
            ans.append(ans[-1]*2)
        print(*ans)

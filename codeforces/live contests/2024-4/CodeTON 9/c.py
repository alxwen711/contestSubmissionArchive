import sys

#input functions
readint = lambda: int(sys.stdin.readline())
readints = lambda: map(int,sys.stdin.readline().split())
readar = lambda: list(map(int,sys.stdin.readline().split()))
flush = lambda: sys.stdout.flush()
readin = lambda: sys.stdin.readline()[:-1]
readins = lambda: map(str,sys.stdin.readline().split())

"""
easy ver: x ^ y is a factor
hard ver: x ^ y is divisible

110 [100,101,111]
101 [100,110]
10 [11]
110 100
100 1 (no cases)

number of factors of x + 1?
1 is the value a such that x = ay ^ y
"""

for _ in range(readint()):
    x,m = readints()
    """
    ans = list()
    for y in range(1,m+1):
        if x != y:
            z = x ^ y
            if x % z == 0 or y % z == 0:
                ans.append(y)
    print(ans)
    """
    l = 1
    while l*2 <= x:
        l *= 2
    ans = 0
    for y in range(l,min(l*2,m)+1):
        if x != y:
            z = x ^ y
            if x % z == 0 or y % z == 0:
                ans += 1
    print(ans)

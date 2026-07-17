import sys

#input functions
readint = lambda: int(sys.stdin.readline())
readints = lambda: map(int,sys.stdin.readline().split())
readar = lambda: list(map(int,sys.stdin.readline().split()))
flush = lambda: sys.stdout.flush()

"""
only min/max values are important as all others will be in between
if min is odd, use 1
else use 2
"""

for _ in range(readint()):
    n = readint()
    ar = readar()
    ans = list()
    an = 0
    a = min(ar)
    b = max(ar)
    while a != b:
        an += 1
        if a % 2 == 1:
            ans.append(1)
            a = (a+1)//2
            b = (b+1)//2
        else:
            ans.append(2)
            a = (a+2)//2
            b = (b+2)//2
    print(an)
    if an != 0 and an <= n: print(*ans)
            

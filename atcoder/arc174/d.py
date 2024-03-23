import sys

#input functions
readint = lambda: int(sys.stdin.readline())
readints = lambda: map(int,sys.stdin.readline().split())
readar = lambda: list(map(int,sys.stdin.readline().split()))
flush = lambda: sys.stdout.flush()

"""
feels like a repeating cycle of a factor of 100 somehow
1 1
80 8
90-99 9
100-109 10
9800 98
9900-9999 99
10000-10099 100
998000 998
999000-999999 999
"""


ranges = list()
for i in range(10):
    ranges.append((10**(2*i),10**(2*i)+(10**i-1)))
    ranges.append((10**(2*i+2)-(10**(i+1)*2),10**(2*i+2)-(10**(i+1)*2)))
    ranges.append((10**(2*i+2)-(10**(i+1)),10**(2*i+2)-1))
#print(ranges)

for _ in range(readint()):
    n = readint()
    ans = 0
    for r in ranges:
        if r[1] <= n: ans += (r[1]-r[0]+1)
        elif r[0] <= n: ans += (n-r[0]+1)
        else: break
    print(ans)

import sys

#input functions
readint = lambda: int(sys.stdin.readline())
readints = lambda: map(int,sys.stdin.readline().split())
readar = lambda: list(map(int,sys.stdin.readline().split()))
flush = lambda: sys.stdout.flush()

"""
2 1 -> 10
3 2 -> 100
only using 1 and 0? 2/3/4 may be needed
5 1 -> 102102102
4 2 -> 1002
5 2 -> 10021
6 2 -> 100210021
can use 21 setup?
7 3 -> 1000201000201
_ 4 -> 10000201000020
if even k: then 1000..00021000..0002...
else: 1000..00201000,,0020...
only need to consider substrings of length k and k+1
"""

for i in range(readint()):
    n,k = readints()
    clen = 1+k+1+((k-1)//2)
    cycles = n//clen
    r = n % clen
    ans = cycles*3
    if r != 0: ans += 1
    if r > (1+k): ans += 2
    print(ans)

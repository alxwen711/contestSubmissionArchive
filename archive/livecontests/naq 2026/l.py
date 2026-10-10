import sys

#input functions
readint = lambda: int(sys.stdin.readline())
readints = lambda: map(int,sys.stdin.readline().split())
readar = lambda: list(map(int,sys.stdin.readline().split()))
flush = lambda: sys.stdout.flush()
readin = lambda: sys.stdin.readline()[:-1]
readins = lambda: map(str,sys.stdin.readline().split())

"""
fractional pushups are allowed, optimize to have same stress on each segment?
"""

for _ in range(readint()):
    n,p = readints()
    ar = readar()
    ans = 0
    rate = p/sum(ar)
    for i in ar:
        v = i*rate
        ans += v*v/i
    print(ans)

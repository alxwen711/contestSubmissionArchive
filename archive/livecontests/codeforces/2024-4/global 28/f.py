import sys

#input functions
readint = lambda: int(sys.stdin.readline())
readints = lambda: map(int,sys.stdin.readline().split())
readar = lambda: list(map(int,sys.stdin.readline().split()))
flush = lambda: sys.stdout.flush()
readin = lambda: sys.stdin.readline()[:-1]
readins = lambda: map(str,sys.stdin.readline().split())

"""
there is a hard limit of ceil(log2(max(ar)))

a smaller operation would have to reduce the ceiling by 2 to be effective
on its own, cases exist with multiple ops
"""

def f(a,b):
    c = a
    ans = 0
    while c != 1:
        c = (c+b-1)//b
        ans += 1
    return ans

for _ in range(readint()):
    n = readint()
    ar = readar()
    br = readar()
    base = f(max(ar),min(br))
    print(base)

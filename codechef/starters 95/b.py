import sys

#input functions
readint = lambda: int(sys.stdin.readline())
readints = lambda: map(int,sys.stdin.readline().split())
readar = lambda: list(map(int,sys.stdin.readline().split()))
flush = lambda: sys.stdout.flush()

"""
most significant bit occurs odd number of times
"""

for i in range(readint()):
    n = readint()
    ar = readar()
    x = 1
    c = max(ar)
    while 2*x <= c:
        x *= 2
    v = 0
    for j in ar:
        if j >= x: v += 1
    print((v+1)//2)

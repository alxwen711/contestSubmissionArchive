import sys

#input functions
readint = lambda: int(sys.stdin.readline())
readints = lambda: map(int,sys.stdin.readline().split())
readar = lambda: list(map(int,sys.stdin.readline().split()))
flush = lambda: sys.stdout.flush()
readin = lambda: sys.stdin.readline()[:-1]
readins = lambda: map(str,sys.stdin.readline().split())

"""
8
12345678 -> 0
87654321 -> 32
"""

for _ in range(readint()):
    n = readint()
    s = 0
    for a in range(1,n+1):
        s += abs(a-(n-a+1))
    print(s//2+1)

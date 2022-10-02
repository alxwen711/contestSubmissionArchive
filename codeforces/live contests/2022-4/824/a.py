import sys

#input functions
readint = lambda: int(sys.stdin.readline())
readints = lambda: map(int,sys.stdin.readline().split())
readar = lambda: list(map(int,sys.stdin.readline().split()))
flush = lambda: sys.stdout.flush()


"""
3 2
4 2
5 2
6 3
7 3
8 3
9 4
"""
for i in range(readint()):
    n = readint()
    n -= 3
    block = (n//3)+1
    a,b = block-1, n-block
    print(min(abs(a-b),abs(a-1),abs(b-1)))

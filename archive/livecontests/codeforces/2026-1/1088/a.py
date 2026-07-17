import sys

#input functions
readint = lambda: int(sys.stdin.readline())
readints = lambda: map(int,sys.stdin.readline().split())
readar = lambda: list(map(int,sys.stdin.readline().split()))
flush = lambda: sys.stdout.flush()
readin = lambda: sys.stdin.readline()[:-1]
readins = lambda: map(str,sys.stdin.readline().split())

"""
1 2 4 3 6 5
"""

for _ in range(readint()):
    n = readint()
    ar = readar()
    if n == 1: print(1)
    elif n == 2: print(2,2)
    elif n == 3: print(2,2,2)
    else:
        ans = ["2"]*n
        print(*ans)
        

import sys

#input functions
readint = lambda: int(sys.stdin.readline())
readints = lambda: map(int,sys.stdin.readline().split())
readar = lambda: list(map(int,sys.stdin.readline().split()))
flush = lambda: sys.stdout.flush()

for i in range(readint()):
    x = readint()
    if x == 1: print(2)
    elif x % 3 == 0: print(x//3)
    else: print(x//3+1)

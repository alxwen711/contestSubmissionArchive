import sys

#input functions
readint = lambda: int(sys.stdin.readline())
readints = lambda: map(int,sys.stdin.readline().split())
readar = lambda: list(map(int,sys.stdin.readline().split()))
flush = lambda: sys.stdout.flush()

n = readint()
while n % 2 == 0:
    n //= 2
while n % 3 == 0:
    n //= 3
if n == 1: print("Yes")
else: print("No")

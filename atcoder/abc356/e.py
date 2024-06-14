import sys

#input functions
readint = lambda: int(sys.stdin.readline())
readints = lambda: map(int,sys.stdin.readline().split())
readar = lambda: list(map(int,sys.stdin.readline().split()))
flush = lambda: sys.stdout.flush()

# score will still be the same with a sorted array
n = readint()
ar = readar()
ar.sort()

# left side will likely have a bunch of 1's tracked (pointer)
index = 0
for i in range(n):
    # left divide to 1
    while index < i:
        if ar[i]//ar[index] > 1: index += 1
        else: break
    ans += i-index + 1
    # left divide above 1?

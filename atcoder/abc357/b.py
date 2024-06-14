import sys

#input functions
readint = lambda: int(sys.stdin.readline())
readints = lambda: map(int,sys.stdin.readline().split())
readar = lambda: list(map(int,sys.stdin.readline().split()))
flush = lambda: sys.stdout.flush()

s = input()
l = 0
u = 0
for j in s:
    if ord(j) >= 97: l += 1
    else: u += 1
if u > l: print(s.upper())
else: print(s.lower())

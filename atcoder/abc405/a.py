import sys

#input functions
readint = lambda: int(sys.stdin.readline())
readints = lambda: map(int,sys.stdin.readline().split())
readar = lambda: list(map(int,sys.stdin.readline().split()))
flush = lambda: sys.stdout.flush()
readin = lambda: sys.stdin.readline()[:-1]
readins = lambda: map(str,sys.stdin.readline().split())

r,x = readints()

if x == 1: print("Yes" if 1600 <= r <= 2999 else "No")
else: print("Yes" if 1200 <= r <= 2399 else "No")

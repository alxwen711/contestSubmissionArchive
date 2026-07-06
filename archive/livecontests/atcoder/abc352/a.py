import sys

#input functions
readint = lambda: int(sys.stdin.readline())
readints = lambda: map(int,sys.stdin.readline().split())
readar = lambda: list(map(int,sys.stdin.readline().split()))
flush = lambda: sys.stdout.flush()

n,x,y,z = readints()
if z > max(x,y) or z < min(x,y): print("No")
else: print("Yes")

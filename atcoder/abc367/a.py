import sys

#input functions
readint = lambda: int(sys.stdin.readline())
readints = lambda: map(int,sys.stdin.readline().split())
readar = lambda: list(map(int,sys.stdin.readline().split()))
flush = lambda: sys.stdout.flush()
readin = lambda: sys.stdin.readline()[:-1]
readins = lambda: map(str,sys.stdin.readline().split())

a,b,c = readints()
if b < c:
    if b > a or a > c: print("Yes")
    else: print("No")
else:
    if c > a or a > b: print("No")
    else: print("Yes")

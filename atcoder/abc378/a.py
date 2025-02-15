import sys

#input functions
readint = lambda: int(sys.stdin.readline())
readints = lambda: map(int,sys.stdin.readline().split())
readar = lambda: list(map(int,sys.stdin.readline().split()))
flush = lambda: sys.stdout.flush()
readin = lambda: sys.stdin.readline()[:-1]
readins = lambda: map(str,sys.stdin.readline().split())

ar = readar()
ar.sort()
a,b,c,d = ar[0],ar[1],ar[2],ar[3]
if a == b and c == d: print(2)
elif a == b or b == c or c == d: print(1)
else: print(0)

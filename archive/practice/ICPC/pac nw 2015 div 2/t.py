import sys

#input functions
readint = lambda: int(sys.stdin.readline())
readints = lambda: map(int,sys.stdin.readline().split())
readar = lambda: list(map(int,sys.stdin.readline().split()))
flush = lambda: sys.stdout.flush()

ar = readar()
br = readar()
ar.sort()
br.sort()
if ar != br: print("NO")
elif ar[0]*ar[0]+ar[1]*ar[1] != ar[2]*ar[2]: print("NO")
else: print("YES")

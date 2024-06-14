import sys

#input functions
readint = lambda: int(sys.stdin.readline())
readints = lambda: map(int,sys.stdin.readline().split())
readar = lambda: list(map(int,sys.stdin.readline().split()))
flush = lambda: sys.stdout.flush()

a,b = readints()
ar = [a,b]
ar.sort()
if ar[0] == ar[1]: print(-1)
elif ar == [1,2]: print(3)
elif ar == [1,3]: print(2)
else: print(1)

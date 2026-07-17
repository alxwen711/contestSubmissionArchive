import sys

#input functions
readint = lambda: int(sys.stdin.readline())
readints = lambda: map(int,sys.stdin.readline().split())
readar = lambda: list(map(int,sys.stdin.readline().split()))
flush = lambda: sys.stdout.flush()

n = readint()
ar = readar()
ans = "Yes"
for i in range(n-1):
    if ar[i] != ar[i+1]: ans = "No"
print(ans)

import sys

#input functions
readint = lambda: int(sys.stdin.readline())
readints = lambda: map(int,sys.stdin.readline().split())
readar = lambda: list(map(int,sys.stdin.readline().split()))
flush = lambda: sys.stdout.flush()
readin = lambda: sys.stdin.readline()[:-1]
readins = lambda: map(str,sys.stdin.readline().split())

n,m,k = readints()
ar = readar()
h = [0]*n
p = 0
for i in range(n):
    if i >= m and h[i-m] == 1:
        p -= ar[i-m]
    
    if p+ar[i] <= k:
        print("Yes")
        h[i] = 1
        p += ar[i]
    else:
        print("No")
        

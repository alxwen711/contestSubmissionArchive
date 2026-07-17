import sys

#input functions
readint = lambda: int(sys.stdin.readline())
readints = lambda: map(int,sys.stdin.readline().split())
readar = lambda: list(map(int,sys.stdin.readline().split()))
flush = lambda: sys.stdout.flush()

for i in range(readint()):
    n,k = readints()
    ar = list()
    for j in range(n):
        tmp = readar()
        ar.append(tmp)
    ans = 0
    for x in range((n*n)//2):
        a,b = x//n,x%n
        if ar[a][b] != ar[-a-1][-b-1]: ans += 1
    if ans > k: print("NO")
    elif (k-ans) % 2 == 0 or n % 2 == 1: print("YES")
    else: print("NO")

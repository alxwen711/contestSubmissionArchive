import sys

#input functions
readint = lambda: int(sys.stdin.readline())
readints = lambda: map(int,sys.stdin.readline().split())
readar = lambda: list(map(int,sys.stdin.readline().split()))
flush = lambda: sys.stdout.flush()
readin = lambda: sys.stdin.readline()[:-1]
readins = lambda: map(str,sys.stdin.readline().split())
"""
6 4 4 6
8 6 4 6 8
10 8 6 6 8 10
"""
for _ in range(readint()):
    n = readint()
    ar = readar()
    ans = "YES"
    for i in range(n):
        if n % 2 == 0:
            if i < n//2:
                v = (n-1-i)*2
                if v >= ar[i]:
                    ans = "NO"
                    break
            else:
                v = i*2
                if v >= ar[i]:
                    ans = "NO"
                    break
        else:
            if i <= n//2:
                v = (n-1-i)*2
                if v >= ar[i]:
                    ans = "NO"
                    break
            else:
                v = i*2
                if v >= ar[i]:
                    ans = "NO"
                    break
    print(ans)

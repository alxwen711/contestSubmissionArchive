import sys

#input functions
readint = lambda: int(sys.stdin.readline())
readints = lambda: map(int,sys.stdin.readline().split())
readar = lambda: list(map(int,sys.stdin.readline().split()))
flush = lambda: sys.stdout.flush()

for i in range(readint()):
    n = readint()
    ar = readar()
    if n <= 2: print("YES")
    else:
        inc = True
        ans = "YES"
        for j in range(n-1):
            if inc:
                if ar[j] > ar[j+1]: inc = False
            else:
                if ar[j] < ar[j+1]: ans = "NO"
        print(ans)

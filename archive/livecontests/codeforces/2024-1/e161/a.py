import sys

#input functions
readint = lambda: int(sys.stdin.readline())
readints = lambda: map(int,sys.stdin.readline().split())
readar = lambda: list(map(int,sys.stdin.readline().split()))
flush = lambda: sys.stdout.flush()

def solve(n,a,b,c):
    ar = list()
    for i in range(n):
        if a[i] != c[i] and b[i] != c[i]:
            print("YES")
            return
    print("NO")
    #print(*ar)
for _ in range(readint()):
    n = readint()
    a = input()
    b = input()
    c = input()
    solve(n,a,b,c)

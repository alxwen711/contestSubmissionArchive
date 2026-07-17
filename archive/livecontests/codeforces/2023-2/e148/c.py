import sys

#input functions
readint = lambda: int(sys.stdin.readline())
readints = lambda: map(int,sys.stdin.readline().split())
readar = lambda: list(map(int,sys.stdin.readline().split()))
flush = lambda: sys.stdout.flush()


def solve(n,ar):
    same = True
    inc = True
    ans = 1
    for j in range(n-1):
        a,b = ar[j],ar[j+1]
        if same:
            if a < b:
                same = False
                ans += 1
                inc = True
            elif a > b:
                same = False
                ans += 1
                inc = False
        else:
            if inc and a > b:
                inc = False
                ans += 1
            elif not inc and a < b:
                inc = True
                ans += 1
    return ans

for i in range(readint()):
    n = readint()
    ar = readar()
    print(solve(n,ar))

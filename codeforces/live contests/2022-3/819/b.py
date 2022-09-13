import sys

#input functions
readint = lambda: int(sys.stdin.readline())
readints = lambda: map(int,sys.stdin.readline().split())
readar = lambda: list(map(int,sys.stdin.readline().split()))
flush = lambda: sys.stdout.flush()

def solve(n,m):
    if n > m:
        print("No")
        return
    if n == 1:
        print("Yes")
        print(m)
        return
    if n == 2:
        if m % 2 == 0:
            print("Yes")
            print(m//2,m//2)
        else: print("No")
        return
    if n % 2 == 1:
        print("Yes")
        ar = [1]*n
        ar[-1] = m-n+1
        print(*ar)
    else:
        if m % 2 == 1: print("No")
        else:
            print("Yes")
            ar = [1]*n
            r = m-n+2
            ar[-1] = r//2
            ar[-2] = r//2
            print(*ar)
    return
            

for i in range(readint()):
    n,m = readints()
    solve(n,m)

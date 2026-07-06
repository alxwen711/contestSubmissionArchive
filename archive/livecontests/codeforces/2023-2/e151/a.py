import sys

#input functions
readint = lambda: int(sys.stdin.readline())
readints = lambda: map(int,sys.stdin.readline().split())
readar = lambda: list(map(int,sys.stdin.readline().split()))
flush = lambda: sys.stdout.flush()

for i in range(readint()):
    n,k,x = readints()
    if x != 1:
        print("YES")
        print(n)
        a = [1]*n
        print(*a)
    else: # x == 1
        if k == 1: print("NO")
        elif k == 2:
            if n % 2 == 0:
                print("YES")
                print(n//2)
                a = [2]*(n//2)
                print(*a)
            else: print("NO")
        else:
            if n == 1: print("NO")
            else:
                print("YES")
                if n % 2 == 0:
                    print(n//2)
                    a = [2]*(n//2)
                    print(*a)
                else:
                    print(n//2)
                    a = [2]*(n//2)
                    a[0] = 3
                    print(*a)
                    

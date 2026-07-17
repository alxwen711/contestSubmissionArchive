import sys

#input functions
readint = lambda: int(sys.stdin.readline())
readints = lambda: map(int,sys.stdin.readline().split())
readar = lambda: list(map(int,sys.stdin.readline().split()))
flush = lambda: sys.stdout.flush()

for i in range(readint()):
    n,k = readints()
    if k % 2 == 1:
        print("YES")
        for j in range(n//2):
            print(2*j+1,2*j+2)
    elif k % 4 == 0: print("NO")
    else:
        print("YES")
        for j in range(n//2):
            if j % 2 == 0: print(2*j+2,2*j+1)
            else: print(2*j+1,2*j+2)

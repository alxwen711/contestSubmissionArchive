import sys

#input functions
readint = lambda: int(sys.stdin.readline())
readints = lambda: map(int,sys.stdin.readline().split())
readar = lambda: list(map(int,sys.stdin.readline().split()))
flush = lambda: sys.stdout.flush()

for i in range(readint()):
    n = readint()
    if n == 3: print("NO")
    elif n % 4 == 3:
        ar = list()
        a,b = -(n//2)+1,n//2
        for j in range(n//2):
            ar.append(a)
            ar.append(b)
        ar.append(a)
        print("YES")
        print(*ar)
    elif n % 4 == 1:
        ar = list()
        a,b = -(n//2)+1,n//2
        for j in range(n//2):
            ar.append(a)
            ar.append(b)
        ar.append(a)
        print("YES")
        print(*ar)
    else:
        ar = list()
        for j in range(n//2):
            ar.append(-1)
            ar.append(1)
        print("YES")
        print(*ar)

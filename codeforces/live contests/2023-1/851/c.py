import sys

#input functions
readint = lambda: int(sys.stdin.readline())
readints = lambda: map(int,sys.stdin.readline().split())
readar = lambda: list(map(int,sys.stdin.readline().split()))
flush = lambda: sys.stdout.flush()

for i in range(readint()):
    n = readint()
    if n % 2 == 0: print("No")
    else:
        print("Yes")
        ar = list()
        for j in range(n):
            ar.append(2*n-j)
        left = n//2
        right = n-left
        for k in range(left//2):
            #swap k and left-k-1
            tmp = ar[k]
            ar[k] = ar[left-k-1]
            ar[left-k-1] = tmp
        for l in range(right//2):
            #swap left+l and -l-1
            tmp = ar[left+l]
            ar[left+l] = ar[-l-1]
            ar[-l-1] = tmp
        for u in range(n):
            print(u+1,ar[u])

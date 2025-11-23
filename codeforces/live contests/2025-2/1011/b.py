import sys

#input functions
readint = lambda: int(sys.stdin.readline())
readints = lambda: map(int,sys.stdin.readline().split())
readar = lambda: list(map(int,sys.stdin.readline().split()))
flush = lambda: sys.stdout.flush()
readin = lambda: sys.stdin.readline()[:-1]
readins = lambda: map(str,sys.stdin.readline().split())


for _ in range(readint()):
    n = readint()
    ar = readar()
    zero = list()
    for i in range(n):
        if ar[i] == 0: zero.append(i)
    if len(zero) == 0:
        print(1)
        print(1,n)
    elif len(zero) >= 2:
        d = zero[-1]-zero[0]+1
        if d != n:
            print(2)
            print(zero[0]+1,zero[-1]+1)
            print(1,n-d+1)
        else:
            print(3)
            print(3,n)
            print(1,2)
            print(1,2)
    else:
        print(2)
        if zero[0] != n-1 and zero[0] != 0:
            print(zero[0]+1,n)
            print(1,zero[0]+1)
        elif zero[0] == n-1:
            print(n-1,n)
            print(1,n-1)
        else:
            print(1,2)
            print(1,n-1)

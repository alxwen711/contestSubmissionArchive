import sys

#input functions
readint = lambda: int(sys.stdin.readline())
readints = lambda: map(int,sys.stdin.readline().split())
readar = lambda: list(map(int,sys.stdin.readline().split()))
flush = lambda: sys.stdout.flush()

for i in range(readint()):
    x = readint()
    ar = list()
    for j in range(x):
        ar.append(j+1)
    print(x)
    for k in range(x-1):
        print(*ar)
        tmp = ar[-k-1]
        ar[-k-1] = ar[-k-2]
        ar[-k-2] = tmp
    print(*ar)

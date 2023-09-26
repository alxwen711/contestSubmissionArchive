import sys

#input functions
readint = lambda: int(sys.stdin.readline())
readints = lambda: map(int,sys.stdin.readline().split())
readar = lambda: list(map(int,sys.stdin.readline().split()))
flush = lambda: sys.stdout.flush()


for i in range(readint()):
    n = readint()
    s = sys.stdin.readline()
    ar = list()
    index = -1
    for j in range(n):
        ar.append(int(s[j]))
        if ar[j] == 1 and index == -1: index = j
    if index != -1 and index <= n-3:
        for snth in range(index+1,n):
            ar[snth] = 0
    print(*ar,sep="")

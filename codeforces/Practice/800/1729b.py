import sys

#input functions
readint = lambda: int(sys.stdin.readline())
readints = lambda: map(int,sys.stdin.readline().split())
readar = lambda: list(map(int,sys.stdin.readline().split()))
flush = lambda: sys.stdout.flush()
"""
00 -> 10/20
xy0 -> 11-26, no 10/20
x -> 1-9
"""
for i in range(readint()):
    n = readint()
    x = input()
    ar = list()
    for j in range(n):
        ar.append(int(x[j]))
    for k in range(n):
        #-k-1
        if ar[-k-1] != " ":
            if ar[-k-1] == 0:
                y = chr(ar[-k-2]+96+(ar[-k-3]*10))
                ar[-k-1] = y
                ar[-k-2] = " "
                ar[-k-3] = " "
    word = list()
    for l in range(n):
        if type(ar[l]) == int: word.append(chr(96+ar[l]))
        elif ar[l] != " ": word.append(ar[l])
    print(*word,sep="")

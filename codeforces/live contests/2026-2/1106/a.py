import sys

#input functions
readint = lambda: int(sys.stdin.readline())
readints = lambda: map(int,sys.stdin.readline().split())
readar = lambda: list(map(int,sys.stdin.readline().split()))
flush = lambda: sys.stdout.flush()
readin = lambda: sys.stdin.readline()[:-1]
readins = lambda: map(str,sys.stdin.readline().split())

"""
there is a fixed number of subtractions
"""

for _ in range(readint()):
    n,c = readints()
    ar = readar()
    br = readar()
    flag = True
    for i in range(n):
        if ar[i] < br[i]:
            flag = False
    if flag:
        print(sum(ar)-sum(br))
    else:
        ar.sort()
        br.sort()
        flag = True
        for i in range(n):
            if ar[i] < br[i]:
                flag = False
        if flag: print(sum(ar)-sum(br)+c)
        else: print(-1)

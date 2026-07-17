import sys

#input functions
readint = lambda: int(sys.stdin.readline())
readints = lambda: map(int,sys.stdin.readline().split())
readar = lambda: list(map(int,sys.stdin.readline().split()))
flush = lambda: sys.stdout.flush()
readin = lambda: sys.stdin.readline()[:-1]
readins = lambda: map(str,sys.stdin.readline().split())

"""
ans is ALWAYS at least 1
"""



for _ in range(readint()):
    n = readint()
    ar = list()
    for _ in range(n):
        tmp = readar()
        ar.append(tmp)
    ans = 0
    backend = list()
    for i in range(n):
        flag = True
        for j in range(n):
            if ar[i][-j-1] != 1:
                flag = False
                backend.append(j)
                break
        if flag: backend.append(n)
    backend.sort()
    for snth in range(n):
        if ans <= backend[snth]: ans += 1
        #else: break
    print(ans)

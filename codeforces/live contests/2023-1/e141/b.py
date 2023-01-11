import sys

#input functions
readint = lambda: int(sys.stdin.readline())
readints = lambda: map(int,sys.stdin.readline().split())
readar = lambda: list(map(int,sys.stdin.readline().split()))
flush = lambda: sys.stdout.flush()

for i in range(readint()):
    n = readint()
    inc = n*n-1
    p = True
    v = 1
    flip = False
    #ans = list()
    for j in range(n):
        tmp = list()
        for k in range(n):
            tmp.append(v)
            if p:
                p = False
                v += inc
            else:
                p = True
                v -= inc
            inc -= 1
        if flip:
            flip = False
            tmp.reverse()
        else:
            flip = True
        #ans.append(tmp)
        print(*tmp)

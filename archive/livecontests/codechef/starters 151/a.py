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
    br = readar()
    cr = list()
    for i in range(n):
        cr.append((ar[i],br[i]))
    cr.sort()
    ans = list()
    for j in cr:
        if len(ans) == 0: ans.append(j)
        else:
            while len(ans) != 0:
                lp,ls = ans[-1][0],ans[-1][1]
                if lp*j[1] > ls*j[0]: ans.pop() # will collide
                else: break
            ans.append(j)
    print(len(ans))

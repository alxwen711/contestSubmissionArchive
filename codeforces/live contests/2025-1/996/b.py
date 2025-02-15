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
    flag = -1
    req = 0
    for i in range(n):
        if br[i] > ar[i]:
            flag = i
            req = br[i]-ar[i]
            break
    if flag == -1: print("YES")
    else:
        ans = "YES"
        for j in range(n):
            if j != flag:
                if ar[j]-req < br[j]:
                    ans = "NO"
                    break
        print(ans)

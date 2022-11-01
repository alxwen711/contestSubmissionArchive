import sys

#input functions
readint = lambda: int(sys.stdin.readline())
readints = lambda: map(int,sys.stdin.readline().split())
readar = lambda: list(map(int,sys.stdin.readline().split()))
flush = lambda: sys.stdout.flush()

def solve(n,ar):
    s = sum(ar)
    if s == 0:
        print(n)
        for why in range(1,n+1):
            print(why,why)
        return
    if s % 2 != 0:
        print(-1)
        return
    s = s // 2
    adjust = [0]*n
    if s > 0: #change 1 to -1
        count = s
        prev = False
        for j in range(1,n):
            if prev: prev = False
            elif ar[j] == 1:
                adjust[j] = 1
                count -= 1
                prev = True
            if count == 0: break
        if count != 0:
            print(-1)
            return
    else: #change -1 to 1
        count = -s
        prev = False
        for k in range(1,n):
            if prev: prev = False
            elif ar[k] == -1:
                adjust[k] = 1
                count -= 1
                prev = True
            if count == 0: break
        if count != 0:
            print(-1)
            return
    ans = list()
    seg = 1
    for m in range(1,n):
        if adjust[m-1] == 0 and adjust[m] == 0: #new seg
            ans.append([seg,m])
            seg = m+1
    ans.append([seg,n])
    print(len(ans))
    for snth in range(len(ans)):
        print(ans[snth][0],ans[snth][1])
    return

for i in range(readint()):
    n = readint()
    ar = readar()
    solve(n,ar)

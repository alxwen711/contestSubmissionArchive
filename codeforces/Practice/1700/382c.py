import sys

#input functions
readint = lambda: int(sys.stdin.readline())
readints = lambda: map(int,sys.stdin.readline().split())
readar = lambda: list(map(int,sys.stdin.readline().split()))
flush = lambda: sys.stdout.flush()

def solve(n,ar):
    ar.sort()
    ans = list()
    if n == 1:
        print(-1)
        return
    elif n == 2:
        #either 2 or 3 solutions
        diff = abs(ar[0]-ar[1])
        if diff == 0:
            print(1)
            print(ar[0])
            return
        ans.append(ar[0]-diff)
        ans.append(ar[1]+diff)
        xx = 2
        if diff % 2 == 0:
            ans.append((ar[0]+ar[1])//2)
            xx += 1
        ans.sort()
        print(xx)
        print(*ans)
        return
    #at least 3 elements
    diffs = list()
    for i in range(n-1):
        diffs.append(ar[i+1]-ar[i])
    diffs.sort()
    if diffs.count(diffs[0]) == n-1: #arithmetic progression
        if diffs[0] == 0:
            print(1)
            print(ar[0])
            return
        print(2)
        print(ar[0]-diffs[0],ar[-1]+diffs[0])
    elif diffs.count(diffs[0]) == n-2 and diffs[0]*2 == diffs[-1]: #special case
        x = diffs[-1]
        print(1)
        for j in range(n-1):
            if ar[j+1]-ar[j] == x:
                print(ar[j]+diffs[0])
                break
    else: print(0)


n = readint()
ar = readar()
solve(n,ar)

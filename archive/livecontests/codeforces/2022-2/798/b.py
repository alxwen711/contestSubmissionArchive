import sys

def solve(n,ar):
    if n == 1: #no sol
        print(-1)
        return
    #not 1, sol exists
    h = [0]*n
    br = list()
    for j in range(n-1):
        for k in range(n):
            if h[k] == 0 and ar[j] != k+1:
                br.append(k+1)
                h[k] = 1
                break
    for m in range(n):
        if h[m] == 0:
            br.append(m+1)
            break
    if br[-1] == ar[-1]:
        tmp = br[-1]
        br[-1] = br[-2]
        br[-2] = tmp
    print(*br)
    return



for i in range(int(sys.stdin.readline())):
    n = int(sys.stdin.readline())
    ar = list(map(int, sys.stdin.readline().split()))
    solve(n,ar)

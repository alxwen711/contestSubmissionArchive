import sys

#input functions
readint = lambda: int(sys.stdin.readline())
readints = lambda: map(int,sys.stdin.readline().split())
readar = lambda: list(map(int,sys.stdin.readline().split()))
flush = lambda: sys.stdout.flush()

def solve(ar,x):
    #no need to choose optimally, there's always a free spot
    ans = list()
    ar.sort()
    upper = len(ar)-1
    lower = 0
    while ar[upper][0] != x and ar[lower][0] != x:
        for k in range(len(ar[upper][2])):
            if ar[upper][2][k] == 1:
                if ar[lower][2][k] == 0:
                    ans.append([ar[upper][1],ar[lower][1],k+1])
                    ar[upper][0] -= 1
                    ar[lower][0] += 1
                    ar[upper][2][k] = 0
                    ar[lower][2][k] = 1
                    if ar[lower][0] == x or ar[upper][0] == x: break
        if ar[upper][0] == x: upper -= 1
        if ar[lower][0] == x: lower += 1
    print(len(ans))
    for g in range(len(ans)):
        print(*ans[g])
    
    


for i in range(readint()):
    n,m = readints()
    ar = list()
    br = list()
    for j in range(n):
        tmp = readar()
        aa = sum(tmp)
        br.append(aa)
        ar.append([aa,j+1,tmp])
    s = sum(br)
    if s % n != 0: print(-1)
    else:
        solve(ar,s//n)
    

import sys
def check(ar,n,m):
    if m == 1: return 1,1
    for p in range(n):
        for q in range(m-1):
            if ar[p][q] > ar[p][q+1]:
                problem = list()
                for why in range(m):
                    problem.append(ar[p][why])
                problem.sort()
                x,y = -1,-1
                for r in range(m):
                    if ar[p][r] != problem[r]:
                        if x == -1: x = r+1
                        elif y == -1: y = r+1
                        else: return -42069,7
                return x,y
    return 1,1
     

for i in range(int(sys.stdin.readline())):
    n,m = map(int,sys.stdin.readline().split())
    ar = list()
    for j in range(n):
        ar.append(list(map(int,sys.stdin.readline().split())))
    a,b = check(ar,n,m)
    if a == b: print(a,b)
    elif a == -42069: print(-1)
    else:
        for k in range(n):
            tmp = ar[k][a-1]
            ar[k][a-1] = ar[k][b-1]
            ar[k][b-1] = tmp
        c,d = check(ar,n,m)
        if c == d: print(a,b)
        else: print(-1)
    

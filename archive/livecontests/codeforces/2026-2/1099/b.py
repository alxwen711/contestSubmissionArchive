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
    m = 0
    for i in range(n-1):
        m = max(m,ar[i]-ar[i+1])
    if m == 0: print("YES")
    else:
        flag = True
        for j in range(n-1):
            if ar[j] > ar[j+1]:
                ar[j+1] += m
        for k in range(n-1):
            if ar[k] > ar[k+1]:
                flag = False
                break
        if flag:
            print("YES")
        else:
            print("NO")
    

import sys

#input functions
readint = lambda: int(sys.stdin.readline())
readints = lambda: map(int,sys.stdin.readline().split())
readar = lambda: list(map(int,sys.stdin.readline().split()))
flush = lambda: sys.stdout.flush()

for i in range(readint()):
    n,k,r,c = readints()
    ar = list()
    for j in range(n):
        tmp = ["."]*n
        ar.append(tmp)

    st = r+c-2
    st = st % k
    while st < 2*n+5:
        for f in range(st+1):
            a,b = f,st-f
            if a < n and b < n: ar[a][b] = "X"
        st += k

    for m in range(n):
        print(*ar[m],sep="")

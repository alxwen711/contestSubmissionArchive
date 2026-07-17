import sys
for i in range(int(sys.stdin.readline())):
    n,m = map(int,sys.stdin.readline().split())
    ar = list(map(int,sys.stdin.readline().split()))
    h = ["B"]*m
    for j in range(n):
        x = ar[j]-1
        alt = m-x-1
        if h[min(x,alt)] == "B": h[min(x,alt)] = "A"
        else: h[max(x,alt)] = "A"
    print(*h,sep="")

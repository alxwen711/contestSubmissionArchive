import sys

for i in range(int(sys.stdin.readline())):
    n = int(sys.stdin.readline())
    ar = list(map(int,sys.stdin.readline().split()))
    ans = 0
    a,b = 0,n-1
    atotal = 0
    btotal = 0
    c = 0
    for j in range(n):
        c += 1
        if atotal > btotal:
            btotal += ar[b]
            b -= 1
        else:
            atotal += ar[a]
            a+= 1
        if atotal == btotal: ans = c
    print(ans)

import sys

#input functions
readint = lambda: int(sys.stdin.readline())
readints = lambda: map(int,sys.stdin.readline().split())
readar = lambda: list(map(int,sys.stdin.readline().split()))
flush = lambda: sys.stdout.flush()
readin = lambda: sys.stdin.readline()[:-1]
readins = lambda: map(str,sys.stdin.readline().split())

for _ in range(readint()):
    n,k = readints()
    s = readin()
    ans = ["+"]*n
    lc,rc,tc = 0,0,0
    for i in s:
        if i == "0":
            lc += 1
        elif i == "1":
            rc += 1
        else:
            tc += 1
    if k != n:        
        for a in range(lc):
            ans[a] = "-"
        for b in range(rc):
            ans[-b-1] = "-"
        lp,rp = lc,n-rc-1 # range of values that are not top/bot
        for c in range(tc):
            ans[c+lp] = "?"
        for d in range(tc):
            ans[rp-d] = "?"
        print(*ans,sep="")
    else:
        ans = ["-"]*n
        print(*ans,sep="")

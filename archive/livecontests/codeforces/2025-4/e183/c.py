import sys

#input functions
readint = lambda: int(sys.stdin.readline())
readints = lambda: map(int,sys.stdin.readline().split())
readar = lambda: list(map(int,sys.stdin.readline().split()))
flush = lambda: sys.stdout.flush()
readin = lambda: sys.stdin.readline()[:-1]
readins = lambda: map(str,sys.stdin.readline().split())
hv = 234567876543234
for _ in range(readint()):
    n = readint()
    s = readin()
    ar = list()
    for i in s:
        if i == "a": ar.append(-1)
        else: ar.append(1)
    t = sum(ar)
    if t == 0: print(0)
    else: # find shortest subsegment of sum -t
        d = {}
        d[hv] = -1
        st = 0
        ans = 999999999999999999
        for i in range(n):
            st += ar[i]
            r = st-t
            if d.get(r^hv) != None: ans = min(ans,i-d[r^hv])
            d[st^hv] = i
        if ans >= n: print(-1)
        else: print(ans)

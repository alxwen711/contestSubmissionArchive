import sys

for i in range(int(sys.stdin.readline())):
    n = int(sys.stdin.readline())
    length = -1
    lec = 1000000001
    low = 1000000001
    loc = 1000000001
    high = 0
    hc = 1000000001
    for i in range(n):
        l, h, c = map(int, sys.stdin.readline().split())
        if l < low: low, loc = l, c
        elif l == low: loc = min(loc,c)
        if h > high: high, hc = h, c
        elif h == high: hc = min(hc,c)
        if h - l > length: length, lec = h - l, c
        elif h - l == length: lec = min(lec,c)
        ans = loc + hc
        if high - low == length: ans = min(ans,lec)
        print(ans)
    

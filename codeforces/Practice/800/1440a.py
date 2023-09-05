import sys

#input functions
readint = lambda: int(sys.stdin.readline())
readints = lambda: map(int,sys.stdin.readline().split())
readar = lambda: list(map(int,sys.stdin.readline().split()))
flush = lambda: sys.stdout.flush()

for i in range(readint()):
    n,a,b,h = readints()
    s = input()
    diff = abs(a-b)
    if diff > h:
        ca = a
        cb = a+h
        if b < a:
            cb = b
            ca = b+h
        ans = 0
        for k in range(n):
            if s[k] == "0": ans += ca
            else: ans += cb
        print(ans)
    else: #no change
        ans = 0
        for j in range(n):
            if s[j] == "0": ans += a
            else: ans += b
        print(ans)
    

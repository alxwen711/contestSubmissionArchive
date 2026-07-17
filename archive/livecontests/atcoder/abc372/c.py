import sys

#input functions
readint = lambda: int(sys.stdin.readline())
readints = lambda: map(int,sys.stdin.readline().split())
readar = lambda: list(map(int,sys.stdin.readline().split()))
flush = lambda: sys.stdout.flush()
readin = lambda: sys.stdin.readline()[:-1]
readins = lambda: map(str,sys.stdin.readline().split())

n,q = readints()
si = readin()
s = list()
for ii in si:
    s.append(ii)
ans = 0
for i in range(n-2):
    if s[i] == "A" and s[i+1] == "B" and s[i+2] == "C": ans += 1
for _ in range(q):
    a,b = readins()
    a = int(a)-1
    if s[a] == b: print(ans)
    else:
        if a-2 >= 0:
            if s[a-2] == "A" and s[a-1] == "B" and s[a] == "C": ans -= 1
        if a-1 >= 0 and a+1 < n:
            if s[a-1] == "A" and s[a] == "B" and s[a+1] == "C": ans -= 1
        if a+2 < n:
            if s[a] == "A" and s[a+1] == "B" and s[a+2] == "C": ans -= 1
        s[a] = b
        if a-2 >= 0:
            if s[a-2] == "A" and s[a-1] == "B" and s[a] == "C": ans += 1
        if a-1 >= 0 and a+1 < n:
            if s[a-1] == "A" and s[a] == "B" and s[a+1] == "C": ans += 1
        if a+2 < n:
            if s[a] == "A" and s[a+1] == "B" and s[a+2] == "C": ans += 1
        
        print(ans)

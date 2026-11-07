import sys

#input functions
readint = lambda: int(sys.stdin.readline())
readints = lambda: map(int,sys.stdin.readline().split())
readar = lambda: list(map(int,sys.stdin.readline().split()))
flush = lambda: sys.stdout.flush()
readin = lambda: sys.stdin.readline()[:-1]
readins = lambda: map(str,sys.stdin.readline().split())


n,k,t = readints()
ar = readar()

segments = list()

for i in ar:
    segments.append((i,-1)) # starts water at this time
    segments.append((i+k,1)) # ends water at this time

v = 0
ans = 0
prev = 0
segments.sort()

for s in segments:
    if s[0] > t: break # not relevant to check
    if v == 0:
        diff = s[0]-prev
        ans += (diff+k-1)//k
    prev = s[0]
    v -= s[1]

if v == 0:
    diff = t-prev
    ans += (diff+k-1)//k
print(ans)

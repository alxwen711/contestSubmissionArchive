import sys

#input functions
readint = lambda: int(sys.stdin.readline())
readints = lambda: map(int,sys.stdin.readline().split())
readar = lambda: list(map(int,sys.stdin.readline().split()))
flush = lambda: sys.stdout.flush()

#implementation hell moment
n = readint()
s = input()

#create the "lookup"
h = list()
for snth in range(26):
    h.append(list())
for i in range(n):
    h[ord(s[i])-97].append(i+1)

for j in range(readint()):
    x = input()
    d = [0]*26
    for k in range(len(x)):
        d[ord(x[k])-97] += 1
    ans = 0
    for l in range(26):
        if d[l] != 0: ans = max(ans,h[l][d[l]-1])
    print(ans)

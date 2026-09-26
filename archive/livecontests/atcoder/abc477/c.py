import sys

#input functions
readint = lambda: int(sys.stdin.readline())
readints = lambda: map(int,sys.stdin.readline().split())
readar = lambda: list(map(int,sys.stdin.readline().split()))
flush = lambda: sys.stdout.flush()
readin = lambda: sys.stdin.readline()[:-1]
readins = lambda: map(str,sys.stdin.readline().split())

# t is at most 10 characters

q = readint()
s = readin()
t = readin()
n,m = len(s),len(t)
prefix = [0]
for i in range(n-m+1):
    v = 1
    for j in range(m):
        if s[i+j] != t[j]:
            v = 0
            break
    prefix.append(prefix[-1]+v)

for _ in range(q):
    l,r = readints()
    if r-l+1 < m: print("No")
    elif prefix[r-m+1] > prefix[l-1]: print("Yes")
    else: print("No")

import sys

#input functions
readint = lambda: int(sys.stdin.readline())
readints = lambda: map(int,sys.stdin.readline().split())
readar = lambda: list(map(int,sys.stdin.readline().split()))
flush = lambda: sys.stdout.flush()

# +w in row for t = 1, +h in t = 2

h,w,m = readints()
hh,ww = h,w
ar = list()
for _ in range(m):
    t,a,x = readints()
    ar.append((t,a,x))
ar.reverse()

dh = [0]*200001
dw = [0]*200001
ans = [0]*200001

for i in range(m):
    l = ar[i][1]
    c = ar[i][2]
    if ar[i][0] == 1:
        if dh[l] == 0:
            dh[l] = 1
            ans[c] += w
            h -= 1
    else:
        if dw[l] == 0:
            dw[l] = 1
            ans[c] += h
            w -= 1
ans[0] = hh*ww-sum(ans[1:])
k = 0
lans = list()
for j in range(200001):
    if ans[j] != 0:
        k += 1
        lans.append((j,ans[j]))
print(k)
for lm in lans:
    print(lm[0],lm[1])

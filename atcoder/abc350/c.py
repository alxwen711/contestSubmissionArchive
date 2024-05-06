import sys

#input functions
readint = lambda: int(sys.stdin.readline())
readints = lambda: map(int,sys.stdin.readline().split())
readar = lambda: list(map(int,sys.stdin.readline().split()))
flush = lambda: sys.stdout.flush()

n = readint()
ar = readar()
for ii in range(n):
    ar[ii] -= 1
ans = list()
p = [0]*n
for i in range(n):
    p[ar[i]] = i
for j in range(n):
    if ar[j] != j:
        pos = p[j]
        ans.append((j,pos))
        ar[pos] = ar[j]
        p[ar[j]] = pos
        ar[j] = j
        p[j] = j
print(len(ans))
for k in ans:
    print(k[0]+1,k[1]+1)

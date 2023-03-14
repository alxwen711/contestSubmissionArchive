import sys

#input functions
readint = lambda: int(sys.stdin.readline())
readints = lambda: map(int,sys.stdin.readline().split())
readar = lambda: list(map(int,sys.stdin.readline().split()))
flush = lambda: sys.stdout.flush()


def blur(ar,n,m):
    br = list()
    for snth in range(n):
        tmp = [0]*m
        br.append(tmp)
    for a in range(n):
        for b in range(m):
            br[a][b] = ar[(a)%n][(b)%m]+ar[(a+1)%n][(b)%m]+ar[(a-1)%n][(b)%m]+ar[(a)%n][(b+1)%m]+ar[(a+1)%n][(b+1)%m]+ar[(a-1)%n][(b+1)%m]+ar[(a)%n][(b-1)%m]+ar[(a+1)%n][(b-1)%m]+ar[(a-1)%n][(b-1)%m]
    return br
    
m,n,c = readints()
ar = list()
for i in range(n):
    tmp = readar()
    ar.append(tmp)

for j in range(c):
    ar = blur(ar,n,m)
d = {}
for x in range(n):
    for y in range(m):
        d[ar[x][y]] = 1
sn = list(d.keys())
print(len(sn))
#print(ar)

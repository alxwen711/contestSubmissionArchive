import sys

#input functions
readint = lambda: int(sys.stdin.readline())
readints = lambda: map(int,sys.stdin.readline().split())
readar = lambda: list(map(int,sys.stdin.readline().split()))
flush = lambda: sys.stdout.flush()

m,n = readints()
ar = list()
v = list()
for i in range(m):
    tmp = [-1]*n
    ar.append(tmp)
    v.append(input())
    
q = list()
ar[0][0] = 0
index = 0
q.append([0,0])
while len(q) != index:
    a,b = q[index][0],q[index][1]
    step = ar[a][b]+1
    k = int(v[a][b])
    if a >= k: #up
        if ar[a-k][b] == -1:
            ar[a-k][b] = step
            q.append([a-k,b])
    if a < m-k: #down
        if ar[a+k][b] == -1:
            ar[a+k][b] = step
            q.append([a+k,b])
    if b >= k: #left
        if ar[a][b-k] == -1:
            ar[a][b-k] = step
            q.append([a,b-k])
    if b < n-k: #right
        if ar[a][b+k] == -1:
            ar[a][b+k] = step
            q.append([a,b+k])
    index += 1
#print(ar)
if ar[-1][-1] == -1: print("IMPOSSIBLE")
else: print(ar[-1][-1])

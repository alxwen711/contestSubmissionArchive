import sys

#input functions
readint = lambda: int(sys.stdin.readline())
readints = lambda: map(int,sys.stdin.readline().split())
readar = lambda: list(map(int,sys.stdin.readline().split()))
flush = lambda: sys.stdout.flush()

ar = list()
for i in range(readint()):
    x = readar()
    ar.append([x[0]+x[2],x[0],x[1]])
ar.sort()
d = [0]*(ar[-1][0]+1)
#d[ar[0][0]] = ar[0][2]
index = 0
for j in range(1,len(d)):
    d[j] = d[j-1]
    while ar[index][0] == j:
        d[j] = max(d[j],ar[index][2]+d[ar[index][1]])
        index += 1
        if index == len(ar): break
    
print(max(d))

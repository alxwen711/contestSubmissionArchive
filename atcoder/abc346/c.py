import sys

#input functions
readint = lambda: int(sys.stdin.readline())
readints = lambda: map(int,sys.stdin.readline().split())
readar = lambda: list(map(int,sys.stdin.readline().split()))
flush = lambda: sys.stdout.flush()

n,k = readints()
ar = readar()
d = {}

ans = (k*k+k)//2
#print(ans)
for i in ar:
    if i <= k and d.get(i) == None:
        ans -= i
        d[i] = 1
        #print(i)
print(ans)

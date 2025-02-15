import sys

#input functions
readint = lambda: int(sys.stdin.readline())
readints = lambda: map(int,sys.stdin.readline().split())
readar = lambda: list(map(int,sys.stdin.readline().split()))
flush = lambda: sys.stdout.flush()
readin = lambda: sys.stdin.readline()[:-1]
readins = lambda: map(str,sys.stdin.readline().split())
"""
0 1 2 3 4 5 6 ...
2 3 5 7 
"""
ans = list()
for i in range(1,100):
    ans = list()
    v = 1
    for j in range(i,101):
        if j % v == v-1:
            ans.append(j)
            v += 1
    if v > 50: break

for _ in range(readint()):
    n = readint()
    print(*ans[:n])
    
    

import sys

#input functions
readint = lambda: int(sys.stdin.readline())
readints = lambda: map(int,sys.stdin.readline().split())
readar = lambda: list(map(int,sys.stdin.readline().split()))
flush = lambda: sys.stdout.flush()
# stable if first and last element in subarray are equal
"""
num of ways to choose two indicies?
"""
for i in range(readint()):
    n = readint()
    ar = readar()
    ans = (n*n-n)//2
    d = {}
    for j in range(n):
        x = ar[j]
        if d.get(x) == None: d[x] = 0
        d[x] += 1
    for v in d.keys():
        l = d[v]
        ans -= (l*l-l)//2
    print(ans)
    

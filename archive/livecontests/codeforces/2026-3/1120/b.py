import sys

#input functions
readint = lambda: int(sys.stdin.readline())
readints = lambda: map(int,sys.stdin.readline().split())
readar = lambda: list(map(int,sys.stdin.readline().split()))
flush = lambda: sys.stdout.flush()
readin = lambda: sys.stdin.readline()[:-1]
readins = lambda: map(str,sys.stdin.readline().split())

"""
n is the least possible
2n-1 is the most possible
"""

for _ in range(readint()):
    n,k = readints()
    if k >= 2*n or k < n: print(-1)
    else:
        mr = 2*n-1-k
        ans = list()
        for _ in range(n):
            tmp = [0]*n
            ans.append(tmp)
        for i in range(n):
            ans[i][min(i,mr)] = i+1
        v = n+1
        for a in range(n):
            for b in range(n-1,-1,-1):
                if ans[a][b] == 0:
                    ans[a][b] = v
                    v += 1
            print(*ans[a])
    

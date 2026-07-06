import sys

#input functions
readint = lambda: int(sys.stdin.readline())
readints = lambda: map(int,sys.stdin.readline().split())
readar = lambda: list(map(int,sys.stdin.readline().split()))
flush = lambda: sys.stdout.flush()
readin = lambda: sys.stdin.readline()[:-1]
readins = lambda: map(str,sys.stdin.readline().split())

for _ in range(readint()):
    n,k = readints()
    if k+1 == n*n: print("NO")
    else:
        print("YES")
        grid = list()
        for _ in range(n):
            tmp = ["D"]*n
            grid.append(tmp)
        if k != n*n:
            grid[0][0] = "R"
            grid[0][1] = "L"
            for j in range(2,min(n*n-k,n)):
                grid[0][j] = "L"
            if k < n*n-n:
                remaining = n*n-n-k
                for a in range(1,n):
                    for b in range(n):
                        grid[a][b] = "U"
                        remaining -= 1
                        if remaining == 0: break
                    if remaining == 0: break
        for i in grid:
            print(*i,sep="")

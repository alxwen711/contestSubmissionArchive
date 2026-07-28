import sys

#input functions
readint = lambda: int(sys.stdin.readline())
readints = lambda: map(int,sys.stdin.readline().split())
readar = lambda: list(map(int,sys.stdin.readline().split()))
flush = lambda: sys.stdout.flush()
readin = lambda: sys.stdin.readline()[:-1]
readins = lambda: map(str,sys.stdin.readline().split())

for _ in range(readint()):
    n = readint()
    ar = readar()
    m = readint()
    for _ in range(m):
        s = readin()
        if len(s) != n: print("NO")
        else:
            ans = "YES"
            d = {}
            for i in range(n):
                x = s[i]
                y = ar[i]
                if d.get(x) == None: d[x] = y
                elif d[x] != y:
                    ans = "NO"
                    break
                if d.get(y) == None: d[y] = x
                elif d[y] != x:
                    ans = "NO"
                    break
                
            print(ans)

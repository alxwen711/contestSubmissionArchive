import sys

#input functions
readint = lambda: int(sys.stdin.readline())
readints = lambda: map(int,sys.stdin.readline().split())
readar = lambda: list(map(int,sys.stdin.readline().split()))
flush = lambda: sys.stdout.flush()

for i in range(readint()):
    n = readint()
    x = input()
    d = {}
    for j in range(n-1):
        if d.get(x[j:j+2]) == None: d[x[j:j+2]] = list()
        d[x[j:j+2]].append(j)
    k = list(d.keys())
    ans = "NO"
    for m in range(len(k)):
        if d[k[m]][-1] - d[k[m]][0] >= 2:
            ans = "YES"
            break
    print(ans)

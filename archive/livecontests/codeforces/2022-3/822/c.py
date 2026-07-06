import sys

#input functions
readint = lambda: int(sys.stdin.readline())
readints = lambda: map(int,sys.stdin.readline().split())
readar = lambda: list(map(int,sys.stdin.readline().split()))
flush = lambda: sys.stdout.flush()

for i in range(readint()):
    n = readint()
    s = input()
    h = list()
    for snth in range(n+1):
        h.append(list())
    ans = 0
    for j in range(n):
        if s[j] == "0":
            x = j+1
            if x <= n//2: h[x*2].append(x)
            if len(h[x]) == 0:
                ans += x
            else:
                ans += h[x][-1]
                for k in range(len(h[x])):
                    t = h[x][k]
                    if x+t <= n: h[x+t].append(t)
        """
        else:
            h[j] = 0
        """
    #print(h)
    print(ans)
    

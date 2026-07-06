import sys

#input functions
readint = lambda: int(sys.stdin.readline())
readints = lambda: map(int,sys.stdin.readline().split())
readar = lambda: list(map(int,sys.stdin.readline().split()))
flush = lambda: sys.stdout.flush()

for i in range(readint()):
    n = readint()
    a = input()
    b = input()
    ar = list()
    for j in range(n):
        if a[j] == "1" and b[j] == "1": ar.append(2)
        elif a[j] == "0" and b[j] == "0": ar.append(0)
        else: ar.append(1)
    """
    0 -> if beside 2, group together for +2, else +1
    1 -> automatic singular, +2
    2 -> if beside 0, group together for +2, else 0
    """
    ans = 0
    h = [1]*n
    for k in range(n):
        if h[k] == 0: continue #already covered
        if ar[k] == 1:
            h[k] = 0
            ans += 2
        elif ar[k] == 0:
            inc = 1
            h[k] = 0
            if k != n-1:
                if ar[k+1] == 2:
                    h[k+1] = 0
                    inc = 2
            ans += inc
        else:
            inc = 0
            h[k] = 0
            if k != n-1:
                if ar[k+1] == 0:
                    h[k+1] = 0
                    inc = 2
            ans += inc
    print(ans)
        
            

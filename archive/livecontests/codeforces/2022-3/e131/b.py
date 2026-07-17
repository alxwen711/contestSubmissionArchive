import sys
for i in range(int(sys.stdin.readline())):
    n = int(sys.stdin.readline())
    h = [0]*n
    ar = list()
    for j in range(n):
        if h[j] == 0:
            ar.append(j+1)
            x = j+1
            h[j] = 1
            while x*2 <= n:
                x = x * 2
                h[x-1] = 1
                ar.append(x)
    print(2)
    print(*ar)

import sys

for i in range(int(sys.stdin.readline())):
    n, k = map(int, sys.stdin.readline().split())
    a = list(map(int, sys.stdin.readline().split()))
    b = list(map(int, sys.stdin.readline().split()))
    c = list()
    for j in range(n):
        c.append((a[j],b[j]))
    c.sort()
    for m in range(n):
        if c[m][0] > k: break
        k += c[m][1]
    print(k)

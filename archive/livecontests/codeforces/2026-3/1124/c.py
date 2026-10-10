import sys

#input functions
readint = lambda: int(sys.stdin.readline())
readints = lambda: map(int,sys.stdin.readline().split())
readar = lambda: list(map(int,sys.stdin.readline().split()))
flush = lambda: sys.stdout.flush()
readin = lambda: sys.stdin.readline()[:-1]
readins = lambda: map(str,sys.stdin.readline().split())

"""
either remove kth element OR kth last element
k is 1 -> everything is out
k is 2 -> everything except 1st or last is out

1 4 8 2 6 3
1 4 2 6 3
1 4 6 3 (this state is always reached)
"""

for _ in range(readint()):
    n,k = readints()
    ar = readar()
    h = [0]*((n+1)//2)
    for i in range(n-k+1):
        if i < len(h): h[i] += 1
        elif n % 2 == 1: h[len(h)-i-2] += 1
        else: h[len(h)-i-1] += 1
    ans = 0
    #print(h)
    for j in range(len(h)):
        if h[j] == 2:
            ans += ar[j]
            ans += ar[-j-1]
        elif h[j] == 1:
            ans += max(ar[j],ar[-j-1])
    print(ans)

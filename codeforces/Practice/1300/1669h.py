import sys

import sys

for i in range(int(sys.stdin.readline())):
    n,k = map(int,sys.stdin.readline().split())
    ar = list(map(int,sys.stdin.readline().split()))
    h = [0]*31
    for j in range(n):
        x = ar[j]
        index = 0
        while x != 0:
            h[index] += (x%2)
            x = x // 2
            index += 1
    h.reverse()
    ans = 0
    for m in range(31):
        ans *= 2
        miss = n-h[m]
        if miss <= k:
            ans += 1
            k -= miss
    print(ans)

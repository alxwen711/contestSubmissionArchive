import sys

#input functions
readint = lambda: int(sys.stdin.readline())
readints = lambda: map(int,sys.stdin.readline().split())
readar = lambda: list(map(int,sys.stdin.readline().split()))
flush = lambda: sys.stdout.flush()
"""
track sum of all remaining values not reached in array,
sorted by digit count
"""
n = readint()
ar = readar()
s = [0]*11
c = [0]*11
for i in range(n):
    index = len(str(ar[i]))
    s[index] += ar[i]
    c[index] += 1
ans = 0
for j in range(n):
    index = len(str(ar[j]))
    s[index] -= ar[j]
    c[index] -= 1
    for k in range(1,11):
        ans = (ans+s[k]+c[k]*ar[j]*(10**k)) % 998244353
print(ans)

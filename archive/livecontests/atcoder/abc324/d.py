import sys
from math import factorial
#input functions
readint = lambda: int(sys.stdin.readline())
readints = lambda: map(int,sys.stdin.readline().split())
readar = lambda: list(map(int,sys.stdin.readline().split()))
flush = lambda: sys.stdout.flush()

def ff(x,n):
    h = [0]*10
    while x != 0:
        h[x % 10] += 1
        x //= 10
        n -= 1
    h[0] += n
    return h

n = readint()
s = sys.stdin.readline()
ar = list()
h = [0]*10 #digits used
for i in range(n):
    ar.append(int(s[i]))
    h[ar[-1]] += 1
base = 1
#for j in range(10):
#    if h[j] > 1: base *= factorial(h[j])

ar.sort()
ar.reverse()
highest = 0
for k in ar:
    highest *= 10
    highest += k

#find the possible squares
x = 0
ans = 0
while x*x <= highest:
    br = ff(x*x,n)
    if br == h: ans += base
    x += 1
print(ans)

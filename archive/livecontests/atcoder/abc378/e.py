import sys

#input functions
readint = lambda: int(sys.stdin.readline())
readints = lambda: map(int,sys.stdin.readline().split())
readar = lambda: list(map(int,sys.stdin.readline().split()))
flush = lambda: sys.stdout.flush()
readin = lambda: sys.stdin.readline()[:-1]
readins = lambda: map(str,sys.stdin.readline().split())

"""
sum of every continuous subarray mod M
you cannot know individual subarrays
ai,m limit is 200000

sample 2 has 65 cases of m to remove
"""

n,m = readints()
ar = readar()
for i in range(n):
    ar[i] = ar[i] % m
mc = 0
ans = 0
back = 0
v = 0

br = list()
inc = n
vv = 0
for c in range(n):
    vv += inc
    br.append(vv)
    inc -= 2
#print(br)
cr = list()
for j in range(n):
    v += ar[-j-1]
    cr.append(v//m)
    ans += ar[j]*br[j]
#print(ar)
#print(cr)
cr.reverse()
inc = sum(cr)

for c in cr:
    mc += inc
    inc -= c
ans -= mc*m
print(ans)

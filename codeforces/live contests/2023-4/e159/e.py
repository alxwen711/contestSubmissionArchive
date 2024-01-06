import sys

#input functions
readint = lambda: int(sys.stdin.readline())
readints = lambda: map(int,sys.stdin.readline().split())
readar = lambda: list(map(int,sys.stdin.readline().split()))
flush = lambda: sys.stdout.flush()

"""
length is either a+b or a+b-2
find number of pairs with with this ratio (can it only be collapsed once?)
collapse is done until not possible (aba ab -> a)
bucket sort the reversed strings for comparisons (base 29, mod 2000004143)
initial is sum of len of all strings * num of strings * 2
"""

        
n = readint()
ar = list()
ans = 0
for _ in range(n):
    s = sys.stdin.readline()[:-1]
    ar.append(s)
    ans += len(s)
ans *= n
ans *= 2

m = 113127131137139149
d = {}
d[0] = 0

for i in range(n):
    x = ar[i]
    parent = 0
    for j in range(len(x)):
        nv = (parent*29+ord(x[j])-96) % m
        if d.get(nv) == None:
            d[nv] = 0
        d[nv] += 1
        parent = nv

for k in range(n):
    x = ar[k]
    target = 0
    for g in range(len(x)):
        nt = (target*29+ord(x[-g-1])-96) % m
        if d.get(nt) == None: break
        ans -= (d[nt]*2)
        target = nt
print(ans)

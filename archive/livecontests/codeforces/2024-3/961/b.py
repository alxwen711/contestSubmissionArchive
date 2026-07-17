import sys

#input functions
readint = lambda: int(sys.stdin.readline())
readints = lambda: map(int,sys.stdin.readline().split())
readar = lambda: list(map(int,sys.stdin.readline().split()))
flush = lambda: sys.stdout.flush()
readin = lambda: sys.stdin.readline()[:-1]
readins = lambda: map(str,sys.stdin.readline().split())

"""
easy part: running sum should work
hard part:

semi-emulate this array method
take everything from a lower value,
add the +1 (if it exists) until just under
if still extra and under, each shift +1
"""
# (value,frequency)
def f(n,m,ar):
    ans = 0
    for i in range(n):
        # attempt to use only first one up to maximum amount
        xi = min(ar[i][1],m//ar[i][0])
        v = xi*ar[i][0]
        rest = m-v

        # add in however many is allowed in the +1, if it exists
        if i != n-1:
            if ar[i+1][0] == ar[i][0]+1: # +1 allowed
                yi = min(ar[i+1][1],rest//ar[i+1][0])
                v += yi*ar[i+1][0]
                rest = m-v
                v += min(xi,rest,ar[i+1][1]-yi)
        ans = max(ans,v)
    return ans

for _ in range(readint()):
    n,m = readints()
    ar = readar()
    br = readar()
    cr = list()
    for i in range(n):
        cr.append((ar[i],br[i]))
    cr.sort()
    print(f(n,m,cr))

"""
for _ in range(readint()):
    n,m = readints()
    ar = readar()
    ar.sort()
    back = 0
    ans = 0
    x = 0
    for i in range(n):
        x += ar[i]
        while (ar[i]-1) > ar[back] or x > m:
            x -= ar[back]
            back += 1
            if back > i: break
        ans = max(ans,x)
    print(ans)
"""

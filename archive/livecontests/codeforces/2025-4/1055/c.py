import sys

#input functions
readint = lambda: int(sys.stdin.readline())
readints = lambda: map(int,sys.stdin.readline().split())
readar = lambda: list(map(int,sys.stdin.readline().split()))
flush = lambda: sys.stdout.flush()
readin = lambda: sys.stdin.readline()[:-1]
readins = lambda: map(str,sys.stdin.readline().split())

"""
if the array is not alternating, there is a way to force all 1's


010101011010
001010010
"""

for _ in range(readint()):
    n,q = readints()
    ar = readar()
    z = [0]
    o = [0]
    alt = [0]
    for i in range(n):
        alt.append(((ar[i]^i) % 2)+alt[-1])
        if ar[i] == 0:
            z.append(z[-1])
            o.append(o[-1]+1)
        else:
            z.append(z[-1]+1)
            o.append(o[-1])
    for _ in range(q):
        l,r = readints()
        zs = z[r]-z[l-1]
        os = o[r]-o[l-1]
        alts = alt[r]-alt[l-1]
        if zs % 3 == 0 and os % 3 == 0:
            ans = zs//3+os//3
            if alts == 0 or alts == r-l+1: # full alt
                ans += 1
            print(ans)
        else: print(-1)

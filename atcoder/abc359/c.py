import sys

#input functions
readint = lambda: int(sys.stdin.readline())
readints = lambda: map(int,sys.stdin.readline().split())
readar = lambda: list(map(int,sys.stdin.readline().split()))
flush = lambda: sys.stdout.flush()

"""
0 1
1 2
"""

sx,sy = readints()
tx,ty = readints()

ans = abs(sy-ty)
if ans == 0: # no vertical inc/dec
    bv = (sx+(sy%2))//2
    ev = (tx+(ty%2))//2
    ans = abs(ev-bv)
else: # could vertical inc/dec
    bx = sx
    if sx < tx: bx += min(tx-sx,abs(sy-ty))
    else: bx -= min(sx-tx,abs(sy-ty))
    if bx < tx and sx % 2 == 0 and sy % 2 == 0: bx += 1
    if bx > tx and sx % 2 == 1 and sy % 2 == 1: bx -= 1
    bv = (bx+(ty%2))//2
    ev = (tx+(ty%2))//2
    ans += abs(bv-ev)
print(ans)

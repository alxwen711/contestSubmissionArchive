import sys

#input functions
readint = lambda: int(sys.stdin.readline())
readints = lambda: map(int,sys.stdin.readline().split())
readar = lambda: list(map(int,sys.stdin.readline().split()))
flush = lambda: sys.stdout.flush()

"""
n,m are not limited in any way
1st turn is the special exception turn
"""

for i in range(readint()):
    n,m,k = readints()
    ar = readar()
    br = readar()
    # turn 1
    mina = min(ar)
    maxb = max(br)
    if mina < maxb:
        ar[ar.index(mina)] = maxb
        br[br.index(maxb)] = mina
    k -= 1
    if k % 2 == 1: #even turn swap
        minb = min(br)
        maxa = max(ar)
        ar[ar.index(maxa)] = minb
    print(sum(ar))

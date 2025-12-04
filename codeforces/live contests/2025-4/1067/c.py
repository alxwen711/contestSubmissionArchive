import sys

#input functions
readint = lambda: int(sys.stdin.readline())
readints = lambda: map(int,sys.stdin.readline().split())
readar = lambda: list(map(int,sys.stdin.readline().split()))
flush = lambda: sys.stdout.flush()
readin = lambda: sys.stdin.readline()[:-1]
readins = lambda: map(str,sys.stdin.readline().split())

"""
do the turns actually matter
compute the best total with a maximum of one update
process backwards
"""

for _ in range(readint()):
    n,k = readints()
    ar = readar()
    br = readar()
    mv = 0
    ans = [ar[0]]
    for i in range(1,n):
        ans.append(max(ar[i],ans[-1]+ar[i]))
    #print(ans)
    if k % 2 == 1:
        mod = [ar[0]+br[0]]
        for i in range(1,n):
            mod.append(max(mod[i-1]+ar[i],ans[i]+br[i]))
        ans = mod
    print(max(ans))

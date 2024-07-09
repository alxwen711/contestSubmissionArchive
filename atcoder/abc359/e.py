import sys

#input functions
readint = lambda: int(sys.stdin.readline())
readints = lambda: map(int,sys.stdin.readline().split())
readar = lambda: list(map(int,sys.stdin.readline().split()))
flush = lambda: sys.stdout.flush()

"""
algorithm looks to be non decreasing subsequence
"""

n = readint()
ar = readar()

v = 0
br = list()
ans = list()
for i in range(n):
    while len(br) != 0:
        if br[-1][0] < ar[i]:
            if len(br) == 1:
                v -= br[-1][0]*(br[-1][1]+1)
            else:
                v -= br[-1][0]*(br[-1][1]-br[-2][1])
            br.pop()
        else: break
    br.append((ar[i],i))
    if len(br) == 1: v += br[-1][0]*(br[-1][1]+1)
    else: v += br[-1][0]*(br[-1][1]-br[-2][1])
    ans.append(v+1)
print(*ans)

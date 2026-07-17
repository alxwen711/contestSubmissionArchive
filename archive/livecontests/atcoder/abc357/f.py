import sys

#input functions
readint = lambda: int(sys.stdin.readline())
readints = lambda: map(int,sys.stdin.readline().split())
readar = lambda: list(map(int,sys.stdin.readline().split()))
flush = lambda: sys.stdout.flush()

"""
offline processing looks useful here
unsure if ntt actually helps here
since no cross multiplication is involved
"""

m = 998244353 # 2**12*19+1

n,q = readints()
ar = readar()
br = readar()
incs = list()
for _ in range(q):
    query = readar()
    if query[0] == 3:
        # update previous
        # eval query
        print(0)
        incs = list()
    else: # add to increment list
        incs.append(query)

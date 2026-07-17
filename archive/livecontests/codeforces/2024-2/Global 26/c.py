import sys

#input functions
readint = lambda: int(sys.stdin.readline())
readints = lambda: map(int,sys.stdin.readline().split())
readar = lambda: list(map(int,sys.stdin.readline().split()))
flush = lambda: sys.stdout.flush()

# optimal to set abs only once?

"""
wait until score is as low as possible, then flip
with the forced flip, every other section where
the score would not be set in the negatives can
be flipped
if multiple low points exist?
do not count previous double counted points
"""
m = 998244353
for _ in range(readint()):
    n = readint()
    ar = readar()
    boost = 1
    index = list()
    c = 0
    ans = -9999999999999
    for i in range(len(ar)):
        c += ar[i]
        if c < 0:
            if abs(c) > boost:
                boost = abs(c)
                index = [i]
            elif abs(c) == boost:
                index.append(i)
    """
    part 1
    ans = max(ans,c+boost+boost)
    print(ans)
    """

    # part 2
    if len(index) == 0: # no break points
        print(pow(2,n,m))
    else:
        pt = 0
        ans = 0
        c = 0
        pivots = 0
        for j in range(n):
            if pt == len(index): break
            if index[pt] == j:
                ans = (ans+pow(2,pivots+(n-j-1),m)) % m
                c += ar[j]
                pt += 1
            else:
                c += ar[j]
                if c >= 0: pivots += 1
        print(ans)

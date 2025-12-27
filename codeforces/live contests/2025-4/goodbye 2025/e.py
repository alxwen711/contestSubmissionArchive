import sys

#input functions
readint = lambda: int(sys.stdin.readline())
readints = lambda: map(int,sys.stdin.readline().split())
readar = lambda: list(map(int,sys.stdin.readline().split()))
flush = lambda: sys.stdout.flush()
readin = lambda: sys.stdin.readline()[:-1]
readins = lambda: map(str,sys.stdin.readline().split())


"""
300 queries, n is at most 100000, just under sqrt(n)

any odd bit in a sum indicates a minimal value existance

the maximum sum of the entire array is only about 2**45

binary search???

what if the sums are the same? eject 2 values and try above again
if the above still produces nothing -> screw it, maybe the arrays are equal??

There must exist some point in the array where the opposing sums are equal
(assuming a concat was used)

then whichever of these is shorter MUST have the higher element
(see flatten rule)

if same length AND same sum: values in each list are identical, select either
this is repeated until a single value is left

this is log n log n queries, which makes sense for 300
"""

def query(low,high):
    print("?",str(low+1),str(high+1))
    flush()
    s = readint()
    return s

def solve():
    n = readint()
    low = 0
    high = n-1
    s = query(low,high)
    while low != high:
        # find summation midpoint
        target = s//2
        li,hi = low,high
        index = -1
        while hi-li > 1:
            mid = (li+hi)//2
            v = query(low,mid)
            if v == target:
                index = mid
                break
            elif v < target:
                li = mid
            else:
                hi = mid
        if index == -1:
            if query(low,li) == target: index = li
            else: index = hi
        if index-low < high-index: low,high = low,index
        else: low,high = index+1,high
        s //= 2
    print("!",str(s))
    flush()

for _ in range(readint()):
    solve()

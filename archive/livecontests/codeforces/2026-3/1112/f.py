import sys

#input functions
readint = lambda: int(sys.stdin.readline())
readints = lambda: map(int,sys.stdin.readline().split())
readar = lambda: list(map(int,sys.stdin.readline().split()))
flush = lambda: sys.stdout.flush()
readin = lambda: sys.stdin.readline()[:-1]
readins = lambda: map(str,sys.stdin.readline().split())

"""
nxn matrix generation (n is at most 2500, 6.25 million values)
all values are 0 to n-1
each row and column is a permutation of 0 to n-1
every 2x2 block has an XOR equal to x

hypothesis is that we can construct an array where adjcencies
XOR to all values in a range 0 to the 2limit-1 excluding one value
which will be A[0]^A[-1]. This value is still important and counted
as part of this array. We then need to find an array construction so
that when shifted by 1 position, the XOR computations all end up as x

in the case x == 0, we instead need to do some array reversal nonsense

example 4:
0 2 1 3 -> 2 3 2 3
2 1 3 0 -> 3 2 3 2

example 5:
0 1 2 3 -> 1 3 1 3
3 2 1 0 -> 3 1 3 1 (with shift then 1 3 1 3)

is there possible issues with odd n?

in some form 0 1 2 will be a row/col

0 1 2
1 2 0
2 0 1

assume all odd n are just impossible
then it is likely there is some sort of array construction and repeatable
transformation that can get to x (maybe)

maybe there is some sort of multiple of 4 rule in some cases??

if n % 4 == 2, is it that only x = 0 can be possible?
"""

for _ in range(readint()):
    n,x = readints()
    if n % 2 == 1:
        print(-1)
    else:
        

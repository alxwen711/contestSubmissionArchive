import sys

#input functions
readint = lambda: int(sys.stdin.readline())
readints = lambda: map(int,sys.stdin.readline().split())
readar = lambda: list(map(int,sys.stdin.readline().split()))
flush = lambda: sys.stdout.flush()
readin = lambda: sys.stdin.readline()[:-1]
readins = lambda: map(str,sys.stdin.readline().split())

"""
blatant O(n^3)
Chell can only declare a continuous set of cakes to be fake
optimal setup is FTFTF...

range dp? binary search to try and force mistakes to occur?

force one mistake -> must have at least 2 cakes where distance is 2+ (FTF)
force 2 mistakes -> 3 cakes where FTFTF subsequence is findable

FTFFTF
FTFTTFTFFT

okay wait FFFFFTTTTTFFFFF has error count 5
counter possiblity is to setup as aggresive as a FTFTFTF... pattern as possible
then brute force

okay so greedily setting up the string is not it here (at least not entirely)

feels like a range dp, unsure how
base case: any length 1 or 2 can always be considered 0

if using a binary search, then the N conditions will state at least how many
or how few in a certain subset of cakes must be real or fake
(and now I'm thinking this becomes a set of conditions so this ain't it)

what if we know how many N's are F??? (if optimal exists then O(n^3))

Given x real cakes and at most y errors:
min seg length to consider is x-y (must all be real)
max seg length to consider is x+y (must include all real)
"""

for _ in range(readint()):
    n = readint()
    s = readin()
    dp = list()
    for _ in range(n):
        tmp = [0]*n
        dp.append(tmp)

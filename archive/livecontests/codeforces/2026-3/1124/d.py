import sys

#input functions
readint = lambda: int(sys.stdin.readline())
readints = lambda: map(int,sys.stdin.readline().split())
readar = lambda: list(map(int,sys.stdin.readline().split()))
flush = lambda: sys.stdout.flush()
readin = lambda: sys.stdin.readline()[:-1]
readins = lambda: map(str,sys.stdin.readline().split())

"""
ar values in 4 bits
adjacent values can be XOR with 3,6,9,12,15

0011
0110
1001
1100


1111

the only other values that could be changed to div 3 are 1010 (10) and 0101 (5)
all others have an odd bit count and are impossible
is there some sort of way such that 5 x or 10 x can ALWAYS end at mult 3?

1010
0101

1111
0000

0 is allowed?

1010
1100

just count values??
"""

valid = [1,0,0,1,0,1,1,0,0,1,1,0,1,0,0,1]

for _ in range(readint()):
    n,q = readints()
    ar = readar()
    ans = list()
    v = 0
    for i in ar:
        if valid[i]: v += 1
    ans.append(v)
    for _ in range(q):
        p,x = readints()
        p -= 1
        if valid[ar[p]]:
            if not valid[x]: v -= 1
        else:
            if valid[x]: v += 1
        ar[p] = x
        ans.append(v)
    print(*ans)


        

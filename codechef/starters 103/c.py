import sys

#input functions
readint = lambda: int(sys.stdin.readline())
readints = lambda: map(int,sys.stdin.readline().split())
readar = lambda: list(map(int,sys.stdin.readline().split()))
flush = lambda: sys.stdout.flush()

"""
k is at most half of n (every bit in s can be manipulated)
01/10 -> 11
00/11 -> 00

for each k group (divide by modulo),
find op count needed to change to all 0 or all 1

IF any k group consists of only 0's, then entire string must be converted to 0
1's, at most 1 0->1 per operation, count 0's
0's, initially burn through all pairs 11, then 2*remaining 1's
no need to be adjacent operations
"""

def convert(ar,one):
    """
    n = len(ar)
    ans = 0
    index = 0
    while index < (n-1):
        if ar[index] == 1 and ar[index+1] == 1:
            one -= 2
            ans += 1
            index += 2
        else: index += 1
    ans += (2*one)
    """
    ans = one//2
    if one % 2 == 1: ans += 2
    return ans

for i in range(readint()):
    n,k = readints()
    s = sys.stdin.readline()
    ans0 = 0
    ans1 = 0
    for j in range(k):
        ar = list()
        index = j
        zero = 0
        one = 0
        while index < n:
            ar.append(int(s[index]))
            index += k
            if ar[-1] == 1: one += 1
            else: zero += 1
        if one == 0: ans1 += 999999999999999999999999999999
        else: ans1 += zero
        ans0 += convert(ar,one)
    print(min(ans0,ans1))

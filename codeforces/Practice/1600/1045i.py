import sys

#input functions
readint = lambda: int(sys.stdin.readline())
readints = lambda: map(int,sys.stdin.readline().split())
readar = lambda: list(map(int,sys.stdin.readline().split()))
flush = lambda: sys.stdout.flush()

def convert(s):
    h = [0]*26
    for i in range(len(s)):
        x = ord(s[i])-97
        h[x] = (h[x] + 1) % 2
    """
    convert to val
    """
    ss = 0
    for snth in range(26):
        ss += (2**snth)*(h[snth])
    return ss

def v(y):
    ans = list()
    for t in range(26):
        ans.append(y ^ (2**t))
    return ans
# += 1 if sum of char strings has at most 1 char of odd freq
"""
x is 2+ odd values
0 - 0 -> auto pass
1 - 0 -> auto pass
x - 0 -> auto fail
1 - 2 -> overlap
x - x -> diff must be one and perfect overlap
how to determine x - x?
"""
d = {}
free = 0
ar = list()
for i in range(readint()):
    x = convert(input())
    if d.get(x) == None: d[x] = 0
    d[x] += 1
    ar.append(x)
ans = 0
for j in range(len(ar)):
    y = ar[j]
    ans += (d[y]-1)
    one = v(y)
    for k in range(26):
        if d.get(one[k]) != None: ans += d[one[k]]
print(ans//2)

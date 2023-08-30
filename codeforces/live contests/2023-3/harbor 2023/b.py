import sys

#input functions
readint = lambda: int(sys.stdin.readline())
readints = lambda: map(int,sys.stdin.readline().split())
readar = lambda: list(map(int,sys.stdin.readline().split()))
flush = lambda: sys.stdout.flush()

"""
either swap any two chrs dist 2 apart, or
reverse order of k consecutive chrs
if k is odd, no point in any swaps
if k is 2, effectively best case bubble sort
k = 4? k is always less than n, so even might be
bubble sort?
"""

for i in range(readint()):
    n,k = readints()
    s = sys.stdin.readline()[:-1]
    ans = list()
    if k % 2 == 0:
        d = [0]*26
        for j in range(n):
            d[ord(s[j])-97] += 1
        for m in range(26):
            for o in range(d[m]):
                ans.append(chr(97+m))
    else:
        even = [0]*26
        odd = [0]*26
        for j in range(n):
            if j % 2 == 0: even[ord(s[j])-97] += 1
            else: odd[ord(s[j])-97] += 1
        ei = 0
        oi = 0
        for m in range(n):
            if m % 2 == 0:
                while even[ei] == 0:
                    ei += 1
                ans.append(chr(97+ei))
                even[ei] -= 1
            else:
                while odd[oi] == 0:
                    oi += 1
                ans.append(chr(97+oi))
                odd[oi] -= 1
    print(*ans,sep="")
                

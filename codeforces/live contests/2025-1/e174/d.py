import sys

#input functions
readint = lambda: int(sys.stdin.readline())
readints = lambda: map(int,sys.stdin.readline().split())
readar = lambda: list(map(int,sys.stdin.readline().split()))
flush = lambda: sys.stdout.flush()
readin = lambda: sys.stdin.readline()[:-1]
readins = lambda: map(str,sys.stdin.readline().split())

"""
aabbcc needs 5
aabbccd needs 6
"""

def pal(s,n,x):
    if x < n//2: # compute inner
        for i in range(x,n//2):
            if s[i] != s[-i-1]: return False
        ar = [0]*26
        for i in range(x):
            ar[ord(s[i])-97] += 1
            ar[ord(s[-i-1])-97] -= 1
        for j in ar:
            if j != 0: return False
        return True
    else: # attempt both sides
        ar = [0]*26
        for i in range(x):
            ar[ord(s[i])-97] += 1
        for i in range(n-x):
            ar[ord(s[-i-1])-97] -= 1
        if min(ar) >= 0: return True
        ar = [0]*26
        for i in range(x):
            ar[ord(s[-i-1])-97] += 1
        for i in range(n-x):
            ar[ord(s[i])-97] -= 1
        if min(ar) >= 0: return True
        return False
def f(s):
    n = len(s)
    low = 1
    high = n-1
    while high-low > 1:
        mid = (low+high)//2
        if pal(s,n,mid): high = mid
        else: low = mid
    if pal(s,n,low): return low
    return high
    

for _ in range(readint()):
    s = readin()
    # reduce ends of string if already palindrome
    n = len(s)
    cutpoint = 0
    for i in range(n//2):
        if s[i] == s[-i-1]: cutpoint += 1
        else: break
    s = s[cutpoint:(n-cutpoint)]
    if len(s) > 1: print(f(s))
    else: print(0)

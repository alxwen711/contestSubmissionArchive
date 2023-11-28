import sys

#input functions
readint = lambda: int(sys.stdin.readline())
readints = lambda: map(int,sys.stdin.readline().split())
readar = lambda: list(map(int,sys.stdin.readline().split()))
flush = lambda: sys.stdout.flush()

"""
do we have the letters to make the target string?
can we eliminate the other letters in a specific way
to be able to create the target string?

anavolimilovana
ana____m____ana
anamana
aamnana
aamanan

with end string:
first m must be before 2 a's
second n has no restrictions
first n must be before 1 a
"""

def bs(ar,x):
    if len(ar) == 0: return -1
    low = 0
    high = len(ar)-1
    while high-low > 1:
        mid = (low+high)//2
        if ar[mid] >= x: high = mid
        else: low = mid
    if ar[high] < x: return ar[high]
    elif ar[low] < x: return ar[low]
    return -1
    
def solve(n,m):
    s = sys.stdin.readline()
    t = sys.stdin.readline()
    letters = list()
    for _ in range(26):
        ou = list()
        letters.append(ou)
    for i in range(n):
        letters[ord(s[i])-97].append(i)
    #highest value just underneath the limit
    limit = [9999999999999999]*26
    for j in range(m-1,-1,-1):
        x = ord(t[j])-97
        l = min(limit[:x+1])
        v = bs(letters[x],l)
        if v == -1: return "NO"
        limit[x] = v
    return "YES"

for _ in range(readint()):
    n,m = readints()
    print(solve(n,m))

import sys

#input functions
readint = lambda: int(sys.stdin.readline())
readints = lambda: map(int,sys.stdin.readline().split())
readar = lambda: list(map(int,sys.stdin.readline().split()))
flush = lambda: sys.stdout.flush()
readin = lambda: sys.stdin.readline()[:-1]
readins = lambda: map(str,sys.stdin.readline().split())

"""
test every divisor for cycle testing, then check if br can be made equal?

the remaining k options have to be used for some sort of cyclic case build

111100
011110
001111

n = 9, k = 2 -> 0,7 and 2,9

from c2 check each distance gap first then freq check
in this case no duplicates thus no matches
"""


for _ in range(readint()):
    n,k = readints()
    ar = readar()
    br = readar()
    h = [0]*(n+1)
    ans = "YES"
    for i in range(n-k):
        if ar[i] != br[i]:
            if br[i] == -1: br[i] = ar[i]
            else: ans = "NO"
        if ar[i+k] != br[i+k]:
            if br[i+k] == -1: br[i+k] = ar[i+k]
            else: ans = "NO"
    for j in br:
        if j != -1:
            if h[j] == 0: h[j] = 1
            else: ans = "NO"
        

    print(ans)

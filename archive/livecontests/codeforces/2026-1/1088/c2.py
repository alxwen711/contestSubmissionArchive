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

this is not cyclic based on the observations in c1, assume some sort of
greedy pattern??

if subtracting and adding same, b array just needs to match itself
if subtracting and adding diff, b array MUST match

everything else could just be a frequency count case
"""


for _ in range(readint()):
    n,k = readints()
    ar = readar()
    br = readar()
    index = 0
    free = list()
    h = [0]*(n+1)
    for i in range(k):
        if br[i] == -1:
            free.append(i)
        else:
            h[br[i]] += 1
    ans = "YES"
    for j in range(k):
        if h[ar[i]] == 0: # must use a free slot
            if len(free) == index: # none left
                ans = "NO"
                break
            br[free[index]] = ar[i]
            index += 1
        else:
            h[ar[i]] -= 1
    

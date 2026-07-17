import sys

#input functions
readint = lambda: int(sys.stdin.readline())
readints = lambda: map(int,sys.stdin.readline().split())
readar = lambda: list(map(int,sys.stdin.readline().split()))
flush = lambda: sys.stdout.flush()
"""
101010100101010
010101010110101

"""
n = readint()
s = sys.stdin.readline()
ar = readar()
br = list() #101010...
cr = list() #010101...
b,c = 0,0
for i in range(n):
    if int(s[i]) == i % 2: # follows 010101
        b += ar[i]
    else:
        c += ar[i]
    br.append(b)
    cr.append(c)
ans = 99999999999999999999999999
for j in range(n-1):
    ans = min(ans,br[j]+cr[-1]-cr[j],cr[j]+br[-1]-br[j])
print(ans)

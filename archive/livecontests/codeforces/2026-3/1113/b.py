import sys

#input functions
readint = lambda: int(sys.stdin.readline())
readints = lambda: map(int,sys.stdin.readline().split())
readar = lambda: list(map(int,sys.stdin.readline().split()))
flush = lambda: sys.stdout.flush()
readin = lambda: sys.stdin.readline()[:-1]
readins = lambda: map(str,sys.stdin.readline().split())

"""
all distinct, thus b can only be at most half of a's size
do fixed pairings work?
"""

for _ in range(readint()):
    n,m = readints()
    ar = readar()
    br = readar()
    if 2*m > n: print("NO")
    else:
        ar.sort()
        br.sort()
        ans = "YES"
        for i in range(m):
            if br[i] < ar[i] or br[i] > ar[-m+i]:
                ans = "NO"
                break
        print(ans)
        

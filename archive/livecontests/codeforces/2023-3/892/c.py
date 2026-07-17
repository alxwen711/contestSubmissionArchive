import sys

#input functions
readint = lambda: int(sys.stdin.readline())
readints = lambda: map(int,sys.stdin.readline().split())
readar = lambda: list(map(int,sys.stdin.readline().split()))
flush = lambda: sys.stdout.flush()

def solve(n):
    ar = list()
    for i in range(1,n+1):
        ar.append(i)
    br = list()
    ans = 0
    for j in range(n):
        br.append(ar.pop())
        v = 0
        inc = 0
        bigl = 0
        for k in range(len(ar)):
            inc += 1
            vv = inc*ar[k]
            v += vv
            bigl = max(bigl,vv)
        for l in range(len(br)):
            inc += 1
            vv = inc*br[l]
            v += vv
            bigl = max(bigl,vv)
        ans = max(ans,v-bigl)
    return ans

for i in range(readint()):
    print(solve(readint()))

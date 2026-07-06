import sys

#input functions
readint = lambda: int(sys.stdin.readline())
readints = lambda: map(int,sys.stdin.readline().split())
readar = lambda: list(map(int,sys.stdin.readline().split()))
flush = lambda: sys.stdout.flush()

#avg of range = avg of endpoints of any subrange
"""
no e x o or o x e
arithmetic sequence could be possible
find longest arithmetic progression
2,3,4,5, 1 ,6,7,8
take two indices, find difference, calculate mid difference then test how many hit
"""

def progression(ar):
    n = len(ar)
    ans = 2
    for i in range(n-1):
        diff = ar[i+1]-ar[i]
        cur = ar[i+1]
        chain = 2
        for k in range(i+2,n):
            if ar[k]-cur == diff:
                chain += 1
                cur = ar[k]
            else:
                cur += diff
        ans = max(chain,ans)
    return ans 

def f(ar,i,j):
    diff = (ar[j]-ar[i])/(j-i)
    ans = 0
    for s in range(n):
        if s == i or s == j: ans += 1
        elif s < i:
            if abs(ar[i] - (diff*(i-s)) - ar[s]) < 0.00000001: ans += 1
        else:
            if abs(ar[i] + (diff*(s-i)) - ar[s]) < 0.00000001: ans += 1
    return ans
def solve(n,ar):
    if n <= 2: return 0
    ans = 2
    for i in range(n-1):
        for j in range(i+1,n):
            ans = max(ans,f(ar,i,j))

    return n-ans
            
    """
    br = list()
    cr = list()
    for snth in range(n):
        h = [0]*n
        br.append(h)
        d = [0]*n
        cr.append(d)
    br[0][0],br[1][0],br[1][1] = 1,2,1
    cr[1][0] = ar[1]-ar[0]
    for i in range(2,n):
        for j in range(i+1):
            if j == i: br[i][j] = 1
            elif j == 0:
                br[i][j] = 2
                cr[i][j] = ar[i]-ar[j]
            else:
                best = 0
                index = -1
                for k in range(j):
                    if ar[i] - ar[j] == cr[j][k] and br[j][k] > best:
                        best = br[j][k]
                        index = k
                if index != -1:
                    br[i][j] = best + 1
                    cr[i][j] = cr[j][index]
                else:
                    br[i][j] = 2
                    cr[i][j] = ar[i]-ar[j]
    ans = 0
    for s in range(n):
        ans = max(ans,max(br[s]))
    """
    return n-ans
                
for i in range(readint()):
    n = readint()
    ar = readar()
    print(solve(n,ar))

import sys

#input functions
readint = lambda: int(sys.stdin.readline())
readints = lambda: map(int,sys.stdin.readline().split())
readar = lambda: list(map(int,sys.stdin.readline().split()))
flush = lambda: sys.stdout.flush()
readin = lambda: sys.stdin.readline()[:-1]
readins = lambda: map(str,sys.stdin.readline().split())

"""
note that largest set that has no triangles is:
1,1,2,3,5,8,13...
so only about 45ish until at least 1 triangle is definitely possible
then only around 48ish to satisfy initial constraints

each query is then brute forcable???
"""
def g(br,x):
    if br[x]+br[x+1] > br[x+4] and br[x+2]+br[x+3] > br[x+5]: return True
    elif br[x]+br[x+2] > br[x+4] and br[x+1]+br[x+3] > br[x+5]: return True
    elif br[x]+br[x+3] > br[x+4] and br[x+1]+br[x+2] > br[x+5]: return True
    elif br[x+1]+br[x+2] > br[x+4] and br[x]+br[x+3] > br[x+5]: return True
    elif br[x+1]+br[x+3] > br[x+4] and br[x]+br[x+2] > br[x+5]: return True
    elif br[x+2]+br[x+3] > br[x+4] and br[x+1]+br[x] > br[x+5]: return True

    elif br[x]+br[x+1] > br[x+3] and br[x+2]+br[x+4] > br[x+5]: return True
    elif br[x]+br[x+2] > br[x+3] and br[x+1]+br[x+4] > br[x+5]: return True
    elif br[x+1]+br[x+2] > br[x+3] and br[x]+br[x+4] > br[x+5]: return True

    elif br[x]+br[x+1] > br[x+2] and br[x+3]+br[x+4] > br[x+5]: return True

    return False


def f(br,x):
    return br[x]+br[x+1] > br[x+2]

n,q = readints()
ar = readar()
for _ in range(q):
    l,r = readints()
    d = r-l+1
    if d >= 50: print("YES")
    else:
        l -= 1
        br = list()
        for i in range(l,r):
            br.append(ar[i])
        br.sort()
        ans = list()
        flag = False
        #print(br)
        for j in range(d-3+1):
            if f(br,j):
                ans.append(j)
        for k in range(d-6+1):
            if g(br,k):
                flag = True
                break
        if flag: print("YES")
        elif len(ans) == 0: print("NO")
        elif ans[-1]-ans[0] >= 3: print("YES")
        else: print("NO")

import sys

#input functions
readint = lambda: int(sys.stdin.readline())
readints = lambda: map(int,sys.stdin.readline().split())
readar = lambda: list(map(int,sys.stdin.readline().split()))
flush = lambda: sys.stdout.flush()
readin = lambda: sys.stdin.readline()[:-1]
readins = lambda: map(str,sys.stdin.readline().split())

"""
number of rounds does not matter, determine singular pair for least dmg
a<b<c<d always has max diff when paired as (a,d) and (b,c); ac/bd also works

thus choose two pairs with values as close to each other as possible
OR are in a non-(a,b)/(c,d) setup
"""

for _ in range(readint()):
    n,k = readints()
    ar = readar()
    br = readar()
    cr = list()
    for i in range(n):
        a,b = ar[i],br[i]
        if b < a: a,b = b,a
        cr.append((a,b))
    cr.sort()
    ans = 9999999999999999999
    #print(cr)
    for j in range(n-1):
        dr = [cr[j][0],cr[j][1],cr[j+1][0],cr[j+1][1]]
        dr.sort()
        p = dr[3]-dr[0]+dr[2]-dr[1]
        ans = min(ans,p-(cr[j][1]-cr[j][0]+cr[j+1][1]-cr[j+1][0]))
        if ans == 0: break
    for snth in range(n):
        ans += abs(ar[snth]-br[snth])
    print(ans)

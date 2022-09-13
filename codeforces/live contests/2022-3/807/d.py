import sys
ar = list()
br = list()

"""
max answer will be 2(n-2)
ends must be equal
possible (6)
01011011
00100101

impossible?
01000100
00101010
"""


def solve(n,ar,br):
    if ar[0] != br[0] or ar[-1] != br[-1]: return -1
    #track island endpoints
    aisle = 0
    ast = list()
    aend = list()
    bisle = 0
    bst = list()
    bend = list()
    one = False
    for k in range(n):
        if one:
            if ar[k] == 0:
                aisle += 1
                one = False
                aend.append(k-1)
        else:
            if ar[k] == 1:
                one = True
                ast.append(k)
    if one:
        aisle += 1
        aend.append(n-1)
        
    one = False
    for m in range(n):
        if one:
            if br[m] == 0:
                bisle += 1
                one = False
                bend.append(m-1)
        else:
            if br[m] == 1:
                one = True
                bst.append(m)
    if one:
        bisle += 1
        bend.append(n-1)
    if aisle != bisle: return -1
    #solvable, calc diff in islands
    ans = 0
    for ff in range(aisle):
        ans += abs(ast[ff]-bst[ff])+abs(aend[ff]-bend[ff])
    return ans

for i in range(int(sys.stdin.readline())):
    ar.clear()
    br.clear()
    n = int(sys.stdin.readline())
    a = input()
    b = input()
    for j in range(n):
        ar.append(int(a[j]))
        br.append(int(b[j]))
    print(solve(n,ar,br))
        

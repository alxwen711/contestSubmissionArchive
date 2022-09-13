import sys

def div(x,m):
    a = 0
    while x % m == 0:
        a += 1
        x = x // m
    return m**a #check against possible 2**30 troll case

for i in range(int(sys.stdin.readline())):
    n,m = map(int,sys.stdin.readline().split())
    ar = list(map(int,sys.stdin.readline().split()))
    k = int(sys.stdin.readline())
    br = list(map(int,sys.stdin.readline().split()))
    #reduce both to base form, check if equal
    aar = list()
    bbr = list()
    for j in range(n):
        c = div(ar[j],m)
        aar.append([ar[j]//c,c])
    for l in range(k):
        d = div(br[l],m)
        bbr.append([br[l]//d,d])
    aaar = list()
    bbbr = list()
    base = 0
    tot = 0
    for f in range(n):
        if base != aar[f][0]:
            if base != 0: aaar.append([base,tot])
            base = aar[f][0]
            tot = 0
        tot += aar[f][1]
    aaar.append([base,tot])
    base = 0
    tot = 0
    for g in range(k):
        if base != bbr[g][0]:
            if base != 0: bbbr.append([base,tot])
            base = bbr[g][0]
            tot = 0
        tot += bbr[g][1]
    bbbr.append([base,tot])
    ans = "Yes"
    if len(aaar) != len(bbbr): ans = "No"
    else:
        for mm in range(len(aaar)):
            if aaar[mm][0] != bbbr[mm][0] or aaar[mm][1] != bbbr[mm][1]:
                ans = "No"
                break
    print(ans)
    
"""
    aar = list()
    bbr = list()
    for j in range(n):
        aar.append(div(ar[j],m))
    for l in range(k):
        bbr.append(div(br[l],m))
    #sum vals, quan vals, pointers
    sa, sb, qa, qb, pa, pb = 0, 0, 0, 0, 0, 0
    ans = "Yes"
    while True:
        if pa == n and pb == k: break
        elif pa == n: #auto b
            sb += br[pb]
            qb += bbr[pb]
            pb += 1
        elif pb == k: #auto a
            sa += ar[pa]
            qa += aar[pa]
            pa += 1
        elif sa > sb: #b is lower
            sb += br[pb]
            qb += bbr[pb]
            pb += 1
        else: #a is lower or same
            sa += ar[pa]
            qa += aar[pa]
            pa += 1
        if sa == sb:
            if qa != qb:
                ans = "No"
                break
            else:
                sa, sb, qa, qb = 0, 0, 0, 0
    if sa != 0 or sb != 0 or qa != 0 or qb != 0: ans = "No"
    print(ans)
""" 

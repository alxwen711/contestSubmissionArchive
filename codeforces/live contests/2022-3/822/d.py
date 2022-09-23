import sys

#input functions
readint = lambda: int(sys.stdin.readline())
readints = lambda: map(int,sys.stdin.readline().split())
readar = lambda: list(map(int,sys.stdin.readline().split()))
flush = lambda: sys.stdout.flush()

for i in range(readint()):
    n,k = readints()
    ar = readar()
    #left first
    lp,rp = k-1,k-1
    lu,ru = ar[lp],ar[rp] #best used in direction
    lh,rh = ar[lp],ar[rp] #current health in both dir
    left = True
    best = ar[lp]
    while lp != 0 and rp != n-1:
        if left:
            if lh+ar[lp-1] >= 0:
                lh += ar[lp-1]
                lp -= 1
                lu = max(lu,lh)
            else:
                if lu > ru: #try right
                    left = False
                    rh += (lu-ru)
                    ru = lu
                else: break
        else:
            if rh+ar[rp+1] >= 0:
                rh += ar[rp+1]
                rp += 1
                ru = max(ru,rh)
            else:
                if ru > lu: #try left
                    left = True
                    lh += (ru-lu)
                    lu = ru
                else: break
    flag = False
    if lp == 0 or rp == n-1: flag = True
    #right
    lp,rp = k-1,k-1
    lu,ru = ar[lp],ar[rp] #best used in direction
    lh,rh = ar[lp],ar[rp] #current health in both dir
    left = False
    best = ar[lp]
    while lp != 0 and rp != n-1 and flag == False:
        if left:
            if lh+ar[lp-1] >= 0:
                lh += ar[lp-1]
                lp -= 1
                lu = max(lu,lh)
            else:
                if lu > ru: #try right
                    left = False
                    rh += (lu-ru)
                    ru = lu
                else: break
        else:
            if rh+ar[rp+1] >= 0:
                rh += ar[rp+1]
                rp += 1
                ru = max(ru,rh)
            else:
                if ru > lu: #try left
                    left = True
                    lh += (ru-lu)
                    lu = ru
                else: break
    if lp == 0 or rp == n-1: flag = True
    if flag: print("YES")
    else: print("NO")
    

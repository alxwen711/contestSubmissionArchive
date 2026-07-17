import sys

#input functions
readint = lambda: int(sys.stdin.readline())
readints = lambda: map(int,sys.stdin.readline().split())
readar = lambda: list(map(int,sys.stdin.readline().split()))
flush = lambda: sys.stdout.flush()
readin = lambda: sys.stdin.readline()[:-1]
readins = lambda: map(str,sys.stdin.readline().split())

for i in range(readint()):
    n = readint()
    aar = readar()
    bbr = readar()
    ar = set(aar)
    br = set(bbr)
    if len(ar) >= 3 or len(br) >= 3: print("YES")
    elif len(ar) == 1 or len(br) == 1: print("NO")
    else: # both are 2
        aar.sort()
        bbr.sort()
        adiff = aar[-1]-aar[0]
        bdiff = bbr[-1]-bbr[0]
        if adiff != bdiff: print("YES")
        else:
            aindex = 0
            for j in range(n-1):
                if aar[aindex] != aar[aindex+1]: break
                aindex += 1
            if bbr[aindex] != bbr[aindex+1] and (aindex == 0 or aindex == n-2):
                print("NO")
            else: print("YES")

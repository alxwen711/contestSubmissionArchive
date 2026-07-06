import sys

#input functions
readint = lambda: int(sys.stdin.readline())
readints = lambda: map(int,sys.stdin.readline().split())
readar = lambda: list(map(int,sys.stdin.readline().split()))
flush = lambda: sys.stdout.flush()

def freq_str(s) -> list:
    ar = [0]*26
    offset = 97 #replace with 65 if upper
    for i in range(len(s)):
        ar[ord(s[i])-offset] += 1
    return ar

def assess(ar,x,j):
    v = x//j
    cr = list()
    for kk in range(26):
        if ar[kk] != 0: cr.append([-ar[kk],kk])
    cr.sort()
    for snth in range(26):
        if ar[snth] == 0: cr.append([0,snth])
    bb = list()
    for ll in range(j):
        bb.append(cr[ll][1])
    st = x
    for p in range(j):
        st -= ar[bb[p]]
        st += abs(ar[bb[p]]-v)
    return st,bb

for i in range(readint()):
    n = readint()
    s = input()
    ar = freq_str(s)
    x = sum(ar)
    best = 3457856874508945084
    br = None #int list of letters to keep
    for j in range(1,27):
        if x % j == 0:
            a,b = assess(ar,x,j)
            if a < best:
                best = a
                br = b
    print(best//2) #changes needed
    #print(br)
    h = [0]*26
    c = x//len(br)
    for k in range(len(br)):
        h[br[k]] = c
    ans = [" "]*x
    #fill in constant spots
    for m in range(x):
        t = s[m]
        if h[ord(t)-97] != 0:
            ans[m] = t
            h[ord(t)-97] -= 1
    #fill in remaining
    inted = 0
    index = 0
    while index != x:
        if ans[index] != " ": index += 1
        else:
            if h[inted] == 0:
                inted += 1
            else:
                h[inted] -= 1
                ans[index] = chr(inted+97)
    print(*ans,sep="")

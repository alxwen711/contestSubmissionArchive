import sys

#input functions
readint = lambda: int(sys.stdin.readline())
readints = lambda: map(int,sys.stdin.readline().split())
readar = lambda: list(map(int,sys.stdin.readline().split()))
flush = lambda: sys.stdout.flush()
readin = lambda: sys.stdin.readline()[:-1]
readins = lambda: map(str,sys.stdin.readline().split())


"""
can this be brute force searched?
1010101
0100101
0101011
0101000
0101111
0101100
0110010
0111110
0000000
1111110
0000010
1111010
0001010
1101010


find some sequence that makes all the bits identical,
then bit flip the corrections into place.
the outlier is if it is full alt, then check for basic flip


do only odd length brute force on full alt?????
01001101010
01010010101
10101010101
"""

def fullalt(ar):
    for i in range(len(ar)-1):
        if ar[i] == ar[i+1]: return False
    return True

def ispal(ar):
    for i in range(len(ar)//2):
        if ar[i] != ar[-i-1]: return False
    return True

def defaultsolve(n,ar,br):
    # find a dup segment in ar
    ans = list()

    if fullalt(ar):
        ans.append((1,3))
        for hh in range(3):
            ar[hh] = ar[hh] ^ 1

    lp,rp = -1,-1
    for i in range(n-1):
        if ar[i] == ar[i+1]: lp,rp = i,i+1

    # invert until we have a mono string
    while True:
        # push pointers as far out as possible
        while lp != 0:
            if ar[lp-1] == ar[lp]: lp -= 1
            else: break

        while rp != n-1:
            if ar[rp+1] == ar[rp]: rp += 1
            else: break

        if lp == 0 and rp == n-1: break # mono segment
        ans.append((lp+1,rp+1))
        for a in range(lp,rp+1):
            ar[a] = ar[a] ^ 1
    
    # find dup segment in br as the fixed point
    for j in range(n-1):
        if br[j] == br[j+1]:
            lp = j
            rp = j+1
            for k in range(j+2,n):
                if br[k] == br[j]: rp = k
                else: break
            break

    # correct around the end points (lp,rp are now limits)
    l,r = 0,n-1
    while True:
        while l != lp:
            if ar[l] == br[l]: l += 1
            else: break
        while r != rp:
            if ar[r] == br[r]: r -= 1
            else: break
        if l == lp and r == rp: break
        ans.append((l+1,r+1))
        for b in range(l,r+1):
            ar[b] = ar[b] ^ 1

    if ar[l] != br[l]: ans.append((l+1,r+1))
    print(len(ans))
    for snth in ans:
        print(snth[0],snth[1])
        

def recurse(ar,i):
    
for _ in range(readint()):
    n = readint()
    s = readin()
    t = readin()
    ar = list()
    br = list()
    for i in s:
        ar.append(int(i))
    for j in t:
        br.append(int(j))
    if ar == br: print(0)
    elif fullalt(br):
        # dummy attempt/recursion needed/idk anymore
        ans = list()
        flag = True
        for i in range(n):
            if ar[i] != br[i]:
                flag = False
                for j in range(i+1,n):
                    if ispal(ar[i:j+1]):
                        flag = True
                        ans.append((i+1,j+1))
                        for c in range(i,j+1):
                            ar[c] = ar[c] ^ 1
                        break
                if not flag: break
        if not flag: print(-1)
        else:
            print(len(ans))
            for snth in ans:
                print(snth[0],snth[1])
                        
        
    else: # a repeat in ar can always be made, br is not full alt, use algo
        defaultsolve(n,ar,br)

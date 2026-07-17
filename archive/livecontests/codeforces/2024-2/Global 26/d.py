import sys
from math import gcd
#input functions
readint = lambda: int(sys.stdin.readline())
readints = lambda: map(int,sys.stdin.readline().split())
readar = lambda: list(map(int,sys.stdin.readline().split()))
flush = lambda: sys.stdout.flush()
"""
t can contain a
the substring must start at latest from the first non-a chr
can take frequencies of non-a chr's, gcd to get possible number
of substrings

if substring exists, only scenario using this case
then compute the residue of a's left over
calculate number of padding scenarios possible

strip left/right tails

something inbetween O(n log n) and O(n**1.5)
"""
def choices(x,y,c): # number of 0-a,0-b combos at most c
    a = min(x,y)
    b = max(x,y)
    ans = 0
    for i in range(a+1):
        v = min(b,c-i)+1
        if v > 0: ans += v
        else: break
    #print(x,y,c,ans)
    return ans

def cmp(s,a,b,c,d):
    for i in range(b-a+1):
        if s[a+i] != s[c+i]: return False
    return True

def viable(s,freq,x): # if possible, return the 'a' residue
    if x == 1: return []
    n = len(s)
    req = list()
    nonzero = 0
    for f in freq:
        req.append(f//x)
        if req[-1] != 0: nonzero += 1
    index = 0 # end index of first grouping
    for i in range(n):
        if ord(s[i]) > 97:
            pos = ord(s[i])-97
            req[pos] -= 1
            if req[pos] == 0: nonzero -= 1
            elif req[pos] == -1: return -1
            if nonzero == 0:
                index = i
                break
    ans = []
    j = index+1
    ac = 0
    while j < n:
        if s[j] == "a":
            ac += 1
            j += 1
        else:
            ans.append(ac)
            ac = 0
            endpoint = j+index
            if endpoint >= n: return -1
            if not cmp(s,0,index,j,endpoint): return -1
            j += index+1
    return ans
        
        
def solve(s):
    n = len(s)
    lt,rt = n,0
    for i in range(n):
        if s[i] != "a":
            lt = i
            break
    if lt == n: return n-1 # edge case of all 'a's
    for j in range(n):
        if s[-j-1] != "a":
            rt = j
            break
    s = s[lt:n-rt] # remove tailends
    freq = [0]*26
    for snth in s:
        if snth != "a": freq[ord(snth)-97] += 1
    g = 0
    for v in freq:
        g = gcd(g,v)
    subcount = 1
    ans = 0
    while subcount*subcount <= g:
        if g % subcount == 0:
            a,b = subcount,g//subcount
            ar = viable(s,freq,a)
            if ar != -1:
                #print(ar,a)
                # increment ans
                if ar == []: ans += ((lt+1)*(rt+1))
                else:
                    limit = min(ar)
                    ans += choices(lt,rt,limit)
            ar = -1
            if a != b: ar = viable(s,freq,b)
            if ar != -1:
                #print(ar,b)
                # increment ans
                limit = min(ar)
                ans += choices(lt,rt,limit)
        subcount += 1
    return ans
                
for _ in range(readint()):
    s = sys.stdin.readline()[:-1]
    print(solve(s))
